def find_length_of_values(data: dict) -> int:
    """
    Return the sum of the length of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of the length of all values in the dictionary.
    """
    s=""
    for i in data:
        s+=data[i]
    return len(s)
print(find_length_of_values( data = {
    'a': 'abc',
    'b': 'def', 
    'c': 'ghi'
  }))
print(find_length_of_values(data = {
    1 : "Khiva", 
    2 : "Namangan", 
    3 : "Samarkand", 
    4 : "Tashkent"
  }))