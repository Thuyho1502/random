import random

print("""Welcomwe multiplication table world!!!
Do you want to play with me?
type 0 for no and another number for yes""")


choice= int(input("Enter your choice:"))
if choice== 0:
        print("bye, see you later")


else:
        def multiplication(num1, num2):
            return num1 * num2
        while True:
            num1 = random.randint(1, 10)
            print(num1)
            num2 = random.randint(1, 10)
            print(num2)
            print(num1, "X", num2)
            i = float(input("enter your answers:"))
            if i== num1 * num2:

                    print("JIPPY, it correct")
            elif i==0:
                print("program is stopped")
                break

            elif i != num1 * num2 and i!= 0:


                    print("""Sadly,it not correct.Do you want to try again?
                    Press 0 for no or other number for yes """)
                    press= int(input("Please press your choice:"))
                    if press==0:
                        print("Thank you for joining")
                        break
                    else:
                        print("""welcome back""")
                        while True:

                            if i == num1 * num2:

                                print("JIPPY, it correct")
                            elif i == 0:
                                print("program is stopped")
                                break
                            elif i != num1 * num2 and i != 0:
                                break


