import math

class MyRound :

    def my_round(value, digits):

        digits_current_value =str(value)[::-1].find('.')

        if (digits_current_value <= int(digits)):
            pattern = "{0:."+str(digits)+"f}"
            return pattern.format(value)    
        else:
            #round down
            truncate_value = math.floor(value * 100)/100.0
            pattern = "{0:."+str(digits)+"f}"
            return pattern.format(truncate_value)