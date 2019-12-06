#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    loop over every item in weights (length number of times)
        insert each item into the hash table
    
    loop over every item in weights (length number of times)
        set a variable that holds -> subtract the limit from the current item we are looking at in this loop.
        set a variable that holds -> check the hash table for the key (which is the variable above) 

        if the weight is not None
            return the weight

    hashtable = ht
    key = weights[item]
    value = item
    """

    for item in range(len(weights)):
        hash_table_insert(ht, weights[item], item)
    
    for item in range(len(weights)):
        subtractifier = limit - weights[item] # weights[item] is the key
        checker = hash_table_retrieve(ht, subtractifier)

        if checker is not None:
            return (checker, item)
        
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
