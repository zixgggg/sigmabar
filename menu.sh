#!/usr/bin/bash
echo -e "(1) install sigma_bar"
echo -e "(2) uninstall sigma_bar"
read -p "enter number:" i < /dev/tty
if [ "$i" = "1" ];then
	./install.sh
elif [ "$i" = "2" ];then
	./uninstall.sh
fi
