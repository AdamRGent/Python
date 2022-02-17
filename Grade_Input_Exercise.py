

def name_finalgrade ():
   print("name:", studentname,", " "final score percentage:" , finalexamscore, "percent")

def grade ():
   print("Your final Grade is:")
   if finalexamscore in range (85,101):
      print("Grade A")
   elif finalexamscore in range (65,85):
      print("Grade B")
   else:
      print("Fail")

studentname = input("what is your name?: ")
studenthomework = input("homework score: ")
studentassessment = input("assessment score: ")
finalexamscore = int (input("final exam score: "))


name_finalgrade ()
grade () 











