# domoticz-python-melcloud
## History

This is a fork of https://github.com/jf67-07/domoticz-python-melcloud.git  which itself is a merge of 

  https://github.com/tuk90/domoticz-python-melcloud.git
and
  https://github.com/nonolk/domoticz-python-melcloud.git
  
The forks was because the connection to Melcloud was not functionning. However the version proposed by jf67-07  seeems the most advanced release providing :

- Thermostat (Temperature set point)
- possibility to select the refresh rate avoiding Melcloud to be overloaded and then possible crash of domoticz. 
- Version 0.9 adds one energy counter per unit (experimental) based on CurrentEnergyConsumed (if device has HasEnergyConsumedMeter == True) 
- Now 8 devices per unit : Mode, Fan, Vane Vertical, Vane Horizontal, temp, temp set point, info, Energy

TestCode has been modified adding required parameters. 


## Installation
1. Clone repository into your domoticz plugins folder
```
cd domoticz/plugins
git clone https://github.com/truffe13/domoticz-python-melcloud.git
Make sure that the plugin directory is writable : the plugin creates 2 files per unit to store offset counter values
```
2. Restart domoticz
3. Make sure that "Accept new Hardware Devices" is enabled in Domoticz settings
4. Go to "Hardware" page and add new item with type "MELCloud plugin"
## Plugin update

```
cd domoticz/plugins/Melcloud
git pull
```
## Testing without Domoticz
1. Clone repository
```
cd scripts/tests
git clone https://github.com/truffe13/domoticz-python-melcloud.git
```
2. Edit TestCode.py
```
Parameters['Username'] = 'xxxxxxxxxxxxx@xxx.xxx'  # your account mail
Parameters['Password'] = 'xxxxxxxxxx'             # your account password
```
3. Run test
```
python3 plugin.py
```
