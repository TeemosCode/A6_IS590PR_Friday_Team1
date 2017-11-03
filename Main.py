import networkx as nx


class Map():
    def __init__(self):
        self.G=nx.DiGraph() #directed

    def add_node(self, Name:str, Address:str, MailCode:int):
        # Name as the key - not good but ok in our small map because there is no duplication
        # If there were only buildings, we can use Mail Code. But there are other nodes..
        self.G.add_node(Name, addr=Address, mc=MailCode)

    def add_nodes(self,L:list):
        for x in L:
            self.add_node(x[0],x[1],x[2])
        #print(self.G.nodes())
        #print(nx.get_node_attributes(self.G,'addr'))

    def add_edge(self, Name:str, From:str, To:str, Distance:int, Direction:str):
        self.G.add_edge(From,To,name=Name,dis=Distance,dir=Direction) # small path doesn't have name..?

    def cal_path(self, From:str, To:str):
        print(nx.dijkstra_path(self.G, From, To,'dis')) # find shortest path depending on 'dis' attribute









def main():
    M=Map()
    # test
    # M.add_node('BuildA','addr Build A',111)
    # M.add_node('BuildB','addr Build B',222)
    # M.add_node('BuildC','addr Build C',333)
    # M.add_node('BuildD','addr Build D',444)
    #
    # M.add_edge('A2B','BuildA','BuildB',200,'North')
    # M.add_edge('B2C','BuildB','BuildC',200,'East')
    # M.add_edge('C2D','BuildC','BuildD',200,'South')
    # M.add_edge('D2A','BuildD','BuildA',200,'West')
    # M.add_edge('A2C','BuildA','BuildC',100,'Cross')
    #
    # M.cal_path('BuildA','BuildC')

    Nodes=[
        ('Foreign Languages Building','707 S. Matthews Ave.',164),
        ('Lincoln Hall','702 S. Wright St.',456)
    ]
    M.add_nodes(Nodes)



main()