#!/bin/bash
$update
echo "Hello $USER"
echo "beginning auto update $(date)"
sudo apt update
sudo apt upgrade
sudo apt autoremove
sudo apt autoclean
echo "completed at $(date)"
echo "took $timer seconds"
echo "1.reboot"
echo "2.shut down"
echo "3. exit script"
read -p "what do you want to do? "  choice
if [ $choice == "1" ]
then
	echo "rebooting"
	sudo shutdown -r now
elif [ $choice == "2" ]
then
        echo "shuting down"
	sudo shutdown -h now
elif [ $choice == "3" ]
then
	echo "exiting script"
	exit
else 
	echo "assuming you wanted to exit script"
fi
