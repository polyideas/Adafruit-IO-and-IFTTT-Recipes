#!/usr/bin/python

# Heavily modified sample script originally written by Tony DiCola.
# Modifed by Jay Doscher (jay@polyideas.com) for use with IFTTT
# and Adafruit IO using the Pysolar library

# Simple example of switching a toggle and reading a slider value from Adafruit IO with the REST API client.
# This script reads the predictive-sunset-value for the desired elevation of the sun
# When the sun falls below predictive-sunset-value, it switches on the toggle predictive-sunset-toggle.


#Pysolar 0.6 is needed to work with Python 2.x
# Download and install manually from https://pypi.python.org/pypi/Pysolar/0.6
import Pysolar, datetime

# Import Adafruit IO REST client.
from Adafruit_IO import Client

# Set to your Adafruit IO key.
ADAFRUIT_IO_KEY = 'your_adafruit_IO_key_here'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_KEY)

# Pull from Adafruit IO
data1 = aio.receive('predictive-sunset-latitude')
data2 = aio.receive('predictive-sunset-longitude')
data3 = aio.receive('predictive-sunset-value')
data4 = aio.receive('predictive-sunset-triggered')

def getsolarangle():
        solarangle = Pysolar.GetAltitude(float('{0}'.format(data1.value)), float('{0}'.format(data2.value)), datetime.datetime.utcnow())
        return solarangle

if (getsolarangle() <= int('{0}'.format(data3.value))) and (('{0}'.format(data4.value)) == "NO"):
        aio.send('predictive-sunset-toggle', "ON")
        aio.send('predictive-sunset-triggered', "YES")
