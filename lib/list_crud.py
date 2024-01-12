def create_an_empty_list():
    return []

# This function should use the literal constructor to create a new list, just like we did above. This time, however, create a list that contains four elements. The four elements can be any elements of your choosing, as long as there are only four of them.
def create_a_list():
    return ["mans", "just", "here", "init"]

# This function takes in two arguments, a list and the element we want to add to it. Use the append() methodLinks to an external site. to add that element to the end of the new list.
def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

# This function takes in two arguments, a list and the element we want to add to it. Use the insert() methodLinks to an external site. to add that element to the start of that list.
def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l

#This function takes in one argument, the list on which we want to operate. Use the pop()Links to an external site. method to remove the last item from the list.
def remove_element_from_end_of_list(l):
    l.pop()
    return l

# This function takes in one argument, the list on which we want to operate. Use the del keywordLinks to an external site. to remove the first item from the list.
def remove_element_from_start_of_list(l):
    del(l[0])
    return l

# This function takes in one argument, the list from which we want to retrieve an element. Use [] notation to return the value stored at the first index of the list. Remember that lists are zero-indexed. This means that the first index number is 0 and it counts up from there. So, the first element of a list is stored at index 0.
def retrieve_first_element_from_list(l):
    return l[0]

# This function takes in two arguments, a list and the index number whose element we want to retrieve. Use the [], bracket notation, to return the element stored at that index number of the given list.
def retrieve_element_from_index(l, index):
    return l[index]

# This function takes in one argument, the list from which we want to retrieve an element. There are a number of ways to do this, but we recommend using the [] notation with the following hint:
# The last element of a list is considered to be stored at an index of -1.
def retrieve_last_element_from_list(l):
    return l[-1]
