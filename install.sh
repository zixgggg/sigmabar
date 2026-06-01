#!/usr/bin/bash
git clone https://github.com/zixgggg/sigmabar.git
cd sigmabar/
cp sigmabar $HOME/.local/bin
mkdir $HOME/.config/sigmabar/
cp config.ini $HOME/.config/sigmabar/
echo "install complete,repository can delete"
