def main():
  student = get_students()
  if student[0] == "Padma":
    student[1] = "Ravenclaw"
  print(f"{student[0]} from {student[1]}")

def get_students():
  name = input("Name: ")
  house = input("House: ")
  return [name, house]
# def get_name():
#   return input("Name: ")


# def get_house():
#   return input("Name: ")

if __name__ == "__main__":
  main()  