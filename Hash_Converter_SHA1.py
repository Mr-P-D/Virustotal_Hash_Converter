import requests
import json
import time

# check a file of hashes with virustotal and save results

# place your api key
apikey = 'API KEY HERE'
hashes = open("hash_input.txt") # input with hashes (create a file)
output = open("hash_output.txt", "w") # Output file
output.write("\t\t\tHash\t\t\t\t\tdetected \n ")

for hashn in hashes:
    try:
        print('Checking hash ' + hashn)
        params = {'apikey': apikey, 'resource': hashn}
        response = requests.post('https://www.virustotal.com/vtapi/v2/file/report',
                                params=params)
        result = response.json()
	output.write(result['sha1'] + "\n") #can either be MD5 or SHA256
    except:
        print("API limit reached!, Waiting")
	time.sleep(1 * 60)
