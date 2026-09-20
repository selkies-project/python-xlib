# Distutils script for python-xlib

from setuptools import setup

setup(
    install_requires=['six>=1.10.0'],
    packages=[
        'Xlib',
        'Xlib.ext',
        'Xlib.keysymdef',
        'Xlib.protocol',
        'Xlib.support',
        'Xlib.xobject'
    ],
)
