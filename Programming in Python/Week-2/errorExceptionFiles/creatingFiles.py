with open("week-2/errorExceptionFiles/newfile.txt", "w") as file:
    # file.write("This is a new file!") // single line
    file.writelines(["This is a new file created!", "\nThis is another line to be added."])


try:
    with open("week-2/errorExceptionFiles/sample/newfile.txt", "a") as file:
        file.writelines(["n/This is a new file created!", "\nThis is another line to be added."])
except FileNotFoundError as e:
    print("ERROR", e)