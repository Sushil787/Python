items = ["one","two","three"]

for item in items:
    with open("{}hello_world.txt".format(item), "w") as f:
        string = input(f"enter any thing you like to write in {one} file: ")
        f.write(string)
        f.write("\nThis is my second line of code with {} the first item in my list".format(item))
