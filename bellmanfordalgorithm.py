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
    stringresult = " --> ".join(results)

    if len(results) == 1:
        texto = f"Não é possível ir de {u} à {v}"
        print("RESULTADO:", texto)
        return

    else:
            for i in range(len(results) - 1):
                stringatual = f"{results[i]} --> {results[i + 1]} : Distância = {((int(weightresult[i + 1]) - int(weightresult[i]))):.1f} Km "
                resultsstring.append(stringatual)

            stringatual = f"\nDistância Total: {weightresult[-1]} Km"
            resultsstring.append(stringatual)
    resultsstring.append(f"\nRota total:\n{stringresult}")
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
            print('Ciclo negativo encontrado!')
            return

    path(pred, p, origin, destiny)

    return True


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
    bellmanford('Zürich Airport', v, 'Frankfurt am Main International Airport')