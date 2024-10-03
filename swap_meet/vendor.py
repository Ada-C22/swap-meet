class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory


    def add(self, item):
        self.inventory.append(item)
        return item


    def remove(self, item):
        if item not in self.inventory:
            return False
        elif item in self.inventory:
            self.inventory.remove(item)
            return item
    

    def get_by_id(self, item_id):
        for item_obj in self.inventory:
            if item_obj.id == item_id:
                return item_obj
        return None
    

    def swap_helper(self, other_vendor, my_item, their_item):
        other_vendor.inventory.append(my_item)
        self.inventory.append(their_item)
        other_vendor.inventory.remove(their_item)
        self.inventory.remove(my_item)


    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory: 
            return False
        if their_item not in other_vendor.inventory:
            return False            
        self.swap_helper(other_vendor, my_item, their_item)

        return True
    

    def swap_first_item(self, other_vendor):
        if not other_vendor.inventory or not self.inventory: 
            return False
        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]
        self.swap_helper(other_vendor, my_first_item, their_first_item)

        return True


    def get_by_category(self, category_str): 
        return [item_obj for item_obj in self.inventory if item_obj.get_category() == category_str]


    def my_max(self, collection, key):
        if not collection:
            raise ValueError
        
        max_item = collection[0]

        for item in collection:
            if key(item) > key(max_item):
                max_item = item
    
        return max_item


    def get_best_by_category(self, category_str):
        '''
        Alternative code before refactoring using list comprehension (line 79) and ternary expression with lambda expression (line 81)
        # max_condition = 0
        # highest_rated_category = None
                # if not same_categories:
        #     return None
        # else:
        #     return self.my_max(same_categories, key=lambda item_obj: item_obj.condition)

        # for item_obj in self.inventory:
        #     if item_obj.get_category() == category_str:
        #         if item_obj.condition > max_condition:
        #             max_condition = item_obj.condition
        #             highest_rated_category = item_obj
        # return highest_rated_category
        '''

        same_categories = [item_obj for item_obj in self.inventory if item_obj.get_category() == category_str]

        return None if not same_categories else self.my_max(same_categories, key=lambda item_obj: item_obj.condition)
    

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        other_vendor_item = other_vendor.get_best_by_category(my_priority)
        my_vendor_item = self.get_best_by_category(their_priority)

        if not other_vendor_item  or not my_vendor_item: 
            return False
        self.swap_helper(other_vendor, my_vendor_item, other_vendor_item)

        return True 
    

    def get_by_age(self, inventory):
        min_age = inventory[0].age
        min_item = inventory[0]
        for item_obj in inventory:
            if not item_obj.age:
                raise ValueError
            elif item_obj.age < min_age:
                min_age = item_obj.age
                min_item = item_obj
        return min_item


    def swap_by_newest(self, other_vendor):
        if not other_vendor.inventory or not self.inventory:
            return "Check if you have items in the inventory!"

        other_vendor_item = other_vendor.get_by_age(other_vendor.inventory)
        my_item = self.get_by_age(self.inventory)

        self.swap_helper(other_vendor, my_item, other_vendor_item)

        return "Newest items have been swapped!"