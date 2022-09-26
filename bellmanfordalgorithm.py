import networkx as nx
import matplotlib.pyplot as plt
import csv
class Vertices:
    def __init__(self):
        self.airports = []
        self.paths = []


def relax(p, u, v, w, pred):
    if p[v] > p[u] + w:
        pred[v] = u
        p[v] = p[u] + w


def path(predecessor, weight, u, v):
    results = [v]
    ant = predecessor[v]

    weightresult = [str(weight[v])]

    while ant != -1:
        results.append(ant)
        weightresult.append(str(weight[ant]))
        ant = predecessor[ant]

    results = results[::-1]
    weightresult = weightresult[::-1]
    resultsstring = []
    stringresult = " > ".join(results)

    if len(results) == 1:

        print("Não é possível ir de", u, "à", v)
        return

    else:
            for i in range(len(results) - 1):
                stringatual = f"{results[i]} > {results[i + 1]} : Distância = {((int(weightresult[i + 1]) - int(weightresult[i]))):.1f} Km "
                resultsstring.append(stringatual)

            stringatual = f"\nDistância total: {weightresult[-1]} Km"
            resultsstring.append(stringatual)
    resultsstring.append(f"\nCaminho:\n{stringresult}")
    stringfinal = "\n".join(resultsstring)

    print("MENOR ROTA:", stringfinal)


def bellmanford(origin, graph, destiny):
    pred = {}
    p = {}
    for i in graph.airports:
        p[i] = 9999999999
        pred[i] = -1

    p[origin] = 0

    for i in range(len(graph.airports) - 1):
        for u, v, w in graph.paths:
            relax(p, u, v, w, pred)

    for u, v, w in graph.paths:
        if p[v] > p[u] + w:
            print('Ciclo negativo detectado')
            return

    path(pred, p, origin, destiny)

    return True

def viewGraph(graph):
    G = nx.DiGraph()
    G.add_edges_from(graph)
    nx.draw_networkx(G)
    plt.show()

v = Vertices()
graph = []
v = Vertices()
with open('dataset.csv', newline='') as csvfile:
    airportdata = csv.reader(csvfile)
    for line in airportdata:
        origin, destination, distance = line[0], line[1], line[2]
        if origin not in v.airports:
            v.airports.append(origin)
        if destination not in v.airports:
            v.airports.append(destination)
        v.paths.append([origin,destination,int(distance)])
        graph.append([origin,destination])
    originInput = input('Digite o aeroporto origem: ')
    destinationInput = input('Digite o aeroporto destino: ')
    if originInput not in v.airports or destinationInput not in v.airports:
        print('Aeroporto não encontrado.')
    else:
        bellmanford(originInput, v, destinationInput)
        viewGraph(graph)