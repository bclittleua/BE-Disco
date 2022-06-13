#!/bin/bash

sudo curl wttr.in/Tucson?format="%l+now:+%t+Sunrise:+%S+Sunset:+%s\n"|sed "s/°//g"|sudo tee /path/to/your/files/weather.txt
