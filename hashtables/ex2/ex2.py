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

    # Insert each ticket into the hash table
    for individual_ticket in range(length):
        flying_from = tickets[individual_ticket].source
        flying_to = tickets[individual_ticket].destination
        hash_table_insert(hashtable, flying_from, flying_to)
    
    # Finds the ticket with its source as "None", since its the origin ticket
    route[0] = hash_table_retrieve(hashtable, "None")

    # Loop over the rest of the table
    for each_ticket in range(1, length):
        # Since we already have the origin ticket we can just subtract 1 from it to get the key of the next ticket
        # we then save that as the next ticket in the route
        route[each_ticket] = hash_table_retrieve(hashtable, route[each_ticket - 1])

    return route
