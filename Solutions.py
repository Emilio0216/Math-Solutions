# √ for later
#imports
import math, time
from time import sleep

#Helper functions
def Question(Answer_Type, Question_Text = "I NEED TO RESET THIS TEXT", Fail_Text = "That is not a valid answer. Please try again.", Text_Time = 0.02):
    Text_Scroll_Effect(Question_Text, Text_Time, True)
    while True:
        Answer = input()
        #probably a better way to do this but im lazy
        try:
            Correct = Answer_Type(Answer)
            break
        except ValueError:
            Text_Scroll_Effect(Fail_Text, .01)
    print('')
    return Correct
def Text_Scroll_Effect(Text, Time, Question = False):
    for char in Text:
        print( char, end='')
        sleep(Time)
    if Question == False:
        print('')
#Math functions
def Intial_Velocity_And_Angle(Intial_X_Velocity, Intial_Y_Velocity):
    # i hate radians with a passion
    Intial_Velocity = ((Intial_X_Velocity ** 2) + (Intial_Y_Velocity ** 2)) ** .5
    Angle = Intial_Y_Velocity / Intial_Velocity
    Angle_Degrees = math.asin(Angle) * (180.0 / math.pi)
    return Intial_Velocity, Angle_Degrees
def Quadratic_Solution(a, b, c):
    Divider = 2 * a
    Before_Root = (b**2) + (-4*(a*c))
    Square_Root = Before_Root**.5
    Total_Positive = ((b * -1) + Square_Root) / Divider
    Total_Negative = ((b * -1) - Square_Root) / Divider
    return (Total_Positive, Total_Negative)
def X_And_Y_Velocity_From_Displacement_And_Time(X_Displacement, Total_Time):
    X_Intial_Velocity = X_Displacement / Total_Time
    Y_Intial_Velocity = (Total_Time / 2) * 9.8
    return X_Intial_Velocity, Y_Intial_Velocity, Intial_Velocity_And_Angle(X_Intial_Velocity, Y_Intial_Velocity)
def X_And_Y_Velocity_From_Intial_Velocity_And_Angle(Intial_Velocity, Angle_Degrees):
    Angle = math.asin(Angle_Degrees)
    print(Angle)

#intial varible list
Text_Time = .02


#Main script
Repeat = True
while(Repeat == True):
    Text_Scroll_Effect("0. Settings\n1. Quadratic solution \n2. For intial velocity and angle\n3. Finding x and y intial velocity off distance and time\n4. Finding x and y intial velocity off intial velocity and angle", Text_Time)
    Equation = Question(int, "What are you solving?: ", "Please choose a whole number 0-5", Text_Time)
    if Equation == 0:
        Text_Time = Question(float, "How fast do you want the text scroll speed: " , "Number from .04 to 0" ,Text_Time)
    elif Equation == 1:
        Text_Scroll_Effect("* in the answer first number will be the positive result and the second number will be the negative result.", Text_Time)
        a = Question(float, "First Number: ", "Answer invalid", Text_Time)
        b = Question(float, "Second Number: ", "Answer invalid", Text_Time)
        c = Question(float, "Third Number: ", "Answer invalid", Text_Time)
        Answer_Text = "Qaudratic solution for those 3 numbers is " + str(Quadratic_Solution(a,b,c))
        Text_Scroll_Effect(Answer_Text, Text_Time)

    elif Equation == 2:
        Intial_X_Velocity = Question(float,'X intial velocity?: ', 'Please Input a number', Text_Time)
        Intial_Y_Velocity = Question(float,'Y intial velocity?: ', 'Please Input a number', Text_Time)
        Answer_Text = "Intial velocity and angle is " + str(velo_angle(Intial_X_Velocity, Intial_Y_Velocity))  + " your job to round"
        Text_Scroll_Effect(Answer_Text)

    elif Equation == 3:
        X_Displacement = Question(float, 'Distance?: ', "You suck", Text_Time)
        Time = float(input('Total Time in air: '))
        print("X and Y Intial velocity = " + str(X_And_Y_Velocity_From_Displacement_And_Time(X_Displacement, Time)))

    elif Equation == 4:
        X_And_Y_Velocity_From_Intial_Velocity_And_Angle(2,30)
    Again = Question(str, "(yes or no) done using the script?: ", "I don't think this is possible to mess up", Text_Time)
    if Again == "yes":
        Repeat == False
    print('')
