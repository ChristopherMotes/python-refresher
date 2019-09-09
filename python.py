#!/usr/bin/env python3
import json

def printAndAdd(dictionary):
    """
    Prints the 
    for keys,values in dictionary.items():
        print("The key {} has the value {}".format(keys, values) )
        
    newDict = {"number2": 2, "string2": "two"}
    print("adding new values to dictionary: {}".format(newDict))
    try:
        dictionary.update(newDict)
    except:
        raise Exception("Updating the dictionary failed")
        
    return dictionary
    
if __name__ == "__main__":
    with open('/home/ec2-user/environment/python-refresher/file.json') as json_file:
        myDict = json.load(json_file)
    try:
        myDict = printAndAdd(myDict)
        print(json.dumps(myDict, indent=4))
    except:
        raise 
    