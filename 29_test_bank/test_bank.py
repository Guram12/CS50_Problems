from bank import value


def main():
    test_value()




def test_value():
    assert value("hello") == 0
    assert value("how are you?") == 20
    assert value("greeting") ==100
    assert value("HELLO") == 0
    assert value("1 2 3") == 100

if __name__ == "__main__":
    main()