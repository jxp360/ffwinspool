#!/bin/bash

source /opt/ffwinspool/.virtualenvs/production/bin/activate

export DJANGO_SETTINGS_MODULE="ffwinpool.settings"

#refresh our internal databases
python /opt/ffwinspool/ffwinspool/scripts/update_scores.py "$@" >> /opt/ffwinspool/logs/update.log 2>&1
now=$(date +"%D::%T")
echo "$now  ******************************** Finished running FF Wins Pool Update Script" >> /opt/ffwinspool/logs/update.log 2>&1

