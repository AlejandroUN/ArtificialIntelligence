#Sistemas Inteligentes
#Ejercicio Práctico - Agentes basados en búsqueda
#Implementación Algoritmo Evolutivo

import numpy as np
import random

orientations = ['vertical', 'horizontal']
rectangles = [[8,3], [5,1], [2,2], [1,1], [9,4], [6,2], [4,3], [5,7], [3,2], [4,2]]
ironLaminateTemplate = np.zeros((10,10))

#Deinimos diferentes genes que consistirán de
#RectanguloId, Orientación, Posición
firstCandidate = [0, 1, [1,2]]
secondCandidate = [1, 1, [1,2]]
thirdCandidate = [2, 1, [1,2]]
fourthCandidate = [3, 1, [1,2]]
fifthCandidate = [4, 1, [1,2]]
sixthCandidate = [5, 1, [1,2]]
seventhCandidate = [6, 1, [1,2]]
eighthCandidate = [7, 1, [1,2]]
ninthCandidate = [8, 1, [1,2]]
tenthCandidate = [9, 1, [1,2]]
eleventhCandidate = [1, 1, [4,2]]
twelfthCandidate = [4, 1, [4,1]]

#Definimos los cromosomas iniciales
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

#Estos cromosomas conformarán la población inicial
initialSetOfSolutions = [[firstSolution,0], [secondSolution,0], [thirdSolution,0], [fourthSolution,0], [fifthSolution,0], [sixthSolution,0], [seventhSolution,0], [eighthSolution,0], [ninthSolution,0], [tenthSolution,0]]

#Retorna 0 si se pudieron posicionar correctamente los rectángulos
#Retorna 1 si había un solapamiento de cortes
#Retorna 2 si intentaba cortar en una posición fuera de la lámina
#Posición mínima [0,0], Orientación y Rectangulo mínimo 0
def positionate(rectangleId, orientationId, position, currentIronLaminate):    
    if orientations[orientationId] == 'vertical':
        #No se permitirá cortar sobre una región fuera de la lámina
        if  ((position[0] + rectangles[rectangleId][0]) < 11) and ((position[1] + rectangles[rectangleId][1]) < 11):
            for x in range(rectangles[rectangleId][0]):
                for y in range(rectangles[rectangleId][1]):                    
                    #No se permitirá cortar sobre una región que ya fue cortada
                    if currentIronLaminate[x+position[0], y+position[1]] > 0:                    
                        return 1      
            #Después de haber evaluado las 2 condiciones se corta la lámina
            # La representación de los cortes se hará con el númeroId del rectángulo     
            for x in range(rectangles[rectangleId][0]):
                for y in range(rectangles[rectangleId][1]):       
                    currentIronLaminate[x+position[0], y+position[1]] = rectangleId+1
        else:
            return 2
    else:
        if  ((position[0] + rectangles[rectangleId][1]) < 11) and ((position[1] + rectangles[rectangleId][0]) < 11):
            for x in range(rectangles[rectangleId][1]):
                for y in range(rectangles[rectangleId][0]):
                    if currentIronLaminate[x+position[0], y+position[1]] > 0:                    
                        return 1
            for x in range(rectangles[rectangleId][1]):
                for y in range(rectangles[rectangleId][0]):
                    currentIronLaminate[x+position[0], y+position[1]] = rectangleId+1
                      
        else:
            return 2
    return 0    

#Calcula el desperdicio en las láminas utilizadas
def calculateWaste(laminatesUsed):
    waste = 0
    for x in laminatesUsed:
        for y in range(10):
            for z in range(10):
                if x[y][z] < 1:
                    waste += 1
    return waste

#Retorna los cromosomas cuyos valores de fitness son mas altos entre toda la población ingreadas
def findBestThree(candidates):
    minimum = min([candidates[0][1], candidates[1][1], candidates[2][1]])
    theBest = [[0,minimum],[0,minimum],[0,minimum]]
    for x in candidates:          
        if x[1] >= theBest[0][1]:            
            #El segundo pasa a ser el tercero y el primero a ser el segundo
            theBest[2] = theBest[1]
            temp = theBest[0]
            theBest[1] = temp            
            #Actualizamos el primero
            theBest[0] = x            
        elif x[1] >= theBest[1][1]:
            #El segundo pasa a ser el tercero
            theBest[2] = theBest[1]            
            #Actualizamos el segundo            
            theBest[1] = x
        elif x[1] >= theBest[2][1]:
            theBest[2][0] = x[0]
            theBest[2][1] = x[1]
    return theBest
    

