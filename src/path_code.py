from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
@app.route('/s_path', methods=['POST'])
def s_path():
    # Gets info froms inputs
    data = request.get_json()
    room1 = int(data.get("room1"))
    room2 = int(data.get("room2"))
    # Processes inputs
    stuff = get_message(room1, room2)
    # Returns results
    response_message = f"Done processing for {room1} and {room2}"
    return jsonify({"message": response_message, "result": stuff})

if __name__ == '__main__':
    app.run(debug=True)
  
import sys

class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.og_nodes = []
        self.graph = self.construct_graph(nodes, init_graph)

        for i in nodes:
            self.og_nodes.append(i)

    def construct_graph(self, nodes, init_graph):
        '''
        This method makes sure that the graph is symmetrical. In other words, if there's a path from node A to B with a value V, there needs to be a path from node B to node A with a value V.
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value

        return graph

    def add(self, start, end, weight):
        if start not in self.nodes:
            self.nodes.append(start)
            self.graph[start] = {}
        elif end not in self.nodes:
            self.nodes.append(end)
            self.graph[end] = {}
        self.graph[start][end] = weight
        self.graph[end][start] = weight

    def remove(self, start, end):
        self.graph[start].pop(end)
        self.graph[end].pop(start)

    def reset(self):
        temp = []
        for i in self.og_nodes:
            temp.append(i)
        for i in self.nodes:
            if i not in self.og_nodes:
                self.graph.pop(i)
        self.nodes = temp

    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes

    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]

#Manual Input Map
timeWeight = {}

distWeight = {
    "SC17": 148,
    "SC15": 180,
    "SC13": 170,
    "SC11": 286,

    "BB10": 299,
    "BB11": 195,
    "BB12": 195,
    "BB13": 212,

    "SS11": 138,
    "SS12": 32,
    "SS13": 64,

    "MC11": 148,
    "MC12": 42,
    "MC13": 42,

    "MD11": 3*32,
    "MD12": 42+32,
    "MD13": 42
}

school_nodes = {"SA1","SI1","SM1","A1","B1","C1","D1","E1","F1","G1","H1","J1","K1","L1","N1","O1"}

roomsInRoad = {
    "SC17": [177,174,173,172,171,170],
    "SC15": [157,156,155,143,153,152,151],
    "SC13": [138,136,137,134,135,132,133,130,131],
    "SC11": ["EXIT"],

    "BB10": ["EXIT"],
    "BB11": [],
    "BB12": [],
    "BB13": ["EXIT"],

    "SS11": ["WR_B","WR_G",160,161,163,162,165,164],
    "SS12": [167,158],
    "SS13": [166,168,"EXIT"],

    "MC11": ["140_Health",141,142,141,144,143,"145_CAP",146,147],
    "MC12": [],
    "MC13": [148,"EXIT"],

    "MD11": [120,122,117,121],
    "MD12": [119,123,124],
    "MD13": [126,128]
}

vertices = {
    "SA1": {"D1"},
    "SI1": {"H1"},
    "SM1": {"L1"},
    "A1": {"B1"},
    "B1": {"A1","C1","F1"},
    "C1": {"B1","D1","H1"},
    "D1": {"SA1","C1","E1"},
    "E1": {"D1"},
    "F1": {"C1","G1","J1"},
    "G1": {"F1","H1","L1"},
    "H1": {"C1","G1","SI1"},
    "J1": {"F1","K1","N1"},
    "K1": {"J1","L1","O1"},
    "L1": {"G1","K1","SM1"},
    "N1": {"J1"},
    "O1": {"K1"}
}

plainGraph = {
    "SC17": {"SA1","D1"},
    "SC15": {"C1","H1"},
    "SC13": {"G1","L1"},
    "SC11": {"K1","O1"},

    "BB10": {"A1","B1"},
    "BB11": {"B1","F1"},
    "BB12": {"F1","J1"},
    "BB13": {"J1","N1"},

    "SS11": {"B1","C1"},
    "SS12": {"C1","D1"},
    "SS13": {"D1","E1"},

    "MC11": {"F1","G1"},
    "MC12": {"G1","H1"},
    "MC13": {"H1","SI1"},

    "MD11": {"J1","K1"},
    "MD12": {"K1","L1"},
    "MD13": {"L1","SM1"}
}

inv_plainGraph = {}
for key in plainGraph:
    if(list(plainGraph[key])[0] not in inv_plainGraph):
        inv_plainGraph[list(plainGraph[key])[0]] = {}
    if(list(plainGraph[key])[1] not in inv_plainGraph):
        inv_plainGraph[list(plainGraph[key])[1]] = {}
    inv_plainGraph[list(plainGraph[key])[0]][list(plainGraph[key])[1]] = key
    inv_plainGraph[list(plainGraph[key])[1]][list(plainGraph[key])[0]] = key

nodes = ["SA1","SI1","SM1","A1","B1","C1","D1","E1","F1","G1","H1","J1","K1","L1","N1","O1"]

init_graph = {}
for node in nodes:
    init_graph[node] = {}

init_graph["SA1"]["D1"] = 148

init_graph["SI1"]["H1"] = 42

init_graph["SM1"]["L1"] = 42

init_graph["A1"]["B1"] = 299

init_graph["B1"]["C1"] = 138
init_graph["B1"]["F1"] = 195

init_graph["C1"]["D1"] = 32
init_graph["C1"]["H1"] = 180

init_graph["D1"]["E1"] = 64

init_graph["F1"]["G1"] = 148
init_graph["F1"]["J1"] = 195

init_graph["G1"]["H1"] = 42
init_graph["G1"]["L1"] = 170

init_graph["J1"]["K1"] = 3*32
init_graph["J1"]["N1"] = 212

init_graph["K1"]["L1"] = 42+32
init_graph["K1"]["O1"] = 286

#previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="Reykjavik")

#djikstra's algorithm
#code taken from udacity and edited for our purposes (https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html)
def shortest_path_alg(graph, start_road,  start, end_road, destination, time):
    global school_nodes
    global plainGraph
    global roomsInRoad
    global distWeight
    weight = distWeight
    if time:
        weight = timeWeight


    # START side adding temp nodes
    road_nodes = list(plainGraph[start_road])
    start_node1 = road_nodes[0]
    start_node2 = road_nodes[1]
    room1 = start

    # setting new temp weights for new road segments
    length1 = weight[start_road]
    roomsInS1 = roomsInRoad[start_road]
    index1 = 0
    for i in range(len(roomsInS1)):
        if roomsInS1[i] == room1:
            index1 = i
    s_1s = (index1 + 1)/(len(roomsInS1)+1)*length1
    s_2s = length1 - s_1s

    # changing original graph to add new roads
    graph.remove(start_node1, start_node2)
    graph.add(start_node1, room1, s_1s)
    graph.add(room1, start_node2, s_2s)

    # END side adding temp nodes
    road_nodes = list(plainGraph[end_road])
    end_node1 = road_nodes[0]
    end_node2 = road_nodes[1]
    room2 = destination

    # setting new temp weights for new road segments
    length2 = weight[end_road]
    roomsInS1 = roomsInRoad[end_road]
    index1 = 0
    for i in range(len(roomsInS1)):
        if roomsInS1[i] == room2:
            index1 = i
    s_1 = (index1 + 1)/(len(roomsInS1)+1)*length2
    s_2 = length2 - s_1

    # changing original graph to add new roads
    if start_road != end_road:
        graph.remove(end_node1, end_node2)
    graph.add(end_node1, room2, s_1)
    graph.add(room2, end_node2, s_2)

    start_node = start
    end_node = destination


    unvisited_nodes = []
    for node in school_nodes:
        unvisited_nodes.append(node)
    unvisited_nodes.append(room1)
    unvisited_nodes.append(room2)

    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph
    shortest_path = {}

    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}

    # We'll use max_value to initialize the "infinity" value of the unvisited nodes
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0
    shortest_path[start_node] = 0

    # The algorithm executes until we visit all nodes
    current_min_node = None
    while current_min_node != destination:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node

        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)

    graph.add(start_node1, start_node2, length1)
    if start_road != end_road:
      graph.add(end_node1, end_node2, length2)
    graph.remove(start_node1, room1)
    graph.remove(room1, start_node2)
    graph.remove(end_node1, room2)
    graph.remove(room2, end_node2)
    graph.reset()

    intersec_path = print_result(previous_nodes, shortest_path, room1, room2, False)
    hallway_path = []
    hallway_path.append(start_road)
    for i in range(len(intersec_path)-3):
        hway = inv_plainGraph[intersec_path[i+1]][intersec_path[i+2]]
        hallway_path.append(hway)
    hallway_path.append(end_road)
    if start_road != end_road:
        return previous_nodes, shortest_path, hallway_path
    else:
        hallway_path = []
        hallway_path.append(start_road)
        return previous_nodes, abs(s_1s-s_1), hallway_path

def print_result(previous_nodes, shortest_path, start_node, target_node, printIt):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    # Add the start node manually
    path.append(start_node)
    for i in range(len(path)):
        path[i] = str(path[i])
    if printIt:
        return "We found the following best path with a length of {}.".format(shortest_path[target_node])+"\nPath: "+" -> ".join(reversed(path))

    return path[::-1]

graph = Graph(nodes, init_graph)
'''
import random

