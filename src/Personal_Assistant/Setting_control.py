import os
input_choice=input("Shutdown the computer ( yes or not) ")
if input_choice == "yes" or input_choice=='y' or input_choice =='Y':
    print("shutting down the os")
    os.system("Shutdown /s /t 30")
else:
    print("Thank you Sir")