import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# @pytest.mark.skip
def test_get_by_age():
    # Arrange
    item_a = Decor(age=2.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )
    
    #Act
    result = tai.get_by_age()

    #Assert
    assert result == item_a
    assert len(tai.inventory) == 3

# @pytest.mark.skip
def test_get_by_age_return_false_if_no_inventory():
    # Arrange
    item_a = Decor(age=2.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[]
    )
    
    #Act
    result = tai.get_by_age()

    #Assert
    assert result == False
    assert len(tai.inventory) == 0

# @pytest.mark.skip
def test_get_newest_by_category():
    # Arrange
    item_a = Decor(age=5.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )
    
    # Act
    result = tai.get_newest_by_category("Decor")

    #Assert
    assert result is item_c
    assert len(tai.inventory) is 3


# @pytest.mark.skip
def test_swap_by_newest():
    # Arrange
    item_a = Decor(age=2.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(age=2.0)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(jesse)

    # Assert
    assert len(tai.inventory) == 3 and len(jesse.inventory)==3
    assert item_a in jesse.inventory and item_a not in tai.inventory
    assert item_d in tai.inventory and item_d not in jesse.inventory

# @pytest.mark.skip
def test_swap_newest_by_category():
    # Arrange
    item_a = Decor(age=2.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(age=2.0)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_newest_by_category(jesse, "Decor", "Decor")

    # Assert
    assert len(tai.inventory) == 3 and len(jesse.inventory)==3
    assert item_a in jesse.inventory and item_a not in tai.inventory
    assert item_e in tai.inventory and item_e not in jesse.inventory

# @pytest.mark.skip
def test_swap_newest_by_category_is_no_item_in_catogory():
    # Arrange
    item_a = Decor(age=2.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(age=2.0)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_newest_by_category(jesse, "Decor", "Clothing")

    # Assert
    assert len(tai.inventory) == 3 and len(jesse.inventory)==3
    assert result is False
    assert item_a in tai.inventory and item_b in tai.inventory and item_c in tai.inventory
    assert item_d in jesse.inventory and item_e in jesse.inventory and item_f in jesse.inventory
