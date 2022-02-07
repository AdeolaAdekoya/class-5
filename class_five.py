import random

data = {
   "3947758475": {
       "name": "desmond",
       "dob": "09-11-11",
       "bvn": "123456789",
       "pin": "1234",
       "bal" : 0
   }
}

print("welcome to astro bank app")
print("enter s to sign up or l to login")
choice = input(">").lower()

if choice == 'l':
    acc_num = input("enter your account number: \n>")
    pin = input("enter your account pin: \n>")

    user = data.get(acc_num)

    # the user exists
    if user and user['pin'] == pin:
        print(f"welcome {user['name']}. \n your account balance is ${user['bal']}")

        print("""what would you like to do ?
        press 1 to withdrawl
        press 2 to deposit
        press 3 to transfer
        press any other key to quit""")

        user_input = input(">")
# withdrawl
        if user_input == '1':
            amount = int(input("how much? \n>")) 
            if amount >= user["bal"]:
                print("insufficient funds")
            else:
                user["bal"]-=amount
                print("please take yout cash")
                print(f"balalnce is {user['bal']}")

# deposit
        elif user_input == '2':
              amount = int(input("how much? \n>")) 
    
              user["bal"]+=amount
              print("please take yout cash")
              print(f"balalnce is {user['bal']}")

        else:
            print("goodbye")
# transfer
        if user_input == '3':
            depositAcc = input("enter the account number you would like to trnasfer to \n")
            amount_Transfered = input("how much ? \n")
            pin = input("input your pin: \n")
            transfer = [("depositAcc", depositAcc),
                       ("amount_Transfered", amount_Transfered)]
   
   
   
    else:
        print("invalid login")


# sign up 

elif choice == "s":
    name = input("input your name: \n")
    dob = input("your date of birth: \n")
    bvn = input ("your bvn:\n ")
    pin = input("input your pin:  \n")
    details = [("name", name), 
                ("dob", dob),
                ("bvn", bvn), 
                ("pin", pin), 
                ("balance", 0)]
    num = [1,2,3,4,5,6,7,8,9,0]
    acc_num_list = [str(random.choice(num)) for _ in range(10)]

    acc_num = "".join(acc_num_list)
    
    data[acc_num] = dict(details)


else:
    print("invalid input")

print(data)


num = [1,2,3,4,5,6,7,8,9,0]

# random.shuffle(num)
print(random.choice(num))






# guess game

# ask the use to guess our number and be


# Trials = 3
# score = 0


# print("welcome to the game: \n" )



# num = [1,2,3,4,5,6,7,8,9,0]
# random.shuffle(num)



# for loop 

# trial = 3
# score = 0


# for i in range(100000000000):
#     if trial == 0:
#         print("game over")
#         print(f"your score is {score}")
#         break
#     choice = random.choice(num)    
#     play =  int(input("enter your number \n>"))

#     if play == choice:
#         trial +=1
#         score +=3
#         print("correct💕😊")
#         print("you have been given extra trial")
#         print("yayy🎉")
#     else:
#         trial -= 1
#         print("incorrect")
#         print(f"you have {trial} trials(s) left")

#  mr desmond while loop

# while trial != 0:
        
#     choice = random.choice(num)    
#     play =  int(input("enter your number \n>"))

#     if play == choice:
#         trial +=1
#         score +=3
#         print("correct💕😊")
#         print("you have been given extra trial")
#         print("yayy🎉")
#     else:
#         trial -= 1
#         print("incorrect")
#         print(f"you have {trial} trials(s) left")



# my answer while loop

# startgame = input("do you want to play a game: 1 (yes) 2(no)\n>")
# game = [1,2,3,4,5,6,7,8,9,0]
# com_choice = random.choice(game)
# if startgame == "1":
#     while Trials != 0:
#         key = int(input("guess a number between 1-10:\n>"))
#         if key == com_choice:
#             print(f"you have won, the answer is{com_choice} ") 
#             score+=1
#             Trials +=1
#             print(f"your score is {score}")
#         else:
#             Trials -=1        
#             print(f"Wrong answer, you have, {Trials} trials left")
#             print(f"Correct answer is {com_choice}")


# elif startgame == "2":
#     print("goodbye")




# print(score)

#lists
 

# chars = ["R", "P", "S"]
# choice = random.choice(chars)  



# # rock paper scissors game

# print("welcome to rock paper scissors")

# characters_data = input("select a character: R (Rock) P (Paper) S (Scissors) \n>")




