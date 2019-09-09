#!/usr/bin/env python3
import json
import math

def printAndAdd(dictionary):
    """
    Prints the current diction and adds new objects
    Keywork Arguements:
    dictionary -- the dictionary
    """
    for keys,values in dictionary.items():
        print("The key {} has the value {}".format(keys, values) )
        
    newDict = {"number2": 2, "string2": "two"}
    print("adding new values to dictionary: {}".format(newDict))
    try:
        dictionary.update(newDict)
    except:
        raise Exception("Updating the dictionary failed")
        
    return dictionary

def seekNumbersAndSquare(dictionary):
    """
    Seeks all numbers in the dict objects and squares them
    Keywork Arguements:
    dictionary -- the dictionary
    """
    print("Squaring objects with integers")
    for key in dictionary:
        if isinstance(dictionary[key], (int, float)):
            dictionary[key] = math.pow(dictionary[key], 2)
        
    return dictionary
    
def seekNumbersAndSquareInLists(dictionary):
    """
    Seeks all lists in the dict objects then squares numbers in those dictionaries
    Keywork Arguements:
    dictionary -- the dictionary
    """
    for key in dictionary:
        if isinstance(dictionary[key], list):
            dictionary[key] = [math.pow(item, 2) if isinstance(item, (int, float)) else item for item in dictionary[key] ]
        
    return dictionary
    
if __name__ == "__main__":
    with open('/home/ec2-user/environment/python-refresher/file.json') as json_file:
        myDict = json.load(json_file)
        myDict = printAndAdd(myDict)
        myDict = seekNumbersAndSquare(myDict)
        myDict = seekNumbersAndSquareInLists(myDict)
    try:
        print(json.dumps(myDict, indent=4))
    except:
        raise 
    