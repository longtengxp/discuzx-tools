#!/bin/bash

docker=$1

if [ "$docker" -eq 0 ]; then
    supervisord -c /home/kylin/Luntan/service-quant/deploy/supervisor_run.conf
else
    supervisorctl -c /home/kylin/Luntan/service-quant/deploy/supervisor_run.conf
fi
