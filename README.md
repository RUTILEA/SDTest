# SDTest - Software Defined Test

[![version][version-badge]][link-github-release]
[![python][python-badge]][link-python]
[![license][license-badge]][file-license]

SDTest (Software-Defined Test) can be implemented (through embedding or installation) in all kinds of testing equipment 
or machinery. By performing image processing on a deep-learning basis, SDTests can be utilized in a wide range of fields 
such as industrial product manufacturing, pharmaceutical manufacturing, manufacturing of synthetic fibers and natural 
woven fabrics, infrastructure inspection, semiconductor manufacturing, sorting of agricultural products, and so on.

## License

Copyright (c) 2019 [RUTILEA, Inc.][link-rutilea]

This program is a free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3 or later as published by
the Free Software Foundation.

This program can be distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

## Getting Started
### Requirements

- **Operating Systems**
  - Windows 7 or later (64-bit)
  - Ubuntu 16.04 or later (64-bit)
  - macOS 10.12.6 (Sierra) or later (64-bit) (no GPU support)
- **Processors**
  - Intel or AMD x64 processor
  - [AVX (Advanced Vector Extensions) supported][link-cpu-avx]
- **GPU Cards (Optional)**
  - CUDA&trade;-enabled GPU card on Ubuntu or Windows
  - If the supported GPU is unavailable, CPU will be used instead
- **Disk**
  - Minimum: 1 GB of HDD space
  - Recommended: An SSD
- **RAM**
  - Minimum: 4 GB
  - Recommended: 8 GB
  - For Polyspace, 4 GB per core is recommended

### Installation

Download the latest [release][link-github-release] and run the installer.

## Development
### Dependencies

- git
- [Python][link-python-download] 3.6 with pip
- [Qt Designer][link-qt-designer]
- Any IDE: [PyCharm][link-pycharm], [IntelliJ IDEA][link-intellij] or 
  [VSCode][link-vscode] is recommended.

### Installation

- `git clone git@github.com:RUTILEA/SDTest.git` clones the repository into "SDTest" directory
- `cd SDTest`
- `python -m venv venv` creates a virtual environment in the project directory
- Activate the virtual environment as your OS:
    - On Mac/Linux: `source venv/bin/activate`
    - On Windows: `call venv\scripts\activate.bat`
- `pip install -r requirements/base.txt` installs the required libraries (most notably, fbs and PyQt5). If this produces errors, try `pip install wheel` first and try again.
- `pip install -r requirements/(YOUR-OS).txt` installs the additional required libraries for your operating system. Replace "(YOUR-OS)" in the command to any of `windows`, `mac` or `linux` before execution.

### Run the app
- `src\build.py run` executes the app and you can debug it on console

### Create an UI file (.ui)

1. Run Qt Designer and create an .ui file into [src/main/python/view/ui/][dir-view-ui].
2. After editing ui, convert the .ui file to .py file by the command `pyuic5 -o FILENAME.py FILENAME.ui` inside that 
   directory. Both .ui and .py files should be stored together there.
3. Create a python file into [src/main/python/view/][dir-view] with the same filename to handle ui behaviors.

### Create a static resource file (.qrc)

1. Run Qt Designer and create a .qrc file into [src/main/python/][dir-python].
2. After editing the resources, convert the .qrc file to .py file by the command 
   `pyrcc5 -o --import-from qrc FILENAME_rc.py FILENAME.qrc` inside that directory. Both .qrc and .py files should be 
   stored together there.

### Deployment
- `src\build.py freeze` turns the app's source code into a standalone executable. This creates the folder 
  `target/SDTest`. You can copy this directory to any other computer (with the same OS as yours) and run the app there.
- `src\build.py installer` generates the app's installer into `targets/`. On Windows, this would be an executable 
  called `SDTestSetup.exe`. Before you can use the installer command on Windows, please install [NSIS][link-nsis] and 
  add its installation directory to your `PATH` environment variable. 

#### Debugging of the standalone executable
- `src\build.py clean`
- `src\build.py freeze --debug`
- `./target/SDTest/SDTest.exe` executes the app and you can debug it on console like `src\build.py run`

#### Code-Sign the executables
- Both `freeze` and `installer` commands automatically code-sign the generated `.exe` files on Windows if the 
  certificate file exists. You must place a certificate file at `src/freeze/base/SDTest.pfx` first. Please note that 
  the file extension of the certificate must be `.pfx`, otherwise it may be shared in the PUBLIC repository.
- Currently automatic code-signing is only implemented for Windows. For others will be supported soon.

## Support
- Report issues on the [GitHub issue tracker][link-github-issues]
- Post questions to the [Contact form][link-contact]

<!-- Links -->
[link-rutilea]: https://www.rutilea.com
[link-contact]: https://www.rutilea.com/inquiery-form.html
[link-license]: http://www.gnu.org/licenses/
[link-cpu-avx]: https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#CPUs_with_AVX
[link-python]: https://www.python.org/downloads/release/python-360/
[link-python-download]: https://www.python.org/downloads/
[link-qt-designer]: https://build-system.fman.io/qt-designer-download
[link-pycharm]: https://www.jetbrains.com/pycharm/
[link-intellij]: https://www.jetbrains.com/idea/
[link-vscode]: https://code.visualstudio.com/
[link-nsis]: http://nsis.sourceforge.net/Main_Page
[link-github-issues]: https://github.com/RUTILEA/SDTest/issues
[link-github-pull-request]: https://help.github.com/articles/creating-a-pull-request/
[link-github-fork]: https://help.github.com/articles/fork-a-repo/
[link-github-release]: https://github.com/RUTILEA/SDTest/releases

<!-- Dirs/Files -->
[dir-src]: ./src/
[dir-python]: ./src/main/python/
[dir-view]: ./src/main/python/view/
[dir-view-ui]: ./src/main/python/view/ui/
[file-license]: ./LICENSE

<!-- Badges -->
[version-badge]: https://img.shields.io/badge/version-0.5.0-blue.svg
[python-badge]: https://img.shields.io/badge/python-3.6-blue.svg
[license-badge]: https://img.shields.io/badge/license-GPLv3-blue.svg
