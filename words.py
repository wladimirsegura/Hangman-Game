import collections
from random import randint
import tkinter as tk


animals=['tiger', 'alpaca', 'albatross','penguin','alligator','dolphin','bulldog', 'elephant',  'shepherd','camel', 'barracuda', 'shark','terrier','buffalo', 'butterfly', 'capybara','catfish','cheetah','centipede','chicken','chihuahua','crocodile','donkey','dragonfly','eagle','gorilla','falcon','flamingo','squirrel','panda','giraffe','grasshopper','greyhound','hamster','hippopotamus','horse','monkey','whale','hyena','impala','rhinoceros','iguana','jackal','jaguar','kangaroo','koala','leopard','lamprey','lemming','lobster','lynx','lion','bear','lungfish','llama','lizard','rabbit','mouse','octopus','oyster','parrot','pelican','piranha','poodle','turtle','seagull','salamander','sardines','sheep','sparrow','starfish','stingray','swan','duck','turkey','toucan','tortoise','wolverine','zebra','shrimp','seahorse','scorpion','salmon','raccoon','panther','hummingbird','gopher','chameleon','bison','armadillo']


# check for double entry
# print(animals)
# wc = collections.Counter(animals)
# for word, count in wc.items():
#     if count > 1:
#         print(word, count)

hit_word = animals[randint(0,len(animals)-1)].upper()
print(hit_word)

window= tk.Tk()
title = tk.Label(
    text='Welcome to Hangman Game !!',
    fg='white',
    bg='#34A2FE',
    width=100,
    height=3
    )
button = tk.Button(
    text="A",
    width=2,
    height=2,
    bg="blue",
    fg="yellow",
)
entry= tk.Entry(
    fg='yellow',
    bg='blue',
    width=20
)

# make keyboard
keyboard = [('q','w','e','r','t','y','u','i','o','p'),('a','s','d','f','g','h','j','k','l'),('z','x','c','v','b','n','m')]
print(keyboard) 
for r in range(3):
    for l in range(len(keyboard[r])):
        print(r,keyboard[r][l])
for i in range(3):
    for j in range(len(keyboard[i])):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1,
            padx=5
        )
        frame.grid(row=i,column=j*4+i,padx=2,pady=2,columnspan=4)        
        label= tk.Label(master=frame, text=keyboard[i][j].upper())
        label.pack()



window.mainloop()