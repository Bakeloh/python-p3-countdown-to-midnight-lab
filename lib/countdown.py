# your code goes here!
def countdown(number):
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
    print ("HAPPY NEW YEAR!")


countdown(5)
# test the function with a large number

import time

def countdown_with_sleep(number):
    while number > 0:
        print(f"{number} SECOND(S)!", end="\r", flush=True) 
        time.sleep(1)
        number -= 1
    print("\nHAPPY NEW YEAR!")
    
countdown_with_sleep(5)    