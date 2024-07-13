import random
TreasureMap = ("    A   B   C\n"
               "1 [ ■ , ■ , ■ ]\n"
               "2 [ ■ , ■ , ■ ]\n"
               "3 [ ■ , ■ , ■ ]\n"
               "")
print(f"\nWelcome to \"FIND THE TREASURE\" game, the rules are pretty simple.\n"
      f"Get the treasure correct location and win !\n\n{TreasureMap}")
list1 = ['■', '■', '■']
list2 = ['■', '■', '■']
list3 = ['■', '■', '■']
Map = [list1, list2, list3]
random_rows = random.randint(0, 2)
random_columns = random.randint(0, 2)
# Map[random_rows][random_columns] = '☑' <- Wrong
Correct_Location = str(random_rows) + str(random_columns)
Available_Locations = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
x = 1
while x < 10:
    # A1 case
    Location = input("Enter a location to search for the treasure: ").upper()
    if ((Location == "A1" or Location == "1A") and Correct_Location == "00"
            and (Available_Locations.count("A1") == 1)):
        Map[0][0] = '☑'
        Available_Locations.remove("A1")
        print(f""
              f"YOU FOUND THE TREASURE MAP !\n"
              f"   A   B   C\n1 {Map[0]}\n2 {Map[1]}\n3 {Map[2]}")
        break
    elif (Location == "A1" or Location == "1A") and Correct_Location != "00"\
            and (Available_Locations.count("A1") == 1):
        Map[0][0] = 'X'
        Available_Locations.remove("A1")
        print(f"Wrong answer, keep trying !\n"
              f"   A   B   C\n1 {Map[0]}\n2 {Map[1]}\n3 {Map[2]}")
    # B1 case
    elif (Location == "B1" or Location == "1B") and Correct_Location == "01"\
            and (Available_Locations.count("B1") == 1):
        Map[0][1] = '☑'
        Available_Locations.remove("B1")
        print(f""
              f"YOU FOUND THE TREASURE MAP !\n"
              f"   A   B   C\n1 {Map[0]}\n2 {Map[1]}\n3 {Map[2]}")
        break
    elif (Location == "B1" or Location == "1B") and Correct_Location != "01"\
            and (Available_Locations.count("B1") == 1):
        Map[0][1] = 'X'
        Available_Locations.remove("B1")
        print(f"Wrong answer, keep trying !\n"
              f"   A   B   C\n1 {Map[0]}\n2 {Map[1]}\n3 {Map[2]}")
    # C1 case
    elif (Location == "C1" or Location == "1C") and Correct_Location == "02"\
            and (Available_Locations.count("C1") == 1):
        Map[0][2] = '☑'
        Available_Locations.remove("C1")
        print(f""
              f"YOU FOUND THE TREASURE MAP !\n"
              f"   A   B   C\n1 {Map[0]}\n2 {Map[1]}\n3 {Map[2]}")
        break
    elif (Location == "C1" or Location == "1C") and Correct_Location != "02"\
            and (Available_Locations.count("C1") == 1):
        Map[0][2] = 'X'
        Available_Locations.remove("C1")
        print(f"Wrong answer, keep trying !\n"
              f"   A   B   C\n1 {Map[0]}\n2 {Map[1]}\n3 {Map[2]}")
    # A2 case
    elif (Location == "A2" or Location == "2A") and Correct_Location == "10"\
            and (Available_Locations.count("A2") == 1):
        Map[1][0] = '☑'
        Available_Locations.remove("A2")
        print(f""
              f"YOU FOUND THE TREASURE MAP !\n"
              f"   A   B   C\n1 {Map[0]}\n2 {Map[1]}\n3 {Map[2]}")
        break
    elif (Location == "A2" or Location == "2A") and Correct_Location != "10"\
            and (Available_Locations.count("A2") == 1):
        Map[1][0] = 'X'
        Available_Locations.remove("A2")
        print(f"Wrong answer, keep trying !\n"
              f"   A   B   C\n1 {Map[0]}\n2 {Map[1]}\n3 {Map[2]}")
    # B2 case
    elif (Location == "B2" or Location == "2B") and Correct_Location == "11"\
            and (Available_Locations.count("B2") == 1):
        Map[1][1] = '☑'
        Available_Locations.remove("B2")
        print(f""
              f"YOU FOUND THE TREASURE MAP !\n"
              f"   A   B   C\n1 {Map[0]}\n2 {Map[1]}\n3 {Map[2]}")
        break
    elif (Location == "B2" or Location == "2B") and Correct_Location != "11"\
            and (Available_Locations.count("B2") == 1):
        Map[1][1] = 'X'
        Available_Locations.remove("B2")
        print(f"Wrong answer, keep trying !\n"
              f"   A   B   C\n1 {Map[0]}\n2 {Map[1]}\n3 {Map[2]}")
    # C2 case
    elif (Location == "C2" or Location == "2C") and Correct_Location == "12"\
            and (Available_Locations.count("C2") == 1):
        Map[1][2] = '☑'
        Available_Locations.remove("C2")
        print(f""
              f"YOU FOUND THE TREASURE MAP !\n"
              f"   A   B   C\n1 {Map[0]}\n2 {Map[1]}\n3 {Map[2]}")
        break
    elif (Location == "C2" or Location == "2C") and Correct_Location != "12"\
            and (Available_Locations.count("C2") == 1):
        Map[1][2] = 'X'
        Available_Locations.remove("C2")
        print(f"Wrong answer, keep trying !\n"
              f"   A   B   C\n1 {Map[0]}\n2 {Map[1]}\n3 {Map[2]}")
    # A3 case
    elif (Location == "A3" or Location == "3A") and Correct_Location == "20"\
            and (Available_Locations.count("A3") == 1):
        Map[2][0] = '☑'
        Available_Locations.remove("A3")
        print(f""
              f"YOU FOUND THE TREASURE MAP !\n"
              f"   A   B   C\n1 {Map[0]}\n2 {Map[1]}\n3 {Map[2]}")
        break
    elif (Location == "A3" or Location == "3A") and Correct_Location != "20"\
            and (Available_Locations.count("A3") == 1):
        Map[2][0] = 'X'
        Available_Locations.remove("A3")
        print(f"Wrong answer, keep trying !\n"
              f"   A   B   C\n1 {Map[0]}\n2 {Map[1]}\n3 {Map[2]}")
    # B3 case
    elif (Location == "B3" or Location == "3B") and Correct_Location == "21"\
            and (Available_Locations.count("B3") == 1):
        Map[2][1] = '☑'
        Available_Locations.remove("B3")
        print(f""
              f"YOU FOUND THE TREASURE MAP !\n"
              f"   A   B   C\n1 {Map[0]}\n2 {Map[1]}\n3 {Map[2]}")
        break
    elif (Location == "B3" or Location == "3B") and Correct_Location != "21"\
            and (Available_Locations.count("B3")):
        Map[2][1] = 'X'
        Available_Locations.remove("B3")
        print(f"Wrong answer, keep trying !\n"
              f"   A   B   C\n1 {Map[0]}\n2 {Map[1]}\n3 {Map[2]}")
    # C3 case
    elif (Location == "C3" or Location == "3C") and Correct_Location == "22"\
            and (Available_Locations.count("C3")):
        Map[2][2] = '☑'
        Available_Locations.remove("C3")
        print(f""
              f"YOU FOUND THE TREASURE MAP !\n"
              f"   A   B   C\n1 {Map[0]}\n2 {Map[1]}\n3 {Map[2]}")
        break
    elif (Location == "C3" or Location == "3C") and Correct_Location != "22"\
            and (Available_Locations.count("C3") == 1):
        Map[2][2] = 'X'
        Available_Locations.remove("C3")
        print(f"Wrong answer, keep trying !\n"
              f"   A   B   C\n1 {Map[0]}\n2 {Map[1]}\n3 {Map[2]}")
    else:
        print("Enter a valid location please..")
        x -= 1
    x += 1
