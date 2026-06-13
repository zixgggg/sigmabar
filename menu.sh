#!/usr/bin/bash
echo "(1) install sigma_bar"
echo "(2) uninstall sigma_bar"
read -p "enter number:" i < /dev/tty
if [ "$i" = "1" ];then
	#./install.sh
	curl -fsSL https://raw.githubusercontent.com/zixgggg/sigmabar/refs/heads/main/install.sh|bash
	echo "installing"
elif [ "$i" = "2" ];then
	#./uninstall.sh
	curl -fsSL https://raw.githubusercontent.com/zixgggg/sigmabar/refs/heads/main/uninstall.sh|bash
	echo "uninstalling"

fi
