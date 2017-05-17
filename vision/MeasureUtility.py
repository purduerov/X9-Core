import networkx as nx
from math import sqrt


def getRealCoordinatesOfPoints(initEdges, actualDistance):

    G = nx.DiGraph()
    G.add_nodes_from(['A', 'B', 'C', 'H'])

    output = []
    #Add the newly measured edges to the new graph
    for i in range(3):
      p1 = initEdges[i][0][0:2]
      p2 = initEdges[i][1][0:2]
      dist = sqrt((p2[0]-p1[0])**2 + (p2[1] - p1[1])**2)
      direct=((p2[0]-p1[0])/dist, (p2[1] - p1[1])/dist)
      G.add_edge(initEdges[i][0][2], initEdges[i][1][2], weight=actualDistance[i],key='{}'.format(i), direct=direct)
      G.add_edge(initEdges[i][1][2], initEdges[i][0][2], weight=actualDistance[i], key ='-{}'.format(i),
          direct=(-1*direct[0], -1*direct[1]))

    # Calculate the actual position of each node in the graph
    for n in ['A', 'B', 'C']:
        pos = (0,0)
        node = 'H'
        for p in nx.shortest_path(G, 'H', n)[1::]:
            x =  (G[node][p]['weight'], G[node][p]['direct'])
            pos = (pos[0] + x[0]*x[1][0], pos[1]+x[0]*x[1][1])
            node = p
        output.append(pos)