def crossover(initializers):
    newGeneration = initializers
    rectanglesUsed = []
    for x in range(7):
        newSolution = []
        for y in range(8):
            currentRectangle = random.choice(initializers[random.choice([0,1,2])][0])
            #El rectángulo no debe haber sido ya seleccionado/cortado
            isAValidRectangle = (currentRectangle[0] not in rectanglesUsed)
            if orientations[currentRectangle[1]] == 'vertical':
                #No se permitirá cortar sobre una región fuera de la lámina
                if  ((currentRectangle[2][0] + rectangles[currentRectangle[0]][0]) < 11) and ((currentRectangle[2][1] + rectangles[currentRectangle[0]][1]) < 11):
                    isAValidRectangle = isAValidRectangle
                else:
                    isAValidRectangle = False
            else:
                if  ((currentRectangle[2][0] + rectangles[currentRectangle[0]][1]) < 11) and ((currentRectangle[2][1] + rectangles[currentRectangle[0]][0]) < 11):
                    isAValidRectangle = isAValidRectangle
                else:
                    isAValidRectangle = False
            
            #Se seleccionarán nuevos genes hasta que cumplan con las condiciones
            while (not isAValidRectangle):
                currentRectangle = random.choice(initializers[random.choice([0,1,2])][0])
                isAValidRectangle = (currentRectangle[0] not in rectanglesUsed)
                if orientations[currentRectangle[1]] == 'vertical':
                    #No se permitirá cortar sobre una región fuera de la lámina
                    if  ((currentRectangle[2][0] + rectangles[currentRectangle[0]][0]) < 11) and ((currentRectangle[2][1] + rectangles[currentRectangle[0]][1]) < 11):
                        isAValidRectangle = isAValidRectangle
                    else:
                        isAValidRectangle = False
                else:
                    if  ((currentRectangle[2][0] + rectangles[currentRectangle[0]][1]) < 11) and ((currentRectangle[2][1] + rectangles[currentRectangle[0]][0]) < 11):
                        isAValidRectangle = isAValidRectangle
                    else:
                        isAValidRectangle = False 
                #Se agrega el gen/rectángulo al actual cromosoma/solución
            newSolution.append(currentRectangle)
        #Se generan nuevos genes aleatorios
        for z in range(2):
            currentRectangle = [random.randint(0,9), random.randint(0,1), [random.randint(0,9), random.randint(0,9)]]
            isAValidRectangle = (currentRectangle[0] not in rectanglesUsed)
            if orientations[currentRectangle[1]] == 'vertical':
                #No se permitirá cortar sobre una región fuera de la lámina
                if  ((currentRectangle[2][0] + rectangles[currentRectangle[0]][0]) < 11) and ((currentRectangle[2][1] + rectangles[currentRectangle[0]][1]) < 11):
                    isAValidRectangle = isAValidRectangle
                else:
                    isAValidRectangle = False
            else:
                if  ((currentRectangle[2][0] + rectangles[currentRectangle[0]][1]) < 11) and ((currentRectangle[2][1] + rectangles[currentRectangle[0]][0]) < 11):
                    isAValidRectangle = isAValidRectangle
                else:
                    isAValidRectangle = False
            #Se seleccionarán nuevos genes hasta que cumplan con las condiciones
            while (not isAValidRectangle):
                currentRectangle = [random.randint(0,9), random.randint(0,1), [random.randint(0,9), random.randint(0,9)]]
                isAValidRectangle = (currentRectangle[0] not in rectanglesUsed)
                if orientations[currentRectangle[1]] == 'vertical':
                    #No se permitirá cortar sobre una región fuera de la lámina
                    if  ((currentRectangle[2][0] + rectangles[currentRectangle[0]][0]) < 11) and ((currentRectangle[2][1] + rectangles[currentRectangle[0]][1]) < 11):
                        isAValidRectangle = isAValidRectangle
                    else:
                        isAValidRectangle = False
                else:
                    if  ((currentRectangle[2][0] + rectangles[currentRectangle[0]][1]) < 11) and ((currentRectangle[2][1] + rectangles[currentRectangle[0]][0]) < 11):
                        isAValidRectangle = isAValidRectangle
                    else:
                        isAValidRectangle = False   
                #Se agrega el gen/rectángulo al actual cromosoma/solución      
            newSolution.append(currentRectangle)                        
            #Se el cromosoma/solución a la nueva generación
        newGeneration.append([newSolution,0])    
    return newGeneration

