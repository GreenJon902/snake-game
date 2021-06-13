from setuptools import setup

APP = ['Snake/main.py']
APP_NAME = "Snake"
DATA_FILES = ["snake/AldotheApache.ttf", "snake/icon.png"]
OPTIONS = {'argv_emulation': True,
           "iconfile": "icons/icon.icns"}
AUTHOR = "GreenJon902"
VERSION = "1.0.0"

setup(
    app=APP,
    name=APP_NAME,
    author=AUTHOR,
    version=VERSION,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
