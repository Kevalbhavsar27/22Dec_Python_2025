import re

# words = "sun rises in east in"

# k = re.match("sun",words)
# k = re.search("in",words)
# k = re.findall("s",words)
# k = re.finditer("s",words)
# k = re.sub("s","T",words)
# k = re.split(" ",words)
# print(k)


# k = re.findall("t.i","hblo, this pythion")
# k = re.search("^hello","hello python")
# k = re.search("n$","hello python")
# k = re.search("ab*c","abbbbbbbc hello python")
# k = re.search("ab+c","abbbc hello python")
# k = re.search("ab?c","abbc hello python")
# k = re.findall("[0-9]","abbbc hello python 232 23")

# k = re.findall(r"\Bbbb\B","abbbc hellooo python hello 232 23 @")
# print(k)


# email = "test@gmail.com"
# pattern = "^[a-zA-Z0-9_-]+@[a-zA-Z]+\\.[a-zA-Z]{2,4}$"

# k = re.match(pattern,email)
# if k is None:
#     print("Invalid email format")
# else:
#     print("Valid formate")


k = re.match(r"^\d{10}$","444444444")
print(k)