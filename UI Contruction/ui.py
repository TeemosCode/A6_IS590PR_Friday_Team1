import MapInfo as mp
import Main_ as M
# ======MapInfo with a class======
# map = mp.MapInfo()
# print(map.Buildings)

# ======MapInfo without a class ======
# print(mp.Buildings)

navi = M.Map() # navigator that contains our Graph object, 'G'.

MI = mp.MapInfo() # MI: for Map Info. The Edges and Verix of the map to be added to the navi graph
print(MI.Buildings[14][2])
# print(navi)

##########  intialize our map graph ######
navi.add_buildings(MI.Buildings) # add all building nodes
navi.add_intersections(MI.Intersections) # add all intersections
navi.add_entries(MI.Entries) # add all entries
navi.add_diEdges(MI.DiEdges) # Add all directed edges
navi.add_undiEdges(MI.UndiEdges) # Add all undirected edges
navi.add_entryPaths(MI.EntryPaths) # Add all entry paths

# print(navi.G.edges)
# print(navi.G.adj)


# The choice for connecting userinput to corresponding data for calculation of smallest path
choice_mail_building = { choicenum : (buildingInfo[0], buildingInfo[2]) for choicenum, buildingInfo in zip( range(1, len(MI.Buildings) + 1 ) , MI.Buildings)}
# print(choice_mail_building)
print(choice_mail_building)

def menu():
	print("""
		 =========================== Choice : (Buildings, Address, Mailcode) ============================
        ('School of Information Sciences', '501 E. Daniel St.', 493),
        ('Illini Union BookStore', '807 S. Wright St.', 312),
        ('Altgeld Hall', '1409 W. Green St.', 382),
        ('Illini Union', '1401 W. Green St.', 384),
        ('Henry Administration Building', '506 S. Wright St.', 339),
        ('English Building', '608 S. Wright St.', 718),
        ('Lincoln Hall', '702 S. Wright St.', 456),
        ('Gregory Hall', '810 S. Wright St.', 462),
        ('Main Library', '1408 W. Gregory Dr.', 522),
        ('Institute For Genomic Biology', '1206 W. Gregory Dr.', 195),
        ('Smith Memorial Hall (Music)', '805 S. Matthews Ave.', 56),
        ('Foreign Languages Building', '707 S. Matthews Ave.', 166),
        ('Davenport Hall', '607 S. Matthews Ave.', 148),
        ('UI Ice Arena', '406 E. Armory Ave.', 525),
        ('Armory', '505 E. Armory Ave.', 528)
    ]
		 """)



