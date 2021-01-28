import random, csv

students = []
student_num = 554

## Establish the distribution of classes among students

math = {
	'Geometry 9': 0.20939,
	'Geometry H': 0.20939,
	'Algebra 2': 0.35017,
	'Algebra 2H': 0.23105
}

science = {
	'Biology': 0.45668,
	'Biology H': 0.54332
}

## Functions for u

def create_student_list(student_num):
	for i in range(student_num):
		student = Student(id=i)
		students.append(student)
	return students

## And this class too uwu

class Student:
	def __init__(self, id):
		self.id = id
		# Don't mind me just random-ishly choosing this fool's classes
		math_choice = random.choices(list(math.keys()), weights=math.values())[0]
		science_choice = random.choices(list(science.keys()), weights=science.values())[0]
		# Setting up some stuff
		self.schedule = [math_choice, science_choice, 'English', 'World History', 'P.E.']
		self.periods = len(self.schedule)
		# Shuffling some stuff for kicks
		self.schedule = shuffle(self.schedule)

## We gon shuffle

def shuffle(input_list):
	return_list = input_list
	random.shuffle(return_list)
	return return_list

## Dump your data, beta

def create_csv():
	with open('cohort_data.csv', 'w', newline='') as file:
	    writer = csv.writer(file)
	    writer.writerow(["Student #", "Period 1", "Period 2", "Period 3", "Period 4", "Period 5"])
	    for student in students:
	    	data = [student.id]
	    	for j in range(student.periods):
	    		data.append(student.schedule[j])
	    	writer.writerow(data)

## Tiny functions are fabulous

def main():
	students = create_student_list(student_num)
	create_csv()

## Literal art

if __name__ == "__main__":
	main()