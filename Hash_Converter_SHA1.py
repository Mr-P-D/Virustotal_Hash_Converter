import requests
import json
import time

# place your api key here
apikey = 'API KEY HERE'
hashes = open("hash_input.txt") # input with hashes (create a file named hash_input.txt and place your hashes into it.)
output = open("hash_output.txt", "w") # Output file
output.write("\t\t\tHash\t\t\t\t\tdetected \n ")

for hashn in hashes:
    try:
        print('Checking hash ' + hashn)
        params = {'apikey': apikey, 'resource': hashn}
        response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',
                                params=params)
        result = response.json()
	output.write(result['sha1'] + "\n") #replace SHA1/MD5/SHA256 to convert existing hashes to the mentioned format.
    except:
        print("API limit reached!, Waiting")
	time.sleep(1 * 60)
