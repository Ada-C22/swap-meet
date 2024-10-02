import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item

#@pytest.mark.skip
def test_swap_items_by_newest_items_returns_true():
    item_a = Item(age=13)
    item_b = Item(age=2)
    item_c = Item(age=24)
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item(age=10)
    item_e = Item(age=14)
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_by_newest(jolie)

    assert len(fatimah.inventory) == 3
    assert item_b not in fatimah.inventory
    assert item_a in fatimah.inventory
    assert item_c in fatimah.inventory
    assert item_d in fatimah.inventory
    assert len(jolie.inventory) == 2
    assert item_d not in jolie.inventory
    assert item_e in jolie.inventory
    assert item_b in jolie.inventory
    assert result

#@pytest.mark.skip
def test_swap_items_when_my_items_age_is_missing_returns_false():
    item_a = Item(age=50)
    item_b = Item(age=14)
    item_c = Item(age=8)
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item(age=34)
    item_e = Item(age=0)
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_by_newest(jolie)

    assert len(fatimah.inventory) == 3
    assert item_c not in fatimah.inventory
    assert item_e in fatimah.inventory
    assert item_b in fatimah.inventory
    assert item_a in fatimah.inventory
    assert len(jolie.inventory) == 2
    assert item_d in jolie.inventory
    assert item_e not in jolie.inventory
    assert result

@pytest.mark.skip
def test_swap_items_when_their_item_is_missing_returns_false():
    item_a = Item()
    item_b = Item()
    item_c = Item()
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item()
    item_e = Item()
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.fatimah.swap_by_newest(jolie)

    assert len(fatimah.inventory) == 3
    assert item_d not in fatimah.inventory
    assert item_a in fatimah.inventory
    assert item_b in fatimah.inventory
    assert item_c in fatimah.inventory
    assert len(jolie.inventory) == 2
    assert item_d in jolie.inventory
    assert item_e in jolie.inventory
    assert not result

@pytest.mark.skip
def test_swap_items_from_my_empty_returns_false():
    fatimah = Vendor(
        inventory=[]
    )

    item_d = Item()
    item_e = Item()
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    nobodys_item = Item()

    result = fatimah.fatimah.swap_by_newest(jolie)

    assert len(fatimah.inventory) == 0
    assert len(jolie.inventory) == 2
    assert not result

@pytest.mark.skip
def test_swap_items_from_their_empty_returns_false():
    item_a = Item()
    item_b = Item()
    item_c = Item()
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jolie = Vendor(
        inventory=[]
    )

    nobodys_item = Item()

    result = fatimah.swap_items(jolie, item_b, nobodys_item)

    try:
        result == False
    except ValueError as err:
        print(f'An exception occurred. Here are the error details {err}')

    assert len(fatimah.inventory) == 3
    assert len(jolie.inventory) == 0
    assert result == False
