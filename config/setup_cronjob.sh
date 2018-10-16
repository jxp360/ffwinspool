#!/bin/bash

crontab -l > tmpcron

#Set up cront job for updating stats
#Let's do it once Wednesday Morning, once Friday Morning, 3xSunday (morning, 4pm, 8pm), Monday Morning, Tuesday Morning
echo "37 08 * * 1,2,3,5,7 /opt/ffwinspool/ffwinspool/scripts/update_ops.sh" >> tmpcron
echo "37 16,20 * * 7 /opt/ffwinspool/ffwinspool/scripts/update_ops.sh" >> tmpcron
echo "37 00 * * 1 /opt/ffwinspool/ffwinspool/scripts/update_ops.sh" >> tmpcron

crontab tmpcron

rm tmpcron
