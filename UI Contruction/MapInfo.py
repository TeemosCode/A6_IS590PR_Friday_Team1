class MapInfo:
    Buildings = [  # information of buildings - name, address, mail code
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
        'Green & Goodvin',
        'Oregon & Mathews',
        'Oregon & Goodwin',
        'Nevada & Mathews',
        'Nevada & Goodwin',
        'Gregory & Goodwin'
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
        'to Foreign Languages Building on Mathews',
        'to Smith Memorial Hall (Music) on Mathews',
        'to Institute For Genomic Biology on Goodwin'
    ]

    DiEdges = [  # directed edges - From, To, Name, Distance, Direction
        ('John & 4th', 'John & 5th', 'E. John St.', 150, 'East'),
        ('John & 5th', 'John & 6th', 'E. John St.', 150, 'East'),
        ('John & Wright', 'John & 6th', 'E. John St.', 150, 'West'),
        ('Daniel & 4th', 'Daniel & 5th', 'E. Daniel St.', 150, 'East'),

        ('Daniel & 5th', 'Daniel & 6th', 'E. Daniel St.', 150, 'East'),  # Entry to iSchool
        ('Daniel & 5th', 'to School of Information Sciences on Daniel', 'E. Daniel St.', 50, 'East'),
        ('to School of Information Sciences on Daniel', 'Daniel & 6th', 'E. Daniel St.', 100, 'East'),

        ('Daniel & 6th', 'Daniel & Wright', 'E. Daniel St.', 150, 'East'),  # Entry to BookStore on Daniel
        ('Daniel & 6th', 'to Illini Union BookStore on Daniel', 'E. Daniel St.', 100, 'East'),
        ('to Illini Union BookStore on Daniel', 'Daniel & Wright', 'E. Daniel St.', 50, 'East'),

        ('Chalmers & 5th', 'Chalmers & 4th', 'E. Chalmers St.', 150, 'West'),
        ('Chalmers & 6th', 'Chalmers & 5th', 'E. Chalmers St.', 150, 'West'),
        ('Chalmers & Wright', 'Chalmers & 6th', 'E. Chalmers St.', 150, 'West'),

        ('Armory & 4th', 'Armory & 5th', 'E. Armory Ave.', 150, 'East'),  # Entry to Ice Arena
        ('Armory & 4th', 'to UI Ice Arena on Armory', 'E. Armory Ave.', 100, 'East'),
        ('to UI Ice Arena on Armory', 'Armory & 5th', 'E. Armory Ave.', 50, 'East'),

        ('Armory & 5th', 'Armory & 6th', 'E. Armory Ave.', 150, 'East'),
        ('Armory & 6th', 'Armory & Wright', 'E. Armory St.', 150, 'East'),
        ('Oregon & Goodwin', 'Oregon & Mathews', 'W. Oregon St.', 150, 'West'),
        ('Nevada & Mathews', 'Nevada & Goodwin', 'W. Nevada St.', 150, 'East'),

        ('John & 6th', 'Daniel & 6th', 'S. 6th St.', 150, 'South'),
        ('Daniel & 6th', 'Chalmers & 6th', 'S. 6th St.', 150, 'South'),
        ('Chalmers & 6th', 'Armory & 6th', 'S. 6th St.', 150, 'South'),
        ('Armory & 6th', 'Gregory & 6th', 'S. 6th St.', 150, 'South'),

        ('Armory & Wright', 'Chalmers & Wright', 'S. Wright St.', 150, 'North'),  # Entry to Lincoln Hall
        ('Armory & Wright', 'to Lincoln Hall on Wright', 'S. Wright St.', 120, 'North'),
        ('to Lincoln Hall on Wright', 'Chalmers & Wright', 'S. Wright St.', 30, 'North'),

        ('Chalmers & Wright', 'Daniel & Wright', 'S. Wright St.', 150, 'North'),  # Entry to English Building
        ('Chalmers & Wright', 'to English Building on Wright', 'S. Wright St.', 100, 'North'),
        ('to English Building on Wright', 'Daniel & Wright', 'S. Wright St.', 50, 'North'),

        ('Daniel & Wright', 'John & Wright', 'S. Wright St.', 150, 'North'),  # Entry to Bookstore and HAB on Wright
        ('Daniel & Wright', 'to Illini Union BookStore on Wright', 'S. Wright St.', 20, 'North'),
        ('to Illini Union BookStore on Wright', 'John & Wright', 'S. Wright St.', 130, 'North'),
        ('Daniel & Wright', 'to Henry Administration Building on Wright', 'S. Wright St.', 50, 'North'),
        ('to Henry Administration Building on Wright', 'John & Wright', 'S. Wright St.', 150, 'North'),
        ('to Illini Union BookStore on Wright', 'to Henry Administration Building on Wright', 'S. Wright St.', 30, 'North'),

        ('John & Wright', 'Green & Wright', 'S. Wright St.', 150, 'North'),  # Entry to Altgeld Hall on Wright
        ('John & Wright', 'to Altgeld Hall on Wright', 'S. Wright St.', 30, 'North'),
        ('to Altgeld Hall on Wright', 'Green & Wright', 'S. Wright St.', 120, 'North'),

        ('Green & Mathews', 'Oregon & Mathews', 'S. Mathews Ave.', 450, 'South'),  # Entry to Davenport Hall
        ('Green & Mathews', 'to Davenport Hall on Mathews', 'S. Mathews Ave.', 420, 'South'),
        ('to Davenport Hall on Mathews', 'Oregon & Mathews', 'S. Mathews Ave.', 30, 'South'),

        ('Oregon & Mathews', 'Nevada & Mathews', 'S. Mathews Ave.', 150, 'South'),  # Entry to Foreign Languages Blg
        ('Oregon & Mathews', 'to Foreign Languages Building on Mathews', 'S. Mathews Ave.', 120, 'South'),
        ('to Foreign Languages Building on Mathews', 'Nevada & Mathews', 'S. Mathews Ave.', 30, 'South'),

        ('Nevada & Mathews', 'to Smith Memorial Hall (Music) on Mathews', 'S. Mathews Ave.', 75, 'South')  # Entry to SMH

    ]

    UndiEdges = [  # undirected edges - From, To, Name, Distance, Direction1(From->To), Direction2(To->From)
        ('Gregory & 4th', 'Gregory & 6th', 'E. Gregory Dr.', 300, 'East', 'West'),  # Entry to Armory on Gregory
        ('Gregory & 4th', 'to Armory on Gregory', 'E. Gregory Dr.', 150, 'East', 'West'),
        ('to Armory on Gregory', 'Gregory & 6th', 'E. Gregory Dr.', 150, 'East', 'West'),

        ('Gregory & 6th', 'Gregory & Goodwin', 'W. Gregory Dr.', 600, 'East', 'West'),  # Entry to Library on Gregory
        ('Gregory & 6th', 'to Main Library on Gregory', 'W. Gregory Dr.', 150, 'East', 'West'),
        ('to Main Library on Gregory', 'Gregory & Goodwin', 'W. Gregory Dr.', 450, 'East', 'West'),

        ('Green & Wright', 'Green & Mathews', 'W. Green Dr.', 300, 'East', 'West'),  # Entry to Altgeld Hall and Illini Union on Green
        ('Green & Wright', 'to Altgeld Hall on Green', 'W. Green Dr.', 30, 'East', 'West'),
        ('to Altgeld Hall on Green', 'Green & Mathews', 'W. Green Dr.', 270, 'East', 'West'),
        ('Green & Wright', 'to Illini Union on Green', 'W. Green Dr.', 140, 'East', 'West'),
        ('to Illini Union on Green', 'Green & Mathews', 'W. Green Dr.', 160, 'East', 'West'),
        ('to Altgeld Hall on Green', 'to Illini Union on Green', 'W. Green Dr.', 110, 'East', 'West'),

        ('Green & Mathews', 'Green & Goodwin', 'W. Green Dr.', 150, 'East', 'West'),

        ('John & 4th', 'Daniel & 4th', 'S. 4th St.', 150, 'North', 'South'),
        ('Daniel & 4th', 'Chalmers & 4th', 'S. 4th St.', 150, 'North', 'South'),
        ('Chalmers & 4th', 'Armory & 4th', 'S. 4th St.', 150, 'North', 'South'),
        ('Armory & 4th', 'Gregory & 4th', 'S. 4th St.', 150, 'North', 'South'),

        ('John & 5th', 'Daniel & 5th', 'S. 5th St.', 150, 'North', 'South'),
        ('Daniel & 5th', 'Chalmers & 5th', 'S. 5th St.', 150, 'North', 'South'),
        ('Chalmers & 5th', 'Armory & 5th', 'S. 5th St.', 150, 'North', 'South'),

        ('Green & Goodwin', 'Oregon & Goodwin', 'S. Goodwin Ave.', 450, 'North', 'South'),
        ('Oregon & Goodwin', 'Nevada & Goodwin', 'S. Goodwin Ave.', 150, 'North', 'South'),

        ('Nevada & Goodwin', 'Gregory & Goodwin', 'S. Goodwin Ave.', 200, 'North', 'South'),  # Entry to IGB
        ('Nevada & Goodwin', 'to Institute For Genomic Biology on Goodwin', 'S. Goodwin Ave.', 150, 'North', 'South'),
        ('to Institute For Genomic Biology on Goodwin', 'Gregory & Goodwin', 'S. Goodwin Ave.', 50, 'North', 'South')

    ]

    EntryPaths = [  # undirected path - name of the entry to building, mail code of the building, distance
        ('to English Building on Wright', 718, 50),
        ('to Lincoln Hall on Wright', 456, 50)
    ]

    # all items for checking
    items = [Buildings, Intersections, Entries, DiEdges, UndiEdges, EntryPaths]
