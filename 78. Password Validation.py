# 6. A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users

def check_smallcase(password):
	check = False
	for p in password:
		if(ord(p)>=ord('a') and ord(p)<=ord('z')):
			check = True
			break
	return check

def check_uppercase(password):
	check = False
	for p in password:
		if(ord(p)>=ord('A') and ord(p)<=ord('Z')):
			check = True
			break
	return check
	
def check_digit(password):
	check = False
	for p in password:
		if (ord(p)>=ord('0') and ord(p)<=ord('9')):
			check = True
			break
	return check

def check_specialChars(password):
	check = False
	specials = "!@#$%^&*()_+=-<>;:,./?\|"
	for p in password:
		if p in specials:
			check = True
			break
	return check

def check_minLength(password):
	return len(password)>=6

def check_maxLength(password):
	return len(password)<=12

passwords = list(set(input("Enter comma seperated passwords : ").split(',')))
valid_passwords = []
for password in passwords:
	if check_smallcase(password) and check_uppercase(password) and check_digit(password) and check_specialChars(password) and check_minLength(password) and check_maxLength(password):
		valid_passwords.append(password)
print(','.join(valid_passwords))