import socket
import subprocess
import time

# put your wifi ssid here
WIFI_SSID = "borma"

def isUp():
	try:
		socket.create_connection((socket.gethostbyname("google.com"), 80), 2)
		return True
	except:
		return False


def connect():
	subprocess.check_output("netsh wlan connect ssid=" + WIFI_SSID + " name=" + WIFI_SSID)

def disconnect():
	subprocess.check_output("netsh wlan disconnect")

def reconnect():
	try:
		disconnect()
		connect()
	except:
		try:
			connect()
		except:
			pass

def loop():
	while True:
		time.sleep(1)

		if isUp():
			print "Network is up"
		else:
			print "Network is down, reconnecting"
			reconnect()

loop()