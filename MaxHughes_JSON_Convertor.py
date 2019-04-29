import json

jsonFile = open('TestData.json', 'r')
jsonData = json.loads(jsonFile.read())

for k,v in jsonData['FileData'].items():
    from random import *
    v['Quantity'] = randint(1, 100)
    print(k,v['Quantity'])

jsonData['MetaData']['FileOwner'] = 'Max Hughes'

with open('TestData.json', 'w') as outfile:
        json.dump(jsonData, outfile)


