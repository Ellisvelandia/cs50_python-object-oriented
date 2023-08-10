class Student:
    def __init__(self, name, house):
        if not name:
            # print("Missing name")
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        # self.patonus = patronus

    def __str__(self):
      return f"{self.name} from {self.house}"
    
    # def charm(self):
    #     match self.patronus:
    #         case "Stag":
    #             return ""
    #         case "Otter":
    #           return ""
    #         case "Jack Russell terrier":
    #             return ""
    #         case _:
    #             return ""


def main():
    student = get_students()
    print(student)
    # print("Expecto Patronum!")
    # print(student.charm())
    # print(f"{student.name} from {student.house}")
    # if student[0] == "Padma":
    #   student[1] = "Ravenclaw"
    # print(f"{student[0]} from {student[1]}")


def get_students():
    name = input("Name: ")
    house = input("House ")
    patronus = input("Patronus: ")
    return Student(name, house,patronus)
    
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
