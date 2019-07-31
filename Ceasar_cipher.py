print('Encrypted msg is :')

ms = """te td fyvyzhy szh pqqpnetgp esp nlpdlc ntaspc hld le esp etxp, mfe te td wtvpwj
ez slgp mppy cpldzylmwj dpnfcp, yze wplde mpnlfdp xzde zq nlpdlc'd pypxtpd
hzfwo slgp mppy twwtepclep lyo zespcd hzfwo slgp lddfxpo esle esp xpddlrpd
hpcp hcteepy ty ly fyvyzhy qzcptry wlyrflrp"""

print(ms)  # display the encrypted message from "ms"


# this function will plus number of shift to "text"(ms) depends on the parameter "shift"
def decrypted_text(text, shift):
    a = ord('a')  # we use ord to
    return ''.join(
        chr((ord(char) - a + shift) % 26 + a) if 'a' <= char <= 'z' else char
        # get the new letter in 'ms' using ord at 'shift'
        for char in text.lower())  # turn every text in 'text' to lower case if it not the lower case


for i in range(1, 100):  # set loop to 100 times
    if i < 100:
        ipt = input("Is this your plaintext ? y/n ")
        if ipt == "n" or ipt == "N":  # if user input n or N will do this condition
            print("==============================================================")
            print(decrypted_text(ms, i))  # send the message from 'ms' and the number of shift that increases by 1 as 'i' every time through function 'decrypted_text'
        if ipt == "y" or ipt == "Y":  # if user input y or Y will do this condition
            i-=1
            print("==============================================================")
            print("cracked!!, number of shift(s) = ", i)  # display the number of shift
            print("==============================================================")
            break  # break the loop
        else:
            print("Please enter y/n")

input(
    "Press ENTER to exit")  # when it comes to .exe file we need to set the waiting point for user to see the result before the program closes
