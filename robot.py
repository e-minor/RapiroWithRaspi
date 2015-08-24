#!/usr/bin/env python

import serial
from curses import ascii
import cgi
import cgitb; cgitb.enable()


form = cgi.FieldStorage()

print "Content-type: text/html\n\n"


if "Submit6" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#M5")
elif "Submit3" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#M0")
elif "Submit1" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#M1")
elif "Submit2" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#M3")
elif "Submit4" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#M4")
elif "Submit5" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#M2")
elif "Submit7" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#M6")
elif "Submit8" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#M7")
elif "Submit9" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#M8")
elif "Submit10" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#M9")
elif "Submit11" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#H")
elif "Submit16" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#PS07A130T010")
elif "Submit12" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#PS05A090T010")
elif "Submit14" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#PS05A180T010")
elif "Submit13" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#PS02A090T010")
elif "Submit15" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#PS02A000T010")
elif "Submit18" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#PS07A090T010")
elif "Submit17" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#PS04A050T010")
elif "Submit19" in form:
    connection = '/dev/ttyAMA0'
    ser = serial.Serial(connection, 57600, timeout=10)
    ser.write("#PS04A090T010")

else:
    print "Error"

print """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

	<link rel="stylesheet" type="text/css" href="/control.css">

	<title>Rapiro Control</title>
	</head>
        <form action="/cgi-bin/test.py" method="post">
	<table width="100%" border="1">
  	<tr>
  	  <td>&nbsp;</td>
	    <td>&nbsp;</td>
	    <td><div class="submit1"><INPUT type="submit" value=" " name="Submit1" /></div></td>
	    <td>&nbsp;</td>
	    <td>&nbsp;</td>
 	</tr>
 	<tr>
 	  <td>&nbsp;</td>
            <td><div class="submit2"><INPUT type="submit" value=" " name="Submit2" /></div></td>
   	    <td><div class="submit3"><INPUT type="submit" value=" " name="Submit3" /></div></td>
            <td><div class="submit4"><INPUT type="submit" value=" " name="Submit4" /></div></td>
            <td>&nbsp;</td>
  	</tr>
  	<tr>
  	  <td>&nbsp;</td>
   	    <td>&nbsp;</td>
    	    <td><div class="submit5"><INPUT type="submit" value=" " name="Submit5" /></div></td>
 	    <td>&nbsp;</td>
 	    <td>&nbsp;</td>
	</tr>
	<tr>
	  <td><div class="submit6"><INPUT type="submit" name="Submit6" value=" "/></div></td>
	    <td><div class="submit7"><INPUT type="submit" name="Submit7" value=" "/></div></td>
	    <td><div class="submit8"><INPUT type="submit" name="Submit8" value=" "/></div></td>
	    <td><div class="submit9"><INPUT type="submit" name="Submit9" value=" "/></div></td>
	    <td><div class="submit10"><INPUT type="submit" name="Submit10" value=" "/></div></td>
	</tr>
	<tr>
	  <td><div class="submit12"><INPUT type="submit" name="Submit12" value=" "/></div></td>
	  <td><div class="submit14"><INPUT type="submit" name="Submit14" value=" "/></div></td>
	  <td>&nbsp;</td>
	  <td><div class="submit13"><INPUT type="submit" name="Submit13" value=" "/></div></td>
	  <td><div class="submit15"><INPUT type="submit" name="Submit15" value=" "/></div></td>
	  </tr>
	<tr>
	  <td><div class="submit16"><INPUT type="submit" name="Submit16" value=" "/></div></td>
	  <td><div class="submit18"><INPUT type="submit" name="Submit18" value=" "/></div></td>
	  <td><div class="submit11"><INPUT type="submit" name="Submit11" value=" "/></div></td>
	  <td><div class="submit17"><INPUT type="submit" name="Submit17" value=" "/></div></td>
	  <td><div class="submit19"><INPUT type="submit" name="Submit19" value=" "/></div></td>
	  </tr>
	</table>
        </form>
	</body>
	</html>"""
