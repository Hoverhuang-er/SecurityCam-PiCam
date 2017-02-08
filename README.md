# rpiPiCam board control script

##### Aim of this script is to control the rpiPiCam board to send messages on the PiCam network.
The expansion board is for raspberry pi mainboard and allows to use the [VPS](http://hoverhuang.com)

You can purchase the board on [Element14](http://sg.element14.com/buy-raspberry-pi?ICID=I-HP-PP-raspberrypi-bundle-boards-01).

Two python scripts are provided :

- sendPiCam.py sends data over the PiCam network.

- sendreceivePiCam.py sends data with a downlink message request. Downlink messages are 8 bytes long. BEWARE : PiCam operators may bill downlink messages, please refer to your contract.

##### Usage

'sendPiCam MESSAGE [path/to/serial]'
'sendreceivePiCam MESSAGE [path/to/serial]'
 
- MESSAGE is an HEXA encoded string; 2 to 24 characters representing 1 to 12 bytes.

- Second parameter an the optional path to the serial port, default is /dev/ttyAMA0.

Examples :
- 'sendPiCam 00AA55BF' : sends the 4 bytes 0x00 0xAA 0x55 0xBF
- 'sendPiCam CCDD /dev/ttyS0' : sends the 2 bytes 0xCC 0xDD over /dev/ttyS0
- 'sendreceivePiCam 0123456789' : sends the 5 bytes 0x01 0x23 0x45 0x67 0x89 with a downlink request

##### Prerequist

Disable Raspberry Pi terminal on serial port with raspi-config utility:

sudo raspi-config

9 Advanced Options >> A8 Serial >> NO

Install pyserial

sudo apt-get install python-serial

##### Pi3 requirements

In '/boot/config.txt' disable if present 'dtoverlay=pi3-miniuart-bt' by adding a '\#' character at line begining

Add if necessary :

dtoverlay=pi3-disable-bt

enable_uart=1

Then reboot : 

sudo reboot

Serial port to use is the script's default one : /dev/ttyAMA0

##### License

MIT License / read license.txt
