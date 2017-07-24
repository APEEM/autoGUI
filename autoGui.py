#import modules
import pyautogui as auto
import pickle

auto.PAUSE = 1
auto.FAILSAFE = True



print("\n", "Welcome to autoGUI. This program will alow you to automate".center(80), "anything you can do with the mouse or keyboard.".center(80),"\n", "To cancel the program, move the mouse to the top left".center(80), "corner of the screen".center(80))

#This is the class used in each step of the program
class automate:
    
    location = 0 #stores location for movement function
    duration = 2 #the duration in seconds for the mouse to move locations
    message = 'print' #the default message for the type function
    move = 0     #uses the move function when value is changed to 1
    click = 0    #uses the click function when value is changed to 1
    pri = 0      #uses the print function when value is changed to 1
    enter = 0    #uses the enter function when the value is changed to 1 
    
    #this definition contains all the functions 
    def doStuff(self):
        if self.move == 1:
            auto.moveTo(self.location, duration = self.duration)
            
            
        elif self.click == 1:
            auto.click()
            
        elif self.pri == 1:
            auto.typewrite(self.message, interval = .1)
            print(self.message)
                
        elif self.enter == 1:
            auto.hotkey('enter')
            

#this variable will contain all the step objects    
step = []        

rs = 0 #variable used to initiate the loading a saved profile
  
#This loop alows the user to enter multiple steps
while True:
    
    step.append(automate()) #creates a new object for each step at the begining of the loop
    
    x = input('What would you like to do with this step: \n1=set location \n2=left click, \n3=type a message, \n4=hit enter, \ns=save steps, \nrs= Run saved steps, \n9=runs steps\n')
    
    
    #this if block changes the variables in the object to determin which function is run
    if x == '1':
        step[len(step) - 1].location = auto.position()
        step[len(step) - 1].move = 1
        print(step[len(step) - 1].location)
    
    elif x == '2':
        step[len(step) - 1].click = 1
    
    elif x == '3': 
        step[len(step) -1].message = input('Enter a message to print: ')
        step[len(step) - 1].pri = 1
    
    elif x == '4': 
        step[len(step) - 1].enter = 1

    elif x == 's':
        with open('company_data.pkl', 'wb') as output:
            for g in range(len(step)-1):
                pickle.dump(step[g], output, pickle.HIGHEST_PROTOCOL)
                
    elif x == 'rs':
        rs = 1
        break
        
            
    #breaks the loop when the user wants to run the steps         
    elif x == '9':
        break

    else:
        print('Please select a valid option')
        
if rs !=1:        
    l = input('How many times would you like these steps to run?\n') or '1'


while True and rs != 1:    
    for n in range(int(l)): #determines how many times the steps are run
        for i in range(int(len(step) - 1)): #this loop call each step object sequentially
            print("Step:", i + 1,",", "Loop count:" , n+1, ",", "Move: ", step[i].move,",", "Click: ", step[i].click,",", "print: ", step[i].pri,",", 'enter: ', step[i].enter )
            step[i].doStuff() 
    br = input('Would you like to run the steps again: y/n')
    if br == 'n':
        break

#used to run saved profile
if rs == 1:
    redo = input('How many times would you like these steps to run?\n' ) or 1
    input('Press enter to start saved profile\n')
    for q in range(int(redo)):
      
        stepsFromSaved = []
        b = 0
        with open('company_data.pkl', 'rb') as i:
            while True:
                    
                stepsFromSaved.append(None)
                try:
                    stepsFromSaved[b] = pickle.load(i)
                except EOFError:
                       break
                b += 1
                    
            for g in range(len(stepsFromSaved) - 1):
                stepsFromSaved[g].doStuff()

    
    
input('Pres enter to exit')

