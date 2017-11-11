import networkx as nx


class Map():
    Buildings = [  # information of buildings - name, address, mail code
        ('School of Information Sciences', '501 E. Daniel St.', 493),
        ('Illini Union BookStore', '807 S. Wright St.', 312),
        ('Altgeld Hall', '1409 W. Green St.', 382),
        ('Illini Union', '1401 W. Green St.', 384),
        ('Henry Administration Building', '506 S. Wright St.', 368),
        ('English Building', '608 S. Wright St.', 718),
        ('Lincoln Hall', '702 S. Wright St.', 456),
        ('Gregory Hall', '810 S. Wright St.', 462),
        ('Main Library', '1408 W. Gregory Dr.', 522),
        ('Institute For Genomic Biology', '1206 W. Gregory Dr.', 195),
        ('Smith Memorial Hall (Music)', '805 S. Mathews Ave.', 56),
        ('Foreign Language Building', '707 S. Mathews Ave.', 164),
        ('Davenport Hall', '607 S. Mathews Ave.', 151),
        ('UI Ice Arena', '406 E. Armory Ave.', 525),
        ('Armory', '505 E. Armory Ave.', 528),
        ('Medical Sciences Building', '506 S. Mathews', 714),
        ('Roger Adams Lab', '600 S. Mathews', 712),
        ('Native American House', '1206 W. Nevada', 139),
        ('Animal Sciences Lab', '1207 W. Gregory', 630),
        ('Edward R. Madigan Lab', '1201 W. Gregory', 51)

    ]

    Intersections = [  # names of the intersection
        'John & 4th',
        'John & 5th',
        'John & 6th',
        'John & Wright',
        'Daniel & 4th',
        'Daniel & 5th',
        'Daniel & 6th',
        'Daniel & Wright',
        'Chalmers & 4th',
        'Chalmers & 5th',
        'Chalmers & 6th',
        'Chalmers & Wright',
        'Armory & 4th',
        'Armory & 5th',
        'Armory & 6th',
        'Armory & Wright',
        'Gregory & 4th',
        'Gregory & 6th',
        'Green & Wright',
        'Green & Mathews',
        'Green & Goodwin',
        'Oregon & Mathews',
        'Oregon & Goodwin',
        'Nevada & Mathews',
        'Nevada & Goodwin',
        'Gregory & Goodwin',
        'Main Quad'
        # 'Gregory & Dorner' Do not need this intersection
    ]

    Entries = [  # names of the entries
        'to School of Information Sciences on Daniel',
        'to UI Ice Arena on Armory',
        'to Armory on Armory',
        'to Armory on Gregory',
        'to Illini Union BookStore on Daniel',
        'to Illini Union BookStore on Wright',
        'to Altgeld Hall on Wright',
        'to Altgeld Hall on Green',
        'to Illini Union on Green',
        'to Henry Administration Building on Wright',
        'to English Building on Wright',
        'to Lincoln Hall on Wright',
        'to Gregory Hall on Wright',
        'to Main Library on Armory',
        'to Main Library on Gregory',
        'to Davenport Hall on Mathews',
        'to Foreign Language Building on Mathews',
        'to Smith Memorial Hall (Music) on Mathews',
        'to Institute For Genomic Biology on Goodwin',
        'to Illini Union on Main Quad',
        'to Henry Administration Building on Main Quad',
        'to English Building on Main Quad',
        'to Lincoln Hall on Main Quad',
        'to Davenport Hall on Main Quad',
        'to Foreign Language Building on Main Quad',
        'to Medical Sciences Building on Mathews',
        'to Roger Adams Lab on Goodwin',
        'to Native American House on Nevada',
        'to Animal Sciences Lab on Gregory',
        'to Edward R. Madigan Lab on Gregory'
    ]

    DiEdges = [  # directed edges - From, To, Name, Distance, Direction
        ('John & 4th', 'John & 5th', 'E. John St.', 150, 'East'),
        ('John & 5th', 'John & 6th', 'E. John St.', 150, 'East'),
        ('John & Wright', 'John & 6th', 'E. John St.', 150, 'West'),

        ('Daniel & 6th', 'Daniel & Wright', 'E. Daniel St.', 150, 'East'),  # Entry to BookStore on Daniel
        ('Daniel & 6th', 'to Illini Union BookStore on Daniel', 'E. Daniel St.', 100, 'East'),
        ('to Illini Union BookStore on Daniel', 'Daniel & Wright', 'E. Daniel St.', 50, 'East'),

        ('Chalmers & Wright', 'Chalmers & 6th', 'E. Chalmers St.', 150, 'West'),
        ('Armory & 6th', 'Armory & Wright', 'E. Armory St.', 150, 'East'),

        ('Oregon & Goodwin', 'Oregon & Mathews', 'W. Oregon St.', 150, 'West'),

        ('Nevada & Mathews', 'Nevada & Goodwin', 'W. Nevada St.', 150, 'East'),  # Entry to Native American House
        ('Nevada & Mathews', 'to Native American House on Nevada', 'W. Nevada St.', 100, 'East'),
        ('to Native American House on Nevada', 'Nevada & Goodwin', 'W. Nevada St.', 50, 'East'),

        ('John & 6th', 'Daniel & 6th', 'S. 6th St.', 150, 'South'),
        ('Daniel & 6th', 'Chalmers & 6th', 'S. 6th St.', 150, 'South'),
        ('Chalmers & 6th', 'Armory & 6th', 'S. 6th St.', 150, 'South'),

        ('Armory & Wright', 'Chalmers & Wright', 'S. Wright St.', 150, 'North'),  # Entry to Lincoln Hall
        ('Armory & Wright', 'to Lincoln Hall on Wright', 'S. Wright St.', 120, 'North'),
        ('to Lincoln Hall on Wright', 'Chalmers & Wright', 'S. Wright St.', 30, 'North'),

        ('Green & Mathews', 'Oregon & Mathews', 'S. Mathews Ave.', 450, 'South'),
        # Entry to Davenport Hall and Medical Blg
        ('Green & Mathews', 'to Medical Sciences Building on Mathews', 'S. Mathews Ave.', 250, 'South'),
        ('to Medical Sciences Building on Mathews', 'Oregon & Mathews', 'S. Mathews Ave.', 200, 'South'),
        ('to Medical Sciences Building on Mathews', 'to Davenport Hall on Mathews', 'S. Mathews Ave.', 170, 'South'),
        ('Green & Mathews', 'to Davenport Hall on Mathews', 'S. Mathews Ave.', 420, 'South'),
        ('to Davenport Hall on Mathews', 'Oregon & Mathews', 'S. Mathews Ave.', 30, 'South'),

        ('Oregon & Mathews', 'Nevada & Mathews', 'S. Mathews Ave.', 150, 'South'),  # Entry to Foreign Languages Blg
        ('Oregon & Mathews', 'to Foreign Language Building on Mathews', 'S. Mathews Ave.', 120, 'South'),
        ('to Foreign Language Building on Mathews', 'Nevada & Mathews', 'S. Mathews Ave.', 30, 'South')
    ]

    UndiEdges = [  # undirected edges - From, To, Name, Distance, Direction1(From->To), Direction2(To->From)
        ('Daniel & 4th', 'Daniel & 5th', 'E. Daniel St.', 150, 'East', 'West'),

        ('Daniel & 5th', 'Daniel & 6th', 'E. Daniel St.', 150, 'East', 'West'),  # Entry to iSchool
        ('Daniel & 5th', 'to School of Information Sciences on Daniel', 'E. Daniel St.', 50, 'East', 'West'),
        ('to School of Information Sciences on Daniel', 'Daniel & 6th', 'E. Daniel St.', 100, 'East', 'West'),

        ('Chalmers & 4th', 'Chalmers & 5th', 'E. Chalmers St.', 150, 'East', 'West'),
        ('Chalmers & 5th', 'Chalmers & 6th', 'E. Chalmers St.', 150, 'East', 'West'),

        ('Armory & 4th', 'Armory & 5th', 'E. Armory Ave.', 150, 'East', 'West'),  # Entry to Ice Arena
        ('Armory & 4th', 'to UI Ice Arena on Armory', 'E. Armory Ave.', 100, 'East', 'West'),
        ('to UI Ice Arena on Armory', 'Armory & 5th', 'E. Armory Ave.', 50, 'East', 'West'),

        ('Armory & 5th', 'Armory & 6th', 'E. Armory Ave.', 150, 'East', 'West'),

        ('Gregory & 4th', 'Gregory & 6th', 'E. Gregory Dr.', 300, 'East', 'West'),  # Entry to Armory on Gregory
        ('Gregory & 4th', 'to Armory on Gregory', 'E. Gregory Dr.', 150, 'East', 'West'),
        ('to Armory on Gregory', 'Gregory & 6th', 'E. Gregory Dr.', 150, 'East', 'West'),

        ('Gregory & 6th', 'Gregory & Goodwin', 'W. Gregory Dr.', 600, 'East', 'West'),
        # Entry to Library on Gregory and Animal Sciences Lab
        ('Gregory & 6th', 'to Main Library on Gregory', 'W. Gregory Dr.', 150, 'East', 'West'),
        ('to Main Library on Gregory', 'Gregory & Goodwin', 'W. Gregory Dr.', 450, 'East', 'West'),
        ('Gregory & 6th', 'to Animal Sciences Lab on Gregory', 'W. Gregory Dr.', 500, 'East', 'West'),
        ('to Animal Sciences Lab on Gregory', 'Gregory & Goodwin', 'W. Gregory Dr.', 100, 'East', 'West'),
        ('to Main Library on Gregory', 'to Animal Sciences Lab on Gregory', 'W. Gregory Dr.', 350, 'East', 'West'),

        ('Green & Wright', 'Green & Mathews', 'W. Green Dr.', 300, 'East', 'West'),
        # Entry to Altgeld Hall and Illini Union on Green
        ('Green & Wright', 'to Altgeld Hall on Green', 'W. Green Dr.', 30, 'East', 'West'),
        ('to Altgeld Hall on Green', 'Green & Mathews', 'W. Green Dr.', 270, 'East', 'West'),
        ('Green & Wright', 'to Illini Union on Green', 'W. Green Dr.', 140, 'East', 'West'),
        ('to Illini Union on Green', 'Green & Mathews', 'W. Green Dr.', 160, 'East', 'West'),
        ('to Altgeld Hall on Green', 'to Illini Union on Green', 'W. Green Dr.', 110, 'East', 'West'),

        ('Green & Mathews', 'Green & Goodwin', 'W. Green Dr.', 150, 'East', 'West'),

        ('John & 4th', 'Daniel & 4th', 'S. 4th St.', 150, 'South', 'North'),
        ('Daniel & 4th', 'Chalmers & 4th', 'S. 4th St.', 150, 'South', 'North'),
        ('Chalmers & 4th', 'Armory & 4th', 'S. 4th St.', 150, 'South', 'North'),
        ('Armory & 4th', 'Gregory & 4th', 'S. 4th St.', 150, 'South', 'North'),

        ('John & 5th', 'Daniel & 5th', 'S. 5th St.', 150, 'South', 'North'),
        ('Daniel & 5th', 'Chalmers & 5th', 'S. 5th St.', 150, 'South', 'North'),
        ('Chalmers & 5th', 'Armory & 5th', 'S. 5th St.', 150, 'South', 'North'),

        ('Armory & 6th', 'Gregory & 6th', 'S. 6th St.', 150, 'South', 'North'),

        ('Chalmers & Wright', 'Daniel & Wright', 'S. Wright St.', 150, 'North', 'South'),  # Entry to English Building
        ('Chalmers & Wright', 'to English Building on Wright', 'S. Wright St.', 100, 'North', 'South'),
        ('to English Building on Wright', 'Daniel & Wright', 'S. Wright St.', 50, 'North', 'South'),

        ('Daniel & Wright', 'John & Wright', 'S. Wright St.', 150, 'North', 'South'),
        # Entry to Bookstore and HAB on Wright
        ('Daniel & Wright', 'to Illini Union BookStore on Wright', 'S. Wright St.', 20, 'North', 'South'),
        ('to Illini Union BookStore on Wright', 'John & Wright', 'S. Wright St.', 130, 'North', 'South'),
        ('Daniel & Wright', 'to Henry Administration Building on Wright', 'S. Wright St.', 50, 'North', 'South'),
        ('to Henry Administration Building on Wright', 'John & Wright', 'S. Wright St.', 150, 'North', 'South'),
        ('to Illini Union BookStore on Wright', 'to Henry Administration Building on Wright', 'S. Wright St.', 30,
         'North', 'South'),

        ('John & Wright', 'Green & Wright', 'S. Wright St.', 150, 'North', 'South'),  # Entry to Altgeld Hall on Wright
        ('John & Wright', 'to Altgeld Hall on Wright', 'S. Wright St.', 30, 'North', 'South'),
        ('to Altgeld Hall on Wright', 'Green & Wright', 'S. Wright St.', 120, 'North', 'South'),

        ('Nevada & Mathews', 'to Smith Memorial Hall (Music) on Mathews', 'S. Mathews Ave.', 75, 'South', 'North'),
        # Entry to SMH

        ('Green & Goodwin', 'Oregon & Goodwin', 'S. Goodwin Ave.', 450, 'South', 'North'),  # Entry to Roger Adams Lab
        ('Green & Goodwin', 'to Roger Adams Lab on Goodwin', 'S. Goodwin Ave.', 320, 'South', 'North'),
        ('to Roger Adams Lab on Goodwin', 'Oregon & Goodwin', 'S. Goodwin Ave.', 130, 'South', 'North'),

        ('Oregon & Goodwin', 'Nevada & Goodwin', 'S. Goodwin Ave.', 150, 'South', 'North'),

        ('Nevada & Goodwin', 'Gregory & Goodwin', 'S. Goodwin Ave.', 200, 'South', 'North'),  # Entry to IGB
        ('Nevada & Goodwin', 'to Institute For Genomic Biology on Goodwin', 'S. Goodwin Ave.', 150, 'South', 'North'),
        ('to Institute For Genomic Biology on Goodwin', 'Gregory & Goodwin', 'S. Goodwin Ave.', 50, 'South', 'North'),

        # Since Intersections coincide with Entry Edges, the distance is equal to 0
        ('Armory & 5th', 'to Armory on Armory', 'S. 5th St.', 0, 'South', 'North'),  # Entry to Armory on Armory
        ('Armory & Wright', 'to Main Library on Armory', 'S. Wright St.', 0, 'South', 'North'),
        # Entry to Main Library on Armory
        ('Armory & Wright', 'to Gregory Hall on Wright', 'E. Armory Ave.', 0, 'East', 'West'),
        # Entry to Gregory Hall on Wright
        ('Gregory & Goodwin', 'to Edward R. Madigan Lab on Gregory', 'W. Goodwin Ave.', 0, 'South', 'North')
        # Entry to Edward Lab from North
    ]

    MainQuadPaths = [
        ('to Illini Union on Main Quad', 'Main Quad', 'Main Quad', 180),
        ('to Henry Administration Building on Main Quad', 'Main Quad', 'Main Quad', 105),
        ('to English Building on Main Quad', 'Main Quad', 'Main Quad', 55),
        ('to Lincoln Hall on Main Quad', 'Main Quad', 'Main Quad', 105),
        ('to Davenport Hall on Main Quad', 'Main Quad', 'Main Quad', 90),
        ('to Foreign Language Building on Main Quad', 'Main Quad', 'Main Quad', 140)
    ]

    EntryPaths = [  # undirected path - name of the entry to building, mail code of the building, distance
        ('to School of Information Sciences on Daniel', 493, 15),
        ('to UI Ice Arena on Armory', 525, 10),
        ('to Armory on Armory', 528, 40),
        ('to Armory on Gregory', 528, 40),
        ('to Illini Union BookStore on Daniel', 312, 5),
        ('to Illini Union BookStore on Wright', 312, 5),
        ('to Altgeld Hall on Wright', 382, 15),
        ('to Altgeld Hall on Green', 382, 100),
        ('to Illini Union on Green', 384, 70),
        ('to Henry Administration Building on Wright', 368, 20),
        ('to English Building on Wright', 718, 20),
        ('to Lincoln Hall on Wright', 456, 20),
        ('to Gregory Hall on Wright', 462, 20),
        ('to Main Library on Armory', 522, 15),
        ('to Main Library on Gregory', 522, 10),
        ('to Davenport Hall on Mathews', 151, 20),
        ('to Foreign Language Building on Mathews', 164, 15),
        ('to Smith Memorial Hall (Music) on Mathews', 56, 25),
        ('to Institute For Genomic Biology on Goodwin', 195, 35),
        ('to Illini Union on Main Quad', 384, 0),
        ('to Henry Administration Building on Main Quad', 368, 0),
        ('to English Building on Main Quad', 718, 0),
        ('to Lincoln Hall on Main Quad', 456, 0),
        ('to Davenport Hall on Main Quad', 151, 0),
        ('to Foreign Language Building on Main Quad', 164, 0),
        ('to Medical Sciences Building on Mathews', 714, 10),
        ('to Roger Adams Lab on Goodwin', 712, 15),
        ('to Native American House on Nevada', 139, 10),
        ('to Animal Sciences Lab on Gregory', 630, 10),
        ('to Edward R. Madigan Lab on Gregory', 51, 25)
    ]

    def __init__(self):
        self.G = nx.DiGraph()  # directed graph
        self.Buildings.sort()
        self.add_buildings(self.Buildings)
        self.add_intersections(self.Intersections)
        self.add_entries(self.Entries)

        self.add_diEdges(self.DiEdges)
        self.add_undiEdges(self.UndiEdges)
        self.add_entryPaths(self.EntryPaths)
        self.add_MQPaths(self.MainQuadPaths)

    def add_building(self, Name: str, Address: str, MailCode: int):  # add a building as a node to the graph
        # use mail code as key
        self.G.add_node(MailCode, name=Name, addr=Address, flag=0)  # flag=0 means this node is a building

    def add_buildings(self, L: list):  # add a list of buildings
        for x in L:
            self.add_building(x[0], x[1], x[2])

    def add_intersection(self, Name: str):  # add a intersection as a node to the graph
        self.G.add_node(Name, flag=1)  # flag=1 means this node is an intersection

    def add_intersections(self, L: list):  # add a list of intersections
        for x in L:
            self.add_intersection(x)

    def add_entry(self, Name: str):  # add an entry as a node to the graph
        self.G.add_node(Name, flag=2)  # flag=2 means this node is an entry to a building

    def add_entries(self, L: list):  # add a list of entries
        for x in L:
            self.add_entry(x)

    def add_diEdge(self, From: str, To: str, Name: str, Distance: int,
                   Direction: str):  # add directed edge to the graph
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

    def add_MQPath(self, From: str, To: str, Name: str, Distance: int):  # add path in the main quad
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
        print('\033[1m' + str("NAME").ljust(40) + '\tMAIL CODE' + '\033[0m')  # bold this title
        for x in tmp:
            print(str(x[1]['name']).ljust(40) + '\t', str(x[0]).rjust(8))

    def cal_path(self, From: int, To: int):  # calculate the shortest path
        Start = self.G.node[From]['name']
        End = self.G.node[To]['name']
        try:
            p = nx.dijkstra_path(self.G, From, To, 'dis')  # find shortest path depending on 'dis' attribute
        except nx.exception.NetworkXNoPath:
            print("There is no path from", Start, "to", End)
        else:
            print('\033[1m' + 'Travel from ' + Start + ' to ' + End + ':' + '\033[0m')
            direction = ''
            intoBldflag = 0  # flag to record whether it is in the building
            for i in range(1, len(p) - 2):
                try:
                    if direction != self.G[p[i]][p[i + 1]]['dir']:
                        if i == 1:
                            print("Starting on ", end="")
                        else:
                            print("At ", end="")
                        print(self.G[p[i]][p[i + 1]]['name'], end="")
                        if self.G[p[i]][p[i + 1]]['dir'] == 'NA':
                            print(" go through the path on the lawn")
                        else:
                            print(" turn " + self.G[p[i]][p[i + 1]]['dir'])
                        direction = self.G[p[i]][p[i + 1]]['dir']
                except KeyError:
                    if intoBldflag == 0:
                        print("Go through the", self.G.node[p[i + 1]]['name'])
                        intoBldflag += 1
                    elif intoBldflag == 1:
                        intoBldflag = 0
            print("Proceed until you arrive at " + End)


if __name__ == "__main__":
    M = Map()
    M.print_buildings()

    M.cal_path(493, 384)
    M.cal_path(522, 51)
    M.cal_path(312, 51)
