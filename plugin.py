#
# MELCloud Plugin
# Author:     Gysmo, 2017 Updated by mitkodotcom 2022 Updated by Dalonsic 2023, Update by truffe13 2025
#
# Release Notes:
# Version: 0.9.2 :
#        - fanspeed issue fixed
#
# Version: 0.9.1 :
#        - fix a problem with language setting,  fixed to bulgarian. thks to fdmekinabo for solving this issue
#
# Version: 0.9.0
#        - add Energy counters (1 per unit) based on CurrentEnergyConsumed (experimental)
#        - Change levels labels to be more explicit (than numbers)  according  MELCloud API : https://github.com/OlivierZal/melcloud-api
#        - Maximum Refresh rate at 5mn, >= 5m causes TCP connection to disconnect and reconnect and minimum set to 20s
#        - Remove clear list_units before a new connexion to MELCloud to avoid conflict with possible simultaneous commands
#
# Version: 0.8.5
# v0.8.5: truffe13 : change connection method to melcloud to melcloud_send_data_json
#                    MELCloud API : https://github.com/OlivierZal/melcloud-api
##
# Release Notes:
# v0.8.4: #38 Addon - Added extra polling intervals to prevent erorr 429 (to manay requests)
# v0.8.3: #37 Fixed - Fix for Error: MelCloud: _plugin.onMessage(Connection, Data) compatibility with Mitkodotcom version
# v0.8.2: #37 Fixed - Try to fix Error: MelCloud: _plugin.onMessage(Connection, Data)
# v0.8.1: #37 Fixed - Clear list_units before a new connexion to MELCloud to prevent duplicate unit's logs
# v0.8.0: #37 Fixed - Heartbeat define to every seconds (old value : 25)
#         #37 Addon - Add Mode2 parameter to select heartbeat interval for unit infos
#         #35 Fixed - 'setPicID' referenced before assignment
#         #30 Addon - Add Mode3 parameter to Multilanguage support
# v0.7.9: #27 Fixed - login to melcloud, updated device discovery logic (using mitkodotcom send json logic thank's to him)

# Author:     Gysmo, 2017 Updated by nonolk 2022
# Version: 0.8.0
#
# Release Notes:
# v0.8.0: Fixed ondisconnect not clearing the list of devices, replaced selecctor switch by setpoiont (previsous devices must be delted and recreated manually) with code cleanup in progress
# v0.7.9: Fixed login to melcloud, updated device discovery logic (using mitkodotcom send json logic thank's to him)


# v0.7.8: Code optimization
# v0.7.7: Add test on domoticz dummy
# v0.7.6: Fix Auto Mode added
# v0.7.5: Fix somes bugs and improve https connection
# v0.7.4: Sometimes update fail. Update function sync to avoid this
# v0.7.3: Add test in login process and give message if there is some errors
# v0.7.2: Correct bug for onDisconnect, add timeoffset and add update time for last command in switch text
# v0.7.1: Correct bug with power on and power off
# v0.7 : Use builtin https support to avoid urllib segmentation fault on binaries
# v0.6.1 : Change Update function to not crash with RPI
# v0.6 : Rewrite of the module to be easier to maintain
# v0.5.1: Problem with device creation
# v0.5 : Upgrade code to be compliant wih new functions
# v0.4 : Search devices in floors, areas and devices
# v0.3 : Add Next Update information, MAC Address  and Serial Number
#         Add Horizontal vane
#         Add Vertival vane
#         Add Room Temp
# v0.2 : Add sync between Domoticz devices and MELCloud devices
#        Usefull if you use your Mitsubishi remote
# v0.1 : Initial release
"""
<plugin key="MELCloud" version="0.9.0" name="MELCloud plugin" author="gysmo mitkodotcom dalonsic truffe13" wikilink="http://www.domoticz.com/wiki/Plugins/MELCloud.html" externallink="http://www.melcloud.com">
    <params>
        <param field="Username" label="Email" width="200px" required="true" />
        <param field="Password" label="Password" width="200px" required="true" password="true"/>
        <param field="Mode1" label="GMT Offset" width="75 px">
            <options>
                <option label="-12" value="-12"/>
                <option label="-11" value="-11"/>
                <option label="-10" value="-10"/>
                <option label="-9" value="-9"/>
                <option label="-8" value="-8"/>
                <option label="-7" value="-7"/>
                <option label="-6" value="-6"/>
                <option label="-5" value="-5"/>
                <option label="-4" value="-4"/>
                <option label="-3" value="-3"/>
                <option label="-2" value="-2"/>
                <option label="-1" value="-1"/>
                <option label="0" value="0" default="true" />
                <option label="+1" value="+1"/>
                <option label="+2" value="+2"/>
                <option label="+3" value="+3"/>
                <option label="+4" value="+4"/>
                <option label="+5" value="+5"/>
                <option label="+6" value="+6"/>
                <option label="+7" value="+7"/>
                <option label="+8" value="+8"/>
                <option label="+9" value="+9"/>
                <option label="+10" value="+10"/>
                <option label="+11" value="+11"/>
                <option label="+12" value="+12"/>
            </options>
        </param>
        <param field="Mode2" label="Refresh interval" width="100px">
            <options>
                <option label="20s"  value="20"/>
                <option label="1m" value="60"/>
                <option label="2m" value="120"/>
                <option label="4m"  value="240" default="true"/>
                <option label="5m" value="300"/>
            </options>
        </param>
        <param field="Mode3" label="Language" width="100px">
            <options>
                <option label="English"     value="0" default="true"/>
                <option label="Български"   value="1"/>
                <option label="Čeština"     value="2"/>
                <option label="Dansk"       value="3"/>
                <option label="Deutsch"     value="4"/>
                <option label="Eesti"       value="5"/>
                <option label="Español"     value="6"/>
                <option label="Français"    value="7"/>
                <option label="Հայերեն"     value="8"/>
                <option label="Latviešu"    value="9"/>
                <option label="Lietuvių"    value="10"/>
                <option label="Magyar"      value="11"/>
                <option label="Nederlands"  value="12"/>
                <option label="Norwegian"   value="13"/>
                <option label="Polski"      value="14"/>
                <option label="Português"   value="15"/>
                <option label="Русский"     value="16"/>
                <option label="Suomi"       value="17"/>
                <option label="Svenska"     value="18"/>
                <option label="Italiano"    value="19"/>
                <option label="Українська"  value="20"/>
                <option label="Türkçe"      value="21"/>
                <option label="Ελληνικά"    value="22"/>
                <option label="Hrvatski"    value="23"/>
                <option label="Română"      value="24"/>
                <option label="Slovenščina" value="25"/>
                <option label="Shqip"       value="26"/>
            </options>
        </param>
        <param field="Mode6" label="Debug" width="150px">
            <options>
                <option label="None" value="0"  default="true" />
                <option label="Python Only" value="2"/>
                <option label="Basic Debugging" value="62"/>
                <option label="Basic+Messages" value="126"/>
                <option label="Connections Only" value="16"/>
                <option label="Connections+Python" value="18"/>
                <option label="Connections+Queue" value="144"/>
                <option label="All" value="-1"/>
            </options>
        </param>
    </params>
</plugin>
"""

