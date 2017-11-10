import networkx as nx
import MapInfo as info
class Map():
    def __init__(self):
        self.G = nx.DiGraph()  # directed graph

    def add_building(self, Name: str, Address: str, MailCode: int):  # add a building as a node to the graph
        # use mail code as key
        self.G.add_node(MailCode, name=Name, addr=Address, flag=0)  # flag=0 means this node is a building

    def add_buildings(self, L: list):  # add a list of buildings
        for x in L:
            self.add_building(x[0], x[1], x[2])

    def add_intersection(self, Name: str): # add a intersection as a node to the graph
        self.G.add_node(Name, flag=1)  # flag=1 means this node is an intersection

    def add_intersections(self, L: list):  # add a list of intersections
        for x in L:
            self.add_intersection(x)

    def add_entry(self, Name: str):  # add an entry as a node to the graph
        self.G.add_node(Name, flag=2)  # flag=2 means this node is an entry to a building

    def add_entries(self, L: list):  # add a list of entries
        for x in L:
            self.add_entry(x)

    def add_diEdge(self, From: str, To: str, Name: str, Distance: int, Direction: str):  # add directed edge to the graph
        self.G.add_edge(From, To, name=Name, dis=Distance, dir=Direction)

    def add_diEdges(self, L: list):  # add a list of directed edges
        for x in L:
            self.add_diEdge(x[0], x[1], x[2], x[3], x[4])

    def add_undiEdge(self, From: str, To: str, Name: str, Distance: int, Direction1: str,
                     Direction2: str):  # add an undirected edge to the graph
        self.G.add_edge(From, To, name=Name, dis=Distance, dir=Direction1)
        self.G.add_edge(To, From, name=Name, dis=Distance, dir=Direction2)

    def add_undiEdges(self, L: list):  # add a list of undirected edges
        for x in L:
            self.add_undiEdge(x[0], x[1], x[2], x[3], x[4], x[5])

    def add_MQPath(self,From: str, To: str, Name: str, Distance: int):  # add path in the main quad
        self.G.add_edge(From, To, name=Name, dis=Distance, dir='NA')
        self.G.add_edge(To, From, name=Name, dis=Distance, dir='NA')

    def add_MQPaths(self, L: list):  # add a list of paths in the main quad
        for x in L:
            self.add_MQPath(x[0], x[1], x[2], x[3])

    def add_entryPath(self, From: str, To: int, Distance: int):  # add an undirected path from an entry to a building
        self.G.add_edge(From, To, dis=Distance)
        self.G.add_edge(To, From, dis=Distance)

    def add_entryPaths(self, L: list):  # add a list of entry path
        for x in L:
            self.add_entryPath(x[0], x[1], x[2])

    def print_buildings(self):  # print all buildings
        tmp = list(filter(lambda x: x[1]['flag'] == 0, self.G.nodes(data=True)))  # all buildings
        tmp.sort(key=lambda x: x[1]['name'])
        print('\033[1m' + 'NAME\t MAIL CODE' + '\033[0m')  # bold this title
        for x in tmp:
            print(x[1]['name'], '\t', x[0])

    def cal_path(self, From: int, To: int):
        Start = self.G.node[From]['name']
        End = self.G.node[To]['name']
        try:
            p = nx.dijkstra_path(self.G, From, To, 'dis')  # find shortest path depending on 'dis' attribute
        except nx.exception.NetworkXNoPath:
            print("There is no path from", Start, "to", End)
        else:
            print('\033[1m' + 'Travel from ' + Start + ' to ' + End + ':' + '\033[0m')
            direction=''
            intoBldflag=0
            for i in range(1, len(p)-2):
                try:
                    if direction != self.G[p[i]][p[i + 1]]['dir']:
                        if i==1:
                            print("Starting on ",end="")
                        else:
                            print("At ",end="")
                        print(self.G[p[i]][p[i + 1]]['name'] ,end="")
                        if self.G[p[i]][p[i + 1]]['dir']=='NA':
                            print(" go through the path on the lawn")
                        else:
                            print(" turn " + self.G[p[i]][p[i + 1]]['dir'])
                        direction = self.G[p[i]][p[i + 1]]['dir']
                except KeyError:
                    if intoBldflag==0:
                        print("Go through the",self.G.node[p[i+1]]['name'])
                        intoBldflag+=1
                    elif intoBldflag==1:
                        intoBldflag=0
            print("Proceed until you arrive at " + End)


def main():
    M = Map()

    M.add_buildings(info.Buildings)
    M.add_intersections(info.Intersections)
    M.add_entries(info.Entries)

    M.add_diEdges(info.DiEdges)
    M.add_undiEdges(info.UndiEdges)
    M.add_entryPaths(info.EntryPaths)
    M.add_MQPaths(info.MainQuadPaths)
    M.print_buildings()


    M.cal_path(493,384)
    M.cal_path(522,51)
    M.cal_path(312, 51)

if __name__ == "__main__":
	main()