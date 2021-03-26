##################################
#        WELCOME  MESSAGE        #
##################################
import time
import sys
money = 0
DL = 10
wage = 5
gender = "Male"


def req_name(msg):
    try:
        return raw_input(msg)
    except NameError:
        return input(msg)


name = req_name("""Hello! What's your name?
""")
while True:
    try:
        response = str(
            input("""
        What is your gender? : M, F, O
        """))
    except ValueError:
        print("Please answer with M, F, Or O.")
        continue
    if str(response) == "M":
        gender = "Mr."
        break
    elif str(response) == "F":
        gender = "Ms."
        break
    elif str(response) == "O":
        gender = ""
        break
    else:
        print("This is not an option!")
        continue

###WELCOME WITH NAME###
print()
time.sleep(.01)
print(
    '#######################################################################')
time.sleep(.01)
print(
    '#    [=====]     [=]         [=]    [=============]   [==========]    #')
time.sleep(.01)
print(
    '#    [=]    [=]    [=]     [=]            [=]         [=]             #')
time.sleep(.01)
print(
    '#    [=]    [=]      [=] [=]              [=]         [=]             #')
time.sleep(.01)
print(
    '#    [=======]         [=]                [=]         [======]        #')
time.sleep(.01)
print(
    '#    [=]    [=]        [=]                [=]         [=]             #')
time.sleep(.01)
print(
    '#    [=]    [=]        [=]                [=]         [=]             #')
time.sleep(.01)
print(
    '#    [======]          [=]                [=]         [==========]    #')
time.sleep(.01)
print(
    '#                                                                     #')
time.sleep(.01)
print(
    '#    [======]       [========]      [=============]   [==========]    #')
time.sleep(.01)
print(
    '#    [=]     [=]    [=]    [=]      [=]               [=]             #')
time.sleep(.01)
print(
    '#    [=]     [=]    [=]    [=]      [=]               [=]             #')
time.sleep(.01)
print(
    '#    [========]     [========]      [=============]   [======]        #')
time.sleep(.01)
print(
    '#    [=]     [=]    [=]    [=]                  [=]   [=]             #')
time.sleep(.01)
print(
    '#    [=]     [=]    [=]    [=]                  [=]   [=]             #')
time.sleep(.01)
print(
    '#    [=======]      [=]    [=]      [=============]   [==========]    #')
time.sleep(.01)
print(
    '#######################################################################')
time.sleep(.01)
print(
    '                           By Andrew Guernsey                          ')
time.sleep(.01)
print()
print('Hello! And welcome to ByteBase! How may we help you,' + str(name) + "?")
print("")
print("1 - Apply for a job at ByteBase!")
print("")
###OPTION START###
while True:
    try:
        response = int(input("""Please respond with the following: '1' : """))
    except ValueError:
        print("Sorry, I didn't understand that.")
        print("")
        continue
    if not response == 1:
        print("This is not a choice!")
        print("")
        continue
    else:
        break
print("")
print(
    "You sent a job application to ByteBase. It was short and stupid. It read..."
)
resume = str(input(str(gender) + " " + str(name) + """, Application:
"""))
print("")
###OPTION END###
print("""Nobody Cared to read your application,
However one of the interns of this badly organized company got you accepted in!
You now Begin your first day at work...
""")
wage += 10
print("")
print("")
input("Press Enter To Continue...")
# DAY END SEQUENCE # -Start
print("")
print("     DAY ONE:")
money += wage
time.sleep(.5)
print("Money......$" + str(money))
time.sleep(.5)
print("Name......." + str(name))
time.sleep(.5)
print("Days Left.." + str(DL))
time.sleep(.5)
print("Wage......." + str(wage))
time.sleep(1)
input("Press Enter To Continue...")
time.sleep(1)


# DAY END SEQUENCE # -End
def credits():
    print("""













           CREDITS:





















    """)
    time.sleep(.5)
    print("""













           CREDITS:
   Andrew Guernsey-




















    """)
    time.sleep(.5)
    print("""













           CREDITS:
   Andrew Guernsey-EVERYTHING




















    """)
    time.sleep(3)
    print("""













   THE END




















    """)
    time.sleep(2)
    print("That's all folks!")
    sys.exit("Credits.end")


