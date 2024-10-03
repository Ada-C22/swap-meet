import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_swap_by_newest():
    # arrange
    item_a = Clothing(age=1)
    item_b = Electronics(age=2)
    item_c = Clothing(age=3)
    item_d = Decor(age=4)
    item_e = Item(age=5)
    item_f = Item(age=6)

    #act
    may = Vendor(
        inventory=[item_a,item_b,item_c]
    )
    anh = Vendor(
        inventory=[item_d, item_e, item_f]
    )
    result = may.swap_by_newest(anh)

    assert result
    assert may.inventory == [item_d, item_b, item_c]
    assert anh.inventory == [item_a, item_e, item_f]

def test_swap_by_newest_defaults():
    item_a = Clothing() #8
    item_b = Electronics()#6
    item_c = Clothing()
    item_d = Decor()#4
    item_e = Item()#10
    item_f = Decor()

    may = Vendor(
        inventory=[item_a,item_b,item_c]
    )
    anh = Vendor(
        inventory=[item_d, item_e, item_f]
    )
    result = may.swap_by_newest(anh)

    assert result
    assert may.inventory == [item_a,item_d,item_c]
    assert anh.inventory == [item_b, item_e, item_f]

def test_swap_by_newest_defaults_reordered():
    item_a = Clothing() #8
    item_b = Electronics()#6
    item_c = Clothing()
    item_d = Decor()#4
    item_e = Item()#10
    item_f = Decor()

    may = Vendor(
        inventory=[item_a,item_b,item_c]
    )
    anh = Vendor(
        inventory=[item_f, item_e, item_d]
    )
    result = may.swap_by_newest(anh)

    assert result
    assert may.inventory == [item_a,item_f,item_c]
    assert anh.inventory == [item_b, item_e, item_d]

def test_swap_by_newest_invalid():
    item_a = Clothing() #8
    item_b = Electronics()#6
    item_c = Clothing()
    item_d = Decor()#4
    item_e = Item()#10
    item_f = Decor()

    may = Vendor(
        inventory=[]
    )
    anh = Vendor(
        inventory=[item_d, item_e, item_f]
    )
    result = may.swap_by_newest(anh)

    assert not result
    assert may.inventory == []
    assert anh.inventory == [item_d, item_e, item_f]

def test_invalid_id():
    with pytest.raises(TypeError):
        item = Item(id="abc") 