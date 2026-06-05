#!/usr/bin/bash
rm $HOME/.local/bin/sigmabar
# read -p 可以直接印出提示字，並把輸入值存進 yn 變數
read -p "delete config path(rm -rf ~/.config/sigmabar/)? (y/N): " yn
if [ "$yn" = "y" ] || [ "$yn" = "Y" ]; then
    rm -rf "$HOME/.config/sigmabar/"
fi	
