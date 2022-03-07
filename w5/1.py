import re

txt = "The    rain        in      Spain"
# x = re.findall("in", txt)

# x = re.search("in", txt)
# if x:
#   print(x.start())
#   print(x.group())

# x = re.split(r'\s+', txt)
# print(x)

# x = re.sub(r'in', '**', txt)
# x = re.sub(r'\s+', ' ', txt)

# print(x)


x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.string)
print(x.group())
