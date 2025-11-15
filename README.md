# VS Colab

Small utility to install and run a headless VS Code (code-server) and expose it via ngrok.

Features
- Install scripts (from `src/`) for `code-server` and `ngrok` (invoked by `setup`).
- Start `code-server` and `ngrok` together with logs written to files.
- Teardown/uninstall helpers.
- Packaging with a console entry point `vsserver`.

Install locally

Create a virtualenv and install:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

Usage

```bash
# setup (runs install scripts under src/)
vsserver setup

# start (will choose a random free port and start code-server + ngrok)
vsserver start --auth-token YOUR_NGROK_TOKEN

# teardown
vsserver teardown
```

Notes
- This project assumes `code-server` and `ngrok` are available or that the
  install scripts in `src/` will install them.
- Background processes write logs to `vsserver.log` and `ngrok.log` by default.

License

MIT
# vs-server-script