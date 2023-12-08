
# importing the module
import re
import os
with open( 'capture20110810.binetflow', 'r') as file:
    fi = file.readlines()

found_ips = []
ips=[]

for entry in fi:
  	ips = re.findall( r'[0-9]+(?:\.[0-9]+){3}', entry )
  	if len(ips)>0:
  		found_ips.append(ips[0])
    # print(ip)
# print( len(found_ips) )
newlist = set(found_ips)
print( len(newlist) )
for x in newlist:
	print('py main.py -p capture20110810.binetflow -ip ' + x )
	os.system('py main.py -p capture20110810.binetflow -ip ' + x )
#2824549
#542077