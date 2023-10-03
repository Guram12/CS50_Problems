from twttr import shorten

def main():
    test_shorten()



def test_shorten():
    assert shorten("gurami") == "grm"
    assert shorten("twitter") == "twttr"
    assert shorten(". , / : ") == ". , / : "
    assert shorten("1 2 3") == "1 2 3"
    assert shorten("GURAM") == "GRM"
if __name__ == "__main__":
    main()