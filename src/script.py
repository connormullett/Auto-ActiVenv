
# maybe add regex to base script
# so that all venvs work

base = '''
function cd() {
  builtin cd "$@"

  if [[ -z "$VIRTUAL_ENV" ]] ; then
      if [[ -d ./%s ]] ; then
        echo ":: Activating virtual environment"
        source ./%s/bin/activate
      fi
  else
      parentdir="$(dirname "$VIRTUAL_ENV")"
      if [[ "$PWD"/ != "$parentdir"/* ]] ; then
        echo ":: Deactivating virtual environment"
        deactivate
      fi
  fi
}
'''

def create_script(name):
    # TODO: add more arguments for greater custimization
    return base % (name, name)