# map = MapInfo()
# print(map.Buildings)



#### Without a Class ####
# Buildings = [  # information of buildings - name, address, mail code
#     ('School of Information Sciences', '501 E. Daniel St.', 493),
#     ('Illini Union BookStore', '807 S. Wright St.', 312),
#     ('Altgeld Hall', '1409 W. Green St.', 382),
#     ('Illini Union', '1401 W. Green St.', 384),
#     ('Henry Administration Building', '506 S. Wright St.', 339),
#     ('English Building', '608 S. Wright St.', 718),
#     ('Lincoln Hall', '702 S. Wright St.', 456),
#     ('Gregory Hall', '810 S. Wright St.', 462),
#     ('Main Library', '1408 W. Gregory Dr.', 522),
#     ('Institute For Genomic Biology', '1206 W. Gregory Dr.', 195),
#     ('Smith Memorial Hall (Music)', '805 S. Matthews Ave.', 56),
#     ('Foreign Languages Building', '707 S. Matthews Ave.', 166),
#     ('Davenport Hall', '607 S. Matthews Ave.', 148),
#     ('UI Ice Arena', '406 E. Armory Ave.', 525),
#     ('Armory', '505 E. Armory Ave.', 528)
# ]

# Intersections = [  # names of the intersection
#     'John & 4th',
#     'John & 5th',
#     'John & 6th',
#     'John & Wright',
#     'Daniel & 4th',
#     'Daniel & 5th',
#     'Daniel & 6th',
#     'Daniel & Wright',
#     'Chalmers & 4th',
#     'Chalmers & 5th',
#     'Chalmers & 6th',
#     'Chalmers & Wright',
#     'Armory & 4th',
#     'Armory & 5th',
#     'Armory & 6th',
#     'Armory & Wright',
#     'Gregory & 4th',
#     'Gregory & 6th',
#     'Green & Wright',
#     'Green & Mathews',
#     'Green & Goodvin',
#     'Oregon & Mathews',
#     'Oregon & Goodwin',
#     'Nevada & Mathews',
#     'Nevada & Goodwin',
#     'Gregory & Goodwin'
#     # 'Gregory & Dorner' Do not need this intersection
# ]

