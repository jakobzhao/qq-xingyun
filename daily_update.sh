#!/bin/sh
# free_mememory.sh
# insurance data collection program
# Oct. 22, 2015
# Harvard Kennedy School
# Bo Zhao
# bo_zhao@hks.harvard.edu
sudo rm /home/qqcrawler/crawler.log
echo "the daily log has been deleted"
cd /home/bo/qqcrawler
sudo git checkout --force
sudo git pull
echo "the program has updated to the latest version"
