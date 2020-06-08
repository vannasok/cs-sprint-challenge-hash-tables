#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


cache = {}


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route = []
    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    route.append(cache['NONE'])

    for index in range(length):
        if route[index] in cache:
            if cache[route[index]] == route[0]:
                continue
            route.append(cache[route[index]])

    return route
