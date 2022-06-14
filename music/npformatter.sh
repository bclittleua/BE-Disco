#!/bin/bash
 
 sed "s/^.*title': '//" nowplayingraw | sed "s/'}.*//g" > nowplaying
 #format of nowplayingraw = [{'source':'**url**','title':'**vid_title**'}, <discord info>]
 #this removes everything before and after the vid_title, then outputs to 'nowplaying'
