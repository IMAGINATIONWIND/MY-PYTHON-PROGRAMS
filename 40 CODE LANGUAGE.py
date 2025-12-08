b = "nametatenamka"
for char in b:
    if (ord(char)<65 or ord(char)>122):
        raise ValueError ("Please enter only alphabets")

