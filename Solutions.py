# symbol for √ for later 
# im planning on adding simplified square roots but that might be too hard idk yet
#auraaaa
#Imports
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
def Intial_Velocity_And_Angle(Intial_X_Velocity, Intial_Y_Velocity, Decimals):
    # i hate radians with a passion
    Intial_Velocity = ((Intial_X_Velocity ** 2) + (Intial_Y_Velocity ** 2)) ** .5
    Angle = Intial_Y_Velocity / Intial_Velocity
    Angle_Degrees = math.asin(Angle) * (180.0 / math.pi)
    return round(Intial_Velocity, Decimals), round(Angle_Degrees, Decimals)

def Quadratic_Solution(a, b, c, Decimals):
    Divider = 2 * a
    Before_Root = (b**2) + (-4*(a*c))
    Square_Root = Before_Root**.5
    Total_Positive = ((b * -1) + Square_Root) / Divider
    Total_Negative = ((b * -1) - Square_Root) / Divider
    return round(Total_Positive,Decimals), round(Total_Negative,Decimals)

def X_And_Y_Velocity_From_Displacement_And_Time(X_Displacement, Total_Time, Decimals):
    X_Intial_Velocity = X_Displacement / Total_Time
    Y_Intial_Velocity = (Total_Time / 2) * 9.8
    return round(X_Intial_Velocity, Decimals), round(Y_Intial_Velocity, Decimals), Intial_Velocity_And_Angle(X_Intial_Velocity, Y_Intial_Velocity, Decimals)

def X_And_Y_Velocity_From_Intial_Velocity_And_Angle(Intial_Velocity, Angle_Degrees, Decimals):
    Intial_X_Velocity = math.cos(math.radians(Angle_Degrees))* Intial_Velocity
    Intial_Y_Velocity = math.sin(math.radians(Angle_Degrees))* Intial_Velocity
    return round(Intial_X_Velocity, Decimals), round(Intial_Y_Velocity, Decimals)

def X_From_Square_Area_And_Perimeter(Area, Perimeter, Decimals):
    Temp_Perimeter = Perimeter/-2
    X = Quadratic_Solution(1,Temp_Perimeter,Area,Decimals)
    return X
#intial varible list
Text_Time = .005
Decimal_Places = 5
Default_Variable_Text = "Default text speed: " + str(Text_Time) + " \nDefault Rounding: " + str(Decimal_Places) + " decimal places \n"
Text_Scroll_Effect(Default_Variable_Text, Text_Time)

#Main script
Repeat = True
while(Repeat == True):
    Text_Scroll_Effect("0. Settings\n1. Quadratic solution \n2. For intial velocity and angle\n3. Finding x and y intial velocity off distance and time\n4. Finding x and y intial velocity off intial velocity and angle\n5. Finding Length and width of a square with Area and Perimeter", Text_Time)
    Equation = Question(int, "What would you like to do?: ", "Please choose a whole number 0-5", Text_Time)
    if Equation == 0:
        Options = Question(int,"1. Text Speed\n2. Decimal place rounding\n what would you like?: ", "a number please", Text_Time)
        if Options == 1:
            Text_Time = Question(float, "How fast do you want the text scroll speed: " , "Number from .04 to 0" ,Text_Time)
        elif Options == 2:
            Decimal_Places = Question(int, "How many decimal places do you want?: " , "Number not text dawg" ,Text_Time)
    elif Equation == 1:
        Text_Scroll_Effect("* in the answer first number will be the positive result and the second number will be the negative result.", Text_Time)
        a = Question(float, "First Number: ", "Answer invalid", Text_Time)
        b = Question(float, "Second Number: ", "Answer invalid", Text_Time)
        c = Question(float, "Third Number: ", "Answer invalid", Text_Time)
        Answer_Text = "Qaudratic solution for those 3 numbers is " + str(Quadratic_Solution(a,b,c,Decimal_Places))
        Text_Scroll_Effect(Answer_Text, Text_Time)

    elif Equation == 2:
        Intial_X_Velocity = Question(float,'X intial velocity?: ', 'Please Input a number', Text_Time)
        Intial_Y_Velocity = Question(float,'Y intial velocity?: ', 'Please Input a number', Text_Time)
        Answer_Text = "Intial velocity and angle is " + str(Intial_Velocity_And_Angle(Intial_X_Velocity, Intial_Y_Velocity, Decimal_Places))
        Text_Scroll_Effect(Answer_Text, Text_Time)

    elif Equation == 3:
        X_Displacement = Question(float, 'Distance?: ', "You suck", Text_Time)
        Time = Question(float,'Total Time in air?: ', "Invalid input, please put a number", Text_Time)
        Answer_Text ="X and Y Intial velocity = " + str(X_And_Y_Velocity_From_Displacement_And_Time(X_Displacement, Time, Decimal_Places))
        Text_Scroll_Effect(Answer_Text , Text_Time)


    elif Equation == 4:
        Intial_Velocity = Question(float, "Initial velocity?: ", "Invalid", Text_Time)
        Angle_Degrees = Question(float, "Angle degrees?: ", "Number not str", Text_Time)
        Answer_Text= "X and Y intial velocitys" + str(X_And_Y_Velocity_From_Intial_Velocity_And_Angle(Intial_Velocity, Angle_Degrees, Decimal_Places),)
        Text_Scroll_Effect(Answer_Text, Text_Time)
    
    elif Equation == 5:
        Area_Of_Square = Question(float, "area?: ", "Invalid", Text_Time)
        Perimeter_Of_Square = Question(float, "perimeter?: ", "Number not str", Text_Time)
        Answer_Text= "Length and width" + str(X_From_Square_Area_And_Perimeter(Area_Of_Square,Perimeter_Of_Square,Decimal_Places))
        Text_Scroll_Effect(Answer_Text, Text_Time)
    
    Again = Question(str, "(yes or no) done using the script?: ", "I don't think this is possible to mess up", Text_Time)
    if Again == "yes":
        Repeat = False

    print('')