print(
    "You start your day at work. Once you make it to your cubicle you find you now have Three options."
)
print("1 : Begin your job")
print("2 : Ask for a promotion")
print("3 : Quit your job")
#  OPTION START  #
promo1 = 0
while True:
    try:
        response = int(
            input(
                """Please respond with one of the following: '1, 2, 3' : """))
    except ValueError:
        print("(!)Please Enter A Number(!)")
        print("")
        continue
    if int(response) == 1:
        print(
            """You begin your custodial work. As you grab your mop you think in your head, "Minimum Wage! fun..." """
        )
        break
    elif int(response) == 2:
        if int(promo1 >= 3):
            print("")
            print(
                "Your boss got so annoyed at you asking for promos that he fired you."
            )
            time.sleep(6)
            print("")
            credits()
        else:
            print(
                """You go up to your boss, but before you even step in his office he says "No." """
            )
            print("")
            promo1 += 1
            continue
    elif int(response) == 3:
        print("")
        print("You quit your job. Everyone is dissapointed.")
        time.sleep(5)
        credits()
#  OPTION END  #
time.sleep(5)
print("cleaning.")
time.sleep(.3)
print("cleaning..")
time.sleep(.3)
print("cleaning...")
time.sleep(.3)
print("cleaning..")
time.sleep(.3)
print("cleaning.")
time.sleep(.3)
print("cleaning..")
time.sleep(.3)
print("cleaning...")
time.sleep(.3)
print("")
print(
    "You turn the corner as you finish cleaning the basement. There's something peculiar there. Should you investigate? It's got a door labeled [REDACTED] What do you do?"
)
time.sleep(1)
## OPTION START ##
while True:
    try:
        response = int(
            input("""
        1 - Enter the room
        2 - Leave it for another day
        3 - Ask your boss about it

        Answer : """))
    except ValueError:
        print("(!)Please Enter A Number(!)")
        print("")
        continue
    if int(response) == 1:
        print(
            "You walk into the room. Something of an alarm goes off and it appears as if you are trapped. A little while later a squad of people come down. They hold up a brick of electronics, point it at your head, and your mind goes black."
        )
        input("""
        Press enter to continue
        """)
        print(
            "You wake up in a dark room. You are cuffed to a chair which is chained into the ground. There are cameras in the room with a speaker."
        )
        time.sleep(.1)
        input("""
        Press enter to continue
        """)
        print(
            "Someone behind that speaker asks you how you got into that room. You say you were simply cleaning and went through that door to finish the job. You hear muffled arguing from the speaker"
        )
        input("""
        Press enter to continue
        """)
        print(
            """The speaker talks again, saying, "Are you sure you saw a door?" """
        )
        while True:
            try:
                response = int(
                    input("""
        1 - Yes
        2 - No
        """))
            except ValueError:
                print("(!)Please Enter A Number(!)")
                print("")
                continue
            if int(response) == 1:
                break
            elif int(response) == 2:
                print(
                    """You say, What door? and the speaker blares again, talking to other people, "Well, that wraps that up!" and you hear the hiss of gas from somewhere in the room as your mind goes black... """
                )
                input("""
                Press enter to continue
                """)
                credits()
            else:
                print("This is not an option!")
                continue
    elif int(response) == 2:
        print(
            "You decide you are interested in the prospect of exploring this unmarked area, but you have a job to do, and you would rather have time to think about it as well."
        )
        break
    elif int(response) == 3:
        print(
            "You tell your boss about it. He says not to go in there. You decide to listen because you just got this job and need to make a good first impression."
        )
        time.sleep(3)
        # DAY END SEQUENCE # -Start
        print("")
        print("     DAY TWO:")
        print(
            "For staying loyal to your employer and keeping out of that room, you were given a 5$ pay raise!"
        )
        wage += 5
        money += wage
        time.sleep(.5)
        print("Money......$" + str(money))
        time.sleep(.5)
        print("Name......." + str(name))
        time.sleep(.5)
        print("Days Left.." + str(DL))
        time.sleep(.5)
        print("Wage......." + str(wage))
        time.sleep(1)
        input("Press Enter To Continue...")
        if gender == "Ms.":
            while True:
                try:
                    response = int(
                        input("""
                    There has been a strike on sexism in the industry. Seeing as you are female, you might want to help fight this. Should you join the union?
                    
                    1 - Yes
                    
                    2 - No
                    """))
                except ValueError:
                    print("(!)Please Enter A Valid answer(!)")
                    print("")
                    continue
                if int(response) == 1:
                    print("""
                    You help fight the inequality, and eventually the group sues for lost wages due to sexism. They win and you recieve 25$ for your efforts
                    """)
                    money += 25
                    break
                elif int(response) == 2:
                    print("""
                    You go home waiting for it to all blow over, but eventually the company fires all in close relationship with the union, and apparently that includes you. Maybe if you'd been there there would have been a different outcome, but oh well.
                    """)
                    time.sleep(3)
                    input("Press enter to continue")
                    credits()
                else:
                    print("(!)Please Enter A Valid answer(!)")
    else:
        print("This is not an option!")
# DON'T GO PAST HERE! FINISH THE TOP FIRST!
credits()
