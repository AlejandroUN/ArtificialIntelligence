#Sistemas Inteligentes
#Ejercicio Práctico - Agentes basados en búsqueda
#Implementación Hill Climbing

import numpy as np
import random

permutations = []

orientations = ['vertical', 'horizontal']
rectangles = [[8,3], [5,1], [2,2], [1,1], [9,4], [6,2], [4,3], [5,7], [3,2], [4,2]]
posiblePositions = []
combinations = []
solutions = []

#Calculamos todas las diferentes ubicaciones para los cortes de los rectángulos
def calculatePosiblePositions():
    for x in range(10):
        for y in range(10):
            posiblePositions.append([x,y])    

calculatePosiblePositions()

def calculateDifferentRectanglesPositions():        
    for x in range(10):
        #Calculamos todas las diferentes combinaciones de posiciones y orientación para cada tipo de rectángulo 
        combination = []
        for y in range(2):
            for z in posiblePositions:
                combination.append([x,y,z])
        combinations.append(combination)        

calculateDifferentRectanglesPositions()

#Calcular todas las posibles soluciones (200^10) tomaría un tiempo considerable
#Así que se procederá a calcular un número de soluciones
#Que se ingresará como parámetro
def calculateSolutions(numberOfSolutions):    
    for x in range(numberOfSolutions):
        solution = []
        rectanglesUsed = np.zeros(10)
        for y in range(10):
            rectangle = random.choice([0,1,2,3,4,5,6,7,8,9])
            while (rectanglesUsed[rectangle] > 0):
                    rectangle = random.choice([0,1,2,3,4,5,6,7,8,9])                          
            rectanglesUsed[rectangle] = rectangle + 1
            solution.append(random.choice(combinations[rectangle]))
        solutions.append(solution)