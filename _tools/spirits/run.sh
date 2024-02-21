#!/bin/bash

set -e

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
black main.py
yamllint spirits.yaml
python main.py $@
deactivate
rm -rf env
