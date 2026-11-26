################################################################
# Install:
# * python.exe -m pip install pypiwin32
# * python.exe -m pip install wmi
#
# Usage:
# * !! Make sure windows-hardware-monitor is running !!
# * python basicwmi.py
################################################################

import wmi

hwmon = wmi.WMI(namespace="root\windows-hardware-monitor")
sensors = hwmon.Sensor(SensorType="Control")

for s in sensors:
	print s
