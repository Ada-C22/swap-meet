import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_get_by_age():
    item_a = Clothing(age=1)
    item_b = Electronics(age=2)
    item_c = Clothing(age=3)
    item_d = Decor(age=4)
    item_e = Item(age=5)
    vendor = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    items = vendor.get_by_age(vendor.inventory)

    assert items == item_a


def test_get_by_age_none_value():
    item_a = Clothing()
    item_b = Item(age=2)
    item_c = Decor(age=3)
    vendor = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    with pytest.raises(ValueError):
        vendor.get_by_age(vendor.inventory)


def test_swap_by_newest():
    item_a = Clothing(age=1)
    item_b = Electronics(age=2)
    item_c = Clothing(age=3)
    item_d = Decor(age=4)
    item_e = Item(age=5)
    izzy = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    item_f = Clothing(age=3)
    item_g = Item(age=2)
    item_h = Decor(age=1)
    kristina = Vendor(
        inventory=[item_f, item_g, item_h]
    )
    result = izzy.swap_by_newest(kristina)

    assert result == "Newest items have been swapped!"
    assert item_a in kristina.inventory
    assert item_h in izzy.inventory
    assert item_a not in izzy.inventory
    assert item_h not in kristina.inventory


def test_swap_by_newest_empty_list():
    item_a = Clothing(age=1)
    item_b = Electronics(age=2)
    item_c = Clothing(age=3)
    item_d = Decor(age=4)
    item_e = Item(age=5)
    izzy = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    kristina = Vendor(
        inventory=[]
    )
    result = izzy.swap_by_newest(kristina)

    assert result == "Check if you have items in the inventory!"