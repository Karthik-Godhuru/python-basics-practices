password=(input("enter the password: "))
has_upper=False
has_digit=False
has_lower=False
for  ch in password:
	if ch.isupper():
		has_upper=True
	if ch.islower():
		has_lower=True
	if ch.isdigit():
		has_digit=True	
if len(password)>=8 and has_upper and has_digit and has_lower:
	print("strong")
else:
	print("weak")