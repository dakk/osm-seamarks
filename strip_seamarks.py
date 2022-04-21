import re
tostrip = ['source', 'wikidata', 'fax', 'email', 'phone', 'website', 'note', 'operator', 'addr', 'ref']

f = open ('seamarks_n.osm', 'r')
data = f.read()
f.close()

f = open ('seamarks_s.osm', 'w')
for x in tostrip:
    data = re.sub('<tag k=\"' + x + '.*\" v=\".*\"/>', '', data)


f.write(data)
f.close()