# Entries = [  # names of the entries
#     'to School of Information Sciences on Daniel',
#     'to UI Ice Arena on Armory',
#     'to Armory on Armory',
#     'to Armory on Gregory',
#     'to Illini Union BookStore on Daniel',
#     'to Illini Union BookStore on Wright',
#     'to Altgeld Hall on Wright',
#     'to Altgeld Hall on Green',
#     'to Illini Union on Green',
#     'to Henry Administration Building on Wright',
#     'to English Building on Wright',
#     'to Lincoln Hall on Wright',
#     'to Gregory Hall on Wright',
#     'to Main Library on Armory',
#     'to Main Library on Gregory',
#     'to Davenport Hall on Mathews',
#     'to Foreign Languages Building on Mathews',
#     'to Smith Memorial Hall (Music) on Mathews',
#     'to Institute For Genomic Biology on Goodwin'
# ]

# DiEdges = [  # directed edges - From, To, Name, Distance, Direction
#     ('John & 4th', 'John & 5th', 'E. John St.', 150, 'East'),
#     ('John & 5th', 'John & 6th', 'E. John St.', 150, 'East'),
#     ('John & Wright', 'John & 6th', 'E. John St.', 150, 'West'),
#     ('Daniel & 4th', 'Daniel & 5th', 'E. Daniel St.', 150, 'East'),

