#!/usr/bin/env python3
import json
import math
import requests
from retrying import retry


@retry(
    stop_max_attempt_number = 3,
    wait_exponential_multiplier=1000,
    wait_exponential_max=10000
    )
def importFromFile():
    with open('/home/ec2-user/environment/python-refresher/file.json') as json_file:
        return json.load(json_file)
    

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
    
def importFromHTTP():
    try:
        requests.adapters.HTTPAdapter(max_retries=0)
        response = requests.get( "https://swapi.com/api/" + "people/1/" )
    except requests.exceptions.ConnectionError as errorMessage:
        print(errorMessage)
    except requestrequests.exceptions.ConnectionRefusedError:
        print("TLCpl1996")
    except:
        raise
    print(response)
    print(response.text)
    return json.loads(response.text)
    
if __name__ == "__main__":
    dataCall = input("Enter file or http: ")
    if dataCall == 'file':
        myDict = importFromFile()
    elif dataCall == 'http':
        myDict = importFromHTTP()
    else:
        raise Exception("I don't know \"{}\"".format(dataCall))
        
    myDict = printAndAdd(myDict)
    myDict = seekNumbersAndSquare(myDict)
    myDict = seekNumbersAndSquareInLists(myDict)
    try:
        print(json.dumps(myDict, indent=4))
    except:
        raise 
    