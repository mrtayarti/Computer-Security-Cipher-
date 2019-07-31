import re

letters_arr = []  # set 'letters_arr' as array
pin = 0  # set 'pin' = 0
for i in range(65, 91):  # loop to add every capital letter into 'letters_arr'
    letters_arr.append(chr(i)) # add value of chr ar i to letters_arr

k = 0  # set k=0 to use k to point the index number
table = [[0 for i in range(5)] for j in range(5)]  # create the matrix 5x5
for i in range(0, 5):  # looping the matrix to add every letter from 'letters_arr'
    for j in range(0, 5):
        table[i][j] = letters_arr[
            k]  # adding each letter in to matrix using 'i' and 'j' to point the index to add store letters from 'letters_arr' at 'k'
        k += 1  # increase k by 1 every round of the looping


def gen_key_matrix(key):  # This funtion creates the matrix 5x5 using input key from user
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # define possible letters that can be in the key table after the user key is added
    gen_key_matrix.table = [[0] * 5 for row in range(5)]  # define the 'gen_key_matrix.table' as 2D array 5x5
    key = re.sub(r'[\W]', '',
                 key.upper())  # read string from 'key' and turn them into UPPERCASE and pass new values to 'key'

    for row in range(5):  # outer loop at 5 times as 'row'
        for col in range(5):  # inner loop at 5 times as 'col'
            if len(key):  # do when length in key is TRUE
                gen_key_matrix.table[row][col] = key[
                    0]  # pass the value from 'key' at first index to gen_key_matrix.table at index row and col
                alphabet = alphabet.replace(key[0], '')  # remove the value in alphabet = key at first index
                key = key.replace(key[0], '', -1)  # replace '' at first index in key and length -1
            else:  # do this when no value left in 'key'
                gen_key_matrix.table[row][col] = alphabet[
                    0]  # pass the value from alphabet at first index to gen_key_matrix.table at index row and col
                alphabet = alphabet[1:]  # shift index of value in alphabet to the next one
    return gen_key_matrix.table  # return value to gen_key_matrix.table


def position(table, letter): # loop from 1 to 25 position to find the position of letter in table to compare with key table
    for row in range(5):
        for col in range(5):
            if table[row][col] == letter: # if found the position of letter return value of row and col
                return [row, col]
    return [row, col]


def encrypt(): # this function encrypt the input plaintext base on input key
    texts = str(input("Enter plaintext:")) # get user plaintext input as string
    gen_key_matrix(key)
    table = gen_key_matrix.table # define 'table' = 'gen_key_matrix.table'
    cipher = '' # set cipher = ''
    texts = re.sub(r'[\W]', '', texts.upper()) # read string from 'texts' and turn them into UPPERCASE and pass new values to 'key'
    text = '' # set text = ''

    for i in range(0, len(texts) - 1): # loop for length of 'texts' (number of plaintext)
        text += texts[i] # add letters to'text' at 'texts' index i
        if texts[i] == texts[i + 1]: # if value in text at i = value in text at i+1 (same letter occur in the same pair) then replace the letter at i+1 with X
            text += 'X'

    text += texts[i + 1] #get pair by take the next letter of plaintext

    print()

    for i in range(0, len(text), 2):
        pair = text[i:i + 2] #take the letters from 'text' at i and i+2 to 'pair'
        a, b = pair[0], 'X' # a = text at index i, b = 'X'
        if len(pair) > 1: # if 'pair' > 1 or has pairs
            b = pair[1]  # then 'b' from 'X' = that letter
        a = position(table, a) # call function position to find the position of 'a' in the key table
        b = position(table, b) # call function position to find the position of 'b' in the key table

        if (a[0] == b[0]): # if 'a' and 'b' are in same row
            if a[1] == 4 and b[1] != 4: # if letter in 'a' is at the back but b is not
                cipher += table[a[0]][(a[1] - 4)] + table[b[0]][(b[1] + 1)] # cipher will store letter at first index of its row
            elif b[1] == 4 and a[1] != 4: # if letter in 'b' is at the back but a is not
                cipher += table[a[0]][(a[1] + 1)] + table[b[0]][(b[1] - 4)] # cipher will store letter at first index of its row
            else: # if not match to conditions above but there are in same row
                cipher += table[a[0]][(a[1] + 1)] + table[b[0]][(b[1] + 1)] # cipher will store letter from 'a' and 'b' at their positions + 1
        elif (a[1] == b[1]):# if 'a' and 'b' are in same column
            if a[0] == 4 and b[0] != 4: # if letter in 'a' is at the bottom but b is not
                cipher += table[(a[0] - 4)][a[1]] + table[(b[0] + 1)][b[1]] # cipher will store letter at top of its column
            elif b[0] == 4 and a[0] != 4:# if letter in 'b' is at the bottom but b is not
                cipher += table[(a[0] + 1)][a[1]] + table[(b[0] - 4)][b[1]] # cipher will store letter at top of its column
            else:# if not match to conditions above but there are in same column
                cipher += table[(a[0] + 1)][a[1]] + table[(b[0] + 1)][b[1]]  # cipher will store letter from 'a' and 'b' at their positions + 1
        else: # if not == to any condition above mean that pair of plaintext is diagonal
            cipher += table[a[0]][b[1]] + table[b[0]][a[1]] #'cipher' will store letter at 'a' row and 'b' column, 'cipher' will store letter at 'b' row but 'a' column
    return cipher;

# this fuction is reverse way of encryption but I reduced condition by using "mod 5"  ex. if 'a'=0 and 'b'=1 are in same row and 'a' is at the front so a=(0-1)mod5 == 4, b=(1-1)mod5 == 0
def decrypt(): # this function decrypt the input encrypted message base on input key
    text = str(input("Enter decrypted message:")) # get input decrypted message from user
    gen_key_matrix(key)
    table = gen_key_matrix.table
    text = re.sub(r'[\W]', '', text.upper())
    texts = ''

    for i in range(0, len(text), 2):
        pair = text[i:i + 2]
        if len(pair) != 2:
            print('Please enter decrypted message')
            quit(-1)
        a, b = pair[0], pair[1]
        a = position(table, a)
        b = position(table, b)

        if a[0] == b[0]:
            texts += table[a[0]][(a[1] - 1) % 5] + table[b[0]][(b[1] - 1) % 5]
        elif (a[1] == b[1]):
            texts += table[(a[0] - 1) % 5][a[1]] + table[(b[0] - 1) % 5][b[1]]
        else:
            texts += table[a[0]][b[1]] + table[b[0]][a[1]]
    return texts


key = input("Enter your key :")  # getting user input into 'key'
key = key.replace(" ", "")  # remove space from 'key'
key = key.upper()  # turn letter in to UPPERCASE
gen_key_matrix(key)
ans = True  # set 'ans' as True
while ans:  # infinity loop to display selection menu using while loop
    print("""==Select Menu==
1.Encryption
2.Decryption
3.EXIT""")
    ans = input("Enter choice :")
    if ans == "1":
        message = encrypt()  # message = call function encrypt
        print("Your encrypted message is :", message,
              "\n")  # display encrypted message and return value of 'message' when ans = "1"
    elif ans == "2":
        message = decrypt()  # message = call function encrypt
        print("Your plaintext is :", message, "\n")  # display plaintext and return value of 'message' when ans = "2"
    elif ans == "3":
        break  # break the loop when ans = "3"
