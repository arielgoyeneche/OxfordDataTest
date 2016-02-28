import pandas as pd
import networkx as nx

source1 = pd.DataFrame({
                    'Names': ['Dan', 'Joe', 'Michael'],
                    'Surnames': ['Tim' ,'Nil', 'Pep'],
                    'CityID': [2 ,3, 2],
                    'PeopleID': [1,2,3],
                  })


tf1 = [
            {'field': 'Names',
             'function': lambda Names : Names
            },
            {'field': 'Surnames',
             'function': lambda Surnames : Surnames
            },
            {'field': 'PeopleID',
             'function': lambda PeopleID : PeopleID
            },
            {'field': 'CityID',
             'function': lambda CityID : CityID
            },
            {'field': 'Full_Name',
             'function': lambda Names, Surnames : Names + ' ' + Surnames
            },

]


source2 = pd.DataFrame({
                    'City': ['London', 'New York', 'Sydney'],
                    'ID': [1,2,3],
                  })


tf2 = [
            {'field': 'City',
             'function': lambda City : 'Dr: ' + City
            },
            {'field': 'CityID',
             'function': lambda ID : ID
            }
]


tf3 = [
            {'field': 'QName',
             'function': lambda Full_Name : 'Dr: ' + Full_Name
            }
]

Gr = nx.DiGraph()

Gr.add_node(1, data=source1)
Gr.add_node(2, data=source2)
Gr.add_node(3, match_keys=['CityID'], producer=True)

Gr.add_edge(1, 3, transformation = tf1)
Gr.add_edge(2, 3, transformation = tf2)


# train = [edge1, edge2]






# Select 2 columns
# -> print( s1[['Names','Surnames']])

# Selects the first 3 elements for the given columns
# -> print( s1.loc[:2,['IDs', 'Surnames']])
# Use numbers
# -> print( s1.iloc[:3, 2])
# Use numbers or names
# print( s1.ix[2:3,['IDs', 4]])

# Creates a new column
# -> s1['value'] = s1['IDs']
# -> print(s1)

#==========ok####