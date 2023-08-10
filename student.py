class Student:
    def __init__(self, name, house):
        if not name:
            # print("Missing name")
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
      return f"{self.name} from {self.house}"


def main():
    student = get_students()
    print(student)
    # print(f"{student.name} from {student.house}")
    # if student[0] == "Padma":
    #   student[1] = "Ravenclaw"
    # print(f"{student[0]} from {student[1]}")


def get_students():
    name = input("Name: ")
    house = input("House ")
    return Student(name, house)
    
    # student = Student()
    # student.name = input("Name: ")
    # student.house = input("House ")
    # return student
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
