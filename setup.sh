#!/usr/bin/env bash
# Simple setup script to install temporary venv into project directory to make cleaning up easier
if [ ! -d ./venv ]
then
    sudo easy_install pip
    pip install virtualenv
    virtualenv venv
    source ./venv/bin/activate
    # fabric so we can use fab commands
    pip install -r requirements.txt
else
    source ./venv/bin/activate
fi

