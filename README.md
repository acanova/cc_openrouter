# Claude Code + OpenRouter

A small launcher for experimenting with Claude Code through OpenRouter's free models. It checks your OpenRouter key, fetches the current catalog, shows free models with tool support, and starts Claude Code with the selected model.

## Requirements

- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code/overview) installed and available as `claude`
- Python 3
- An [OpenRouter API key](https://openrouter.ai/settings/keys)

No Python packages are required.

## Usage

Run the script from the directory where you want Claude Code to work:

```sh
python3 /path/to/cc_openrouter.py
```

Paste your OpenRouter key when prompted, then choose a model by number. The key is hidden while you type; the script uses it for OpenRouter requests and passes it to the Claude Code process it starts.

You can also provide the key through an environment variable:

```sh
export OPENROUTER_API_KEY="your-key-here"
python3 /path/to/cc_openrouter.py
```

For repeated use, a shell alias keeps the command short:

```sh
alias cc-openrouter='python3 /path/to/cc_openrouter.py'
```

Add the alias to `~/.zshrc` or `~/.bashrc` to keep it between terminal sessions.

### Keeping the key handy

Avoid putting the key directly in shell history or committing it to a file. A few convenient options:

- Export `OPENROUTER_API_KEY` once per terminal session.
- Load it from a password manager CLI before running the launcher.
- On macOS, save it in Keychain once:

  ```sh
  security add-generic-password -a "$USER" -s openrouter-api-key -w
  ```

  Then add this function to `~/.zshrc`:

  ```sh
  cc-openrouter() {
    OPENROUTER_API_KEY="$(security find-generic-password -a "$USER" -s openrouter-api-key -w)" \
      python3 /path/to/cc_openrouter.py
  }
  ```

## Notes

OpenRouter's free-model list is dynamic: models may appear, disappear, or change limits without notice. Tool support in the catalog is only a first filter, so not every listed model will work correctly with Claude Code.

This project is intended mainly for Claude Code experimentation and study.
