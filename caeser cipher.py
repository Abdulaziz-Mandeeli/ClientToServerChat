import string

# ENCRYPTION/DECRYPTION USING CAESER CIPHER

msg="abdulaziz mandeeli"
shift = 4
print("Plain text : "+msg,shift)

#encrypttion:
shift %= 26
alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)
msg1 = msg.translate(table)
print("encrypttion: "+msg1)

#decrypttion:
dec = 26-shift
dec %= 26
alphabet = string.ascii_lowercase
shifted = alphabet[dec:] + alphabet[:dec]
table = str.maketrans(alphabet, shifted)
msg1 = msg1.translate(table)
print("decrypttion: "+msg1)