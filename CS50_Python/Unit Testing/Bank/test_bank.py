from bank import value
def main():
    test_return_zero()
    test_return_twenty()
    test_return_hundred()
#test return zero
def test_return_zero():
    assert value ('hello sa')==0
    assert value ('hello')==0
    assert value ('hello Sa')==0
#test return zero
def test_return_twenty():
    assert value ('Hi')==20
    assert value ('hey')==20
#test return hundred
def test_return_hundred():
    assert value ("Good Morning")==100
    assert value ("what's up?")==100



if __name__ == "__main__":
    main()
