import telnetlib
import time
import sys

# tn = telnetlib.Telnet("172.18.2.213", 9010)
# test_var = ["test"]
# print (test_var)
# time.sleep(5)
# tn_read =  tn.read_very_eager()
# print (repr(tn_read))

HOST = "172.18.2.213"
PORT = "9010"

telnetObj=telnetlib.Telnet(HOST,PORT)
# message = ("GET /index.html HTTP/1.1\nHost:"+HOST+"\n\n").encode('ascii')
# telnetObj.write(message)
# output=telnetObj.read_all()
# print(output)
# telnetObj.close()
print('Success')