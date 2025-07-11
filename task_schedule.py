# Task schedule 

Tasks = input("Enter your tasks for today separated by a comma: ")
Tasks_list = Tasks.split(",")
Done_tasks = []
Ongoing_tasks = []
for task in Tasks_list:
  print(f"\n{task}\n")
  response = input(f"Did you finish {task} already? (yes/no): ").lower()
  if response == "yes":
    print("Nice job")
    Done_tasks.append(task)
  else:
    print("Try not to put it off")
    Ongoing_tasks.append(task)
  print("")
progress = input("Do you want to see your today's progress? (yes/no): ").lower()
if progress == "yes":
  print("\n********** Done Tasks **********")
  print(Done_tasks)
  print("\n********** Ongoing Tasks **********")
  print(Ongoing_tasks)
else :
  print("Thanks for using our program")