myfloat = 7.0
print(myfloat)
print(type(myfloat))

myfloat = float(7)
print(myfloat)
print(type(myfloat))

myfloat = float("7.0")
print(myfloat)
print(type(myfloat))

a,b,c,d = 10, 20.0, "hello", "world"
print(a)
print(b)
print(c)
print(d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))


mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    # print("String: %s" % mystring)
    print(f"String: {mystring}")
if isinstance(myfloat, float) and myfloat == 10.0:
    # print("Float: %f" % myfloat)
    print(f"Float: {myfloat}")
if isinstance(myint, int) and myint == 20:
    # print("Integer: %d" % myint)
    print(f"Integer: {myint}")


name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# concatenation
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

# adding whitespaces to strings
print("python")
print("\tpython")
print("languages:\npython\nc\njavascript")
print("languages:\n\tpython\n\tc\n\tjavascript")

# stripping whitespaces
name = "ada lovelace"
print(name.title())