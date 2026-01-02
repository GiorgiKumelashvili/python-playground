<div align="center">
  <img src="https://skillicons.dev/icons?i=python" alt="Python Logo" width="150"/>
  <h1>Python Playground</h1>
</div>

- Python v3.14.2
- Pip v25.3

# Setup guide

1. Recreate .venv folder
    - `rm -rf ./.venv`
    - `python3 -m venv ./.venv`
    - `source ./.venv/bin/activate`
2. check python & pip versions/paths
    - `python --version && pip --version`
    - `which python && which pip` - should be coming from .venv
3. install requirements/packages
    - `pip install -r requirements.txt`
4. finally run main.py
    - `python main.py`

