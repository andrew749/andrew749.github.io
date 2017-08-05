#!/bin/bash

# setup environment variables

export CODE_HOME=/var/www/andrew749.github.io;

cd CODE_HOME;

# update the code to the latest revision
# TODO: Base this off tags so that its easier to revert code.
git pull

echo "Updated Code."

# build all necessary files

make -C $CODE_HOME db

echo "Built database."

make -C $CODE_HOME build_css

echo "Built css."

# restart the webserver
service apache2 restart

echo "Server reloaded."

# setup this to run periodically
crontab $CODE_HOME/crontab