class student:

  def __init__(self):
    self.fromClass = ""
    self.goClass = ""

  def setFromClass(self, className):
    self.fromClass = className

  def setGoClass(self, className):
    self.goClass = className

  def randomRoom(self):
    roomLst = [177,174,173,172,171,170,157,156,155,143,153,152,151,138,136,137,134,135,132,133,130,131,160,161,163,162,165,164,167,158,166,168,141,142,141,144,143,146,147,148,120,122,117,121,119,123,124,126,128]
    randRoom = random.choice(roomLst)

    randRoad = ""
    for road in roomsInRoad:
        for room in roomsInRoad[road]:
            if room == randRoom:
                randRoad = road
                break
    return randRoad, randRoom

  def randomExit(self):
    randomInt = random.randint(0,9)
    exitHalls = ["SS13","MC13","MD13","SC11"]
    if randomInt <= 4:
      return "BB10"
    elif randomInt <= 7:
      return "BB13"
    else:
      return random.choice(exitHalls)

class hallway:
  def __init__(self, name):
    self.name = name
    self.timesTraveled = 0
    #self.length = length
    self.classrooms = roomsInRoad[name]

  def travelOnce(self):
    self.timesTraveled += 1

import math
# BASED OFF OF PAPER's GRAPH page 2 (https://www.sciencedirect.com/science/article/abs/pii/0191261594900132)
# density = People/(distance*width) * (3.28084)^2
# speed = (1.83792*1.7411^(-density)+0.2)*3.28084
# time = distance / speed

