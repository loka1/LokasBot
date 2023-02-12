#!/bin/bash
#set -euo pipefail

. "$HOME"/repos/.venvs/lokas-bot-scripts/bin/activate

export PYWIKIBOT_DIR="$HOME/repos"

python3  "$HOME"/repos/tasks/requests/link_replacement/read.py
python3  "$HOME"/repos/tasks/requests/template_distribution/read.py
python3  "$HOME"/repos/tasks/requests/add_category/read.py

# Exit the script after running all the Python files
exit 0
