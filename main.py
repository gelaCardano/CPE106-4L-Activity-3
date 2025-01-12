from student import Student

#defining student objects
stud1 = Student("Angela",100)
stud2 = Student("Franz",99)
stud3 = Student("Allen",100)
stud4 = Student("Julian",95)
stud5 = Student("Marcus",80)
stud6 = Student("Angela",98)

print("Testing Student Comparison Methods:")
print("Comparing Object One Less Than Four: " +str(stud1<stud4))
print("Comparing Object One Equal Six: " +str(stud1==stud6))
print("Comparing Object Two Greater Than or Equal Five: " +str(stud2>=stud5))
print("")

#loading student objects to a list
studentList = [stud1, stud2, stud3, stud4, stud5,stud6]
#sorting and printing the list
studentList.sort()
for x in studentList:
    print(x.name,x.grade)
