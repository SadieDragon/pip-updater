
from re import split, UNICODE
from subprocess import run

# Grab the list of packages that need to be updated
outdated_packages = run(['pip', 'list', '-o'], capture_output=True, text=True)
# PEP 8 greatness
outdated_packages = outdated_packages.stdout.strip().split('\n')

# Append pip to be the first package, and remove the blank lines
outdated_packages = ['pip'] + outdated_packages[2:]

# Go through, and announce then update the packages.
for index, package in [*enumerate(outdated_packages)]:
    # Pip doesn't have a version or type plonked on.
    update_notif = 'pip was updated.'
    # Everything else does.
    if index != 0:
        # Remove the excess whitespace
        # https://stackoverflow.com/a/28607213
        pkg_vs_type = " ".join(split("\s+", package, flags=UNICODE))
        # And then split it (PEP8, woo!)
        pkg_vs_type = pkg_vs_type.split(' ')

        # Update the package variable to just be the package name
        package = pkg_vs_type[0]

        # The notif will be '{package} (from {vs1} to {vs2}) (type: {type})
        update_notif = (f'{package} (from {pkg_vs_type[1]} to'
                        f' {pkg_vs_type[2]}) (type: {pkg_vs_type[3]})')

    # Upgrade the package to the latest version.
    run(['pip', 'install', '-U', package])