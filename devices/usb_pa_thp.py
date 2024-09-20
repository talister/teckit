# -*- coding: utf-8 -*-
#
# DogRatIan USB-PA THP sensor
# Copyright (c) 2024-2024, Tim Lister (talister)

import json
import serial

class thp_sensor():
    temp = 38.5
    data = ""
    ppm = 0.0
    status_flag = 1
    temp_status_flag = 1
    global exttemp
    global rh
    global hectopascals
    global tec_rtd
    global calibration_params


    def __init__(self, port, name):
        print ("\033[1;5H \033[0;33mCOM[\033[1m%s\033[0;33m] : USB-PA BME280\033[0;39m" % port)
        self.inst = serial.Serial(port=port, baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=1)
        self.name = name
        self.inst.write(b'\n')

    def getTHP(self):
        error = 0
        # Request all values in JSON
        self.inst.write(b'GJSON\n')
        line = self.inst.readline()
        try:
            data = json.loads(line.decode("Ascii"))
            self.exttemp = data['T']
            self.rh = data['H']
            self.press = data['P']
        except json.JSONDecodeError:
            error = 1
        return (error,self.exttemp,self.rh,self.press)