from fbs.cmdline import command
from fbs.builtin_commands import prompt_for_value
from os.path import dirname, abspath, exists
from pathlib import Path
from fbs_runtime import platform
from main.python.model.fbs import AppInfo

import fbs.builtin_commands
import fbs.cmdline
import git
import os


def generate_version():
    # Set the current commit hash on the git repository as revision number
    repo = git.Repo(search_parent_directories=True)
    sha = repo.head.object.hexsha
    ver_revision = repo.git.rev_parse(sha, short=7)

    # Write data
    Path(project_dir + 'src/freeze/base/version').write_text(ver_revision)


def code_signing():
    app_name = AppInfo().app_name()
    path_cert = project_dir + 'src\\freeze\\base\\' + app_name + '.pfx'
    path_program_exe = project_dir + 'target\\' + app_name + '\\' + app_name + '.exe'
    path_program_installer = project_dir + 'target\\' + app_name + 'Setup.exe'
    code_signing_timestamp_url = "http://timestamp.comodoca.com/authenticode"

    # Code Signing for Windows executable
    if platform.is_windows():
        cert_password = prompt_for_value('Password for your code signing certificate', default='')

        if exists(path_program_exe) and exists(path_cert):
            os.system('signtool sign /f "' + path_cert + '" ' +
                      '/p ' + cert_password + ' /t ' + code_signing_timestamp_url + ' /d "' + app_name + '" ' +
                      path_program_exe)

        if exists(path_program_installer) and exists(path_cert):
            os.system('signtool sign /f "' + path_cert + '" ' +
                      '/p ' + cert_password + ' /t ' + code_signing_timestamp_url + ' /d "' + app_name + '" ' +
                      path_program_installer)


@command
def freeze(debug=False):
    generate_version()
    fbs.builtin_commands.freeze(debug)
    code_signing()


@command
def installer():
    generate_version()
    # fbs.builtin_commands.installer()
    code_signing()


@command
def run():
    generate_version()
    fbs.builtin_commands.run()


if __name__ == '__main__':
    # Set project_dir
    project_dir = dirname(abspath(__file__)) + '/../'

    # Execute command
    fbs.cmdline.main(project_dir)
