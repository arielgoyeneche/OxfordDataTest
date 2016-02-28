import pandas as pd

# Define a dataframe using pandas
s1 = pd.DataFrame({
                    'Names': ['Dan', 'Joe', 'Michael'],
                    'Surnames': ['Tim' ,'Nil', 'Pep'],
                    'IDs': [1,2,3],
                  })

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

step1 = {   'field': 'Surnames',
            'function': lambda Names, Surnames : Names + ' ' + Surnames
        }
step2 = {   'field': 'Surnames',
            'function': lambda Surnames : 'Dr:' + Surnames
        }

train = [step1, step2]


def apply_step(df, step):

    args = dict((ar, df[ar]) for ar in step['function'].__code__.co_varnames)
    df[step['field']] = step['function'](**args)
    return(df)



print(s1)
for s in train:
    s1 = apply_step(s1, s)
    print(s1)


#==========ok####

