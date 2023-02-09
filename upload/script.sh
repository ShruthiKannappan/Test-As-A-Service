#!/bin/bash
# Ask the user for login details
read -p 'Username: ' uservar
read -sp 'Password: ' passvar
read -p 'Project: ' Project
pytest --json-report -v $Project/
# pytest -v filename --json-report=genpreport.json
python3 post.py $uservar $passvar $(date "+%Y.%m.%d-%H.%M.%S") $Project
