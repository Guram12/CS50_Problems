def convert(s: str) -> str:
    s = s.replace(":)", "🙂")
    s = s.replace(":(", "🙁")
    return s
s = input("write your smiles and words here ->> ")
converted_s = convert(s)
print(converted_s)

