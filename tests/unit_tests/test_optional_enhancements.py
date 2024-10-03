import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# @pytest.mark.skip
def test_swap_by_newest():
    # Arrange
    item_a = Decor(age=2)
    item_b = Electronics(age=4)
    item_c = Decor(age=3)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(age=5)
    item_e = Decor(age=7)
    item_f = Clothing(age=1)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )
    # act
    result = tai.swap_by_newest(
        other_vendor=jesse
    )

    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert tai.inventory == [item_f, item_b, item_c]
    assert jesse.inventory == [item_d, item_e, item_a] 

# @pytest.mark.skip
def test_swap_by_newest_no_inventory_is_false():
    tai = Vendor(
        inventory=[]
    )

    item_d = Clothing(age=5)
    item_e = Decor(age=7)
    item_f = Clothing(age=1)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_by_newest(
        other_vendor=jesse
    )

    assert not result
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory

# @pytest.mark.skip
def test_swap_by_newest_no_other_inventory_is_false():
    item_a = Decor(age=2)
    item_b = Electronics(age=4)
    item_c = Decor(age=3)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jesse = Vendor(
        inventory=[]
    )

    result = tai.swap_by_newest(
        other_vendor=jesse
    )

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory