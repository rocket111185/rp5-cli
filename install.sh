#!/bin/bash

printf 'Deleting the temporary files...\n';
./uninstall.sh;
printf 'Installation of needed packages...\n';
sudo pip3 install bs4 lxml tabulate google;
printf 'Preparing the files...\n';
sudo mkdir /usr/share/rp5-cli;
sudo cp rp5-cli /usr/bin;
sudo cp *.py /usr/share/rp5-cli;
printf 'Done.\n'