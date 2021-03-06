import numpy as np


def create_field_above_100(data):
    '''
    input: pandas dataframe

    This functions creates a new field 'above_100' that depicts whether the price is
    above 100 or not.
    '''
    data['above_100'] = np.nan
    for index, row in data.iterrows():
        value = row['price']
        if value > 100:
            data.loc[index, 'above_100'] = True
        else:
            data.loc[index, 'above_100'] = False
    return data