<<<<<<< HEAD
import math
from swap_meet.item import Item

=======
>>>>>>> bbcbf31a2ec976f0bc33abf970f310bc2022d21c
class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if not inventory else inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item
    
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    
<<<<<<< HEAD
    def swap_items(self,other_vendor,my_item,their_item):
        if my_item not in self.inventory or \
            their_item not in other_vendor.inventory:
            return False      
=======
    def swap_items(self, other_vendor, my_item, their_item):
        if (my_item not in self.inventory or
            their_item not in other_vendor.inventory):
            return False
        
>>>>>>> bbcbf31a2ec976f0bc33abf970f310bc2022d21c
        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)
<<<<<<< HEAD
        return True


    def swap_first_item(self,other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        my_first = self.inventory[0]
        their_first = other_vendor.inventory[0]
        # if my_first not in self.inventory or \
        #     their_first not in other_vendor.inventory:
        #     return False
        self.swap_items(other_vendor,my_first,their_first)

        return True
    
    def get_by_category(self,category):
        res = []
        for item in self.inventory: 
            if item.get_category() == category:
                res.append(item)
        return res

    def get_best_by_category(self,category):
        best_condition = 0.0
        best_item = None
        for item in self.inventory:
            if item.get_category() == category:
                if item.condition > best_condition:
                    best_condition = item.condition
                    best_item = item
        
        return best_item
    
    def swap_best_by_category(self,other_vendor,my_priority,their_priority):

        my_best= self.get_best_by_category(their_priority)
        their_best = other_vendor.get_best_by_category(my_priority)

        if not my_best or not their_best:
            return False
  
        self.swap_items(other_vendor,my_best,their_best)

        return True

    ##optional

    # swap the newest from my_vendor and other_vendor
    #regardless of the catergory
    def swap_by_newest(self,other_vendor,my_priority,their_priority):
    
        pass

    def get_newest_by_age(self,category):
        newest_age = 100
        newest_item = None
        for item in self.get_by_category(category):
            if item.age < newest_age:
                newest_age = item.age
                newest_item = item
        return newest_item



=======
        return True
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        my_first = self.inventory[0]
        their_first = other_vendor.inventory[0]
        self.swap_items(other_vendor, my_first, their_first)
        return True

    def get_by_category(self, category):
        items_in_category = []
        for item in self.inventory:
            if item.get_category() == category:
                items_in_category.append(item)
        
        return items_in_category
    
    def get_best_by_category(self, category):
        highest_condition = 0.0
        highest_item = None
        
        for item in self.get_by_category(category):
            if item.condition > highest_condition:
                highest_condition = item.condition
                highest_item = item
        return highest_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other_vendor.get_best_by_category(my_priority)
        
        if not my_best or not their_best:
            return False
        
        return self.swap_items(other_vendor, my_best, their_best)
>>>>>>> bbcbf31a2ec976f0bc33abf970f310bc2022d21c
