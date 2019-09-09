#!/usr/bin/env python3
import json

def funtionOne(dictionary):
    print(dictionary)
    for keys,values in dictionary.items():
        print("The key {} has the value {}".format(keys, values) )
        
    dictionary.update({"number2": 2, "string2": "two"})
        
    return True
    
if __name__ == "__main__":
    with open('/home/ec2-user/environment/python-refresher/file.json') as json_file:
        myDict = json.load(json_file)
    if funtionOne(myDict):
        print("test valid")
    else:
        print("test invalid")
    