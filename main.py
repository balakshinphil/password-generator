import random


quantity_characters = 30

alphabet = 'abcdefghijklmnopqrstuvwxyz'
upper_alphabet = alphabet.upper()
special_characters = '!\"#$%&\'()*+-/:;{}'


characters = [alphabet, upper_alphabet]

password = ''

for i in range(quantity_characters):
	r1 = random.randint(0,3)
	if r1 == 0 or r1 == 1:
		r2 = random.randint(0, 25)
		password += characters[r1][r2]
	elif r1 == 2:
		r2 = random.randint(0, len(special_characters)-1)
		password += special_characters[r2]
	else:
		r2 = random.randint(0, 9)
		password += str(r2)
			
print(password)

