import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor

def test_swap_by_newest():
    item_a = Item(age=2)
    item_b = Item(age=4)
    item_c = Item(age=3)
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item(age=1)
    item_e = Item(age=4)
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_by_newest(jolie)

    assert len(fatimah.inventory) == 3
    assert item_b in fatimah.inventory
    assert item_a not in fatimah.inventory
    assert item_c in fatimah.inventory
    assert item_d in fatimah.inventory
    assert len(jolie.inventory) == 2
    assert item_d not in jolie.inventory
    assert item_e in jolie.inventory
    assert item_a in jolie.inventory
    assert result