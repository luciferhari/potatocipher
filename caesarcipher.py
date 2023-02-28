def caesarcipher_encryption():
    plaintext=input("enter the text=")
    key=int(input("enter the key value="))
    encrypted_message=""
    for char in plaintext:
        if char.isalpha:
            code=ord(char.lower())+key
            if code>=ord('z'):
                code-=26
            encrypted_text=chr(code)
            if  char.isupper:
                encrypted_char=encrypted_text.upper()
                encrypted_message+=encrypted_char 
        else:
            encrypted_message+=char
    return encrypted_message 
def caesarcipher_decryption(plaintext,shift):
    encrypted_message=""
    for char in plaintext:
        if char.isalpha:
            code=ord(char.lower())-shift
            if code>=ord('z'):
                code-=26
            encrypted_text=chr(code)
            if  char.isupper:
                encrypted_char=encrypted_text.upper()
                encrypted_message+=encrypted_char 
        else:
            encrypted_message+=char
    return encrypted_message   


def switch(choice):
    if choice==1:
        return caesarcipher_encryption()
    if choice==2:
        return caesarcipher_decryption()

choice=int(input("enter the choice:"))
    
print(switch(choice))
