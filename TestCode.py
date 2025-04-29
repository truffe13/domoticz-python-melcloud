# version JP

import json
from Domoticz import Connection
from Domoticz import Device
from Domoticz import Devices
from Domoticz import Parameters

# your params

Parameters['Mode1'] = '0'# GMT Offset
Parameters['Mode2'] = '20' # refresh interval
Parameters['Mode3'] = '7' # Language (French)
Parameters['Username'] = 'xxxxxxxxxxxxx@xxx.xxx'  # your account mail
Parameters['Password'] = 'xxxxxxxxxx'             # your account password
Parameters['Mode6'] = '62'                     # Basic Debug


def runtest(plugin):

    plugin.onStart()

    # First Heartbeat
    plugin.onHeartbeat()

    # Second Heartbeat
    plugin.onHeartbeat()

    exit(0)