#     ('Daniel & 5th', 'Daniel & 6th', 'E. Daniel St.', 150, 'East'),  # Entry to iSchool
#     ('Daniel & 5th', 'to School of Information Sciences on Daniel', 'E. Daniel St.', 50, 'East'),
#     ('to School of Information Sciences on Daniel', 'Daniel & 6th', 'E. Daniel St.', 100, 'East'),

#     ('Daniel & 6th', 'Daniel & Wright', 'E. Daniel St.', 150, 'East'),  # Entry to BookStore on Daniel
#     ('Daniel & 6th', 'to Illini Union BookStore on Daniel', 'E. Daniel St.', 100, 'East'),
#     ('to Illini Union BookStore on Daniel', 'Daniel & Wright', 'E. Daniel St.', 50, 'East'),

#     ('Chalmers & 5th', 'Chalmers & 4th', 'E. Chalmers St.', 150, 'West'),
#     ('Chalmers & 6th', 'Chalmers & 5th', 'E. Chalmers St.', 150, 'West'),
#     ('Chalmers & Wright', 'Chalmers & 6th', 'E. Chalmers St.', 150, 'West'),

#     ('Armory & 4th', 'Armory & 5th', 'E. Armory Ave.', 150, 'East'),  # Entry to Ice Arena
#     ('Armory & 4th', 'to UI Ice Arena on Armory', 'E. Armory Ave.', 100, 'East'),
#     ('to UI Ice Arena on Armory', 'Armory & 5th', 'E. Armory Ave.', 50, 'East'),

#     ('Armory & 5th', 'Armory & 6th', 'E. Armory Ave.', 150, 'East'),
#     ('Armory & 6th', 'Armory & Wright', 'E. Armory St.', 150, 'East'),
#     ('Oregon & Goodwin', 'Oregon & Mathews', 'W. Oregon St.', 150, 'West'),
#     ('Nevada & Mathews', 'Nevada & Goodwin', 'W. Nevada St.', 150, 'East'),

#     ('John & 6th', 'Daniel & 6th', 'S. 6th St.', 150, 'South'),
#     ('Daniel & 6th', 'Chalmers & 6th', 'S. 6th St.', 150, 'South'),
#     ('Chalmers & 6th', 'Armory & 6th', 'S. 6th St.', 150, 'South'),
#     ('Armory & 6th', 'Gregory & 6th', 'S. 6th St.', 150, 'South'),

#     ('Armory & Wright', 'Chalmers & Wright', 'S. Wright St.', 150, 'North'),  # Entry to Lincoln Hall
#     ('Armory & Wright', 'to Lincoln Hall on Wright', 'S. Wright St.', 120, 'North'),
#     ('to Lincoln Hall on Wright', 'Chalmers & Wright', 'S. Wright St.', 30, 'North'),

#     ('Chalmers & Wright', 'Daniel & Wright', 'S. Wright St.', 150, 'North'),  # Entry to English Building
#     ('Chalmers & Wright', 'to English Building on Wright', 'S. Wright St.', 100, 'North'),
#     ('to English Building on Wright', 'Daniel & Wright', 'S. Wright St.', 50, 'North'),

#     ('Daniel & Wright', 'John & Wright', 'S. Wright St.', 150, 'North'),  # Entry to Bookstore and HAB on Wright
#     ('Daniel & Wright', 'to Illini Union BookStore on Wright', 'S. Wright St.', 20, 'North'),
#     ('to Illini Union BookStore on Wright', 'John & Wright', 'S. Wright St.', 130, 'North'),
#     ('Daniel & Wright', 'to Henry Administration Building on Wright', 'S. Wright St.', 50, 'North'),
#     ('to Henry Administration Building on Wright', 'John & Wright', 'S. Wright St.', 150, 'North'),
#     ('to Illini Union BookStore on Wright', 'to Henry Administration Building on Wright', 'S. Wright St.', 30, 'North'),

#     ('John & Wright', 'Green & Wright', 'S. Wright St.', 150, 'North'),  # Entry to Altgeld Hall on Wright
#     ('John & Wright', 'to Altgeld Hall on Wright', 'S. Wright St.', 30, 'North'),
#     ('to Altgeld Hall on Wright', 'Green & Wright', 'S. Wright St.', 120, 'North'),

#     ('Green & Mathews', 'Oregon & Mathews', 'S. Mathews Ave.', 450, 'South'),  # Entry to Davenport Hall
#     ('Green & Mathews', 'to Davenport Hall on Mathews', 'S. Mathews Ave.', 420, 'South'),
#     ('to Davenport Hall on Mathews', 'Oregon & Mathews', 'S. Mathews Ave.', 30, 'South'),

