import numpy as np
from math import sin, cos, sqrt, atan2, radians
import csv
import datetime

def degreeToDistY(lat2):
    R = 6373.0
    lat2 = float(lat2)
    lat1 = radians(-26)
    lon1 = radians(129)
    lat2 = radians(lat2)
    lon2 = radians(129)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

def degreeToDistX(lon2):
    R = 6373.0
    lon2 = float(lon2)
    lat1 = radians(-26)
    lon1 = radians(129)
    lat2 = radians(-26)
    lon2 = radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

def gridRef(distance):
    if distance < 500:
        X = int(0)
    if 500 <= distance < 1000:
        X = int(1)
    if 1000 <= distance < 1500:
        X = int(2)
    if 1500 <= distance < 2000:
        X = int(3) 
    return X
#x=degreeToDistX(138.6784668)
#print(x)
#print(gridRef(x))

#-29.613764, 140.152697 lake callobana
#-33.356690, 137.855433 port pirie
def flinders(lat, lon):
    lat1 = float(lat)
    lon1 = float(lon)
    flinders = 'N'
    if -29.613764 >= lat1 >= -33.356690:
        if 137.855433 <= lon1 <=  140.152697:
            flinders = 'Y'
    return flinders


GridRef = []
inFlinders=[]
matrix = np.zeros((4,4))
np.set_printoptions(suppress=True)
with open('EQs_Clusters.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    lineNum = 0
    for row in reader:
        if lineNum == 0:
            lineNum += 1
            continue
        else:
            y = degreeToDistY(row[9])
            y = gridRef(y)
            x = degreeToDistX(row[8])
            x = gridRef(x)
            Ref = str(x)+"."+str(y)
            matrix[y][x]+=1
            GridRef.append(Ref)
            inFlinders.append(flinders(row[9],row[8]))
               


Dict={}
for item in GridRef:
    if item in Dict.keys():
        Dict[item]+=1
    else:
        Dict[item]=1

print(Dict)
print(matrix)

with open('EQs_Clusters.csv','r') as csvinput:
    with open('EQs_Clusters_smallGrid.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)
        all=[]
        i=0
        lineNum=0
        for row in reader:
            if lineNum == 0:
                row.append("Flinder's Range")
                all.append(row)
                lineNum += 1
                continue
            
            else:    
                row[23] = GridRef[i]
                row.append(inFlinders[i])
                all.append(row)
                i+=1
            

        writer.writerows(all)

