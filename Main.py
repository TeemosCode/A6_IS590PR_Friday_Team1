import networkx as nx


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
                     Direction2: str):  # add an undireted edge to the graph
        self.G.add_edge(From, To, name=Name, dis=Distance, dir=Direction1)
        self.G.add_edge(To, From, name=Name, dis=Distance, dir=Direction2)

    def add_undiEdges(self, L: list):  # add a list of undireted edges
        for x in L:
            self.add_undiEdge(x[0], x[1], x[2], x[3], x[4], x[5])

    def add_entryPath(self, From: str, To: int, Distance: int):  # add a undirected path from an entry to a building
        self.G.add_edge(From, To, dis=Distance)
        self.G.add_edge(To, From, dis=Distance)

    def add_entryPaths(self, L: list):  # add a list of entry path
        for x in L:
            self.add_entryPath(x[0], x[1], x[2])

    def print_buildings(self):  # print all buildings
        tmp = list(filter(lambda x: x[1]['flag'] == 0, self.G.nodes(data=True)))  # all buildings
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
            for i in range(1, len(p)-2):
                if direction != self.G[p[i]][p[i + 1]]['dir']:
                    print("Starting on " + self.G[p[i]][p[i + 1]]['name'] + " turn " + self.G[p[i]][p[i + 1]]['dir'])
                    direction = self.G[p[i]][p[i + 1]]['dir']
            print("Proceed until you arrive at " + End)


def main():
    M = Map()
    # test
    # M.add_building('BuildA', 'addr Build A', 111)
    # M.add_building('BuildB', 'addr Build B', 222)
    # M.add_building('BuildC', 'addr Build C', 333)
    # M.add_building('BuildD', 'addr Build D', 444)
    #
    # M.add_edge('A2B', 'BuildA', 'BuildB', 200, 'North')
    # M.add_edge('B2C', 'BuildB', 'BuildC', 200, 'East')
    # M.add_edge('C2D', 'BuildC', 'BuildD', 200, 'South')
    # M.add_edge('D2A', 'BuildD', 'BuildA', 200, 'West')
    # M.add_edge('A2C', 'BuildA', 'BuildC', 100, 'Cross')
    #
    # M.cal_path('BuildA', 'BuildC')

    Buildings = [  # information of buildings - name, address, mail code
        ('Foreign Languages Building', '707 S. Matthews Ave.', 164),
        ('Lincoln Hall', '702 S. Wright St.', 456),
        ('Enlish Building', '608 S. Wright St.', 718),
        ('Armory','505 E. Armory St.',532)
    ]

    Intersections = [  # names of the intersection
        'Chalmers & Wright',
        'Daniel & Wright',
        'Armory & Wright'
    ]

    Entries = [  # names of the entries
        'to Foreign Languages Building on Mathews',
        'to Lincoln Hall on Wright',
        'to English Building on Wright',
        'to xxxbuilding on xxxroad'
    ]

    DiEdges = [  # directed edges - From, To, Name, Distance, Direction
        ('Armory & Wright', 'to Lincoln Hall on Wright', 'S. Wright St.', 150, 'North'),
        ('to Lincoln Hall on Wright', 'Chalmers & Wright', 'S. Wright St.', 50, 'North')
    ]

    UndiEdges = [  # undirected edges - From, To, Name, Distance, Direction1(From->To), Direction2(To->From)
        ('Chalmers & Wright', 'to English Building on Wright', 'S. Wright St.', 100, 'North', 'South'),
        ('to Lincoln Hall on Wright', 'Chalmers & Wright', 'S. Wright St.', 50, 'North', 'South'),
    ]

    EntryPaths = [  # undirected path - name of the entry to building, mail code of the building, distance
        ('to English Building on Wright', 718, 50),
        ('to Lincoln Hall on Wright', 456, 50)
    ]

    M.add_buildings(Buildings)
    M.add_intersections(Intersections)
    M.add_entries(Entries)

    M.add_diEdges(DiEdges)
    M.add_undiEdges(UndiEdges)
    M.add_entryPaths(EntryPaths)

    M.print_buildings()
    M.cal_path(456, 718)


main()
