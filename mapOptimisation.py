import mrtdata
from math import pi, sin, cos, atan2, sqrt

#bringing over the context
STN_NAME='STN_NAME'
INDX='INDX'
STN_NO='STN_NO'
Latitude='Latitude'
Longitude='Longitude'
COLOR='COLOR'
mrtStations = mrtdata.mrtStations
adjDict = mrtdata.adjDict

#temp database
random={
    'a':{'f':10},
    'b':{'f':5},
    'c':{'f':4},
    'd':{'f':90}
    }

#tested
node1 = {STN_NAME:'BOON LAY MRT STATION',INDX:17,STN_NO:'EW27',Latitude:'1.338604054',Longitude:'103.7060994',COLOR:'GREEN'}
node2 = {STN_NAME:'PIONEER MRT STATION',INDX:125,STN_NO:'EW28',Latitude:'1.337586882',Longitude:'103.6973586',COLOR:'GREEN'}
node3 = {STN_NAME:'KENT RIDGE MRT STATION',INDX:85,STN_NO:'CC24',Latitude:'1.293462633',Longitude:'103.7846438',COLOR:'YELLOW'}
node4 = {STN_NAME:'BUONA VISTA MRT STATION',INDX:30,STN_NO:'EW21/CC22',Latitude:'1.307183467',Longitude:'103.7902028',COLOR:['GREEN','YELLOW'],}
node5 = {STN_NAME:'BOTANIC GARDENS MRT STATION',INDX:18,STN_NO:'DT9/CC19',Latitude:'1.322423979',Longitude:'103.8161362',COLOR:['BLUE','YELLOW'],}
node6 = {STN_NAME:'CHOA CHU KANG MRT STATION',INDX:40,STN_NO:'NS4',Latitude:'1.385361693',Longitude:'103.744367',COLOR:['RED','BUKIT PANJANG'],}
node7 = {STN_NAME:'CHANGI AIRPORT MRT STATION',INDX:34,STN_NO:'CG2',Latitude:'1.357314545',Longitude:'103.9883212',COLOR:'GREEN',}
node8 = {STN_NAME:'RAFFLES PLACE MRT STATION',INDX:133,STN_NO:'EW14/NS26',Latitude:'1.284125611',Longitude:'103.8514572',COLOR:['GREEN','RED'],}

#temp list
tlist = [random['a'], random['b'], random['c']]

#main function
#the input nodes are just one layer of dictionary
def findBestRoute(startNode, endNode):
    #trackers
    openList = []
    closedList = []
    
    #setting f&g values for startNode
    startNode['f']=0
    startNode['g']=0
    print(f"step1 f:{startNode['f']} g:{startNode['g']}")
    print('\n')
    
    openList.append(startNode)

    while openList:
        currentNode = lowest_f(openList)
        #end condition
        if (currentNode['STN_NAME'] == endNode['STN_NAME']):
            print('reached final step')
            print('\n')
            return finalPath(startNode, currentNode)

        #finding neighboring stations
        neighborList = adjDict[currentNode[STN_NAME]]
        print(f"step2 establish neighborList: {neighborList}")
        print('\n')
        neighborArray = []

        #adding the information node into the array, instead of just using the name
        for neighbor in neighborList:
             neighborArray.append(mrtStations[neighbor])

        print(f"step3 establish neighborArray: {neighborArray}")
        print('\n')
        
        #running through the neighborArray
        for neighbor in neighborArray:
            if (neighbor not in openList) and (neighbor not in closedList):
                neighbor['g'] = currentNode['g']+1000 #1000 is arbituary to balance distance and stops
                neighbor['h'] = findH(endNode, neighbor)
                neighbor['f'] = neighbor['g'] + neighbor['h']
                neighbor['p'] = currentNode
                openList.append(neighbor)

                print('first condition')
                print(f"step4 establish neighbor new keys, g:{neighbor['g']}, h:{neighbor['h']}, f:{neighbor['f']}, p:{neighbor['p']}")
                print('\n')

                      
            elif (neighbor in openList) and ((currentNode['g']+1000)<neighbor['g']):
                neighbor['g'] = currentNode['g'] + 1000
                neighbor['h'] = findH(endNode, neighbor)
                neighbor['f'] = neighbor['g'] + neighbor['h']
                neighbor['p']= currentNode
                
                print('second condition')
                print(f"Step4 establish neighbor updated keys, g:{neighbor['g']}, h:{neighbor['h']}, f:{neighbor['f']}, p:{neighbor['p']}")
                print('\n')

            else:
                print('fell through all conditions because it is in openList but is not shortest')
                print('\n')

        #shove currendNode in current iteration into closedList and remove from openList
        closedList.append(currentNode)
        openList.remove(currentNode)

#supporting functions
def lowest_f(alist):
    fValues = []
    for i in alist:
        fValues.append(i['f'])
    lowest = min(fValues)
    lowest_index = fValues.index(lowest)
    return alist[lowest_index]

def findH(node1, node2):
    def toRadians(angle):
        return float(angle)*pi/180
    
    lat1 = float(node1[Latitude])
    long1 = float(node1[Longitude])
    lat2 = float(node2[Latitude])
    long2 = float(node2[Longitude])
    R = 6371000 #meters

    a = toRadians(lat1)
    b = toRadians(lat2)
    da = toRadians(lat2-lat1)
    lam = toRadians(long2-long1)

    A = (sin(da/2)**2)+(cos(a)*cos(b)*(sin(lam/2)**2))
    C = 2*atan2(sqrt(A), sqrt(1-A))
    D = R * C
    return D

why = [];
def finalPath(startNode, node):
    if startNode[STN_NAME] == node[STN_NAME]:
        why.append(startNode[STN_NAME])
        return why        
    else:
        why.append(node[STN_NAME])
        return finalPath(startNode, node['p'])



        
        

                

        

