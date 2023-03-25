# 88. Assuming that we have some email addresses in the \"username@companyname.com\" format,
# please write program to print the user name of a given email address
# Both user names and company names are composed of letters only

def username(email: str):
	return email.split('@')[0]

email = input("Enter email address : ")
print(username(email))