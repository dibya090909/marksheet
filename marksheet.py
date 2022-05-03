name=input("enter the name of the student:")
roll=int(input("enter the roll number of the student:"))
english=int(input("enter the english marks:"))
physics=int(input("enter the physics marks:"))
chemistry=int(input("enter the chemistry marks:"))
maths=int(input("enter the maths marks:"))
obmarks=int(english+physics+chemistry+maths)
percentage=int(obmarks/400*100)


print("----------------------------")
print("        MARKSHEET           ")
print("----------------------------")
print("Name:"+name)
print("Roll no:"+str(roll))
print("English Marks:"+str(english))
print("Physics Marks:"+str(physics))
print("Chemistry Marks:"+str(chemistry))
print("Maths:"+str(maths))
print("Total marks: 400")
print("Obmarks:"+str(obmarks))
print("Percentage:"+str(percentage))
if int(obmarks>300) and int(obmarks<=400):
    print("Grade A")
elif int(obmarks>200) and (obmarks<=300):
    print("Grade B")
elif int(obmarks>100) and int(obmarks<=200):
    print("Grade C")
else:
    print("Grade D")
