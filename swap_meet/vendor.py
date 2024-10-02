# testing comment
class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    # def __init__(self, inventory=[]):
    #     self.inventory = inventory

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
        
        # swap_item = Vendor.swap_items(self, other_vendor, first_item_in_my_inventory, first_item_in_vendor_inventory)
        # print(self.inventory)
        # print(other_vendor.inventory)

        self.inventory[0] = first_item_in_vendor_inventory
        other_vendor.inventory[0] = first_item_in_my_inventory
        
        return True


# mine = Vendor(inventory=["item_x", "item_y", "item_z"])
# fatimah = Vendor(inventory=["item_a", "item_b", "item_c"])

# print(mine.swap_first_item(fatimah))
