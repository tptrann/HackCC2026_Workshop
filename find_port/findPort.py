#--------------------------------------------------
#---------------HackCC 2026 Workshop---------------
#-------Finding port that connects to ESP32--------
#--------------------------------------------------

import serial
import serial.tools.list_ports

if __name__ == "__main__":
    ports = serial.tools.list_ports.comports()
    for port in ports:
        # Indentify popular port in ESP32 (CP210x, CH340, USB Serial)
        if "CP210" in port.description or "CH340" in port.description or "USB" in port.description:
            print(port.device)
            