#print("This is the data_base.py module")
#print("It's name is {}" .format(__name__))

from blood_calculator import hdl_analysis #specifically import just this function
#import blood_calculator

import blood_calculator as bc

answer = hdl_analysis(55)
#answer = blood_calculator.hdl_analysis(55)
print("The analysis of 55 HDL is {}" .format(answer))
answer2 = bc.ldl_analysis(200)
print("The analysis of 200 LDL is {}" .format(answer2))

