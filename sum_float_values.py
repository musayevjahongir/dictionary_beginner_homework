def sum_float_values(data: dict) -> float:
    '''
    Return the sum of all float values in dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        float: The sum of all float values in the dictionary.
    '''
    s=0
    for i in data:
        if "." in str(data[i]):
            s+=data[i]
    return s
print(sum_float_values(data = {
    'a': 1, 
    'b' : 2.5, 
    'c': 3.0
  }))
print(sum_float_values(data = {
    1: 22.4, 
    2: 3.5, 
    4: 1, 
    6: 7.6, 
    5: 2, 
    7: 3
  }))