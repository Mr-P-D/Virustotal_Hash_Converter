import requests
import json
import time

# Put your API Key Here
apikey = 'API KEY'
hashes = open("hash_input.txt") # Input With Hashes
hash_output = open("hash_output.txt", "w") # OUTPUT File
hash_output.write("Converted Hashes below \n")

for i in hashes:
    try:
        print('Checking hash ' + i)
        param = {'apikey': apikey, 'resource': i}
        response = requests.post('https://www.virustotal.com/vtapi/v2/file/report',param=param)
        result = response.json()
	hash_output.write(result['sha1'] + "\n")
    except:
        print("API limit reached!, wait for a bit") #5 Hashes per minute with Public API Key
	time.sleep(1 * 60)
