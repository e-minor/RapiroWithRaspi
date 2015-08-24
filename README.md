# RapiroWithRaspi
The RAPIRO is a programmable DIY robot kit with endless possibilities.Goto the [offical website](http://www.rapiro.com/) for more information.<br>
'''[Arduino sketch](https://github.com/Ishiwatari/RAPIRO)'''

## Using python-serial to control RAPIRO
* In order to use the Raspberry Pi’s serial port, we need to disable getty (the program that displays login screen) by find this line in file /etc/inittab
<pre>
T0:23:respawn:/sbin/getty -L ttyAMA0 115200 vt100
And comment it out by adding # in front of it
\#T0:23:respawn:/sbin/getty -L ttyAMA0 115200 vt100 
<pre\>

* To prevents the Raspberry Pi from sending out data to the serial ports when it boots, go to file /boot/cmdline.txt and find the line and remove it<br>
<pre>
console=ttyAMA0,115200 kgdboc=ttyAMA0,115200
<pre\>

* Reboot the Raspberry Pi using this command:
<pre>
$ sudo reboot
<pre\>

* Now, Install minicom
<pre>
$ sudo apt-get install minicom<br>

* test it by issuing the following command:
<pre>
$ echo "#PR255G000B000T050#PR255G000B255T050" | sudo minicom -b 57600 -o -D /dev/ttyAMA0
This should change colors of the eyes only.
<pre\>

* Using Python programming language, you can make Raspberry Pi do many fascinating stuff with the RaPiRo when you are connected. Install Py-Serial first:
<pre>
$ sudo apt-get install python-serial
$ sudo chmod 666 /dev/ttyAMA0
<pre\>

* Now test it by saving this file as serialtest.py<br>
<pre>
import serial
import time
ser = serial.Serial('/dev/ttyAMA0', 57600, timeout=1)
ser.open()
ser.write("#PS06A060T001")
time.sleep(2)
ser.write("#PS05A000T030")
time.sleep(2)
ser.write("#PS05A120T001")
time.sleep(2)
ser.write("#PS06A050T001")
time.sleep(2)
ser.write("#H")
ser.close()
<pre\>

* Then run it form terminal issuing this command:
<pre>
$ python serialtest.py
This should raise the left hand and strike it down again.
<pre\>

* Install Apache2
<pre>
$ sudo apt-get install apache2 libapache2-mod-python
$ sudo usermod -aG dialout www-data
<pre\>

* Download the files that is needed for the webserver to handle the RaPiRo and copy them to the apropriate directories.
The python cgi script goes to /usr/lib/cgi-bin/:
<pre>
$ wget https://dl.dropboxusercontent.com/u/54426040/test.py
$ sudo chmod 755 /usr/lib/cgi-bin/test.py
<pre\>

* You should rename that file to rapiro.py but then you also have to change the reference in the code (line 103) to rapiro.py instead of test.py as well.
The CSS syle sheet goes to /var/www/:
<pre>
$ wget https://dl.dropboxusercontent.com/u/54426040/control.css
The files for the icons should be extracted to the /var/www/ folder
$ wget https://dl.dropboxusercontent.com/u/54426040/Remote.Control.Icons.zip
<pre\>

* Then access the homepage from the webbrowser of your choise using the ip-address of the internal Raspberry Pi WiFi adapter.
<pre>http://rapirorpiIP/test.py<pre\>
<pre>or<pre\>
<pre>http://rapirorpiIP/rapiro.py<pre\><br>
* depending on if you renamed the file or not.
* depending on your apache setup you may need to use:
<pre>
http://rapirorpiIp/cgi-bin/test.py
<pre\>

# Usage
* Using wifi dongle to get on local wireless network 
* Download the codes
<pre>git clone https://github.com/e-minor/RapiroWithRaspi.git <pre\>

* running
<pre>python server.py<pre\> 

* Setting on boot startup adding a shell command at rc.local
<pre>
\# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
  python /home/pi/rapiro/server.py &
fi
<pre\>

* Finally  Deploy [MrRobot](https://github.com/e-minor/MrRobot) to a ubuntu phone and control the robot 

