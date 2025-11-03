khmer = int(input("Enter khmer score  "))
math =  int(input("Enter math score  "))
physic = int(input("Enter physic score  "))
sciene = int(input("Enter sciene score "))
total = khmer + math + physic + sciene
average = total/4
print(average)
print(average)

if average > 90:
    print("grade A")
elif average >= 80:
    print("Grade B")
elif average > 70:
    print("Grade C")
elif average > 60:
    print("Grade D")
elif average > 50:
    print("Grade E")
elif average < 50:
    print("tlek hz pov meas ")
else:
    print("Error score")