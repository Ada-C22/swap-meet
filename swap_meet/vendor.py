from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory


    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None
    

    def swap_items(self, other_vendor, my_item, their_item):
        """
        If this Vendor's inventory contain my_item and 
        the friend's inventory contain their_item. 
        The method returns True,
        else the method returns False.
        """
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.inventory.remove(my_item) 
            other_vendor.inventory.append(my_item)
            # if their_item in other_vendor.inventory:
            other_vendor.remove(their_item) 
            self.inventory.append(their_item)
            return True
        else: 
            return False
            
    def swap_first_item(self, other_vendor):
        """
        Function swaps my first item with their first item.
        
        Input: other vendor

        Output: Returns either True or False. 
        - Returns False if my inventory or their inventory is empty. 
        - Otherwise, returns True.        
        """

        if not self.inventory or not other_vendor.inventory:
            return False
        
        first_item_in_my_inventory = self.inventory[0]
        first_item_in_vendor_inventory = other_vendor.inventory[0]
        

        self.inventory[0] = first_item_in_vendor_inventory
        other_vendor.inventory[0] = first_item_in_my_inventory
        
        return True


    def get_by_category(self, category):
        """
        Returns a list of items aligned to the same category. 

        Input: a string, representing a category.

        Output: returns a inventory list of items with the same category.
        """

        item_list_by_category = []

        for item in self.inventory:
            if item.get_category() == category:
                item_list_by_category.append(item)

        return item_list_by_category

    
    def get_best_by_category(self, category):
        """
        Finds item with the best condition in a certain category 

        Input: a string, representing a category

        Output: returns single item which has the highest condition and same category
        """

        items = self.get_by_category(category)

        if not items:
            return None
        
        best_item = items[0]
        for item in items:
            if item.condition > best_item.condition:
                best_item = item

        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        """
        Swaps the best item of a certain category.

        Input: other_vendor, my_priority (aka my category I want to receive), their_priority
        (aka their category they want to receive).

        Output: returns True if both can swap best item, returns false if vendor 
        or self doesn't have a matching item to swap.

        """
        best_item = self.get_best_by_category(their_priority)

        their_best_item = other_vendor.get_best_by_category(my_priority)

        if best_item and their_best_item:
            self.swap_items(other_vendor, best_item, their_best_item)
            return True
        return False
    