import json
import Domoticz
import os


class BasePlugin:

    heartbeat = 0
    melcloud_conn = None
    melcloud_baseurl = "app.melcloud.com"
    melcloud_port = "443"
    melcloud_key = None
    melcloud_state = "Not Ready"

    melcloud_urls = {}
    melcloud_urls["login"] = "/Mitsubishi.Wifi.Client/Login/ClientLogin"
    melcloud_urls["list_unit"] = "/Mitsubishi.Wifi.Client/User/ListDevices"
    melcloud_urls["set_unit"] = "/Mitsubishi.Wifi.Client/Device/SetAta"
    melcloud_urls["unit_info"] = "/Mitsubishi.Wifi.Client/Device/Get"

    list_units = []
    dict_devices = {}

    list_switchs = []
    list_switchs.append({"id": 1, "name": "Mode", "typename": "Selector Switch",
                         "image": 16, "levels": "Off|Warm|Cold|Vent|Dry|Auto"})
    list_switchs.append({"id": 2, "name": "Fan", "typename": "Selector Switch",
                         "image": 7, "levels": "1-VerySlow|2-Slow|3-Moderate|4-Fast|5-VeryFast|Auto|Silence"})
    list_switchs.append({"id": 3, "name": "Temp", "typename": "Thermostat"})
    list_switchs.append({"id": 4, "name": "Vane Horizontal", "typename": "Selector Switch",
                         "image": 7, "levels": "LeftWards|CenterLeft|Center|CenterRight|RightWards|Swing|Auto"})
    list_switchs.append({"id": 5, "name": "Vane Vertical", "typename": "Selector Switch",
                         "image": 7, "levels": "UpWards|MidHigh|Middle|MidLow|DownWards|Swing|Auto"})
    list_switchs.append({"id": 6, "name": "Room Temp", "typename": "Temperature"})
    list_switchs.append({"id": 7, "name": "Unit Infos", "typename": "Text"})
    list_switchs.append({"id": 8, "name": "KWh", "typename": "Counter"})



    domoticz_levels = {}
    domoticz_levels["mode"] = {"0": 0, "10": 1, "20": 3, "30": 7, "40": 2, "50": 8}
    domoticz_levels["mode_pic"] = {"0": 9, "10": 15, "20": 16, "30": 7, "40": 11, "50": 11}
    domoticz_levels["fan"] = {"0": 1, "10": 2, "20": 3, "30": 4, "40": 5, "50": 0, "60": 1}
    domoticz_levels["vaneH"] = {"0": 1, "10": 2, "20": 3, "30": 4, "40": 5, "50": 12, "60": 0}
    domoticz_levels["vaneV"] = {"0": 1, "10": 2, "20": 3, "30": 4, "40": 5, "50": 7, "60": 0}

    # currentEnergyConsumed
    list_units_kWh = []
    runCounterkWhValue = 1200+3 # 20mn
    runCounterkWh = runCounterkWhValue
    unitsJustCreated = False
    plugin_path = ""
    # For tests
    #valeur_test=[20,21,22,23,24,25,10,11,12,13,0,1,2,3]
    #nvaleur_test=14
    #ivaleur_test=0


    runCounter = 0
    runAgain = 6
    enabled = False

    def __init__(self):
        return

    def onStart(self):
        self.runCounter = 18 # Run 18s after login then Mode 2 parameter
        self.runCounterkWh = 10 # Run 10s after login then  runCounterkWhValue
        self.list_units.clear()

        self.plugin_path = os.path.dirname(os.path.abspath(__file__))

        Domoticz.Heartbeat(1)
        
        if Parameters["Mode6"] != 0:
            Domoticz.Debugging(int(Parameters["Mode6"]))
        
        # Start connection to MELCloud
        self.melcloud_conn = Domoticz.Connection(Name="MELCloud", Transport="TCP/IP",
                                                 Protocol="HTTPS", Address=self.melcloud_baseurl,
                                                 Port=self.melcloud_port)
        if __name__ == "__main__":
            self.melcloud_conn.bp = self
        self.melcloud_conn.Connect()
        return True

    def onStop(self):
        self.list_units.clear()
        Domoticz.Log("Goobye from MELCloud plugin.")

    def onConnect(self, Connection, Status, Description):
        if Status == 0:
            Domoticz.Log("MELCloud connection OK")
            self.melcloud_state = "READY"
            self.melcloud_login()
        else:
            Domoticz.Log("MELCloud connection FAIL: "+Description)

    def extractDeviceData(self, device):
        if device['DeviceName'] not in self.dict_devices.keys():
            self.dict_devices['DeviceName'] = device
            # print('\n---device\n', device, '\n---\n')
            if 'HasEnergyConsumedMeter' in device['Device'].keys():
                ## For tests
                #if device['DeviceName'] == 'Chambre' :
                #    device['Device']['CurrentEnergyConsumed']=self.valeur_test[self.ivaleur_test]
                #    if self.ivaleur_test < (self.nvaleur_test-1) :
                #        self.ivaleur_test += 1
                #    else :
                #        self.ivaleur_test=0
                #    return device['Device']['CurrentEnergyConsumed']
                #else:
                #    return device['Device']['CurrentEnergyConsumed']
                # Return value in Wh ( not kWh)
                return device['Device']['CurrentEnergyConsumed']
            else:
                return 0

    def searchUnits(self, building, scope, idoffset):
        # building["Structure"]["Devices"]
        # building["Structure"]["Areas"]
        # building["Structure"]["Floors"]
        nr_of_Units = 0
        cEnergyConsumed = 0
        # Search in scope

        def oneUnit(self, device, idoffset, nr_of_Units, cEnergyConsumed, building, scope):
            self.melcloud_add_unit(device, idoffset)
            idoffset += len(self.list_switchs)
            nr_of_Units += 1
            self.extractDeviceData(device)
            currentEnergyConsumed = self.extractDeviceData(device)
            cEnergyConsumed += currentEnergyConsumed
            text2log = "Found {} in building {} {} CurrentEnergyConsumed {} kWh"
            text2log = text2log.format(device['DeviceName'],
                                       building["Name"],
                                       scope, currentEnergyConsumed)
            Domoticz.Log(text2log)
            return (nr_of_Units, idoffset, cEnergyConsumed)

        for item in building["Structure"][scope]:
            if scope == 'Devices':
                if item["Type"] == 0:
                    (nr_of_Units, idoffset, cEnergyConsumed) = oneUnit(self, item, idoffset,
                                                                       nr_of_Units, cEnergyConsumed,
                                                                       building, scope)
            elif scope in ('Areas', 'Floors'):
                for device in item["Devices"]:
                    (nr_of_Units, idoffset, cEnergyConsumed) = oneUnit(self, device, idoffset,
                                                                       nr_of_Units, cEnergyConsumed,
                                                                       building, scope)
                if scope == 'Floors':
                    for device in item["Devices"]:
                             (nr_of_Units, idoffset, cEnergyConsumed) = oneUnit(self, device, idoffset,
                                                                   nr_of_Units, cEnergyConsumed,
                                                                   building, scope)
                    for area in item["Areas"]:
                          for device in area["Devices"]:
                             (nr_of_Units, idoffset, cEnergyConsumed) = oneUnit(self, device, idoffset,
                                                                   nr_of_Units, cEnergyConsumed,
                                                                   building, scope)
                
        text2log = 'Found {} devices in building {} {} of the Type 0 (Aircondition) CurrentEnergyConsumed {:.0f} kWh'
        text2log = text2log.format(str(nr_of_Units), building["Name"], scope, cEnergyConsumed)
        Domoticz.Log(text2log)
        
        return (nr_of_Units, idoffset, cEnergyConsumed)

    # Store / Read offset to apply when reading melcloud Devices value
    def melcloud_store_offset (self,name, kwh):
        melcloud_file =  self.plugin_path + "/melcloud_offset_values_"+ name + ".txt"
        Domoticz.Debug("Write files" + melcloud_file)
        with open(melcloud_file, "w") as f:
                f.write(str(kwh))

    def melcloud_read_offset (self,name):
        melcloud_file = self.plugin_path + "/melcloud_offset_values_"+ name + ".txt"
        Domoticz.Debug("Read files" + melcloud_file)
        with open(melcloud_file, "r") as f:
                return f.read()


    # Store / Read offset to apply to Domoticz counters
    def melcloud_store_domcounter_offset (self,name, kwh):
        melcloud_file =  self.plugin_path + "/melcloud_offset_dvalues_"+ name + ".txt"
        Domoticz.Debug("Write files" + melcloud_file)
        with open(melcloud_file, "w") as f:
                f.write(str(kwh))

    def melcloud_read_domcounter_offset (self,name):
        melcloud_file = self.plugin_path + "/melcloud_offset_dvalues_"+ name + ".txt"
        Domoticz.Debug("Read files" + melcloud_file)
        with open(melcloud_file, "r") as f:
                return f.read()


    def updatekWh(self, building ):
        # building["Structure"]["Devices"]
        # building["Structure"]["Areas"]
        # building["Structure"]["Floors"]
        scope = 'Devices'
        found = False
        Domoticz.Debug ("updatekWh : ")
        for item in building["Structure"][scope]:
            melcloud_unit_kWh = {}
            if item['Type'] == 0 :
                currentkWh = self.extractDeviceData(item)
            Domoticz.Debug ("updatekWh : 1 ")
            for unit_kWh in self.list_units_kWh:
                Domoticz.Debug ("updatekWh : 2 ")
                if unit_kWh ['name'] == item['DeviceName']:
                    Domoticz.Debug ("updatekWh : " + str( item['DeviceName']) + str( currentkWh))
                    if (currentkWh >= unit_kWh['Offset_DevClim']) :
                        unit_kWh['Current_kWh'] = currentkWh
                        Domoticz.Debug("updatekWh " + item['DeviceName'] + " with retrieved value : " +  str(currentkWh))
                    else :
                        # in case of retrieved value < Offset_DevClim value
                        # For instance a clim Reset counter ?
                        Domoticz.Debug("updatekWh 4 : " + item['DeviceName'] + " Current kWh : " + str(currentkWh) + " < Offset_DevClim : " + str(unit_kWh['Offset_DevClim']) + " Offset_DomkWh : " + str(unit_kWh['Offset_DomkWh']))

                        unit_kWh['Offset_DomkWh'] += unit_kWh['Current_kWh'] - unit_kWh['Offset_DevClim']
                        unit_kWh['Offset_DevClim'] = currentkWh
                        unit_kWh['Current_kWh'] = currentkWh

                        self.melcloud_store_offset(item['DeviceName'],unit_kWh['Offset_DevClim'])
                        self.melcloud_store_domcounter_offset(item['DeviceName'],unit_kWh['Offset_DomkWh'])


                        Domoticz.Debug("updatekWh 4 : " + item['DeviceName'] + " Current kWh : " + str(currentkWh) + " < Offset_DevClim : " + str(unit_kWh['Offset_DevClim']) + " Offset_DomkWh : " + str(unit_kWh['Offset_DomkWh']))

                    found = True
            if found == False :
                melcloud_unit_kWh['name'] = item['DeviceName']
                melcloud_unit_kWh['Current_kWh']= currentkWh
                if self.unitsJustCreated == True:
                    melcloud_unit_kWh['Offset_DevClim']= currentkWh
                    melcloud_unit_kWh['Offset_DomkWh'] = 0
                    self.melcloud_store_offset(item['DeviceName'],currentkWh)
                    self.melcloud_store_domcounter_offset(item['DeviceName'],0)
                else:
                    melcloud_unit_kWh['Offset_DevClim'] = float(self.melcloud_read_offset (item['DeviceName']))
                    melcloud_unit_kWh['Offset_DomkWh'] = float(self.melcloud_read_domcounter_offset (item['DeviceName']))

                # print("\n melcloud_unit_kWh : " , melcloud_unit_kWh )
                self.list_units_kWh.append(melcloud_unit_kWh)



        return

    def updateUnitkWh(self, unitName ):
        kWh = 0
        for unit_kWh in self.list_units_kWh:
            if unit_kWh ['name'] == unitName:
                kWh = unit_kWh['Current_kWh'] - unit_kWh['Offset_DevClim'] + unit_kWh['Offset_DomkWh']
                Domoticz.Debug("updateUnitkWh  , Domoticz Counter : " + str(kWh) + " , Current_kWh : " + str(unit_kWh['Current_kWh']) + " , Offset_DomkWh : " + str(unit_kWh['Offset_DomkWh']) + " , Offset_DevClim : " + str(unit_kWh['Offset_DevClim']) )
        return kWh

    def onMessage(self, Connection, Data):
        Status = int(Data["Status"])
        if Status == 200:
            strData = Data["Data"].decode("utf-8", "ignore")
            response = json.loads(strData)
            Domoticz.Debug("JSON REPLY: "+str(response))
            if self.melcloud_state == "LOGIN":
                if ("ErrorId" not in response.keys()) or (response["ErrorId"] is None):
                    Domoticz.Log("MELCloud login successfull")
                    self.melcloud_key = response["LoginData"]["ContextKey"]
                    self.melcloud_units_init()
                elif response["ErrorId"] == 1:
                    Domoticz.Log("MELCloud login fail: check login and password")
                    self.melcloud_state = "LOGIN_FAILED"
                else:
                    Domoticz.Log("MELCloud failed with unknown error "+str(response["ErrorId"]))
                    self.melcloud_state = "LOGIN_FAILED"

            elif self.melcloud_state == "UNITS_INIT":
                idoffset = 0
                Domoticz.Log(" Find " + str(len(response)) + " buildings")
                for building in response:
                    Domoticz.Log("Find " + str(len(building["Structure"]["Areas"])) +
                                 " areas in building "+building["Name"])
                    Domoticz.Log("Find " + str(len(building["Structure"]["Floors"])) +
                                 " floors in building "+building["Name"])
                    # Search in devices
                    (nr_of_Units, idoffset, cEnergyConsumed) = self.searchUnits(building, "Devices", idoffset)
                    # Search in areas
                    (nr_of_Units, idoffset, cEnergyConsumed) = self.searchUnits(building, "Areas", idoffset)
                    # Search in floors
                    (nr_of_Units, idoffset, cEnergyConsumed) = self.searchUnits(building, "Floors", idoffset)
                self.melcloud_create_units()
            elif self.melcloud_state == "UNIT_INFO":
                Domoticz.Log(" UNIT INFO")
                for unit in self.list_units:
                    if unit['id'] == response['DeviceID']:
                        Domoticz.Log("Update unit {0} information.".format(unit['name']))
                        unit['power'] = response['Power']
                        unit['op_mode'] = response['OperationMode']
                        unit['room_temp'] = response['RoomTemperature']
                        unit['set_temp'] = response['SetTemperature']
                        unit['set_fan'] = response['SetFanSpeed']
                        unit['vaneH'] = response['VaneHorizontal']
                        unit['vaneV'] = response['VaneVertical']
                        unit['kWh']= self.updateUnitkWh(unit['name'])
                        unit['next_comm'] = False
                        Domoticz.Debug("Heartbeat unit info: "+str(unit))
                        self.domoticz_sync_switchs(unit)
            elif self.melcloud_state == "SET":
                for unit in self.list_units:
                    if unit['id'] == response['DeviceID']:
                        date, time = response['NextCommunication'].split("T")
                        hours, minutes, sec = time.split(":")
                        mode1 = Parameters["Mode1"]
                        if mode1 == '0':
                            mode1 = '+0'
                        sign = mode1[0]
                        value = mode1[1:]
                        Domoticz.Debug("TIME OFFSET :" + sign + value)
                        if sign == "-":
                            hours = int(hours) - int(value)
                            if hours < 0:
                                hours = hours + 24
                        else:
                            hours = int(hours) + int(value)
                            if hours > 24:
                                hours = hours - 24
                        next_comm = date + " " + str(hours) + ":" + minutes + ":" + sec
                        unit['next_comm'] = "Update for last command at "+next_comm
                        Domoticz.Log("Next update for command: " + next_comm)
                        self.domoticz_sync_switchs(unit)
            elif self.melcloud_state == "DEV_INFO":
                Domoticz.Log(" DEV INFO")
                idoffset = 0
                Domoticz.Log(" Retrieve " + str(len(response)) + " buildings")
                for building in response:
                    self.updatekWh(building)
            else:
                Domoticz.Log("State not implemented:" + self.melcloud_state)
        else:
            Domoticz.Log("MELCloud receive unknonw message with error code "+Data["Status"])

    def onCommand(self, Unit, Command, Level, Hue):
        Domoticz.Log("onCommand called for Unit " + str(Unit) +
                     ": Parameter '" + str(Command) + "', Level: " + str(Level))
        # ~ Get switch function: mode, fan, temp ...
        switch_id = Unit
        while switch_id > 8:
            switch_id -= 8
        switch_type = self.list_switchs[switch_id-1]["name"]
        # ~ Get the unit in units array
        current_unit = False
        for unit in self.list_units:
            if (unit['idoffset'] + self.list_switchs[switch_id-1]["id"]) == Unit:
                current_unit = unit
                break
        if switch_type == 'Mode':
            if Level == 0:
                flag = 1
                current_unit['power'] = 'false'
                Domoticz.Log("Switch Off the unit "+current_unit['name'] +
                             " with ID offset " + str(current_unit['idoffset']))
                Devices[1+current_unit['idoffset']].Update(nValue=0, sValue=str(Level), Image=9)
                Devices[2+current_unit['idoffset']].Update(nValue=0,
                                                           sValue=str(Devices[Unit + 1].sValue))
                Devices[3+current_unit['idoffset']].Update(nValue=0,
                                                           sValue=str(Devices[Unit + 2].sValue))
                Devices[4+current_unit['idoffset']].Update(nValue=0,
                                                           sValue=str(Devices[Unit + 3].sValue))
                Devices[5+current_unit['idoffset']].Update(nValue=0,
                                                           sValue=str(Devices[Unit + 4].sValue))
                Devices[6+current_unit['idoffset']].Update(nValue=0,
                                                           sValue=str(Devices[Unit + 5].sValue))
            elif Level == 10:
                Domoticz.Log("Set to WARM the unit "+current_unit['name'])
                Devices[1+current_unit['idoffset']].Update(nValue=1, sValue=str(Level), Image=15)
            elif Level == 20:
                Domoticz.Log("Set to COLD the unit "+current_unit['name'])
                Devices[1+current_unit['idoffset']].Update(nValue=1, sValue=str(Level), Image=16)
            elif Level == 30:
                Domoticz.Log("Set to Vent the unit "+current_unit['name'])
                Devices[1+current_unit['idoffset']].Update(nValue=1, sValue=str(Level), Image=7)
            elif Level == 40:
                Domoticz.Log("Set to Dry the unit "+current_unit['name'])
                Devices[1+current_unit['idoffset']].Update(nValue=1, sValue=str(Level), Image=11)
            elif Level == 50:
                Domoticz.Log("Set to Auto the unit "+current_unit['name'])
                Devices[1+current_unit['idoffset']].Update(nValue=1, sValue=str(Level), Image=11)
            if Level != 0:
                flag = 1
                current_unit['power'] = 'true'
                self.melcloud_set(current_unit, flag)
                flag = 6
                current_unit['power'] = 'true'
                current_unit['op_mode'] = self.domoticz_levels['mode'][str(Level)]
                Devices[2+current_unit['idoffset']].Update(nValue=1,
                                                           sValue=str(Devices[Unit + 1].sValue))
                Devices[3+current_unit['idoffset']].Update(nValue=1,
                                                           sValue=str(Devices[Unit + 2].sValue))
                Devices[4+current_unit['idoffset']].Update(nValue=1,
                                                           sValue=str(Devices[Unit + 3].sValue))
                Devices[5+current_unit['idoffset']].Update(nValue=1,
                                                           sValue=str(Devices[Unit + 4].sValue))
                Devices[6+current_unit['idoffset']].Update(nValue=1,
                                                           sValue=str(Devices[Unit + 5].sValue))
        elif switch_type == 'Fan':
            flag = 8
            current_unit['set_fan'] = self.domoticz_levels['fan'][str(Level)]
            Domoticz.Log("Change FAN  to value {0} for {1} ".format(self.domoticz_levels['fan'][str(Level)], current_unit['name']))
            Devices[Unit].Update(nValue=Devices[Unit].nValue, sValue=str(Level))
        elif switch_type == 'Temp':
            flag = 4
            Domoticz.Log("Change Temp to " + str(Level) + " for "+unit['name'])
            current_unit['set_temp'] = str(Level)
            Devices[Unit].Update(nValue=Devices[Unit].nValue, sValue=str(Level))
        elif switch_type == 'Vane Horizontal':
            flag = 256
            current_unit['vaneH'] = self.domoticz_levels['vaneH'][str(Level)]
            Domoticz.Log("Change Vane Horizontal to value {0} for {1}".format(self.domoticz_levels['vaneH'][str(Level)], current_unit['name']))
            Devices[Unit].Update(Devices[Unit].nValue, str(Level))
        elif switch_type == 'Vane Vertical':
            flag = 16
            current_unit['vaneV'] = self.domoticz_levels['vaneV'][str(Level)]
            Domoticz.Log("Change Vane Vertical to value {0} for {1}".format(self.domoticz_levels['vaneV'][str(Level)], current_unit['name']))
            Devices[Unit].Update(Devices[Unit].nValue, str(Level))
        else:
            Domoticz.Log("Device not found")
        self.melcloud_set(current_unit, flag)
        return True

    def onNotification(self, Name, Subject, Text, Status, Priority, Sound, ImageFile):
        Domoticz.Log("Notification: " + Name + "," + Subject + "," + Text + "," +
                     Status + "," + str(Priority) + "," + Sound + "," + ImageFile)

    def onDisconnect(self, Connection):
        self.melcloud_state = "Not Ready"
        Domoticz.Log("MELCloud has disconnected")
        self.runAgain = 1

    def onHeartbeat(self):
        Domoticz.Debug("onHeartbeat")
        # Device info for getting kWh
        self.runCounterkWh = self.runCounterkWh - 1
        self.runCounter = self.runCounter - 1

        if (self.runCounterkWh <= 0):
            Domoticz.Debug("List units to get kWh")
            self.runCounterkWh = self.runCounterkWhValue
            if (self.melcloud_conn is not None and (self.melcloud_conn.Connecting() or self.melcloud_conn.Connected())):
                if self.melcloud_state != "LOGIN_FAILED":
                    Domoticz.Debug("Current MEL Cloud Key ID:"+str(self.melcloud_key))
                    Domoticz.Debug(" Get kWh")
                    self.melcloud_device_info()

        # Unit info
        if (self.runCounter <= 0):
            Domoticz.Debug("Poll unit")
            self.runCounter = int(Parameters['Mode2'])
            if (self.melcloud_conn is not None and (self.melcloud_conn.Connecting() or self.melcloud_conn.Connected())):
                if self.melcloud_state != "LOGIN_FAILED":
                    Domoticz.Debug("Current MEL Cloud Key ID:"+str(self.melcloud_key))
                    for unit in self.list_units:
                        self.melcloud_get_unit_info(unit)

        else:
            Domoticz.Debug("Polling unit in " + str(self.runCounter) + " heartbeats.")
        # Connection
        if (self.melcloud_conn is None or self.melcloud_state == "LOGIN_FAILED" or self.melcloud_state == "Not Ready"):
            self.runAgain = self.runAgain - 1
            if self.runAgain <= 0:
                Domoticz.Debug("[MELCloud][v0.9.0][onHeartbeat] Reconnection... ("+str(self.melcloud_state)+")")
                # self.list_units.clear()
                self.melcloud_conn = Domoticz.Connection(Name="MELCloud", Transport="TCP/IP", Protocol="HTTPS",
                                                         Address=self.melcloud_baseurl, Port=self.melcloud_port)
                self.melcloud_key = None
                self.melcloud_conn.Connect()
                self.runAgain = 6
                self.runCounter = 0
            else:
                Domoticz.Debug("MELCloud https failed. Reconnected in "+str(self.runAgain)+" heartbeats.")

    def melcloud_create_units(self):
        # Domoticz.Log("Units infos " + str(self.list_units))
        if len(Devices) == 0 :
            # Init Devices
            # Creation of switches
            Domoticz.Log("Find " + str(len(self.list_units)) + " devices in MELCloud")
            for device in self.list_units:
                Domoticz.Log("Creating device: " + device['name'] + " with melID " + str(device['id']))
                for switch in self.list_switchs:
                    # Create switchs
                    if switch["typename"] == "Selector Switch":
                        switch_options = {"LevelNames": switch["levels"], "LevelOffHidden": "false", "SelectorStyle": "1"}
                        Domoticz.Device(Name=device['name'] + " - "+switch["name"], Unit=switch["id"]+device['idoffset'],
                                        TypeName=switch["typename"], Image=switch["image"], Options=switch_options, Used=1).Create()
                    elif switch["typename"] == "Thermostat":
                        Domoticz.Device(Name=device['name'] + " - "+switch["name"], Unit=switch["id"]+device['idoffset'],
                                        Type=242, Subtype=1, Used=1).Create()
                    elif switch["typename"] == "Counter":
                        Domoticz.Device(Name=device['name'] + " - "+switch["name"], Unit=switch["id"]+device['idoffset'],
                                        Type=113, Used=1 ).Create()
                    else:
                        Domoticz.Device(Name=device['name'] + " - "+switch["name"], Unit=switch["id"]+device['idoffset'],
                                        TypeName=switch["typename"], Used=1).Create()
            self.unitsJustCreated = True
        else:
            self.unitsJustCreated = False


    def melcloud_send_data(self, url, values, state):
        self.melcloud_state = state
        if self.melcloud_key is not None:
            headers = {'Content-Type': 'application/x-www-form-urlencoded;',
                       'Host': self.melcloud_baseurl,
                       'User-Agent': 'Domoticz/1.0',
                       'X-MitsContextKey': self.melcloud_key}
            if state == "SET":
                self.melcloud_conn.Send({'Verb': 'POST', 'URL': url, 'Headers': headers, 'Data': values})
            else:
                self.melcloud_conn.Send({'Verb': 'GET', 'URL': url, 'Headers': headers, 'Data': values})
        else:
            headers = {'Content-Type': 'application/x-www-form-urlencoded;',
                       'Host': self.melcloud_baseurl,
                       'User-Agent': 'Domoticz/1.0'}
            self.melcloud_conn.Send({'Verb': 'POST', 'URL': url, 'Headers': headers, 'Data': values})
        return True

    def melcloud_send_data_json(self, url, values, state):
        self.melcloud_state = state
        if self.melcloud_key is not None:
            headers = {'Content-Type': 'application/json;',
                       'Host': self.melcloud_baseurl,
                       'User-Agent': 'Domoticz/1.0',
                       'X-MitsContextKey': self.melcloud_key}
            if state == "SET":
                self.melcloud_conn.Send({'Verb': 'POST', 'URL': url, 'Headers': headers, 'Data': values})
            else:
                self.melcloud_conn.Send({'Verb': 'GET', 'URL': url, 'Headers': headers, 'Data': values})
        else:
            headers = {'Content-Type': 'application/json;',
                       'Host': self.melcloud_baseurl,
                       'User-Agent': 'Domoticz/1.0'}
            self.melcloud_conn.Send({'Verb': 'POST', 'URL': url, 'Headers': headers, 'Data': values})
        return True

    def melcloud_login(self):
        lang = Parameters.get("Mode3", "0") # Default to English (0) if not set
        post_fields = "Appversion:'{0}',CaptchaResponse:{1},Email:'{2}',Language:{3},Password:'{4}',Persist:{5}"
        post_fields = post_fields.format("1.23.4.0", "null", str(Parameters["Username"]), lang, str(Parameters["Password"]), "true")
        self.melcloud_send_data_json(self.melcloud_urls["login"], "{" + post_fields + "}", "LOGIN")
        return True

    def melcloud_add_unit(self, device, idoffset):
        melcloud_unit = {}
        melcloud_unit['name'] = device["DeviceName"]
        melcloud_unit['id'] = device["DeviceID"]
        melcloud_unit['macaddr'] = device["MacAddress"]
        melcloud_unit['sn'] = device["SerialNumber"]
        melcloud_unit['building_id'] = device["BuildingID"]
        melcloud_unit['power'] = ""
        melcloud_unit['op_mode'] = ""
        melcloud_unit['room_temp'] = ""
        melcloud_unit['set_temp'] = ""
        melcloud_unit['set_fan'] = ""
        melcloud_unit['vaneH'] = ""
        melcloud_unit['vaneV'] = ""
        melcloud_unit['kWh'] = ""
        melcloud_unit['next_comm'] = False
        melcloud_unit['idoffset'] = idoffset
        # avoid duplicate
        found = False
        for unit in self.list_units:
            if unit['id'] == melcloud_unit['id'] :
                found = True
        if found == False :
            self.list_units.append(melcloud_unit)
        #Domoticz.Log('\n LIST UNITS '+ str(self.list_units))

    def melcloud_units_init(self):
        self.melcloud_send_data(self.melcloud_urls["list_unit"], None, "UNITS_INIT")
        return True

    def melcloud_device_info(self):
        self.melcloud_send_data(self.melcloud_urls["list_unit"], None, "DEV_INFO")
        return True

    def melcloud_set_urlencode(self, unit, flag):
        post_fields = 'Power={0}&DeviceID={1}&OperationMode={2}&SetTemperature={3}&SetFanSpeed={4}&VaneHorizontal={5}&VaneVertical={6}&EffectiveFlags={7}&HasPendingCommand=true'
        post_fields = post_fields.format(str(unit['power']).lower(), unit['id'], unit['op_mode'], unit['set_temp'], unit['set_fan'], unit['vaneH'], unit['vaneV'], flag)
        Domoticz.Debug("SET COMMAND SEND {0}".format(post_fields))
        self.melcloud_send_data(self.melcloud_urls["set_unit"], post_fields, "SET")

    def melcloud_set(self, unit, flag):
        post_fields = "'Power':{0},'DeviceID':{1},'OperationMode':{2},'SetTemperature':{3},'SetFanSpeed':{4},'VaneHorizontal':{5},'VaneVertical':{6},'EffectiveFlags':{7},'HasPendingCommand':true"
        post_fields = post_fields.format(str(unit['power']).lower(), unit['id'], unit['op_mode'], unit['set_temp'], unit['set_fan'], unit['vaneH'], unit['vaneV'], flag)
        Domoticz.Debug("SET COMMAND SEND {0}".format(post_fields))
        self.melcloud_send_data_json(self.melcloud_urls["set_unit"], "{"+post_fields+"}", "SET")

    def melcloud_get_unit_info(self, unit):
        url = self.melcloud_urls["unit_info"] + "?id=" + str(unit['id']) + "&buildingID=" + str(unit['building_id'])
        self.melcloud_send_data(url, None, "UNIT_INFO")

    def domoticz_sync_switchs(self, unit):
        # Default value in case of problem
        setDomFan = 0
        setDomVaneH = 0
        setDomVaneV = 0
        
        if unit['next_comm'] is not False:
            Devices[self.list_switchs[6]["id"]+unit["idoffset"]].Update(nValue=1, sValue=str(unit['next_comm']))
        else:
            if unit['power']:
                #Domoticz.Log(str(unit['power']))
                switch_value = 1
                for level, mode in self.domoticz_levels["mode"].items():
                    if mode == unit['op_mode']:
                        setModeLevel = level
            else:
                switch_value = 0
                setModeLevel = '0'
            for level, pic in self.domoticz_levels["mode_pic"].items():
                if level == setModeLevel:
                    setPicID = pic
                    Devices[self.list_switchs[0]["id"]+unit["idoffset"]].Update(nValue=switch_value,
                                                                                sValue=setModeLevel,
                                                                                Image=setPicID)
            for level, fan in self.domoticz_levels["fan"].items():
                if fan == unit['set_fan']:
                    setDomFan = level
                    Devices[self.list_switchs[1]["id"]+unit["idoffset"]].Update(nValue=switch_value,
                                                                                sValue=setDomFan)
            Devices[self.list_switchs[2]["id"]+unit["idoffset"]].Update(nValue=switch_value,
                                                                    sValue=str(unit['set_temp']))
            for level, vaneH in self.domoticz_levels["vaneH"].items():
                if vaneH == unit['vaneH']:
                    setDomVaneH = level
                    Devices[self.list_switchs[3]["id"]+unit["idoffset"]].Update(nValue=switch_value,
                                                                                sValue=setDomVaneH)
            for level, vaneV in self.domoticz_levels["vaneV"].items():
                if vaneV == unit['vaneV']:
                    setDomVaneV = level
                    Devices[self.list_switchs[4]["id"]+unit["idoffset"]].Update(nValue=switch_value,
                                                                                sValue=setDomVaneV)
            Devices[self.list_switchs[5]["id"]+unit["idoffset"]].Update(nValue=switch_value,
                                                                        sValue=str(unit['room_temp']))
            Devices[self.list_switchs[7]["id"]+unit["idoffset"]].Update(nValue=switch_value,
                                                                        sValue=str(unit['kWh']))


global _plugin
_plugin = BasePlugin()


def onStart():
    """ On start """
    global _plugin
    _plugin.onStart()


def onStop():
    global _plugin
    """ On stop """
    _plugin.onStop()


def onConnect(Connection, Status, Description):
    global _plugin
    """ On connect """
    _plugin.onConnect(Connection, Status, Description)


def onMessage(Connection, Data):
    global _plugin
    """ On message """
    _plugin.onMessage(Connection, Data)


def onCommand(Unit, Command, Level, Hue):
    global _plugin
    """ On command """
    _plugin.onCommand(Unit, Command, Level, Hue)


def onNotification(Name, Subject, Text, Status, Priority, Sound, ImageFile):
    """ On notification """
    global _plugin
    _plugin.onNotification(Name, Subject, Text, Status, Priority, Sound, ImageFile)


def onDisconnect(Connection):
    """ On disconnect """
    global _plugin
    _plugin.onDisconnect(Connection)


def onHeartbeat():
    """ Heartbeat """
    global _plugin
    _plugin.onHeartbeat()


if __name__ == "__main__":
    from Domoticz import Parameters
    from Domoticz import Devices
    from TestCode import runtest

    runtest(BasePlugin())
    exit(0)
