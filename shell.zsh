# Source this from your main `.zshrc`
# Run from Mac OS 15.5 with ZShell

# Since learning, leaving in open for now
# But convention I believe is .pyenv or something
export DEFAULT_PY_VENV_DIR=py-venv

creVenv () {
  local envDir="${1:-$DEFAULT_PY_VENV_DIR}"
  python -m venv $envDir
}

pyVAck () {
  local envDir="${1:-$DEFAULT_PY_VENV_DIR}"
  local activateScript="./$envDir/bin/activate"

  source $activateScript
}

alias pipi="pip install"
alias py="python"
