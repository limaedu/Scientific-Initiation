
import numpy as np
import random
from math import radians,cos,sin,asin,sqrt


tamanhoPop = 8




class Cidade(self,numero,lat,long):
    self.numero = numero
    self.lat = lat
    self.long = long
    
    def __repr__(self):
        return self.numero

def distancia(self,cidade):
        distX = abs(self.x - cidade.x)
        distY = abs(self.y - cidade.y)
        distancia = np.sqrt(distX**2 + distY**2)
        return distancia
           

def __repr__(self):
        return   self.numero
    

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
    
def DistanciaRota(rota): #Calcula a distância entre cada cidade usando a fórmula de Harversine
        sumDistancia = 0
        for i in range(len(rota)):
            if (i+1) < len(rota):
                Saida = rota[i]
                Chegada = rota[i+1]
                distancia = haversine(Saida.long,Saida.lat,Chegada.long,Chegada.lat)
                sumDistancia += distancia
                
                
            elif (i+1) ==len(rota):
                
                Saida = rota[i]
                Chegada = rota[0]  #Caso esteja na última cidade, retorna à origem
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
        fitnessTotal += round(Fitness(populacao[i]),5) #Fitness da população 
    
    
    
    for j in range(len(populacao)):
        fitnessRank["Rota "+str(j+1)] =   round( 100 * (Fitness(populacao[j]) / fitnessTotal),5)

    return sorted(fitnessRank.items(), key = lambda x:x[1]) #Lista ordenada 
                                                            #com a fitness em ordem crescente




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
            
    return intervalo #Dicionário do tipo {'Rota x': (intervalo fitness) }
    


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


def CrossoverOrdenado(parent1,parent2):
    
    filho1 = np.zeros((1,6), dtype=np.float64)
    filho2 = np.zeros((1,6), dtype = np.float64)
    
    
    while True:
      gene1 = int(random.random()*len(parent1))
      gene2 = int(random.random()*len(parent1))
      if gene1 != gene2:
        break
    
    inicio = min(gene1,gene2)
    fim = max(gene1,gene2)
    
    print (inicio,fim)
    
    for i in range(inicio,fim):
      print (i)
      filho1[0][i] = parent1[i]
      filho2[0][i] = parent2[i]
    
    
    for i in range(-(len(parent2)-fim),fim):
      print (i)
      for j in range(-(len(parent2)-fim),fim):
        if filho1[0][i] == 0 and parent2[i] not in filho1:
          if filho1[0][j] == 0:
            filho1[0][j] = parent2[i]
        if filho2[0][i] == 0 and parent1[i] not in filho2:
          if filho2[0][j] == 0:
            filho2[0][j] = parent1[i]
    
    
    print (filho1)
    
    for i in range(len(parent2)):
      for j in range(len(parent2)):
        if filho1[0][i] == 0 and filho1[0][i] not in parent2:
          if parent2[j] not in filho1:
            filho1[0][i] = parent2[j]
        if filho2[0][i] == 0 and filho2[0][i] not in parent1:
          if parent1[j] not in filho2:
              filho2[0][i] = parent1[j]
    
    return (filho1,filho2)




         

C1 = Cidade("1",-22.908892,-43.177138)
C2 = Cidade("2",-23.550483,-46.633106)
C3 = Cidade("3",-30.033914,-51.229154)
C4 = Cidade("4",-20.319933,-40.336296)
C5 = Cidade("5",-7.120034,-34.876211)
C6 = Cidade("6",-25.433171,-49.27147)
C7 = Cidade("7",-27.593237,-48.543736)
Lista = [C1,C2,C3,C4,C5,C6,C7]
I1 = GerarCromossomo(Lista)

print (I1)



P1 = (GerarPopInicial(tamanhoPop,Lista))

print (FitnessPercent(P1))
print (Roleta(P1))
print (Selecao(P1))
#print (CrossoverOrdenado(I1,I1))
