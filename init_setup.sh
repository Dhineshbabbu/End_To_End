echo [$(date)]: "START"

echo [$(date)]: "Creating ENV with python 3.11 version"

python3.11 -m venv env

echo [$(date)]: "Activating the Environment"

source env\\Scripts\\activate

echo [$(date)]: "Installing the dev requirement"

pip install -r requirements.txt

echo [$(date)]: "END"