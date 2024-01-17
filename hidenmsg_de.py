
print("----------WELCOME TO MESSAGE DECODER---------")
# Encoded message
encoded_message =input("Enter the encoded message")

def decode_message(encoded_message):
    decoded_message=''
    for char in encoded_message:
        decoded_message+= chr(ord(char)+1)
    return decoded_message


# Decode and print the message
hidden_message = decode_message(encoded_message)
print(f'Your hidden message is : {hidden_message}')




# def encode_message2 (message2):
#     encoded_message2=''
#     for char in message2:
#         encoded_message2+=chr(ord(char)-1)
#     return encoded_message2

# ######
# message2= input("Enter Your message here: ")
# #####
# hidden_message2=encode_message2(message2)
# print(f'Your hidden message is : {hidden_message2}')
