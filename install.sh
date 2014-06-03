#!/usr/bin/env bash

# System requirements
sudo python install/install_system.py

# Project requirements
python install/install_project.py

# Python requirements
. env/bin/activate && sudo pip install -r requirements.txt
