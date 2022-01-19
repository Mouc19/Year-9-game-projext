from random import choice
import time #Imports a module to add a pause
import art
#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]


friends= 0
principalhelp = 0
required = ("\nUse only A, B, or C\n") #Cutting down on duplication
win = art.text2art("YOU WIN !!")
lose = art.text2art("YOU LOSE !")
#The story is broken into sections, starting with "intro"

def intro():
  print ("welcome to the blue brightest!")
  name = input("Please Type your name: ")
  welcome= art.text2art("welcome " + name)
  print (welcome)

  userfeeling = input("how are you feeling today? good or bad ? : ") 
  if "good" in userfeeling.lower():
     print ("That's great I hope you keep feeling that way ! ")
  if "bad" in userfeeling.lower():
    print ("im sorry you feel that way.. I hope you feel better by the end of this game... that is.. if you win of course! ")
  else: 
     print (" I hope you feel better by the end of this game... that is.. if you win of course!")

  print ("\nAre you ready to start this game? yes or no ?"
  " (tip: the game will start regardless of your answer so.. press yes!)")
  choice = input(">>> ")
  if choice in yes:
   print("\nGood choice! The game will start in")  
  time.sleep(1)
  print ("3")
  time.sleep(1)
  print ("2")
  time.sleep(1)
  print ('1')
  time.sleep(1)
  print 
  intro2 ()

def intro2 ():
  print ("\nToday is your first day of school, more importantly it's your first day wearing wearing the hijab!"
  " Before leaving your mom kisses you goodbye, "
   "\n embarassed you say goodbye and go on your way to school."
  " On your way to school two kids point at your hijab and start laughing! What will you do ?")
  time.sleep(2)
  print ("""  A. Approach the boys and try to educate them about the hijab
  B. Find a near by rock and throw it at them
  C. Run back home and tell your mom""")
  choice = input(">>> ") #Here is your first choice.
  if choice in answer_A:
    option_bullyencounter()
  elif choice in answer_B:
    print ("\nWelp, that was quick. "
    "\n\n violence is never the solution!" + lose)
  elif choice in answer_C:
    option_runhome()
  else:
    print (required)
    intro2 ()

def option_bullyencounter(): 
  print ("\n As you walk up to the boys you tell them that the hijab is an " 
  "is an imporant piece of clothing in your religion that covers your hair,"
  " but instead of listening they\n call you silly names and run to school "
   "what will you do? ")
  time.sleep(1)
  print ("""  A. Run home and tell your mom
  B. Take matters into your own hands a fight them at school.
  C. Ignore them and be the bigger person""")
  choice = input(">>> ")
  if choice in answer_A:
    option_runhome()
  elif choice in answer_B:
    print ("\nYou decided to fight them!" 
    " as if that would make them understand the"
    " concept of hijab and stop them from bullying"
    " other people! Violence is never the solution! \n\n\n"+ lose)
  elif choice in answer_C:
    option_friendhelp()
  else:
    print (required)
    option_bullyencounter

def option_friendhelp():
  print ("\n Ever sice you started ignoring the bullies they"
  " kept on teasing you, your friends saw that"
  " and offered to help you stop the bullies. Will you accept their"
  " help ? \n (Y/N) ? ")
  choice = input(">>> ")
  if choice in no:
    print(" you shoudlve accept their help now the bullies wont ever"
     "listen to you and will kept dirsrespecting cultures and religions!"
     "Helping eachother is a big part of equity ! \n\n" + lose)
  else:
    friends = 1 #adds friends to the equation I could say
    print ("\nWhat will you do now that your "
    "friends are willing to help you ?")
    time.sleep(1)
    print ("""   A. Tell a teacher
    B. Confront the bullies one more time in hopes that
    they will get intimated by you and your friends and hear what you have to say
    C. Run home and tell your mom""")
    choice = input(">>> ")
    if choice in answer_A:
      print ("\n Although telling your teacher was the right thing "
      " you had no real evidence that they bullied you so they lied and said that they didnt.  " 
      " Unfortunately justice wasn't served "
      "good choice but...\n\n " + lose)
    elif choice in answer_B:
      if friends > 0:
        print("\nAfter school you and your friends talked to the bullies"
      " and to your surprise, they where intimidated by you and your friends. After you explained"
      " to them that the Hijab is an important piece of clothing in your religion" 
      "This time they listened until you finished talking and they sincerly apoligized and promised to"
      " accept peoples religion and cultures. Will you accept their apologie? Y/N? ")
      choice = input(">>> ")
      if choice in yes:
        print("Aw shucks what a good person you are!... \n" + win)
      else: #If the user didn't accept their apologies
        print ("Cold but Gold.... \n" + win)   
    elif choice in answer_C:
      option_runhome()
    else:
      print (required)
      option_friendhelp()


def option_runhome():
  print ("\nYou run back home and tell your mom about the bullies."
  " After that your mom tells you, if you dont want to wear the hijab you dont have to"
  " but after you see your\n little sister sad that people are bullying you because of your hijab" 
  " you decide to be brave and go to school. After you go back to school you see the"
  " bullies\n  what will you do ?")
  
  time.sleep(1)
  print ("""  A. Make fun of them and start bullying them
  B. Scream and tell them to stop
  C. Talk to the principal""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("doing the same thing they did to you does not make it right! "
    "\n\n" + lose)
  elif choice in answer_B:
    print ("\n Screaming on them only makes them want to bother you more!! "
    "\n\n" + lose)
  elif choice in answer_C:
    option_principalhelp()
  else:
    print (required)
    option_runhome()
    
def option_principalhelp():
  time.sleep(1)
  print ("\n Although there was no evidence your principal was "
  " determined to help you, he said he thought that it is really "
  "important for students to be able to respect cultures\n since "
  "the school is really diverse "
  " Will you accept his help Y/N ?\n")
  choice = input(">>> ")
  if choice in no:
    print ("The principal was willing to help you and you declined!!" + lose )
    print ("And you desrved to!")
  else:
    principalhelp = 1 #adds principal to equation
  print ("what will you do now that the principal"
  " wants to help you?\n")
  time.sleep(1)
  print ("""A. Suspend the bullies for three days
    B. Organize a presentation for the whole school
    including the bullies speaking about respecting 
    cultures and religions 
    C. Ask the principal to switch classes so you wont be with the bullies""")
  choice = input(">>> ")
  if choice in answer_A:
      print ("\n You got revenge.... but at what cost ? the bullies wont learn"
      " anything from a three day suspension\n\n " + lose)
  elif choice in answer_B:
      if principalhelp > 0:
        print("\n After hearing your idea the principal loved it and agreed to do the presentation."
        " the following day after the presentation\n the bullies appologized for disrespectingyour religion"
        "and promised to never do it again. Will you accept their apologie ?")
      choice = input(">>> ")
      if choice in yes:
        print("Aw shucks what a good person you are!... \n" + win)
      else: #If the user didn't accept their apologies
        print ("Cold but Gold.... \n" + win)   
  elif choice in answer_C:
    print("you got rid of the bullies but they didnt learn anything"
    " just because you got rid of the bullies that doesn't mean they won't bully"
    " someone else. Good try but" + lose)

intro()

