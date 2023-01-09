import os.path
import subprocess
import sys
import random
import string
import cryptography.fernet
import stdiomask

def generateMasterPassword():
	key = cryptography.fernet.Fernet.generate_key()
	with open("./master.key", "wb") as masterPasswordWriter:
		masterPasswordWriter.write(key)

def loadMasterPassword():
	return open("./master.key", "rb").read()

def createVault():
	return open("./.vault.txt", "wb")
	vault.close()

def encryptData(_data):
	f = cryptography.fernet.Fernet(loadMasterPassword())
	with open("./.vault.txt", "rb") as vaultReader:
		encrypted_data = vaultReader.read()
	if encrypted_data.decode() == '':
		return f.encrypt(_data.encode())
	else:
		decrypted_data = f.decrypt(encrypted_data)
		new_data = decrypted_data.decode() + _data
		return f.encrypt(new_data.encode())

def decryptedData(_encrypted_data):
	f = cryptography.fernet.Fernet(loadMasterPassword())
	return f.decrypt(_encrypted_data)

def appendNewPassword():
	print()
	username = input("Enter a username: ")
	password = stdiomask.getpass(prompt="Enter a password: ", mask="*")
	website = input("Enter a website: " )
	print()

	username_line = "Username: " + username + "\n"
	password_line = "Password: " + password + "\n"
	website_line = "Website: " + website + "\n\n"

	encryptedData = encryptData(username_line + password_line + website_line)
	with open("./.vault.txt", "wb") as vaulWriter:
		vaulWriter.write(encryptedData)

def readPasswords():
	with open("./.vault.txt", "rb") as passwordsReader:
		encryptedData = passwordsReader.read()
	print()
	print(decryptedData(encryptedData).decode())

def generateNewPassword(_password_length):
	randomString = string.ascii_letters + string.digits + string.punctuation
	new_psswd = ''
	for i in range(_password_length):
		new_psswd += random.choice(randomString	)
	print()
	print("Here is your new password: " + new_psswd)

# CLI
subprocess.call("clear", shell=True)

print('-' * 60)
print("Welcome to your password manager! (ctrl + c to quit)")
print('-' * 60)

app_run = True

try:
	while app_run == True:
		if os.path.exists("./.vault.txt") and os.path.exists("./master.key"):
			print("Select one of the following options - \n")
			print("1 - Save a new password")
			print("2 - Generate a new password")
			print("3 - Get the list of your passwords")
			print("4 - Quit app")

			user_choice = input("\nPick an option: ")

			if user_choice == "1":
				appendNewPassword()
			elif user_choice == "2":
				password_length = input("Select your password length: ")
				if not (string.ascii_letters in password_length):
					generateNewPassword(int(password_length))
				else:
					print("Please, enter a digit next time...")
					sys.exit()
			elif user_choice == "3":
				readPasswords()
			elif user_choice == "4":
				print("See you later.")
				sys.exit()
			else:
				print("The selected option is incorrect...")
				sys.exit()
		else:
			print("Password and vault generation...")
			generateMasterPassword()
			createVault()
			print("Generation completed")
except KeyboardInterrupt:
	print("\n[+] See you later.\n")