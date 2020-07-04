#!/usr/bin/env python3

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
