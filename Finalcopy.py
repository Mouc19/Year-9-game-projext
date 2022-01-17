import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Grabbing objects
friends= 0
flower = 0

required = ("\nUse only A, B, or C\n") #Cutting down on duplication

#The story is broken into sections, starting with "intro"
def intro():
  print ("Today is your first day of school more importantly it's your first day wearing wearing the hijab!"
  "Before leaving your mom kisses you goodbye, embarassed you say goodbye and go on your way to school"
  "On your way to school two kids point at your hijab and start laughing! what will you do ?")
  time.sleep(1)
  print ("""  A. Approach the boys and try to educate them about the hijab
  B. Find a near by rock and throw it at them
  C. shrug it off and ignore them""")
  choice = input(">>> ") #Here is your first choice.
  if choice in answer_A:
    option_rock()
  elif choice in answer_B:
    print ("\nWelp, that was quick. "
    "\n\nYou lost ! violence is never the solution!")
  elif choice in answer_C:
    option_run()
  else:
    print (required)
    intro()


def option_rock(): 
  print ("\n As you walk up to the boys you tell them that the hijab is an Hijab" 
  "is an Islamic concept of modesty and privacy, most notably expressed in women's"
  "clothing that covers most of the body, but instead of listening they call you"
  "silly names and run to school what will you do? ")
  time.sleep(1)
  print ("""  A. Think of a different way to mak them understand the hijab
  B. take matters into your own hands a fight them at school.
  C. ignore them and let them and go on with your day""")
  choice = input(">>> ")
  if choice in answer_A:
    option_run()
  elif choice in answer_B:
    print ("\nYou decided to throw fight them!" 
    " as if that would make them understand the"
    " concept of hijab and stop them from bullying"
    " other people! "
    "Violence is never the solution! \n\nYou lost!")
  elif choice in answer_C:
    option_cave()
  else:
    print (required)
    option_rock()

def option_cave():
  print ("\n Ever sice you started ignoring the bullies they"
  "kept on teasing you, your friends couldnt help but notice that"
  " and offered to help you stop the bullies. Will you take their"
  " help ? (Y/N) ? ")
  choice = input(">>> ")
  if choice in no:
    print(" you shoudlve accept their help now the bullies wont ever"
     "listen to you and will kept dirsrespecting cultures and religions!"
     "Helping eachother is a big part of equity ! \n\nYou lost!")
  else:
    friends = 1 #adds friends to the equation i could say
    print ("\nWhat will you do now that your "
    "friends are willing to helo you ?")
    time.sleep(1)
    print ("""  A. Tell a teacher
    B. Confront the bullies one more time in hopes that
    they will get intimated by you and your friends and hear what you have to say
    C. Run""")
    choice = input(">>> ")
    if choice in answer_A:
      print ("\n Although telling your teacher was the right thing "
      " you had no concrete evidence that they bullied you so they lied and said that they didnt "
      "good choice but...\n\n you lost!")
    elif choice in answer_B:
      if friends > 0:
        print("\nAfter school you and your friends talked to the bullies"
      "and to your surprise, they where scared, once again you explained"
      "to them hoe the Hijab is an Islamic concept of modesty and privacy"
      "which is most notably expressed in women's clothing that covers most of the body."
      "and they listned to everything in the end they sicerly apoligized and promised to"
      "Accept peoples religion and cultures. Will you accept their apologie? Y/N? ")
      choice = input(">>> ")
      if choice in yes:
        print("Aw shucks what a good person you are!... \n you win!!")
      else: #If the user didn't accept their apologies
        print ("cold but gold.... \n You win !")   
    elif choice in answer_C:
      print ("As the orc enters the dark cave, you sliently "
      "sneak out. You're several feet away, but the orc turns "
      "around and sees you running.")
      option_run()
    else:
      print (required)
      option_cave()


def option_run():
  print ("\nYou run as quickly as possible, but the orc's "
  "speed is too great. You will:")
  time.sleep(1)
  print ("""  A. Hide behind boulder
  B. Trapped, so you fight
  C. Run towards an abandoned town""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("You're easily spotted. "
    "\n\nYou died!")
  elif choice in answer_B:
    print ("\nYou're no match for an orc. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_town()
  else:
    print (required)
    option_run()
    
def option_town():
  print ("\nWhile frantically running, you notice a rusted "
  "sword lying in the mud. You quickly reach down and grab it, "
  "but miss. You try to calm your heavy breathing as you hide "
  "behind a delapitated building, waiting for the orc to come "
  "charging around the corner. You notice a purple flower "
  "near your foot. Do you pick it up? Y/N")
  choice = input(">>> ")
  if choice in yes:
    flower = 1 #adds a flower
  else:
    flower = 0
  print ("You hear its heavy footsteps and ready yourself for "
  "the impending orc.")
  time.sleep(1)
  if flower > 0:
    print ("\nYou quickly hold out the purple flower, somehow "
    "hoping it will stop the orc. It does! The orc was looking "
    "for love. "
    "\n\nThis got weird, but you survived!")
  else: #If the user didn't grab the sword
     print ("\nMaybe you should have picked up the flower. "
     "\n\nYou died!")

intro()