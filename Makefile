all:
	python download_seamarks.py
	#osmium cat -c version -c timestamp -c changeset -c uid -c user temp/*.osm -o seamarks_n.osm --overwrite
	osmium cat temp/*.osm -o seamarks_n.osm --overwrite
	python strip_seamarks.py
	mv seamarks_s.osm seamarks.osm
	osmium cat seamarks.osm -f pbf -o seamarks.pbf --overwrite

clean:
	rm seamarks_n.osm