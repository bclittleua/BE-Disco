#!/bin/sh
cd "$(dirname "$0")";
CWD="$(pwd)"
echo $CWD
sudo python3 mbot.py
