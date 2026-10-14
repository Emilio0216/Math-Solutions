# √ for later
import math, time
from time import sleep
def Question(Answer_Type):
    while True:
        Answer = input()
        #probably a better way to do this but im lazy
        try:
            Correct = Answer_Type(Answer)
            break
        except ValueError:
            Text_Scroll_Effect("That is not a valid answer. Please try again.", .01, False)
    return Correct
def Text_Scroll_Effect(Text, Time, Question):
    for char in Text:
        print( char, end='')
        sleep(Time)
    if Question == False:
        print('')
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

Text_Time = .02
Repeat = False
while(Repeat == False):
    Text_Scroll_Effect("0. Settings\n1. Quadratic solution \n2. For intial velocity and angle\n3. Finding x and y intial velocity off distance and time\n4. Finding x and y intial velocity off intial velocity and angle", Text_Time, False)
    Text_Scroll_Effect("What are you solving?: ", Text_Time, True)
    Equation = int(input(''))
    print("")
    if Equation == 0:
        Text_Scroll_Effect("How fast do you want the text scroll speed: ", Text_Time, True)
        Text_Time = Question(float)
    
    elif Equation == 1:
        print("* in the answer first number will be the positive result and the second number will be the negative result.")
        a = float(input('1st number: '))
        b = float(input('2nd number: '))
        c = float(input('3rd number: '))
        print("Qaudratic solution for those 3 numbers is " + str(Quadratic_Solution(a,b,c)))

    elif Equation == 2:
        Intial_X_Velocity = float(input('X intial velocity: '))
        Intial_Y_Velocity = float(input('Y intial velocity: '))
        print("\n Intial velocity and angle is " + str(velo_angle(Intial_X_Velocity, Intial_Y_Velocity)) + " your job to round")

    elif Equation == 3:
        X_Displacement = float(input('Distance: '))
        Time = float(input('Total Time in air: '))
        print("X and Y Intial velocity = " + str(X_And_Y_Velocity_From_Displacement_And_Time(X_Displacement, Time)))

    elif Equation == 4:
        X_And_Y_Velocity_From_Intial_Velocity_And_Angle

    Again = input("\n(yes or no) done using the script?: ")
    if Again == "yes":
        sys.Program_Crash_On_Purpose
    print('')
