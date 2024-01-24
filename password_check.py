import re 

def check_password(passwords):
	passwords_split = passwords.split(',')
	print(passwords_split)
	res =  []
	pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[$#@]).{6,12}$"

	for password in passwords_split:
		if re.match(pattern, password):
			res.append(password)
		else:
			print('no match:', password)

	return ','.join(res)