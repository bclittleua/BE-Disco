#!/bin/bash
# should run this script once an hour when motion is active

# find and delete .jpg older than 5 mins
sudo find /var/lib/motion -name '*.jpg' -mmin +5 -delete

# find and delete .avi older than 45 mins
sudo find /var/lib/motion -name '*.avi' -mmin +45 -delete
