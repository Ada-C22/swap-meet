import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_get_oldest_items():
    item_a = Clothing(age=2)
    item_b = Electronics(age=1)
    item_c = Clothing(age=2)
    item_d = Decor()
    item_e = Item(age=7)
    vendor = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )
    oldest = vendor.get_oldest()

    assert oldest == item_e