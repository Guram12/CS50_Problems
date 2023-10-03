from plates import is_valid

def main():
    test_is_valid()


def test_is_valid():
    assert is_valid("12BBDFDG") == False
    assert is_valid("A") == False
    assert is_valid("123456") == False
    assert is_valid("AA5BB") == False
    assert is_valid("AAA222") == True
    assert is_valid("A,1./;:") == False
    assert is_valid("ABC012") == False
    assert is_valid("A1b2C3") == False
    assert is_valid("ab") == True
    assert is_valid("a1") == False
    assert is_valid("cs32") == True
    assert is_valid("cs.,32") == False


if __name__ == "__main__":
    main()