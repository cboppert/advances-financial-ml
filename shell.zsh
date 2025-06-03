# Source this from your main `.zshrc`
# Run from Mac OS 15.5 with ZShell

# Since learning, leaving in open for now
# But convention I believe is .pyenv or something
export DEFAULT_PY_VENV_DIR=py-venv

activatePyVenv () {
  local envDir="${1:-$DEFAULT_PY_VENV_DIR}"
  local activateScript="./$envDir/bin/activate"

  source $activateScript
}
