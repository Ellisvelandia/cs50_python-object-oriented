def main():
  student = get_students()
  # if student[0] == "Padma":
  #   student[1] = "Ravenclaw"
  # print(f"{student[0]} from {student[1]}")
  print(f"{student['name']} from {student['house']}")

def get_students():
  student = {}
  student["name"] = input("Name: ")
  student["house"] = input("House: ")
  return student
# def get_name():
#   return input("Name: ")


# def get_house():
#   return input("Name: ")

if __name__ == "__main__":
  main()  