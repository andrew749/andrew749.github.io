#!/bin/bash

# setup environment variables

export CODE_HOME=/var/app;

# build all necessary files

make -C $CODE_HOME db
make -C $CODE_HOME build_css

# restart the webserver
service nginx restart

crontab $CODE_HOME/crontab
