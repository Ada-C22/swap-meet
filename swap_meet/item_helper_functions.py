def get_highest_item(list_items, key):
        if not list_items:
            return False
        
        highest = list_items[0]
        for item in list_items:
            if key(item) > key(highest):
                highest = item
        return highest


def get_newest_item(list_items, key):
    newest = list_items[0]
    for item in list_items:
        if key(item) < key(newest):
            newest = item
    return newest