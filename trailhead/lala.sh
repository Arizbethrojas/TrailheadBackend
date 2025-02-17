# Deactivate the virtual environment (if active)
deactivate

# Remove the current environment
rm -rf myenv

# Create a new virtual environment using Homebrew's Python 3
/opt/homebrew/bin/python3 -m venv myenv

# Activate the new virtual environment
source myenv/bin/activate

# Verify if the correct Python version is being used
which python
which pip

