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

On macOS or Linux, you can make it directly executable once:

```sh
chmod +x /path/to/cc_openrouter.py
```

Then run it without typing `python3`:

```sh
/path/to/cc_openrouter.py
```

The script's first line selects Python 3 automatically. Git records the executable bit, so once this mode change is committed, macOS and Linux users should receive it when they clone the repository. Windows users can continue to run `python cc_openrouter.py` or `python3 cc_openrouter.py`.

To make the launcher available from any directory, install it somewhere on your `PATH`:

```sh
mkdir -p ~/.local/bin
install -m 755 cc_openrouter.py ~/.local/bin/cc-openrouter
```

If `~/.local/bin` is not already on your `PATH`, add this to `~/.zshrc` or `~/.bashrc`:

```sh
export PATH="$HOME/.local/bin:$PATH"
```

Open a new terminal, enter any project directory, and run:

```sh
cc-openrouter
```

Paste your OpenRouter key when prompted, then choose a model by number. The key is hidden while you type; the script uses it for OpenRouter requests and passes it to the Claude Code process it starts.

You can also provide the key through an environment variable:

```sh
export OPENROUTER_API_KEY="your-key-here"
cc-openrouter
```

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
      command cc-openrouter
  }
  ```

## Notes

OpenRouter's free-model list is dynamic: models may appear, disappear, or change limits without notice. Tool support in the catalog is only a first filter, so not every listed model will work correctly with Claude Code.

This project is intended mainly for Claude Code experimentation and study.
