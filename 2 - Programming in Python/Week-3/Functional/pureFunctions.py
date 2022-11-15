# no effect beyond its own scope


my_list = [1,2,3]

""" 
def add_to_list(item): # non pure function
    return my_list.append(item)
add_to_list(4)
"""

def add_to_list(lst, item): # pure function
    nl = lst.copy()
    nl.append(item)
    return nl
new_list = add_to_list(my_list, 4) 
print(my_list)
print(new_list)