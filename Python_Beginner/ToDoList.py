print ("Prepare a To Do List & Save")

file_obj = open("todolist.txt", "w")
print ("Enter List of TO DO items")
todolist = []
while True:
    item = input()
    if item == 'x':
        break
    else:
        todolist.append(item + "\n")

save_flg = input("Would you like to Save the To Do list items")
if save_flg == 'Y':
    file_obj.writelines(todolist)

file_obj.close()
