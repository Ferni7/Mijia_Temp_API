#!/usr/bin/env python3

# mitemp_bt library from here https://github.com/ratcashdev/mitemp/tree/master/mitemp_bt
# Install bluepy first
# sudo apt-get install libglib2.0-dev
# sudo pip install bluepy
# Run sudo blescan to get the MAC of your Mijia device
# Make sure flask and btlewrap is installed via pip3
# pip3 install flask
# pip3 install btlewrap

import argparse
import re
import logging
import sys

from flask import Flask, jsonify, request
from btlewrap import available_backends, BluepyBackend, GatttoolBackend, PygattBackend
from mitemp_bt.mitemp_bt_poller import MiTempBtPoller, MI_TEMPERATURE, MI_HUMIDITY, MI_BATTERY

def poll(mac):
    """Poll data from the sensor."""
    poller = MiTempBtPoller(mac, BluepyBackend)
    print("Getting data from Mi Temperature and Humidity Sensor with MAC: {}".format(mac))
    print("FW: {}".format(poller.firmware_version()))
    print("Name: {}".format(poller.name()))
    print("Battery: {}".format(poller.parameter_value(MI_BATTERY)))
    print("Temperature: {}".format(poller.parameter_value(MI_TEMPERATURE)))
    print("Humidity: {}".format(poller.parameter_value(MI_HUMIDITY)))

    return jsonify(name=poller.name(),
                   firmware=poller.firmware_version(),
                   battery=poller.parameter_value(MI_BATTERY),
                   temperature=poller.parameter_value(MI_TEMPERATURE),
                   humidity=poller.parameter_value(MI_HUMIDITY))

app = Flask(__name__)

@app.route('/device/<deviceid>', methods=['GET'])
def get_device(deviceid):
  return poll(deviceid)
