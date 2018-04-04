#!/bin/sh

# install required dependencies
sudo apt-get install -y sass python-pip python

# install python dependencies
pip install -r requirements.txt
