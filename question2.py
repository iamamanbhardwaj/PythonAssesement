import csv
from pprint import pprint

def extractDateWithMaxStockPrice(filename= "shareprice.csv"):
    #Returns an list of extracted data with company name , value, and time dictonary.

    #Parameters:
    #    inputString (str):The string or row which is to be interpreted.

    #Returns:
    #    list: list of extracted data with company name , value, and time dictonary. 

    with open(filename) as csvfile:
        reader = list(csv.reader(csvfile, delimiter=','))
        headerRow = reader[0]
        numberOfCompanies = len(headerRow)-2
        
        outputList = []
        #outer loop to through all companies data sequencially 
        for companyIndex in range(0,numberOfCompanies):
            companyName = headerRow[companyIndex+2]
            
            values =  [value[companyIndex+2] for value in reader[1:]]
            maxValueIndex = values.index(max(values))
            maxValue = values[maxValueIndex]
            outputList.append({'CompanyName':companyName, 'MaxPrice':maxValue, 'Month':reader[maxValueIndex+1][1] , 'Year':reader[maxValueIndex+1][0]})
        return outputList
        
# pretty print with indentation of 2
pprint(extractDateWithMaxStockPrice(),indent=2)