#!/bin/bash

sudo curl wttr.in/Tucson?format="%l+now:+%t+Sunrise:+%S+Sunset:+%s\n"|sudo tee weather.txt