#     ('Oregon & Mathews', 'Nevada & Mathews', 'S. Mathews Ave.', 150, 'South'),  # Entry to Foreign Languages Blg
#     ('Oregon & Mathews', 'to Foreign Languages Building on Mathews', 'S. Mathews Ave.', 120, 'South'),
#     ('to Foreign Languages Building on Mathews', 'Nevada & Mathews', 'S. Mathews Ave.', 30, 'South'),

#     ('Nevada & Mathews', 'to Smith Memorial Hall (Music) on Mathews', 'S. Mathews Ave.', 75, 'South')  # Entry to SMH

# ]

# UndiEdges = [  # undirected edges - From, To, Name, Distance, Direction1(From->To), Direction2(To->From)
#     ('Gregory & 4th', 'Gregory & 6th', 'E. Gregory Dr.', 300, 'East', 'West'),  # Entry to Armory on Gregory
#     ('Gregory & 4th', 'to Armory on Gregory', 'E. Gregory Dr.', 150, 'East', 'West'),
#     ('to Armory on Gregory', 'Gregory & 6th', 'E. Gregory Dr.', 150, 'East', 'West'),

#     ('Gregory & 6th', 'Gregory & Goodwin', 'W. Gregory Dr.', 600, 'East', 'West'),  # Entry to Library on Gregory
#     ('Gregory & 6th', 'to Main Library on Gregory', 'W. Gregory Dr.', 150, 'East', 'West'),
#     ('to Main Library on Gregory', 'Gregory & Goodwin', 'W. Gregory Dr.', 450, 'East', 'West'),

#     ('Green & Wright', 'Green & Mathews', 'W. Green Dr.', 300, 'East', 'West'),  # Entry to Altgeld Hall and Illini Union on Green
#     ('Green & Wright', 'to Altgeld Hall on Green', 'W. Green Dr.', 30, 'East', 'West'),
#     ('to Altgeld Hall on Green', 'Green & Mathews', 'W. Green Dr.', 270, 'East', 'West'),
#     ('Green & Wright', 'to Illini Union on Green', 'W. Green Dr.', 140, 'East', 'West'),
#     ('to Illini Union on Green', 'Green & Mathews', 'W. Green Dr.', 160, 'East', 'West'),
#     ('to Altgeld Hall on Green', 'to Illini Union on Green', 'W. Green Dr.', 110, 'East', 'West'),

#     ('Green & Mathews', 'Green & Goodwin', 'W. Green Dr.', 150, 'East', 'West'),

#     ('John & 4th', 'Daniel & 4th', 'S. 4th St.', 150, 'North', 'South'),
#     ('Daniel & 4th', 'Chalmers & 4th', 'S. 4th St.', 150, 'North', 'South'),
#     ('Chalmers & 4th', 'Armory & 4th', 'S. 4th St.', 150, 'North', 'South'),
#     ('Armory & 4th', 'Gregory & 4th', 'S. 4th St.', 150, 'North', 'South'),

#     ('John & 5th', 'Daniel & 5th', 'S. 5th St.', 150, 'North', 'South'),
#     ('Daniel & 5th', 'Chalmers & 5th', 'S. 5th St.', 150, 'North', 'South'),
#     ('Chalmers & 5th', 'Armory & 5th', 'S. 5th St.', 150, 'North', 'South'),

#     ('Green & Goodwin', 'Oregon & Goodwin', 'S. Goodwin Ave.', 450, 'North', 'South'),
#     ('Oregon & Goodwin', 'Nevada & Goodwin', 'S. Goodwin Ave.', 150, 'North', 'South'),

#     ('Nevada & Goodwin', 'Gregory & Goodwin', 'S. Goodwin Ave.', 200, 'North', 'South'),  # Entry to IGB
#     ('Nevada & Goodwin', 'to Institute For Genomic Biology on Goodwin', 'S. Goodwin Ave.', 150, 'North', 'South'),
#     ('to Institute For Genomic Biology on Goodwin', 'Gregory & Goodwin', 'S. Goodwin Ave.', 50, 'North', 'South')

# ]

# EntryPaths = [  # undirected path - name of the entry to building, mail code of the building, distance
#     ('to English Building on Wright', 718, 50),
#     ('to Lincoln Hall on Wright', 456, 50)
# ]