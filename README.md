# SDTest - Software Defined Test

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

A Software-Defined Testing Software

## License

Copyright (c) 2019 [RUTILEA, Inc.](https://www.rutilea.com)

This program is a free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3 or later as published by
the Free Software Foundation.

This program can be distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

## Requirements

### For software users
- **Operating Systems**
  - Windows 8 or higher
  - Mac OS 10 or higher
- **Processors**
  - Recommended: Any Intel or AMD x86-64 processor
- **Disk**
  - Minimum: 1 GB of HDD space
  - Recommended: An SSD
- **RAM**
  - Minimum: 4 GB
  - Recommended: 8 GB
  - For Polyspace, 4 GB per core is recommended

### For contributers
- [Python](https://www.python.org/downloads/) 3.6 with pip
- [Qt Designer](https://build-system.fman.io/qt-designer-download)
- Any IDE: [PyCharm](https://www.jetbrains.com/pycharm/), [IntelliJ IDEA](https://www.jetbrains.com/idea/) or 
  [VSCode](https://code.visualstudio.com/) is recommended.

## Installation
- For software users: Download the latest [release](https://github.com/RUTILEA/SDTest/releases) and run the installer.
- For contributers: Execute following commands for creating your development environment:
    ```sh
    # Clone the repository into "SDTest" directory
    $ git clone git@github.com:RUTILEA/SDTest.git
    $ cd SDTest
    
    # Create a virtual environment in the project directory:
    $ python -m venv venv
    
    # Activate the virtual environment:
    # On Mac/Linux:
    $ source venv/bin/activate
    # On Windows:
    $ call venv\scripts\activate.bat
    
    # Install the required libraries (most notably, fbs and PyQt5):
    # (If this produces errors, try pip install wheel first.)
    $ pip install -r requirements.txt
    ```

## Contribute

### Debug application

Use the following command to run the app on debug mode:

```sh
# Activate the virtual environment:
# On Mac/Linux:
$ source venv/bin/activate
# On Windows:
$ call venv\scripts\activate.bat

# Run application
$ fbs run
```

### Create a standalone executable

Use the following command to turn the app's source code into a standalone executable:

```sh
# Activate the virtual environment:
# On Mac/Linux:
$ source venv/bin/activate
# On Windows:
$ call venv\scripts\activate.bat

$ fbs freeze
```

This creates the folder `target/SDTest`. You can copy this directory to any other computer 
(with the same OS as yours) and run the app there.

To debug this, add the `--debug` flag to freeze:
```sh
# Activate the virtual environment:
# On Mac/Linux:
$ source venv/bin/activate
# On Windows:
$ call venv\scripts\activate.bat

$ fbs clean
$ fbs freeze --debug
```

### Develop UI files

#### Create an UI file (.ui)

1. Run Qt Designer and create an .ui file into `src/main/python/view/ui/`.
2. After editing ui, convert the .ui file to .py file by the command `pyuic5 -o FILENAME.py FILENAME.ui` inside that 
   directory. Both .ui and .py files should be stored together there.
3. Create a python file into `src/main/python/view/` with the same filename to handle ui behaviors.

#### Create a static resource file (.qrc)

1. Run Qt Designer and create a .qrc file into `src/main/python/`.
2. After editing the resources, convert the .qrc file to .py file by the command 
   `pyrcc5 -o FILENAME.py FILENAME.qrc` inside that directory. Both .qrc and .py files should be stored together there.

## Support
- Report issues on the [GitHub issue tracker](https://github.com/RUTILEA/SDTest/issues)
- Post questions to the [Contact form](https://www.rutilea.com/inquiery-form.html)
