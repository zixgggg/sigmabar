#!/usr/bin/bash
#curl https://raw.githubusercontent.com/zixgggg/sigmabar/refs/heads/main/install.sh
git clone https://github.com/zixgggg/sigmabar.git
cd sigmabar/
cp sigmabar $HOME/.local/bin
mkdir $HOME/.config/sigmabar/
cp config.ini $HOME/.config/sigmabar/

