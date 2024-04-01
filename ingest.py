import csv
from tabulate import tabulate
import os

def intel(source, threat, ioc, ioc_type, notes):

    # Check if intel.csv exists
    if not os.path.exists('./intel.csv'):
        intel = open('./intel.csv', 'a', newline='')
        writer = csv.writer(intel)
        fields = ["ioc","threat","ioc_type","notes","source"]
        writer.writerow(fields)
    else:
        intel = open('./intel.csv', 'a', newline='')
        writer = csv.writer(intel)
        
    # IOC Type
    ioc_types = {
        1: "cmd",
    }
    
    ioc_type = ioc_types[ioc_type]
    
    # Threat
    threats = {
        1: "kimsuky",
    
    }

    threat = threats[threat]
    
    # Parse Indicator
    indicators = []
    delimiters = [' ','"']
    exclusions = ['BASE64','>','FILENAME']
    
    if ioc_type == "cmd":
        for delimiter in delimiters:
            ioc = ' '.join(ioc.split(delimiter))
        
        for cmd in ioc.split():
            if cmd not in indicators:
                indicators.append(cmd)
        
        ioc = ' '.join(indicators)
    
    writer.writerow([ioc,threat,ioc_type,notes,source])