HELP = '''help - справка
add- добавить
show- печатать
exit- выход'''
tasks = []
todays = list()
tomorrows = list()
others = list()
while True:
  command = input("Введите команду: ")
  if command == "help":
   print(HELP)
  elif command == "add":
   task= input("Добавить команду: ")
   tasks.append(task)
   print("Добавлено.")
   date = input("Введите дату: ")
   if date == "today":
     todays.append(date)
   if date == "tomorrow":
     tomorrows.append(date)
   else:
     others.append(date)
  elif command == "show": 
   print(tasks,todays,tomorrows,others)
  elif command == "exit":
    print("Спасибо за использование! До свидания!")
    break
  else:
    print("Неизвестная программа")
    break

  
  
    
    

