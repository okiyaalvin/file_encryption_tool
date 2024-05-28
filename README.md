encrypt.py file has the encryption and functions
Main.py file is the main code which has the UI allowing user to log in or create account
The UI file also has authentication functions 
######################################################
The user is allowed to create acoount,from which upon successful account creation, 
He/she can log into the account
The main.py file does the authentication and if successful, the encrypt.py file is called
It then can be used to perform the encruption, decryption.
########################################################
The algorithm used is fernet algorithm which is a combination of AES 128 and Cipher Block Chaining
This make it a secure encryption algoriythm as it encrypts multiple blocks of data at a time.
