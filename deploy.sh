#!/bin/bash

# update the code to the latest revision
# TODO: Base this off tags so that its easier to revert code.
git pull

# setup environment variables

export CODE_HOME=/var/www/andrew749.github.io;

# build all necessary files

make -C $CODE_HOME db
make -C $CODE_HOME build_css

# restart the webserver
service apache2 restart

# setup this to run periodically
crontab $CODE_HOME/crontab
