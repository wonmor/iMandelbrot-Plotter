from setuptools import setup

import os

import platform

def get_path(filename):
        name = os.path.splitext(filename)[0]
        ext = os.path.splitext(filename)[1]

        # For macOS only...
        if platform.system() == "Darwin" or platform.system() == "Darwin":
            from AppKit import NSBundle
            file = NSBundle.mainBundle().pathForResource_ofType_(name, ext)
            return file or os.path.realpath(filename)
        else:
            return os.path.realpath(filename)

APP = [get_path('src/mandelbrot.py')]
DATA_FILES = [get_path('src')]
OPTIONS = {
    'argv_emulation': False, # Originally, 'open up a window on start' should turn on when argv_emulation is True, but here it's opposite for some reason... think is a bug...
    'site_packages': True,
    'iconfile': get_path('icon.icns'),
    'packages': ['pygame', 'AppKit', 'pkg_resources'],
    'plist': {
        'CFBundleName': 'iMandelbrot',
        'CFBundleDisplayName': 'iMandelbrot',
        'CFBundleSpokenName': 'iMandelbrot',
        'CFBundleShortVersionString':'1.2.0',
        'CFBundleVersion': '1.2.0',
        'CFBundleIconName': 'iMandelbrot-Default',
    }
}
setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

'''
TIPS & TRICKS

HOW TO FIX JARACO ISSUE: https://github.com/pyinstaller/pyinstaller/issues/6564
PY2APP KNOWN ISSUES: JARACO, MACOS PATH, IMPORT APPKIT AND PKG RESOURCES
CURRENT APP ISSUE: CAN'T RUN NATIVELY ON ARM64 MACS
HOW TO MAKE IT RUN ON ROSETTA 2 BY DEFAULT: https://apple.stackexchange.com/questions/438044/how-do-i-make-my-python-app-default-to-run-in-rosetta
'''