for hallway in distWeight:
    if timesTraveled[hallway] != 0:
        density = timesTraveled[hallway] / (distWeight[hallway] * 9) * (3.28084 ** 2)
        if hallway[0:2] == "BB":
            density = density * 16 / 9
        speed = (1.83792*1.7411**(-density)+0.2)*3.28084
        timeWeight[hallway] = distWeight[hallway] / speed
    else:
        timeWeight[hallway] = distWeight[hallway] / 4.4

time_init_graph = {}
for hallway in timeWeight:
    node1 = list(plainGraph[hallway])[0]
    node2 = list(plainGraph[hallway])[1]
    if node1 not in time_init_graph:
        time_init_graph[node1] = {}
    if node2 not in time_init_graph:
        time_init_graph[node2] = {}
    time_init_graph[node1][node2] = timeWeight[hallway]
    time_init_graph[node2][node1] = timeWeight[hallway]

timeGraph = Graph(nodes, time_init_graph)
'''

# THIS ONE IS FOR USER INPUT
def get_message(room1, room2):
    findPath = True
    global roomsInRoad
    global graph
    while findPath:
        fromHall = ""
        while fromHall == "":
            startRoom = room1
            for road in roomsInRoad:
                for room in roomsInRoad[road]:
                    if room == startRoom:
                        fromHall = road
                        break
            if fromHall == "":
                return "Start classroom doesn't exist! At least not for learning purposes..."

        goHall = ""
        while goHall == "":
            endRoom = room2
            for road in roomsInRoad:
                for room in roomsInRoad[road]:
                    if room == endRoom:
                        goHall = road
                        break
            if goHall == "":
                return "End classroom doesn't exist! At least not for learning purposes..."
        
        findPath = False
        intersec_path, length, path = shortest_path_alg(graph, fromHall, startRoom, goHall, endRoom, False)
        return print_result(intersec_path, length, startRoom, endRoom, True)
      