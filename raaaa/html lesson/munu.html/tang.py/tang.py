
math = int(input("enter a math: "))
khmer = int(input("enter a khmer: "))
physic = int(input("enter physic "))

is_invalid = False
total = math + khmer + physic 
average = total / 3 

if math > 100 or math < 0:
    print("yout math is invalid")
    is_invalid = True


if khmer > 100 or khmer < 0:
    print("yout khmer is invalid")
    is_invalid = True


if physic  > 100 or physic < 0:
    print("yout math is invalid")
    is_invalid = True



if average > 50 and average < 100:
        grade = "Pass"
elif average < 50 and average > 0 :
    grade = "Fail"

else:
    grade = "Error"

    print(f"total {total}")
    print(f"average {average}")
    print(f"grade {grade}")
else:
    print("error grade")
   