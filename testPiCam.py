#import packages
from imutils.video import VideoStream
from smbus import SMBus
import datetime
import argparse
import imutils
import time
import cv2
from opencv import config
from opencv import face
from lcd import backlight
from lcd import screen
from lcd import display
from PiCam import sendPiCam

#send message
sgfx = sendPiCam.PiCam("/dev/ttyAMA0")
message = "bed room"
sgfx.sendMessage(message)
