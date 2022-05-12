from src import controller

"""
mylist = []
for ask in range(4):
    mylist.append(int(input("Please enter a number:")))
for number in mylist:
    print(number)
mylist[0], mylist[3] = mylist[3], mylist[0]
print(mylist)
"""

def main():
    #pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
    game=controller.Controller()
    game.mainloop()
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

main()
