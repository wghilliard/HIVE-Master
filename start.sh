#/bin/bash

/usr/bin/mongod --fork --logpath /data/db/mongodb.log
/etc/init.d/rabbitmq-server restart
source /etc/lariatsoft_setup.sh
python /opt/master/runserver.py
