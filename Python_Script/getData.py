import serial
import sqlite3
import time
import datetime
import serial.tools.list_ports

# Variable
PORT = "COM3"
BAUDRATE = 115200
DATA_FILE = "data.db"

def find_esp32_port():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        # Nhận diện các chip nạp phổ biến trên ESP32 (CP210x, CH340, USB Serial)
        if "CP210" in port.description or "CH340" in port.description or "USB" in port.description:
            print(port.device)
            return port.device
    return None

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
    port = find_esp32_port()
    if not port:
        print("Error: ESP32 not found.")
        conn.close()
        exit()

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

                if response == "DATA: Object detected":
                    timeDetection = datetime.datetime.now()
                    timeToStore = timeDetection.strftime("%H:%M:%S")

                    cursor.execute("INSERT INTO ultrasound_detection (time, object) VALUES(?,?)", (timeToStore, "Object detected"))
                    conn.commit()      
    except KeyboardInterrupt:
        print("\nStopped by user. Database saved.")

    finally:
        ser.close()
        conn.close()




