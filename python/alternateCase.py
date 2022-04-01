
def alternateCase(string):

	temp = ''

	for i in string:
		if i == i.lower():
			temp = temp + i.upper()
		if i == i.upper():
			temp = temp + i.lower()
	return temp


print(alternateCase("abc"))
print(alternateCase("ABC"))
print(alternateCase("Hello World"))
print(alternateCase("mAs WiLdaN gaNTeng"))
