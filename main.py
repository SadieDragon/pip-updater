from subprocess import run

# Print the packages that need to be updated.
# Also print that pip was obviously updated first.
print('On top of pip, the following packages were updated:\n\n')
# print(run(['pip', 'list', '-o']))  # DEBUG

# Maybe this works? (to) Upgrade pip first.
run(['pip', 'install', '-U', 'pip'])

# pip install -U `pip list --outdated | awk 'NR>2 {print $1}'`
# Upgrade all outdated packages
run(['pip', 'install', '-U', "`pip list --outdated | awk 'NR>2 {print $1}'`"])