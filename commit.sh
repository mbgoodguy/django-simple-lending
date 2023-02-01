#!/bin/bash
datatime_now=`date "+%Y-%m-%d %H:%M"`
git config --global user.name "mbgoodguy"
git config --global user.email "nerooren4001@gmail.com"
git add *
git commit -m "$datatime_now"
git branch -M main
git push -u origin main
