import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
from datetime import datetime

# @pytest.mark.skip
def test_get_items_by_category():
    item_a = Clothing()
    item_b = Electronics()
    item_c = Clothing()
    item_d = Decor()
    item_e = Item()
    vendor = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    items = vendor.get_by_category("Clothing")

    assert len(items) == 2
    assert item_a in items
    assert item_c in items

# @pytest.mark.skip
def test_get_no_matching_items_by_category():
    item_a = Clothing()
    item_b = Item()
    item_c = Decor()
    vendor = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    items = vendor.get_by_category("Electronics")

    assert items == []

# @pytest.mark.skip
def test_best_by_category():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=2.0)
    item_c = Clothing(condition=4.0)
    item_d = Decor(condition=5.0)
    item_e = Clothing(condition=3.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    best_item = tai.get_best_by_category("Clothing")

    assert best_item.get_category() == "Clothing"
    assert best_item.condition == pytest.approx(4.0)

# @pytest.mark.skip
def test_best_by_category_no_matches_is_none():
    item_a = Decor(condition=2.0)
    item_b = Decor(condition=2.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    best_item = tai.get_best_by_category("Electronics")

    assert best_item is None

# @pytest.mark.skip
def test_best_by_category_with_duplicates():
    # Arrange
    item_a = Clothing(condition=2.0)
    item_b = Clothing(condition=4.0)
    item_c = Clothing(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # Act
    best_item = tai.get_best_by_category("Clothing")

    # Assert
    assert best_item.get_category() == "Clothing"
    assert best_item.condition == pytest.approx(4.0)

# @pytest.mark.skip
def test_swap_best_by_category():
    # Arrange
    # me
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_best_by_category(
        other_vendor=jesse,
        my_priority="Clothing", # tai priority
        their_priority="Decor"  # jesse priority
    )

    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert jesse.inventory == [item_d, item_e, item_c]
    # assert jesse.inventory == [item_d, item_e, item_c]

    # Assertions should check:
    # - That the results is truthy
    # - That tai and jesse's inventories are the correct length
    # - That all the correct items are in tai and jesse's inventories, including the items which were swapped from one vendor to the other

# @pytest.mark.skip
def test_swap_best_by_category_reordered():
    # Arrange
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)   # jesse priority
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)   # tai priority
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_best_by_category(
        other_vendor=jesse,
        my_priority="Clothing",   # tai priority
        their_priority="Decor"    # jesse priority
    )

    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert tai.inventory == [item_b, item_a, item_f]
    assert jesse.inventory == [item_e, item_d, item_c]
    # Assertions should check:
    # - That result is truthy
    # - That tai and jesse's inventories are the correct length
    # - That all the correct items are in tai and jesse's inventories, and that the items that were swapped are not there

# @pytest.mark.skip
def test_swap_best_by_category_no_inventory_is_false():
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=4.0)
    item_c = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.swap_best_by_category(
        other_vendor=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert not result
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory

# @pytest.mark.skip
def test_swap_best_by_category_no_other_inventory_is_false():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=4.0)
    item_c = Clothing(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jesse = Vendor(
        inventory=[]
    )

    result = tai.swap_best_by_category(
        other_vendor=jesse,
        my_priority="Decor",
        their_priority="Clothing"
    )

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

# @pytest.mark.skip
def test_swap_best_by_category_no_match_is_false():
    # Arrange
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_best_by_category(
        other_vendor=jesse,
        my_priority="Clothing",
        their_priority="Clothing"
    )

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert tai.inventory == [item_a, item_b, item_c]
    assert jesse.inventory == [item_d, item_e, item_f]
    # Assertions should check:
    # - That result is falsy
    # - That tai and jesse's inventories are the correct length
    # - That all the correct items are in tai and jesse's inventories

# @pytest.mark.skip
def test_swap_best_by_category_no_other_match_is_false():
    # Arrange
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)    # jesse priority
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_best_by_category(
        other_vendor=jesse,
        my_priority="Electronics",   # tai priority
        their_priority="Decor"       # jesse priority
    )

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert tai.inventory == [item_c, item_b, item_a]
    assert jesse.inventory == [item_f, item_e, item_d]

    # Assertions should check:
    # - That result is falsy
    # - That tai and jesse's inventories are the correct length
    # - That all the correct items are in tai and jesse's inventories

def test_item_has_valid_age():
    # Arrange
    age = (2024,7,8)
    # Act
    item = Item(age=age)
    # Assert
    assert item.age
    assert item.age == datetime(*age).date()

def test_swap_by_newest_returns_true():
    # Arrange
    item_a = Decor(age=(2024,9,6)) # newest
    item_b = Electronics(age=(2023,6,6))
    item_c = Decor(age=(2022,12,6))   
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(age=(2024,9,1))
    item_e = Decor(age=(2023,9,6))
    item_f = Clothing(age=(2024,9,8))   # newest
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )
    # Act
    exchanged = tai.swap_by_newest(jesse)
    
    # Assert
    assert exchanged
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert tai.inventory == [item_c, item_b, item_f]
    assert jesse.inventory == [item_e, item_d,item_a]
    
def test_swap_by_newest_swaps_first_newest_in_inventory():
    # Arrange
    item_a = Decor(age=(2024,9,6)) # newest
    item_b = Electronics(age=(2023,6,6))
    item_c = Decor(age=(2024,9,6)) # newest
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(age=(2024,9,1))
    item_e = Decor(age=(2023,9,6))
    item_f = Clothing(age=(2024,9,8))   # newest
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )
    # Act
    print(f"{tai.inventory=}")
    print(f"{jesse.inventory=}")
    exchanged = tai.swap_by_newest(jesse)
    print(f"{tai.inventory=}")
    print(f"{jesse.inventory=}")
    
    # Assert
    assert exchanged
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert tai.inventory == [ item_b, item_a, item_f]
    assert jesse.inventory == [ item_e, item_d, item_c ]
    
def test_swap_by_newest_returns_false_with_empty_inventory():
    # Arrange
    item_a = Decor(age=(2024,9,6)) # newest
    item_b = Electronics(age=(2023,6,6))
    item_c = Decor(age=(2024,9,6)) # newest
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    jesse = Vendor(
        inventory=[]
    )
    # Act
    exchanged = tai.swap_by_newest(jesse)
    
    # Assert
    assert not exchanged
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert tai.inventory == [item_c, item_b, item_a]
    assert jesse.inventory == []
    