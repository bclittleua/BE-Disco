#!/bin/bash
sudo find /var/lib/motion -name '*.jpg' -mmin +5 -delete
sudo find /var/lib/motion -name '*.avi' -mmin +45 -delete
