def locate_card(cards, query):
    """
    Locate the position of the query in the cards list using a brute force approach.

    Args:
    cards (list): A list of integers representing the cards.
    query (int): The integer value to locate in the cards list.

    Returns:
    int: The index of the query in the cards list if found, otherwise -1.
    """
    # Create a variable "position" with an initial value of 0
    position = 0
    # Use a while loop to iterate through the cards list until the position is less than the length of the cards list 
    while position < len(cards):
        # Check if element at the current position is equal to the query
        if cards[position] == query:
            # Answer found! Return the current position and exit the loop.
            return position
        # Increment the position variable by 1
        position += 1
    # If we have reached the end of the list, return -1 to indicate that the query was not found.
    return -1