from fbs import path
from fbs.cmdline import command
from os.path import dirname, abspath, exists
from pathlib import Path

import fbs.builtin_commands
import fbs.cmdline
import git


def generate_version():
    # Set the current commit hash on the git repository as revision number
    repo = git.Repo(search_parent_directories=True)
    sha = repo.head.object.hexsha
    ver_revision = repo.git.rev_parse(sha, short=7)

    # Write data
    Path('src/freeze/base/version').write_text(ver_revision)


@command
def freeze(debug=False):
    generate_version()
    fbs.builtin_commands.freeze(debug)


@command
def run():
    generate_version()
    fbs.builtin_commands.run()


if __name__ == '__main__':
    # Set project_dir
    project_dir = dirname(abspath(__file__)) + '/../'

    # Execute command
    fbs.cmdline.main(project_dir)
