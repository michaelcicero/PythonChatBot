# # - * - coding: utf-8 - * -
""" Eliza homework """
_author_="Michael Cicero"

import re

#find bye function

def findBye(a): 
    if(re.findall(r'bye', curInp, re.IGNORECASE)):
         print("It was nice speaking with you. Goodbye")
         quit()

#find ed function

def findEd(b):
    l = b.split(" ")

    for ed in l:
        if(re.findall('ed$', ed)):
            return ed

#get name

print("Greetings. I'm chatbot. Can you remind me of your name?")
name = input()
curInp = name
findBye(curInp)
if(re.findall(r'(i am)|(my name is)', curInp, re.IGNORECASE)):
     name = re.sub(r'([iI] am)|([mM]y name is)',"", curInp)
   
while len(name) == 0:
    print("What is your name?")
    name = input()
    curInp = name
    findBye(curInp)

#how are you

print("Hello " + name + "! How are you doing today?")
hay = input()
curInp = hay
if(re.findall(r'([you?]{4})', curInp, re.IGNORECASE)):
    print("Don't worry about me. I am more interested in hearing about you. I'll be asking the questions from now on.")

while len(hay) == 0:
    print("Sorry, I couldn't hear you. How are you doing today?")
    hay = input()
    curInp = hay

findBye(curInp)

#while loop containing all further checks

while True: 
    if(re.findall(r'(ok|alright|fine|not bad|not too bad)',curInp, re.IGNORECASE)):
        print("I'm glad you are feeling ok. Why aren't you good?")
        curInp = input()
        findBye(curInp)
        if(bool(re.search("ed", curInp))):
            edMatch = findEd(curInp)
            print("why did it " + re.sub("ed", "",edMatch) + "?")
            curInp = input()
            findBye(curInp)
         
    elif(re.findall(r'(sad|depress|sick|unwell|bad|poor|not well|not very well|not good|not very good|not great)',curInp, re.IGNORECASE)):
        print("I'm sorry you arent feeling well. Why haven't you been feeling well?")
        curInp = input()
        findBye(curInp)
        if(bool(re.search("ed", curInp))):
            edMatch = findEd(curInp)
            print("why did it " + re.sub("ed", "",edMatch) + "?")
            curInp = input()
            findBye(curInp)
       
    elif(re.findall(r'(good|great|excellent|superb|wonderful|extraordinary|well|happy|joy)',curInp, re.IGNORECASE)):
        print("Wonderful, I'm glad you're good. Why are you so good?")
        curInp = input()
        findBye(curInp)
        if(bool(re.search("ed", curInp))):
            edMatch = findEd(curInp)
            print("why did it " + re.sub("ed", "",edMatch) + "?")
            curInp = input()
            findBye(curInp)
        
    elif(re.findall(r'(mom|mother|mommmy|momma)',curInp, re.IGNORECASE)):
        print("Tell me more about your mother.")
        curInp = input()
        findBye(curInp)
        if(bool(re.search("ed", curInp))):
            edMatch = findEd(curInp)
            print("why did it " + re.sub("ed", "",edMatch) + "?")
            curInp = input()
            findBye(curInp)
    
    elif(re.findall(r'(friend|bud|pal)',curInp, re.IGNORECASE)):
        print("Tell me more about your friend.")
        curInp = input()
        findBye(curInp)
        if(bool(re.search("ed", curInp))):
            edMatch = findEd(curInp)
            print("why did it " + re.sub("ed", "",edMatch) + "?")
            curInp = input()
            findBye(curInp)
        
    elif(re.findall(r'(dad|father|daddy)',curInp, re.IGNORECASE)):
        print("Tell me more about your father.")
        curInp = input()
        findBye(curInp)
        if(bool(re.search("ed", curInp))):
            edMatch = findEd(curInp)
            print("why did it " + re.sub("ed", "",edMatch) + "?")
            curInp = input()
            findBye(curInp)
              
    elif(re.findall(r'(brother|bro)',curInp, re.IGNORECASE)):
        print("Tell me more about your brother.")
        curInp = input()
        findBye(curInp)
        if(bool(re.search("ed", curInp))):
            edMatch = findEd(curInp)
            print("why did it " + re.sub("ed", "",edMatch) + "?")
            curInp = input()
            findBye(curInp)
          
    elif(re.findall(r'(sister|sis)',curInp, re.IGNORECASE)):
        print("Tell me more about your sister.")
        curInp = input()
        findBye(curInp)
        if(bool(re.search("ed", curInp))):
            edMatch = findEd(curInp)
            print("why did it " + re.sub("ed", "",edMatch) + "?")
            curInp = input()
            findBye(curInp)

    else:
        print("Intresting, mind telling me a bit more about this?")
        curInp = input()
        findBye(curInp)
        if(bool(re.search("ed", curInp))):
            edMatch = findEd(curInp)
            print("why did it " + re.sub("ed", "",edMatch) + "?")
            curInp = input()
            findBye(curInp)
            
        
    
        