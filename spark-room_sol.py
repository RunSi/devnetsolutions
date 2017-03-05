import json
import requests

accessToken = "ZDM5NWZkNjktNzBlYy00ZjdmLWJhNjAtNjJlYTA0NWQwMjdlMGY3OTM2ZGItODJj" #put your access token here between the quotes.


def setHeaders():         
	accessToken_hdr = 'Bearer ' + accessToken
	spark_header = {'Authorization': accessToken_hdr, 'Content-Type': 'application/json; charset=utf-8'}
	return spark_header


def getRooms(theHeader):    
	uri = 'https://api.ciscospark.com/v1/rooms'
	resp = requests.get(uri, headers=theHeader)
	print("SparkAPI: ")	
	return resp.json()
    

header=setHeaders()
value=getRooms(header)
for room in value['items']:
    for room_info in room:
        key = room_info
        value = str(room[room_info])
        print(key + ": " +value)
    print()
    print()
#print (json.dumps(value, indent=4, separators=(',', ': ')))
#print(value)
