import numpy as np

# Western names follow a format like so:
# "First Name " " Last Name

# Assumptions made
# Leave Jr., II, III in the Last Name


def name_splitter(data):
    # input: pandas dataframe
    # This functions splits the name column into first and last name

    data['first_name'] = np.nan
    data['last_name'] = np.nan
    for index, row in data.iterrows():
        name = row['name']
        name_tuple = name.partition(" ")
        first_name = name_tuple[0]
        last_name = name_tuple[2]
        data.loc[index, 'first_name'] = first_name
        data.loc[index, 'last_name'] = last_name

    return data