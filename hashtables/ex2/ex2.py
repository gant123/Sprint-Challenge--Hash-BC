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

    for t in tickets:
        hash_table_insert(hashtable, t.source, t.destination)

    route[0] = hash_table_retrieve(hashtable, 'NONE')
    current_index = 1

    for t in range(length):
        if hash_table_retrieve(hashtable, route[current_index - 1]) != 'NONE':
            next_location = hash_table_retrieve(
                hashtable, route[current_index - 1])

            route[current_index] = next_location
            current_index += 1
        else:
            route[length - 1] = route[current_index - 1]
    return route[:length - 1]
