
from setuptools import setup

setup(
    name='auto-activenv',
    install_requires = [
        'click',
    ],
    version='0.1.0',
    entry_points={
        'console_scripts': [
            'activenv=src.main:install'
        ]
    }
)

