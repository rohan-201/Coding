def pop_item(lst, index=-1):
    
    if not lst:
        raise IndexError("Cannot pop from empty list")
    return lst.pop(index)
