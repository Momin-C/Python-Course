import pickle,Student

f = open("student.dat","wb")
s = Student.Student(123,"John",90)
print(s.id)
pickle.dump(s,f)
f.close()
