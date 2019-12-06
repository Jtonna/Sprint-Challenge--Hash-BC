#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    let key = source
    let value = destination

    for each individual ticket in range(len(tickets))
        insert the source and destination as the key & value
    
    find the key with None as the value as that is the source of the journey
        pass that value key:value pair to route[0]
    ^^
    ^ ---- Could be done in one line as a variable assignment
    
    for each item we look at in the loop of the hash table
        pass that value:key pair to route
        ^^
        ^ ---- also a one line variable assignment

    """

    

    return route
