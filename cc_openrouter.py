#!/usr/bin/env python3
"""Escolhe um modelo gratuito do OpenRouter e inicia Claude Code nesta pasta."""
import getpass
import json
import os
import shutil
import subprocess
import sys
from urllib.error import HTTPError
from urllib.request import Request, urlopen


def main():
    claude = shutil.which("claude")
    if not claude:
        sys.exit("Claude Code não encontrado no PATH.")
    key = getpass.getpass("Chave OpenRouter (oculta): ").strip()
    if not key:
        sys.exit("Chave vazia. Cancelado.")

    def api(path):
        request = Request("https://openrouter.ai/api/v1/" + path,
                          headers={"Authorization": "Bearer " + key})
        with urlopen(request, timeout=30) as response:
            return json.load(response)["data"]

    api("key")  # Valida a chave antes de abrir o Claude Code.
    models = sorted(
        (m for m in api("models")
         if m["id"].endswith(":free")
         and "tools" in (m.get("supported_parameters") or [])
         and float(m.get("pricing", {}).get("prompt", "1")) == 0
         and float(m.get("pricing", {}).get("completion", "1")) == 0),
        key=lambda m: m["id"],
    )
    if not models:
        sys.exit("Nenhum modelo gratuito com ferramentas disponível no catálogo.")
    for i, m in enumerate(models, 1):
        print(f"{i:2}. {m['id']}  |  contexto: {m.get('context_length', '?')}")
    while True:
        choice = input("Modelo [número; Enter cancela]: ").strip()
        if not choice:
            return
        if choice.isascii() and choice.isdecimal() and 1 <= int(choice) <= len(models):
            break
        print("Escolha um número da lista.")

    model = models[int(choice) - 1]["id"]
    env = os.environ.copy()
    env.update(ANTHROPIC_BASE_URL="https://openrouter.ai/api",
               ANTHROPIC_AUTH_TOKEN=key, ANTHROPIC_API_KEY="",
               ANTHROPIC_MODEL=model, CLAUDE_CODE_SUBAGENT_MODEL=model)
    for tier in ("HAIKU", "SONNET", "OPUS", "FABLE"):
        env[f"ANTHROPIC_DEFAULT_{tier}_MODEL"] = model
    print(f"\nAbrindo {model} em {os.getcwd()}...", flush=True)
    return subprocess.call([claude, "--model", model], env=env)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (KeyboardInterrupt, EOFError):
        sys.exit("\nCancelado.")
    except HTTPError as error:
        sys.exit(f"OpenRouter: HTTP {error.code}. Verifique chave, conta e limites.")
    except (OSError, ValueError, KeyError, TypeError) as error:
        sys.exit(f"Erro: {error}")