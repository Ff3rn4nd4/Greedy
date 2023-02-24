#Utilizando el algoritmo de greedy

#nota: este algoritmo tampoco es muy preciso esto por las fracciones de objetos que agrega 

def greedy(Pesos, Beneficios, PesoMax):
    #len: funcion para leer la cantidad de objetos que hay en nuestra lista
    n = len(Pesos)
    ratios = [(Beneficios[i] / Pesos[i], Pesos[i], Beneficios[i]) for i in range(n)]
    ratios.sort(reverse=True) # Ordenar en orden ascendente por relación beneficio/peso
    #inicializando las variables
    Beneficio_Max = 0
    Peso_Total = 0
     #ratio= relacion benf/peso
     #Estos ciclos representarian nuestra funcion heuristica
     # B/P >= Bi+1/Pi+1 para 1=<i<n
    for ratio, Peso, Beneficio in ratios:
        if Peso_Total + Peso <= PesoMax:
            Beneficio_Max += Beneficio
            Peso_Total += Peso
        else:
            #este algortimo tiene la peculiaridad de meter una fraccion del que considere siguiente objeto que
            #debe de entrar, esto para llenar nuestra mochila
            fraccionObjeto = (PesoMax - Peso_Total) / Peso
            Beneficio_Max += fraccionObjeto * Beneficio
            break
    return Beneficio_Max

#Aplicando valores
Pesos = []
Beneficios = []
PesoMax = n
Beneficio_Max = greedy(Pesos, Beneficios, PesoMax)
print(f"El valor máximo que se puede obtener con una capacidad de {PesoMax} es {Beneficio_Max}")