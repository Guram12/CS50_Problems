user = input("start conversation!")
low_user = user.lower()
if "hello" in low_user :
    print("$0")
elif "h" in low_user[0] :
    print("$20")
else:
    print("$100")