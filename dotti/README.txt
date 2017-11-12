sudo apt-get update
sudo apt-get install python-pip python-dev ipython

sudo apt-get install bluetooth libbluetooth-dev
sudo pip install pybluez
sudo pip install pygatt

sudo setcap cap_net_raw+ep /usr/bin/hcitool

hciconfig

hcitool -i hci0 lescan 
