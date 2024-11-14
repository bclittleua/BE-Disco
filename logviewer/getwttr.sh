#!/bin/bash
# FOR RPi LINUX! save as getwttr.sh
sudo curl wttr.in/Tucson?format="%l+now:+%t+Sunrise:+%S+Sunset:+%s\n"|sudo tee /home/pi/bin/weather.txt


''' 
#!/bin/bash
# FOR OSX! save as: getwttr.sh
# Fetch weather information and save it to weather.txt
curl wttr.in/Tucson?format="%l+now:+%t+Sunrise:+%S+Sunset:+%s\n" | tee /Users/yourusername/Desktop/weather.txt
'''


'''
# Fetch weather information and save it to weather.txt
# FOR WINDOWS! save as: getwttr.bat
@echo off
curl "wttr.in/Tucson?format=%l+now:+%t+Sunrise:+%S+Sunset:+%s" > C:\Users\YOURUSERNAME\Desktop\weather.txt
echo Weather data saved to weather.txt
'''
