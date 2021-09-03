#print("This is the blood_calculator.py module") #started python with this module so given main
#print("It's name is {}" .format(__name__))

def interface():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
        print("Make a choice")
        print("1 - HDL Analysis")
        print("9 - Quit")
        choice = int(input("Make a choice: "))
        print(type(choice))
        if choice == 9:
            keep_running = False
        elif choice == 1:
            HDL_Driver()
        elif choice == 2:
            LDL_Driver()
        
        
    print(choice)
    return choice

def HDL_Driver():
    HDL_value = hdl_input()
    HDL_character = hdl_analysis(HDL_value)
    hdl_output(HDL_value, HDL_character)


def hdl_input():
    hdl_value = int(input("Enter HDL Value: "))
    return hdl_value

def hdl_analysis(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif 40 <= HDL_value < 60:
        return "Borderline Low"
    else:
        return "Low"

def hdl_output(HDL_value, HDL_answer):
    print("The HDL value of {} is considered {}" .format(HDL_value, HDL_answer))
    return 




def LDL_Driver():
    LDL_value = ldl_input()
    LDL_character = ldl_analysis(LDL_value)
    ldl_output(LDL_value, LDL_character)


def ldl_input():
    ldl_value = int(input("Enter LDL Value: "))
    return ldl_value

def ldl_analysis(LDL_value):
    if LDL_value < 130:
        return "Normal"
    elif 130 <= LDL_value < 160:
        return "Borderline High"
    elif 160 <= LDL_value < 190:
        return "High" 
    else:
        return "Very High"

def ldl_output(LDL_value, LDL_answer):
    print("The LDL value of {} is considered {}" .format(LDL_value, LDL_answer))
    return 

if __name__ == "__main__":
    interface() ##cant put this before you define it, will not run the interface unless you run it directly. if you import into other files it will not run directly. 
    #Always use this name main statement and put the functionality you used to start the program inside the if statement block. If your import this it will not run the interface, but will import everything in it to another code
