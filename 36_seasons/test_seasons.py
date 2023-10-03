from seasons import convert , subtract_minutes
from datetime import date, datetime
def main():
    convert()
    subtract_minutes()



def test_convert():
    assert convert(12) == "Twelve minutes"
    assert convert(130) == "One hundred thirty minutes"



def test_subtract_minutes():
    t = datetime.fromisoformat("1500-12-11").date()
    d = date.today()
    assert subtract_minutes(t,d) == 274809600.0



if __name__ == "__main__":
    main()