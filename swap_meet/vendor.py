from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        if inventory is not None:
            self.inventory = inventory
        else: 
            self.inventory = []

    def add(self,item):
        inventory = self.get_inventory()
        inventory.append(item)
        return item
    
    def remove(self,item):
        inventory = self.get_inventory()
        if item in inventory:
            inventory.remove(item)
            return item
        else: 
            return False
    
    def get_by_id(self,item_id):
        for item in self.get_inventory(): 
            if item.id == item_id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item is None or their_item is None:
            return False
        my_removed_item = self.remove(my_item)
        their_removed_item = other_vendor.remove(their_item)
        if my_removed_item is not False and their_removed_item is not False: 
            self.add(their_item)
            other_vendor.add(my_item)
            return True
        else: 
            if my_removed_item is not False:
                self.add(my_item)
            if their_removed_item is not False: 
                other_vendor.add(their_item)
            return False
        
    def swap_first_item(self, other_vendor):
        my_inventory = self.get_inventory()
        their_inventory = other_vendor.get_inventory()
        if self.check_lists_valid(my_inventory, their_inventory) == True:
            my_first_item = self.get_first_item(my_inventory)
            their_first_item = self.get_first_item(their_inventory)
            self.swap_items(other_vendor, my_first_item, their_first_item)
            return True
        else: 
            return False
    
    def get_by_category(self, category):
        items_in_category = []
        for item in self.get_inventory():  
            if item.get_category() == category: 
                items_in_category.append(item)
        return items_in_category

    def get_best_by_category(self, category):
        best_item = None
        items_in_category = self.get_by_category(category)
        self.get_best_item_by_keyword(items_in_category, condition)
        # for item in items_in_category:
        #     if best_item == None: 
        #         best_item = item
        #     elif best_item.condition < item.condition:
        #         best_item = item
        # return best_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_item_swap = self.get_best_by_category(their_priority)
        their_item_swap = other_vendor.get_best_by_category(my_priority)
        return self.swap_items(other_vendor, my_item_swap, their_item_swap)
        

        

##### Helper functions ######

    def get_inventory(self):
        return self.inventory
    
    def list_not_empty(self, list_input):
        if not list_input:
            return False
        else:
            return True
    def check_lists_valid(self, list_1, list_2):
        result_1 = self.list_not_empty(list_1)
        result_2 = self.list_not_empty(list_2)
        if result_1 is True and result_2 is True: 
            return True
        else: 
            return False

    def get_first_item(self, item_list):
        print(self, item_list)
        return item_list[0]
    

    def get_max_item(self, item_list, key_arg):
        return item_list, lambda item: item[key_arg]
    
    def get_best_item_by_keyword(self, item_list, item_keyword):
        best_item = None
        for item in item_list:
            if best_item == None: 
                best_item = item
            elif best_item.item_keyword < item.item_keyword:
                best_item = item
        return best_item