import numpy as np

orientations = ['vertical', 'horizontal']
rectangles = [[8,3], [5,1], [2,2], [1,1], [9,4], [6,2], [4,3], [5,7], [3,2], [4,2]]
ironLaminateTemplate = np.zeros((10,10))

#RectanguloId, Orientación, Posición
firstCandidate = [0, 1, [1,2]]
secondCandidate = [0, 1, [1,2]]
thirdCandidate = [0, 1, [1,2]]
fourthCandidate = [0, 1, [1,2]]
fifthCandidate = [0, 1, [1,2]]
sixthCandidate = [0, 1, [1,2]]
seventhCandidate = [0, 1, [1,2]]
eighthCandidate = [0, 1, [1,2]]
ninthCandidate = [0, 1, [1,2]]
tenthCandidate = [0, 1, [1,2]]
eleventhCandidate = [1, 1, [4,2]]
twelfthCandidate = [4, 1, [4,1]]

firstSolution = [eleventhCandidate, secondCandidate, thirdCandidate, fourthCandidate, fifthCandidate, sixthCandidate, seventhCandidate, eighthCandidate, ninthCandidate, tenthCandidate]
secondSolution = [twelfthCandidate, secondCandidate, thirdCandidate, fourthCandidate, fifthCandidate, sixthCandidate, seventhCandidate, eighthCandidate, ninthCandidate, tenthCandidate]
thirdSolution = [firstCandidate, secondCandidate, thirdCandidate, fourthCandidate, fifthCandidate, sixthCandidate, seventhCandidate, eighthCandidate, ninthCandidate, tenthCandidate]
fourthSolution = [firstCandidate, secondCandidate, thirdCandidate, fourthCandidate, fifthCandidate, sixthCandidate, seventhCandidate, eighthCandidate, ninthCandidate, tenthCandidate]
fifthSolution = [firstCandidate, secondCandidate, thirdCandidate, fourthCandidate, fifthCandidate, sixthCandidate, seventhCandidate, eighthCandidate, ninthCandidate, tenthCandidate]
sixthSolution = [firstCandidate, secondCandidate, thirdCandidate, fourthCandidate, fifthCandidate, sixthCandidate, seventhCandidate, eighthCandidate, ninthCandidate, tenthCandidate]
seventhSolution = [firstCandidate, secondCandidate, thirdCandidate, fourthCandidate, fifthCandidate, sixthCandidate, seventhCandidate, eighthCandidate, ninthCandidate, tenthCandidate]
eighthSolution = [firstCandidate, secondCandidate, thirdCandidate, fourthCandidate, fifthCandidate, sixthCandidate, seventhCandidate, eighthCandidate, ninthCandidate, tenthCandidate]
ninthSolution = [firstCandidate, secondCandidate, thirdCandidate, fourthCandidate, fifthCandidate, sixthCandidate, seventhCandidate, eighthCandidate, ninthCandidate, tenthCandidate]
tenthSolution = [firstCandidate, secondCandidate, thirdCandidate, fourthCandidate, fifthCandidate, sixthCandidate, seventhCandidate, eighthCandidate, ninthCandidate, tenthCandidate]

initialSetOfSolutions = [[firstSolution,0], [secondSolution,0], [thirdSolution,0], [fourthSolution,0], [fifthSolution,0], [sixthSolution,0], [seventhSolution,0], [eighthSolution,0], [ninthSolution,0], [tenthSolution,0]]
#Posición mínima [0,0], Orientación y Rectangulo mínimo 0
def positionate(rectangleId, orientationId, position, currentIronLaminate):    
    if orientations[orientationId] == 'vertical':
        for x in range(rectangles[rectangleId][0]):
            for y in range(rectangles[rectangleId][1]):
                if currentIronLaminate[x+position[0], y+position[1]] > 0:                    
                    return 1
                currentIronLaminate[x+position[0], y+position[1]] = rectangleId+1
    else:
        for x in range(rectangles[rectangleId][1]):
            for y in range(rectangles[rectangleId][0]):
                if currentIronLaminate[x+position[0], y+position[1]] > 0:                    
                    return 1
                currentIronLaminate[x+position[0], y+position[1]] = rectangleId+1  
    return 0    

def calculateWaste(laminatesUsed):
    waste = 0
    for x in laminatesUsed:
        for y in range(10):
            for z in range(10):
                if x[y][z] < 1:
                    waste += 1
    return waste

def findBestThree(candidates):
    minimum = min([candidates[0][1], candidates[1][1], candidates[2][1]])
    theBest = [[0,minimum],[0,minimum],[0,minimum]]
    for x in candidates:
        print("Current ", x[1])
        print(theBest[0][1], " ", theBest[1][1], " ", theBest[2][1])
        if x[1] >= theBest[0][1]:            
            #El segundo pasa a ser el tercero y el primero a ser el segundo
            theBest[2] = theBest[1]
            temp = theBest[0]
            theBest[1] = temp
            print(theBest[0][1], " ", theBest[1][1], " ", theBest[2][1])
            #Actualizamos el primero
            theBest[0][0] = x[0]
            print(theBest[0][0], " ", theBest[1][0], " ", theBest[2][0])
            theBest[0][1] = x[1]
            print(theBest[0][1], " ", theBest[1][1], " ", theBest[2][1])
            
        elif x[1] >= theBest[1][1]:
            #El segundo pasa a ser el tercero
            theBest[2] = theBest[1]            
            #Actualizamos el segundo            
            theBest[1][0] = x[0]
            theBest[1][1] = x[1]            
        elif x[1] >= theBest[2][1]:
            theBest[2][0] = x[0]
            theBest[2][1] = x[1]
    return theBest

def evolutionaryAlgorithm(initialSolutions):
    laminates = [np.zeros((10,10))]
    rectanglesRepetition = 0    
    putRectangle = np.zeros(10)
    currentLaminate = 0
    currentSolutions = initialSolutions
    for x in currentSolutions:
        laminates = [np.zeros((10,10))]
        rectanglesRepetition = 0        
        putRectangle = np.zeros(10)
        currentLaminate = 0            
        for y in x[0]:
            if putRectangle[y[0]] > 0:
                rectanglesRepetition += 1
            else:
                putRectangle[y[0]] = y[0]+1                
                if positionate(y[0], y[1], y[2], laminates[currentLaminate]) > 0:                    
                    laminates.append(np.zeros((10,10)))
                    currentLaminate += 1                      
        x[1] = - rectanglesRepetition - calculateWaste(laminates)                
    print(findBestThree(currentSolutions))

evolutionaryAlgorithm(initialSetOfSolutions)

def printValues():
    values = np.zeros(10)
    i=0
    for x in initialSetOfSolutions:
        values[i] = x[1]
        i += 1
    print(values)

printValues()        



 