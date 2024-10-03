import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_condition_description():
    item_a = Clothing(condition=5)
    item_b = Electronics(condition=4.2)
    item_c = Clothing(condition=3.5)
    item_d = Decor(condition=2.1)
    item_e = Item(condition=1.5)
    item_f = Item(condition=0.5)
    vendor = Vendor(inventory=[item_a, item_b, item_c, item_d, item_e, item_f])

    result_a = item_a.condition_description()
    result_b = item_b.condition_description()
    result_c = item_c.condition_description()
    result_d = item_d.condition_description()
    result_e = item_e.condition_description()
    result_f = item_f.condition_description()

    assert len(vendor.inventory) == 6
    assert result_a and result_b == "Excellent!"
    assert result_c and result_d == "Good!"
    assert result_e and result_f == "Worn"

# Specific to Jen's implementation
@pytest.mark.skip
def test_swap_by_newest():
    item_a = Decor(age=2.5)
    item_b = Electronics(age=3.0)
    item_c = Decor(age=2.0)
    tai = Vendor(inventory=[item_a, item_b, item_c])
    item_d = Clothing(age=10.5)
    item_e = Decor(age=5.5)
    item_f = Clothing(age=12.0)
    jesse = Vendor(inventory=[item_d, item_e, item_f])

    result = tai.swap_by_newest(other_vendor=jesse)

    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_e in tai.inventory
    assert item_d in jesse.inventory
    assert item_f in jesse.inventory
    assert item_c in jesse.inventory
    assert item_c not in tai.inventory
    assert item_e not in jesse.inventory
    assert item_a.age == pytest.approx(2.5)
    assert item_b.age == pytest.approx(3.0)
    assert item_c.age == pytest.approx(2.0)
    assert item_d.age == pytest.approx(10.5)
    assert item_e.age == pytest.approx(5.5)
    assert item_f.age == pytest.approx(12.0)

@pytest.mark.skip
def test_swap_by_newest_reordered():
    item_a = Decor(age=2.5)
    item_b = Electronics(age=3.0)
    item_c = Decor(age=2.0)
    tai = Vendor(inventory=[item_c, item_b, item_a])
    item_d = Clothing(age=10.5)
    item_e = Decor(age=5.5)
    item_f = Clothing(age=12.0)
    jesse = Vendor(inventory=[item_e, item_f, item_d])

    result = tai.swap_by_newest(other_vendor=jesse)

    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_e in tai.inventory
    assert item_d in jesse.inventory
    assert item_f in jesse.inventory
    assert item_c in jesse.inventory
    assert item_c not in tai.inventory
    assert item_e not in jesse.inventory
    assert item_a.age == pytest.approx(2.5)
    assert item_b.age == pytest.approx(3.0)
    assert item_c.age == pytest.approx(2.0)
    assert item_d.age == pytest.approx(10.5)
    assert item_e.age == pytest.approx(5.5)
    assert item_f.age == pytest.approx(12.0)

@pytest.mark.skip
def test_swap_by_newest_no_inventory_is_false():
    tai = Vendor(inventory=[])
    item_a = Clothing(age=10.5)
    item_b = Decor(age=5.5)
    item_c = Clothing(age=12.0)
    jesse = Vendor(inventory=[item_a, item_b, item_c])
    result = tai.swap_by_newest(other_vendor=jesse)

    assert not result
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory
    assert item_a.age == pytest.approx(10.5)
    assert item_b.age == pytest.approx(5.5)
    assert item_c.age == pytest.approx(12.0)

@pytest.mark.skip
def test_swap_by_newest_no_other_inventory_is_false():
    item_a = Decor(age=2.5)
    item_b = Electronics(age=3.0)
    item_c = Decor(age=2.0)
    tai = Vendor(inventory=[item_a, item_b, item_c])
    jesse = Vendor(inventory=[])

    result = tai.swap_by_newest(other_vendor=jesse)

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert item_a.age == pytest.approx(2.5)
    assert item_b.age == pytest.approx(3.0)
    assert item_c.age == pytest.approx(2.0)

@pytest.mark.skip
def test_swap_by_newest_items_same_age():
    item_a = Decor(age=2.5)
    item_b = Electronics(age=2.5)
    item_c = Decor(age=2.5)
    tai = Vendor(inventory=[item_a, item_b, item_c])
    item_d = Clothing(age=2.5)
    item_e = Decor(age=2.5)
    item_f = Clothing(age=2.5)
    jesse = Vendor(inventory=[item_d, item_e, item_f])

    result = tai.swap_by_newest(other_vendor=jesse)
    
    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert item_d in tai.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory
    assert item_a in jesse.inventory
    assert item_a not in tai.inventory
    assert item_d not in jesse.inventory

    for item in tai.inventory:
        assert item.age == pytest.approx(2.5)
    for item in jesse.inventory:
        assert item.age == pytest.approx(2.5)