"""Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json"

Upload this program to the same repository you used for the XML assignment
Save this assignment as "assignment03-cso.py"
This program should not be a long one
I don't need you to reformat or analyse the data in any way
It should be about 10ish lines long (I have not counted)
You will need to find the dataset in CSO.ie, try economic and then finance.
"""

# Import packages 
import requests
import json

#Hard code in url - this could be changed to select the dataset without the full url 
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"


# Reading in the data from the url above, returns a json response
def read_data():
    response = requests.get(url)
    return (response.json())



if __name__ == "__main__":   
# Writes the data to a file named cso.json and formats it as a string (dumps)

    with open("cso.json", "wt") as fp:
        print(json.dumps(read_data()), file=fp)

