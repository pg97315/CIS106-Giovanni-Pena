def define_list():
  #1.Prompt the user for a number which will represent the number of items in a list.
  #Then use a for loop to add that many integers to the list.
  global n
  global main_list
  n = int(input("Enter the number of items: "))
  main_list = []
  return main_list, n


def prompt_number(n, main_list):
  for item in range(0, n, 1):
    item = int(input("Enter the item: "))
    main_list.append(item)
  print("\nYour list:", main_list)
  return main_list


def main_list_game(main_list):
  #2.Insert the score of 99 at position 1 within the list. Display the updated list.
  score_99 = 99
  main_list.insert(1, score_99)
  print("Adding 99: ", main_list)

  #3.	Replace the value of 99 with the value 100. Display the updated list.
  score_index = main_list.index(99)
  main_list[score_index] = 100
  print("Changing it to 100: ", main_list)


def second_list_game(main_list):
  #4.	Create a second list with the values 500, 600, 700, 800, 900. Display this list.
  global second_list
  second_list = [500, 600, 700, 800, 900]
  print("\nSecond list:", second_list)
  # Extend the first list with this second list. Display the first list.
  main_list.extend(second_list)
  print("Both list:", main_list)

  #5.	Remove the value 800 from the first list. Display the first list.
  main_list.remove(800)
  print("Remove the 800: ", main_list)

  #6.	Remove the third item from the first list. Display the first list.
  main_list.pop(2)
  print("Remove third element:", main_list)
  return main_list, second_list


def grade_list_game():
  #7.	Create a list of grades: grades =["A", "B", "C", "A", "A", "C"]
  global grade_list
  grade_list = ["A", "B", "C", "A", "A", "C"]
  print("\nThe grade list is:", grade_list)

  # 8.	Display a count of the number of A grades.
  count_grades = grade_list.count("A")
  print("Number of A in the list:", count_grades)

  #9.	Display the index (position) of the first B grade.
  B_position = grade_list.index("B")
  print("B position:", B_position, "\nB index position: ", B_position - 1)

  #10.Look for grade of F. Display a message that F is not in the list.
  #(Do not let the code generate an error).
  look_for = "F"
  if "F" in grade_list:
    print("The F position is: ", grade_list.index(look_for))
  else:
    print("There is not a F in this list.")
  return grade_list


def clear_second_list(second_list):
  #11.Clear (but do not delete) the second list of integers. Display the list.
  second_list.clear()
  print("New second list: ", second_list)

  #12.	Delete the second list. Try to display it. (
  # should get an error because the list no longer exists.
  del second_list
  print(second_list)


def players_list_game():
  #13.Create a list of players in this order (“Rizzo”, “Davis”, “Baez”, “Happ”, “Bryan”)
  global player_list
  player_list = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
  print("\nPlayer list: ", player_list)

  # 14.	Sort the list of players. Display the sorted list.
  player_list.sort()
  print("Sorted list: ", player_list)

  # 15.	Make a copy of the list of players called players2. Display players2.
  players2 = player_list.copy()
  print("Copy of the list: ", players2)

  # 16.	Reverse the order of players2. Display players, then display players2.
  players2.sort(reverse=True)
  print("\nPlayer: ", player_list, "\nPlayers in reverse:\
  ", players2)


define_list()
prompt_number(n, main_list)
main_list_game(main_list)
second_list_game(main_list)
grade_list_game()
players_list_game()
