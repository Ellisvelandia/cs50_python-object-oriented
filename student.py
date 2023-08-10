class Student:
   def __init__(self, name , house):
    #  self.name = name
    #  self.house = house


def main():
  student = get_students()
  print(f"{student.name} from {student.house}")
  # if student[0] == "Padma":
  #   student[1] = "Ravenclaw"
  # print(f"{student[0]} from {student[1]}")

def get_students():
  name = input("Name: ")
  house = input("House ")
  student = Student(name, house)
  # student = Student()
  # student.name = input("Name: ")
  # student.house = input("House ")
  return student
  # student = {}
  # student["name"] = input("Name: ")
  # student["house"] = input("House: ")
  # return student
# def get_name():
#   return input("Name: ")


# def get_house():
#   return input("Name: ")

if __name__ == "__main__":
  main()  