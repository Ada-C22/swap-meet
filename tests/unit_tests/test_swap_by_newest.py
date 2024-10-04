from swap_meet.vendor import Vendor
from swap_meet.item import Item 

def test_swap_by_newest():
    #arrange
    item_a = Item(age= 45)
    item_b = Item(age= 70)
    item_c = Item(age= 100)
    item_d = Item(age= 10)

    vendor1 = Vendor(
        inventory=[item_a, item_d]
    )
    vendor2 = Vendor(
        inventory=[ item_b, item_c]
    )
    #act    
    result = vendor1.swap_by_newest(vendor2)
    
    #assert
    assert result == True
    assert item_a in vendor1.inventory
    assert item_b in vendor1.inventory
    assert item_c in vendor2.inventory
    assert item_d in vendor2.inventory 

def test_swap_by_newest_returns_false_if_no_items_in_other_vendor():

#arrange
    item_a = Item(age= 45)
    item_d = Item(age= 10)

    vendor1 = Vendor(
        inventory=[item_a, item_d]
        )
    vendor2 = Vendor(
        inventory=[]
        )
    #act    
    result = vendor1.swap_by_newest(vendor2)
    
    #assert
    assert result == False
    assert item_a in vendor1.inventory
    assert item_d in vendor1.inventory
    assert len(vendor2.inventory) == 0
    assert len(vendor1.inventory) == 2

def test_swap_by_newest_returns_false_if_no_items_in_vendor():

#arrange
    item_a = Item(age= 45)
    item_d = Item(age= 10)

    vendor1 = Vendor(
        inventory=[]
        )
    vendor2 = Vendor(
        inventory=[item_a, item_d]
        )
    
    #act    
    result = vendor1.swap_by_newest(vendor2)
    
    #assert
    assert result == False
    assert item_a in vendor2.inventory
    assert item_d in vendor2.inventory
    assert len(vendor2.inventory) == 2
    assert len(vendor1.inventory) == 0 
