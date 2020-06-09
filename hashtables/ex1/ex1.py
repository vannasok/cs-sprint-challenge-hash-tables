def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    for index in range(length):
        need = limit - weights[index]
        if need in cache:
            subtract = cache[need]
            new_list = [index, subtract]
            new_list.sort(reverse=True)
            return new_list
        else:
            cache[weights[index]] = index

    return None
