d = 0
print("1. First, take a colour A4 sheet, colour penicls, platignums, pens,glue,flowers,stickers etc. to decorate")
print("1. Yes")
print("2. No")
do = int(input("Did you do it? 1 or 2 :"))
if do == 1:
    print("2. Then, fold the colour A4 sheet.")
    do = int(input("Did you do it? 1 or 2 :"))
    if do == 1:
        print("3. Write the text 'HAPPY BIRTHDAY' on the first page of your birthday card.")
        do = int(input("Did you do it? 1 or 2 :"))
        if do == 1:
            print(
                "4. Then, draw a cake or something related to birthday inside the card or paste it.")
            do = int(input("Did you do it? 1 or 2 :"))
            if do == 1:
                print(
                    "5. Then write who send this card and to whom send the card below the cake or whatever you have drawn")
                do = int(input("Did you do it? 1 or 2 :"))
                if do == 1:
                    print(
                        "6. Now decorate it as you like with platignums, stikers, flowers etc.")

                    print("7.1. Online")
                    print("  2. Letter")

                    send = int(
                        input("How do you like to send this card ? Enter 1 or 2 :"))
                    if send == 1:
                        print("8.First, pen the app you want to send the card.")
                        print(
                            "9.Then, Send the card to the reciver's phone number or email.")
                    elif send == 2:
                        print("8.First, put the birthday card into a letter.")
                        print(
                            "9.Then, write the reciver's adress and paste a stamp.")
                        print(
                            "10.Finally, go to the post office and send the birthday card.")
                    else:
                        pass
