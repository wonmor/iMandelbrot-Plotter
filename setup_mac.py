from setuptools import setup

import os

import platform

'''
THIS IS A PRESET FILE FOR THE PY2APP PACKAGE THAT GENERATES A .APP FILE FOR MACOS PLATFORMS
WRITTEN BY JOHN SEONG
'''

# Get the relative path of the file name that is inputted into a function...
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

# Define the constants that will be used in generating the .app file... first one being where the main python file is located at...
APP = [get_path('src/mandelbrot.py')]
# Data files indicate where all the files associated to a python script... such as an image or a music file...
DATA_FILES = [get_path('src')]
OPTIONS = {
    'argv_emulation': False, # Originally, 'open up a window on start' should turn on when argv_emulation is True, but here it's opposite for some reason... think is a bug...
    'site_packages': True, # Site packages = Dependencies
    'iconfile': get_path('icon.icns'), # Set the path of where the icon file is
    'packages': ['pygame', 'AppKit', 'pkg_resources'], # List all the dependencies
    'plist': {
        'CFBundleName': 'iMandelbrot',
        'CFBundleDisplayName': 'iMandelbrot',
        'CFBundleSpokenName': 'iMandelbrot',
        'CFBundleShortVersionString':'1.2.0',
        'CFBundleVersion': '1.2.0',
        'CFBundleIconName': 'iMandelbrot-Default',
    } # These info. will be written on the plist file where it dictates the properties of a macOS app
}

# This is the default function that will run when trying to convert a python script to an .app file...
setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    license="MIT",
    author="John Seong",
)

'''
TIPS & TRICKS

HOW TO FIX JARACO ISSUE: https://github.com/pyinstaller/pyinstaller/issues/6564
PY2APP KNOWN ISSUES: JARACO, MACOS PATH, IMPORT APPKIT AND PKG RESOURCES
CURRENT APP ISSUE: CAN'T RUN NATIVELY ON ARM64 MACS
HOW TO MAKE IT RUN ON ROSETTA 2 BY DEFAULT: https://apple.stackexchange.com/questions/438044/how-do-i-make-my-python-app-default-to-run-in-rosetta
PYGAME DOES NOT SUPPORT ARM64 MACS!

HOW TO THIN OUT A UNIVERSAL BINARY APP (BASICALLY CONVERTING A UNIVERSAL APP TO EITHER INTEL-ONLY OR M1-ONLY APP):
https://eclecticlight.co/2020/07/30/instant-weight-loss-how-to-strip-universal-apps/
https://ss64.com/osx/lipo.html
REMOVE ARM VERSION FROM UNIVERAL BINARY: lipo -remove arm64 Mints.app/Contents/MacOS/Mints -output 


██████╗░██╗░░░██╗░██████╗░░█████╗░███╗░░░███╗███████╗  ██████╗░░█████╗░███████╗░██████╗  ███╗░░██╗░█████╗░████████╗
██╔══██╗╚██╗░██╔╝██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██╔══██╗██╔════╝██╔════╝  ████╗░██║██╔══██╗╚══██╔══╝
██████╔╝░╚████╔╝░██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║██║░░██║█████╗░░╚█████╗░  ██╔██╗██║██║░░██║░░░██║░░░
██╔═══╝░░░╚██╔╝░░██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║██║░░██║██╔══╝░░░╚═══██╗  ██║╚████║██║░░██║░░░██║░░░
██║░░░░░░░░██║░░░╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ██████╔╝╚█████╔╝███████╗██████╔╝  ██║░╚███║╚█████╔╝░░░██║░░░
╚═╝░░░░░░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ╚═════╝░░╚════╝░╚══════╝╚═════╝░  ╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░

░██████╗██╗░░░██╗██████╗░██████╗░░█████╗░██████╗░████████╗  ░█████╗░██████╗░███╗░░░███╗  ███╗░░░███╗░█████╗░░█████╗░
██╔════╝██║░░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝  ██╔══██╗██╔══██╗████╗░████║  ████╗░████║██╔══██╗██╔══██╗
╚█████╗░██║░░░██║██████╔╝██████╔╝██║░░██║██████╔╝░░░██║░░░  ███████║██████╔╝██╔████╔██║  ██╔████╔██║███████║██║░░╚═╝
░╚═══██╗██║░░░██║██╔═══╝░██╔═══╝░██║░░██║██╔══██╗░░░██║░░░  ██╔══██║██╔══██╗██║╚██╔╝██║  ██║╚██╔╝██║██╔══██║██║░░██╗
██████╔╝╚██████╔╝██║░░░░░██║░░░░░╚█████╔╝██║░░██║░░░██║░░░  ██║░░██║██║░░██║██║░╚═╝░██║  ██║░╚═╝░██║██║░░██║╚█████╔╝
╚═════╝░░╚═════╝░╚═╝░░░░░╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░

██╗░░░██╗███████╗████████╗██╗
╚██╗░██╔╝██╔════╝╚══██╔══╝██║
░╚████╔╝░█████╗░░░░░██║░░░██║
░░╚██╔╝░░██╔══╝░░░░░██║░░░╚═╝
░░░██║░░░███████╗░░░██║░░░██╗
░░░╚═╝░░░╚══════╝░░░╚═╝░░░╚═╝

'''