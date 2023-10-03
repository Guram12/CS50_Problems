from fuel import convert , gauge
import pytest

def main():
    test_convert()
    test_gauge()



def test_convert():
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("3/3") == 100
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("one/two")


def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"

if __name__ == "__main__":
    main()

























