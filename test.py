import sys
class Grader():
	def calCulate(_self,g):

		if int(g)>90:
			return "A"
		elif int(g)>80 and int(g)<90:
			return "B"
		else:
			return "C"
	def genCard(_self,g,name,a):
		msg  = str(name)
		msg = msg+"@fullsail.edu"
		msg = msg+"\nHere is your grade for "+str(a)+" assingment: "+_self.calCulate(g)
		msg = msg+"\nGrade details:"
		msg = msg+"\n"+_self.reasons(g)

		return msg
	def reasons(_self,g):
		if int(g)>90:
			return "You have met all the requirements for full grade"
		elif int(g)>80 and int(g)<90:
			return "It looks like you are missing some of the functionality"
		else:
			return "It looks like you are missing most of the functionality"

mygrade = Grader()
g = raw_input("Enter Grade: ")

a = raw_input("Enter assingment name: ")

n = raw_input("Enter student name: ")

print(mygrade.genCard(g,n,a))