def caesarcipher_encryption(plaintext,key):
    
    encrypted_message=""
    for char in plaintext:
        if char.isalpha():
            code=ord(char.lower())+key
            encrypted_text=chr(code)
            if code>=ord('z'):
                code-=26
            if  char.isupper():
                encrypted_char=encrypted_text.upper()
                encrypted_message+=encrypted_char 
            else:
                 encrypted_message+=encrypted_text
        else:
                encrypted_message+=char
    return encrypted_message 
def caesarcipher_decryption(encrypted_text,shift):
    decrypted_message=""
    for char in encrypted_text:
        if char.isalpha():
            code=ord(char.lower())-shift
            decrypted_text=chr(code)
            if code>=ord('z'):
                code+=26
            if  char.isupper():
                decrypted_char=decrypted_text.upper()
                decrypted_message+=decrypted_char
            else:
                 decrypted_message+=decrypted_text
        else:
                decrypted_message+=char
    return decrypted_message   

def switch(choice):
    if choice==1:
        plaintext=input("enter the text=")
        key=int(input("enter the shift value="))

        return caesarcipher_encryption(plaintext,key)

    elif choice==2:
       
         encrypted_text=input("enter the encrypted message:")
         shift=int(input("enter the shift:"))

         return caesarcipher_decryption(encrypted_text,shift)
    else:
        return "invaid choice"

choice=int(input("enter the choice ,1 for encryption and 2 for decryption:"))
    
print(switch(choice))
