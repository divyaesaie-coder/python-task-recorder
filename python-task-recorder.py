#Task recorder

tasks=[]
while True:
    print("1)Add task:")
    print("2)View history:")
    print("3)Remove task:")
    print("4)Exit:")

    ch=input("Choose:")

    if ch=="1":
        task=input("Enter the task:")
        mark=input("Enter True/False(Completion):")

        tasks.append({"Task":task,"Done":mark})

        file=open("Task recorder.txt","a")
        file.write(task + "," + mark + "\n")
        file.close()

    if ch=="2":
        print(tasks)

    if ch=="3":
        task=input("Enter the task:")
        for t in tasks:
            if t["Task"]==task:
                tasks.remove(t)
                print("Removed!")
                break
        else:
            print("Doesnt exist!")

    if ch=="4":
        print("Bye!")
        break

