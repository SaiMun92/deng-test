# Cases to take note:
# Mr, Ms, Miss, Mrs
# MD (Med doc), DDS(doctor of dental surgery), DVM (doctor of vet med)


def remove_salutation(data):
    '''
    input: pandas dataframe
    '''

    data['name'].replace(r'(^\w{2,4}\. ?)', r'', regex=True, inplace=True)


def remove_position(data):
    '''
    input: pandas dataframe
    '''
    data['name'].replace({
        'MD': '',
        'DDS': '',
        'DVM': '',
        'PhD': '',
    }, regex=True, inplace=True)


def remove_rows_with_missing_name(data):
    data.dropna(subset=['name'], inplace=True)
