def remove_zeros_prepended_at_price(data):
    # input: pandas dataframe
    # example
    # 0161.7688908056352 -> 161.7688908056352
    # row 22, 33, 34
    '''
    Pandas automatically remove zeros prepended to the value when reading in the csv file
    '''
    return