# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import numpy as np
import random
from math import radians,cos,sin,asin,sqrt


tamanhoPop = 8



class Cidade:
    def __init__(self,nome,lat,long):
        self.lat = lat #Latitude da cidade 
        self.long = long #Longitude da cidade
        self.nome = nome
    
    '''def distancia(self,cidade):
        distX = abs(self.x - cidade.x)
        distY = abs(self.y - cidade.y)
        distancia = np.sqrt(distX**2 + distY**2)
        return distancia
        '''    

    def __repr__(self):
        return   "Nome: {}  ".format(self.nome)
    

def GerarCromossomo(ListaDeCidades):
    rota = random.sample(ListaDeCidades,len(ListaDeCidades)) #Gera um sample(amostra) com itens da lista de cidades
    return rota                                              #com o tamanho da lista de cidades


def GerarPopInicial(tamanhoPop,ListaDeCidades): #Gera uma pop inicial de rotas(indivíduos) 
    ListaPop = []
    for i in range(tamanhoPop):
        ListaPop.append(GerarCromossomo(ListaDeCidades)) 
        
    
    return ListaPop


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r    
    
def DistanciaRota(rota): #Calcula a distância entre cada cidade usando a fórmula de Harversine, voltando à origem
        sumDistancia = 0
        for i in range(len(rota)):
            if (i+1) < len(rota):
                Saida = rota[i]
                Chegada = rota[i+1]
                distancia = haversine(Saida.long,Saida.lat,Chegada.long,Chegada.lat)
                sumDistancia += distancia
                
                
            elif (i+1) ==len(rota):
                
                Saida = rota[i]
                Chegada = rota[0]
                distancia = haversine(Saida.long,Saida.lat,Chegada.long,Chegada.lat)
                sumDistancia += distancia
        
        return sumDistancia
    


def Fitness(lista): 
    
    fitness = (1/(DistanciaRota(lista))) * 10000
    
    return fitness
    

def FitnessPercent(populacao):
    fitnessTotal = 0
    fitnessRank = {}
    for i in range(len(populacao)):
        fitnessTotal += round(Fitness(populacao[i]),5)
    
    
    
    for j in range(len(populacao)):
        fitnessRank["Rota "+str(j+1)] =   round( 100 * (Fitness(populacao[j]) / fitnessTotal),5)

    return sorted(fitnessRank.items(), key = lambda x:x[1]) #Lista ordenada com a fitness percentual em ordem crescente




def Roleta(populacao):
    soma = 0
    intervalo = {}
    valoresfitness = []
    ranked = FitnessPercent(populacao)
    for j in range(len(ranked)):
        valoresfitness.append(ranked[j][1])
    print (valoresfitness)    
    for i in range(len(ranked)):
        if i == 0:
            intervalo[ranked[i][0]] = (0.0,ranked[i][1])
            soma += ranked[i][1]
        else:
            intervalo[ranked[i][0]] = (soma, soma +ranked[i][1])
            soma += ranked[i][1]
            
    return intervalo
    


def Selecao(populacao):
    selecionados = []
    roleta = Roleta(populacao)
    for _ in range(len(roleta)):
        aleatorio = random.uniform(0,100)
        print (aleatorio)
        for i in roleta:
            interval = roleta[i]
            if aleatorio > interval[0] and aleatorio < interval[1]:
                selecionados.append(i)
    

    return selecionados
    


# MUDEI AQUI Ó
    
    
    
    
    
    

C1 = Cidade("RJ",-22.908892,-43.177138)
C2 = Cidade("SP",-23.550483,-46.633106)
C3 = Cidade("RS",-30.033914,-51.229154)
C4 = Cidade("ES",-20.319933,-40.336296)
C5 = Cidade("PA",-7.120034,-34.876211)
C6 = Cidade("PR",-25.433171,-49.27147)
C7 = Cidade("SC",-27.593237,-48.543736)
Lista = [C1,C2,C3,C4,C5,C6,C7]
I1 = GerarCromossomo(Lista)





P1 = (GerarPopInicial(tamanhoPop,Lista))

#print (FitnessPercent(P1))
print (Roleta(P1))
print (Selecao(P1))