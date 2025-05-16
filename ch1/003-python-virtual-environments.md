# Python Virtual Environments

In order to manage packages we gotta learn about these Python virtual environments it looks like.

https://docs.python.org/3/library/venv.html

*System Environment: * Mac OS 15.5, zsh 5.9, M1 Arm processor

## Venv

- Lightweight "virtual environments" with packages in `site` directory`
- Created on top of existing Python installation known as "base"
- Can isolate from globally installed packages
- Common installation tools (e.g. `pip`) will work with virtual env when called from within one
- Usually contained in `.venv` directory (`./py-venv`)
- Not checked into version control systems (VCS) (e.g. `git`)
- Not movable or copyable - just recreate at target

Create with `python3 -m venv ./env`

## Pip


