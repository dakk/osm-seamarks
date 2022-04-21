import os 
import time 

#<bbox-query s="35.00" w="-5.00" n="45.00" e="18.00"/>
q = open('query.xml', 'r').read()

LONG_S = 45
LAT_S = 45

i = 0
n = 360/LONG_S * 180/LAT_S

for x in range(-180, 180, LONG_S):
	for y in range(-90, 90, LAT_S):
		i += 1
		qq = q.replace('SS', str(y)).replace('NN', str(y+LAT_S))
		qq = qq.replace('WW', str(x)).replace('EE', str(x+LONG_S))
		f = open('temp/tquery.xml', 'w')
		f.write(qq)
		f.close()
		print (i, 'of', n, y, x)
		os.system('wget --post-file=temp/tquery.xml -O temp/seamarks_'+str(x)+'_'+str(y)+'.osm http://overpass-api.de/api/interpreter')
		time.sleep(16)
		
# Merge
os.system('osmium cat -c version -c timestamp -c changeset -c uid -c user temp/*.osm -o seamarks_n.osm --overwrite')
