# HackCC 2026 Workshop
    Hey, welcome to HackCC! Hope this workshop today could help to build your project!

## Start Here!
1. If you haven't installed Python yet, please download and install it from https://www.python.org/downloads/

    **<u>Important:</u>** Make sure to check **"Add Python to PATH"** during installation!
2. Then, install Pyserial library
  
    Open terminal on VS Code and enter the command
    
    **<u> Win user:</u>**    ```pip install pyserial```

    **<u> Mac user:</u>**    ```pip3 install pyserial```

3. Create a ```.py``` file and try ```import serial```
   
   If you encounter an error, you might have selected the wrong Python interpreter.

   Press `Ctrl + Shift + P` (or `Cmd + Shift + P` on Mac), search for and select ```Python: Select Interpreter```, then choose the Python version where you installed pyserial.

## Slide
Check out the **[slides](./slides/)** , which covers everything discussed in the workshop, including the syntax needed to develop a `.py` script to get data from the ESP32.

## Workshop Demo
1. Check out the **[find_port](./find_port/)** folder for code to find port connected to ESP32.
2. Check out the **[Python_script](./Python_Script/)** folder for the script.
3. Check out the **[ultrasonic_sensor](./ultrasonic_sensor/)** folder for C++ code in Arduino IDE for ultrasonic sensor.
4. Open **[database](./Database/data.db)** in VS Code while running python script to view the incoming data.
   
   You can install **SQLite3 Editor** extension in VS Code to view `.db` files directly.