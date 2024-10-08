import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_age_valid_is_true():
    num = 5

    item = Item(age=num)
    assert isinstance(item.age, int)
    assert item.age == num

def test_swap_by_newest_no_inventory_is_false():
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(age=1)
    item_b = Decor(age=3)
    item_c = Clothing(age=5)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.swap_by_newest(
        other_vendor=jesse
    )

    assert not result
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory

def test_swap_by_newest_valid_input_true():
    # Arrange
    # me
    item_a = Decor(age=2)
    item_b = Electronics(age=4)
    item_c = Decor(age=4)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=2)
    item_e = Decor(age=4)
    item_f = Clothing(age=4)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(
        other_vendor=jesse
    )
    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_d in tai.inventory
    assert item_b in tai.inventory