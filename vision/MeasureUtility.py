import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def getRealCoordinatesOfPoints(initEdges, actualDistance, hCoord):

    G = nx.DiGraph()
    G.add_nodes_from(['A', 'B', 'C', 'H'])

    output = []
    #Add the newly measured edges to the new graph
    for i in range(3):
      p1 = np.array(initEdges[i][0][0:2])
      p2 = np.array(initEdges[i][1][0:2])
      dist = np.linalg.norm(p1-p2)
      direct = (p2 - p1) / dist
      G.add_edge(initEdges[i][0][2], initEdges[i][1][2], weight=actualDistance[i], direct=direct)
      G.add_edge(initEdges[i][1][2], initEdges[i][0][2], weight=actualDistance[i],direct=-1*direct)

    # Calculate the actual position of each node in the graph
    for n in ['A', 'B', 'C']:
        pos = np.array(hCoord)
        node = 'H'
        for p in nx.shortest_path(G, 'H', n)[1::]:
            pos += G[node][p]['weight'] * np.array(G[node][p]['direct'])
            node = p
        output.append(pos)
    return output

if __name__ == "__main__":
    edges = [((224.29906542056074, 158.1308411214953, 'B'), (347.10280373831773, 142.99065420560746, 'C')),
             ((224.29906542056074, 158.1308411214953, 'B'), (128.97196261682242, 270.2803738317757, 'A')),
             ((347.10280373831773, 142.99065420560746, 'C'), (339.8130841121495, 271.9626168224299, 'H'))]
    dists =[101.39033484509261, 99.02019995940222, 64.03124237432849]
    coords = getRealCoordinatesOfPoints(edges, dists, (5.0,5.0))
    coords = np.array(coords)


    print(coords[:,0])
    plt.plot(coords[:,0], -1*coords[:,1], 'o')
    plt.plot(0,0, 'o')

    plt.show()
    print(coords)
