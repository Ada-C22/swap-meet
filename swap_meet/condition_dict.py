''' 
This module contains the condition table dictionary used by the Item class.
The dictionary maps condition values to their corresponding descriptions. 
It is used by the condition_description method in the Item class. 
'''

condition_table = {
            5: "Brand New",
            4: "Used - Like New/ Open Box/ Without Tags",
            3: "Used - Good",
            2: "Used - Fair",
            1: "Used - Poor",
            0: "For Parts - Not Working"
        }