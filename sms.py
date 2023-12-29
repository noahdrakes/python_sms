import smtplib
import getpass

email_address = "noah.i.drakes@gmail.com"
email_password = "pozh maqt iqpf qzge" 

while True:
    recipient_phone_number = input("Input Recieient Phone Number **no dashes, no spaces**: ")

    sms_gateway = ""
    sms_carrier_character = ""

    sms_gateway_dictionary = {  'ver': 'vtext.com', 
                                'att': 'txt.att.net',
                                'tmob': 'tmomail.net',
                                'spr': 'messaging.sprintpcs.com',
                                'met': 'mymetropcs.com'}

    print("What carrier is your recipient using ?")

    for key, value in sms_gateway_dictionary.items():
        print(f'{key}: {value}')

    sms_carrier_character = input("input: ")

    sms_carrier_character = sms_carrier_character.lower()


    if sms_carrier_character == "ver":
        sms_gateway = sms_gateway_dictionary["ver"]
    elif sms_carrier_character == "att":
        sms_gateway = sms_gateway_dictionary["att"]
    elif sms_carrier_character == "tmob":
        sms_gateway = sms_gateway_dictionary["tmob"]
    elif sms_carrier_character == "spr":
        sms_gateway = sms_gateway_dictionary["spr"]
    elif sms_carrier_character == "met":
        sms_gateway = sms_gateway_dictionary["met"]
    else:
        print("ERROR: Iyour carrier is not supported", end="")
        exit()


    text_message = input("Input Text Message: ")

    sms_address = f'{recipient_phone_number}@{sms_gateway}'

    # Set up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_address, email_password)

    # Send the email
    result = server.sendmail(email_address, sms_address, text_message) # this method returns a dictionary of failed email addresses


    # if the dictionary is empty result = false
    # so if not results should = true if the message is sent sucessfully

    if not result:
        print("message sent successfully!", end="")
    else: 
        print("ERROR: message unsuccessfully!", end="")


    continueProgram = input("send another message (y/n) ?")

    continueProgram = continueProgram.lower()

    if continueProgram != "y":
        break

# Quit the server
server.quit()