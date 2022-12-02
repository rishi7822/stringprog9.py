# importing the module
from re import sub

# function to convert string to camelCase
def camelCase(string):
  string = sub(r"(_|-)+", " ", string).title().replace(" ", "")
  return string[0].lower() + string[1:]

# main code
s1 = "Hello world"
s2 = "Hello,world"
s3 = "Hello_world"
s4 = "hello_world.txt_includehelp-WEBSITE"

print("s1: ", s1)
print("camelCase(s1): ", camelCase(s1))
print()

print("s2: ", s2)
print("camelCase(s2): ", camelCase(s2))
print()

print("s3: ", s3)
print("camelCase(s3): ", camelCase(s3))
print()

print("s4: ", s4)
print("camelCase(s4): ", camelCase(s4))
print()