def printValues(set):
    values = np.zeros(10)
    i=0
    for x in set:
        values[i] = x[1]
        i += 1
    print(values)    

def printLaminateOfSolution(solut):
    laminates = [np.zeros((10,10))]
    putRectangle = np.zeros(10)
    rectanglesRepetition = 0
    currentLaminate = 0
    outsideLaminateCuts = 0
    for y in solut:
        print(y[0]+1, " orientación", y[1], " position ", y[2])
        if putRectangle[y[0]] > 0:
            print('Repetido')
            rectanglesRepetition += 1
        else:       
            putRectangle[y[0]] =  y[0]+1
            positionResult = positionate(y[0], y[1], y[2], laminates[currentLaminate])
            if positionResult == 1:                    
                laminates.append(np.zeros((10,10)))
                currentLaminate += 1    
                positionate(y[0], y[1], y[2], laminates[currentLaminate])
            elif positionResult == 2:
                outsideLaminateCuts += 1 
    print(laminates)

#Evalúa si todas las diferentes medidas de rectángulo se encuentran en la lámina
def areAllRectanglesInLaminate(solLaminates):    
    currentLaminateRectangle = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ideal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    errors = 0
    for x in solLaminates:
        for y in x:
            for z in y:                
                currentLaminateRectangle[z.astype(np.int64)] = z.astype(np.int64)
    for x in range(11):        
        if currentLaminateRectangle[x] != ideal[x]:
            errors += 1            
    return errors

def evolutionaryAlgorithm(initialSolutions, iterations):
    laminates = [np.zeros((10,10))]
    rectanglesRepetition = 0    
    putRectangle = np.zeros(10)
    currentLaminate = 0
    currentSolutions = initialSolutions   
    solutionLaminate = [] 
    #Imprimimos la población inicial
    printValues(currentSolutions)   
    printLaminateOfSolution(currentSolutions[0][0])      
    for i in range(iterations):
        for x in currentSolutions:
            solutionLaminate = [] 
            laminates = [np.zeros((10,10))]
            rectanglesRepetition = 0        
            putRectangle = np.zeros(10)
            currentLaminate = 0
            outsideLaminateCuts = 0        
            for y in x[0]:
                #Evalúa si el rectángulo actual ya fue cortado
                if putRectangle[y[0]] > 0:
                    rectanglesRepetition += 1
                else:
                    putRectangle[y[0]] = y[0]+1 
                    positionResult = positionate(y[0], y[1], y[2], laminates[currentLaminate])
                    if positionResult == 1:                    
                        laminates.append(np.zeros((10,10)))                        
                        currentLaminate += 1    
                        positionate(y[0], y[1], y[2], laminates[currentLaminate])
                    elif positionResult == 2:
                        outsideLaminateCuts += 1             
            x[1] = - calculateWaste(laminates)  - (outsideLaminateCuts*100)  - (areAllRectanglesInLaminate(laminates)*2000)
        if i==0:
                #Imprimimos los valores de la función inicial
            printValues(currentSolutions)     
        #Evaluada la población, generamos una nueva mediante el método crossover     
        currentSolutions = crossover(findBestThree(currentSolutions)) 
    printValues(currentSolutions)                   
    printLaminateOfSolution(currentSolutions[0][0])       
    
evolutionaryAlgorithm(initialSetOfSolutions,100000)