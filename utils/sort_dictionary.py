def sort_dictionary(dictionary):
    """Sorts a dictionary by value, returns a list of tuples"""
    return sorted(dictionary.items(), key=lambda x: x[1])