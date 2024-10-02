import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


def test_swap_newest_item():
# Arrange
    # me
    item_a = Decor(age=2.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=7.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=2.0)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=3.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(other_vendor=jesse)


    # - That the results is truthy
    assert result is True
    # - That tai and jesse's inventories are the correct length
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    # - That all the correct items are in tai and jesse's inventories, including the items which were swapped from one vendor to the other
    assert item_d in tai.inventory
    assert item_a in jesse.inventory
    
