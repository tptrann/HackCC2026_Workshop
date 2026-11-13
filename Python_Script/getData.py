#-----------------------------------------------------------
#-------------------HackCC 2026 Workshop--------------------
#-------Reading data from ESP32 using serial library--------
#-----------------------------------------------------------

import serial
import sqlite3
import time
import datetime

# Variable
PORT = "COM3"           
BAUDRATE = 115200       # Make sure you use the same baudrate as in Arduino IDE
DATA_FILE = "data.db"   # Your database file 

if __name__ == "__main__":

    # Connect to database
    conn = sqlite3.connect(DATA_FILE)
    cursor = conn.cursor()

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS ultrasound_detection (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                time TEXT,
                object TEXT
            )
    """)

    cursor.execute("DELETE FROM ultrasound_detection")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='ultrasound_detection'")

    conn.commit()

    # Connect to ESP32
    try:    
        ser = serial.Serial(PORT, BAUDRATE, timeout = 1)
        time.sleep(2)
    except Exception as ex:
        print(f"Error: {ex}")
        exit()

    print("Ready to read data")

    # Read data from serial
    try:
        while True:
            if ser.in_waiting > 0: 
                response = ser.readline().decode('utf-8', errors = 'ignore').strip()

                # Make sure the data format in your Python script 
                # matches what you print to the Serial Monitor in your ESP32 code
                if response == "DATA: Object detected":
                    timeDetection = datetime.datetime.now()
                    timeToStore = timeDetection.strftime("%H:%M:%S")

                    # Wite to database
                    cursor.execute("INSERT INTO ultrasound_detection (time, object) VALUES(?,?)", (timeToStore, "Object detected"))
                    conn.commit()      
    except KeyboardInterrupt:
        print("\nStopped by user. Database saved.")

    finally:
        ser.close()
        conn.close()




