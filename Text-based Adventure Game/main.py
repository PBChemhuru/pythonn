import random
import time

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]
sword = 0
eric = 0
required = "\nUse only A, B, or C\n"


def dice():
    mini = 1
    maxi = 6
    roll = random.randint(mini, maxi)
    print("you rolled a " + str(roll) + ".")
    return roll


def intro():
    print(
        "So the story begins in with you enjoying the warmth of your fireplace in your cottage. "
        "\nThe wind blows furiously outside,winter is beginning to pick up and most people have been holed up in their "
        "home. "
        "\nAs you watch the flame consume the firewood your tranquility is disturbed by a knock at your door."
        "\nThis catches you by surprised as you don't usually get guests,as your house is located on the outskirts "
        "of the town and you have a reputation of not being the most hospitably.\nYou rise from your seat wondering "
        "what you should do.")
    time.sleep(1)
    print("""  A. Grab your sword and answer the door
  B. Ignore the door
  C. Peek through the curtain and see who it is""")
    choice = input(">>> ")
    if choice in answer_A:
        option_armed()
    elif choice in answer_B:
        option_ignore()
    elif choice in answer_C:
        option_peek()


def option_armed():
    sword == 1
    print("Sword in hand you answer the door with your usually scowl.You see a child panting hard he looks up "
          "to you panic in his eyes \n 'Are your Northern hermit' you give me a nod and his panic turns to hope "
          "'Please save my mommy,bad men came and they trying to  take her away'"
          "\n'Go ask the city guards to help you kid i cant do anything for you' you wave him off"
          "\n'Please mommy says you are strong and that you used to be in the army' tears start streaming down his face"
          "'Mommy is the only family i have left if i lose her then i will be all alone' his knees buckle and he "
          "falls to his knees in the snow.\nYou sigh scratching your head,what do you do?")
    time.sleep(1)
    print("""  A. Go with child immediately
  B. Let the child inside the house and find out more
  C. Refuse and close the doors""")
    choice = input(">>> ")
    if choice in answer_A:
        option_house()
    elif choice in answer_B:
        option_home()
    elif choice in answer_C:
        option_ignore2()


def option_ignore():
    print("You ignore the continuous knocking and eventually it stops,clearly who ever it was got bored and moved on"
          "\nWELL THAT'S GAME OVER,NOTHING CHANGES IF YOU DO NOTHING.")


def option_peek():
    print("You look through window by the door peeling the curtain back a bit and see a child.He knocks on the door "
          "and looks around almost as if he is on the look out for someone chasing him.What do you do?")
    time.sleep(1)
    print("""  A. Open the door for him
  B. ignore the door""")
    choice = input(">>> ")
    if choice in answer_A:
        option_house()
    elif choice in answer_B:
        option_ignore2()


def option_house():
    print("You follow the child to what you believe to be their home and unsurprisingly you find it in shambles the "
          "homes didn't seem to have much but what ever little they had in their humble home is broken and in "
          "shambles.\nThe home has been ransacked but the perpetrators are gone adn the house is "
          "lifeless.\n'Mommy!'the boy calls out running into the house searching for his mother'\nYou step out of the "
          "home and stop a homeless man near by you walk over to and ask him if he has seen what happen but he "
          "refuses to comply ,you figure he is hoping to make a quick coin off of you.\nWhat do you do?")
    time.sleep(1)
    print("""  A. Threaten him
  B. Find clues in the house""")
    choice = input(">>> ")
    if choice in answer_A:
        option_threaten()
    elif choice in answer_B:
        option_clues()


def option_ignore2():
    print("You ignore the continuous knocking and pleads of the child and eventually it stops.You carry your night "
          "unbothered by it all "
          "\nWOW YOU HAVE NO HEART WHAT SO EVER.ARE YOU EVEN HUMAN?.ANYWAY GAME OVER.")


def option_threaten():
    if sword == 1:
        print("You draw your sword putting it up to his neck 'if you don't want to lose your heard i suggest you "
              "start speaking before you lose your head' under the influence of your encouragement the man begins to "
              "talk.\nYou find out that the child's mother had being taken by the local gang that harass some of the "
              "local townspeople.You sigh you really don't want to get involved with the local gang but you have "
              "already come this fun you might as well see it through.Rising to your feet you sheathed your sword you "
              "know where the gangs hang out and know its dangerous.\nWill you bring the child with you?")
        time.sleep(1)
        print("""  A. Take him with you
        B. Leave him them""")
        choice = input(">>> ")
        if choice in answer_A:
            eric == 1
            option_team()
        elif choice in answer_B:
            option_solo()
    elif sword == 0:
        rol = dice()
        if rol > 2:
            print("You succeeded in persuading the man"
                  "\nYou find out that the child's mother had being taken by the local gang that harass some of the "
                  "local townspeople.You sigh you really don't want to get involved with the local gang but you have "
                  "already come this fun you might as well see it through.Rising to your feet you sheathed your sword "
                  "you "
                  "know where the gangs hang out and know its dangerous.\nWill you bring the child with you?"
                  )
            time.sleep(1)
            print("""  A. Take him with you
              B. Leave him them""")
            choice = input(">>> ")
            if choice in answer_A:
                option_team()
            elif choice in answer_B:
                option_solo()
        else:
            print("Your threats fails and the man refuses to say anything else")
            option_clues()


def option_clues():
    print("You return to the ransacked and start looking for clues but unfortunately you are no tracker and are "
          "unable to find anything.Without any clues you have no choice to give up the pursuit")
    print("Game Over,Nice try but that is as far a you go")


def option_team():
    print("You walk with eric to the den of the gangster as you get closer you take this moment to decide how you are "
          "gonna approach you.")
    print("""  A. Draw you sword and enforce justice
      B. Try talk to the gangsters
      """)
    choice = input(">>> ")
    if choice in answer_A:
        rol = dice()
        if rol > 3:
            print("eric saves you")
        else:
            print("you died")
    elif choice in answer_B:
        rol = dice()
        if rol > 5:
            print("you convince them to let go eric mother")
        else:
            print("you died")


def option_solo():
    rol = dice()
    if rol > 4:
        print("you survive solo But eric's mother does not survive ")
    else:
        print("you died")


def option_home():
    print("You have the child come inside and sit him down and explain in which you find out his name is Eric .He "
          "tells you of how a group of men have been coming to his home regularly and normalLy they go away but it "
          "seemed today they didn't just leave they decided both Eric and his mother would come with them,his mother "
          "fought back and Eric managed to escape and came here for help.")

    print("\nAs you listen to him a sharp knock cuts the boy off and you proceeded to answer the door and see rough "
          "looking lad he looks at you annoyed"
          "\n'Oi the kid is here isn't he hand him over id you don't want trouble' he flick out a knife."
          "\nWhat do you do?")
    time.sleep(1)
    print("""  A. Disarm him
              B. Lie to him""")
    choice = input(">>> ")
    if choice in answer_A:
        option_disarm()
    elif choice in answer_B:
        option_lie()


def option_disarm():
    rol = dice()
    if rol > 3:
        print("You succeeded"
              "\nYou find out that the child's mother had being taken by the local gang that harass some of the "
              "local townspeople.You sigh you really don't want to get involved with the local gang but you have "
              "already come this fun you might as well see it through.Rising to your feet you sheathed your sword "
              "you "
              "know where the gangs hang out and know its dangerous.\nWill you bring the child with you?"
              )
    else:
        print()


def option_lie():
    print("he stabs you died")


intro()
