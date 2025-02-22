#AI agent creation
environment = ["walls", "open area", "trash bin"]
def move_decide_act():
    for element in environment:
        print(f"I see: {element}")
        if element == "walls":
            print("I came across the wall, hence changed the direction")
        elif element == "open area":
            print("I am in the open area, can move freely")
        elif element == "trash bin":
            print("Ah found the trash bin, I'll now take out all the trash")
        print(".......")
move_decide_act()
environment = ["walls", "open area", "trash bin"]
def perceive(element):
    print(f"I see: {element}")
def move_decide_act():
        for element in environment:
            perceive(element)
            if element == "walls":
                print("I see the wall, instead of moving forward, I changed the direction")
            elif element== "open area":
                print("As I am in the open area, I can mover freely")
            elif element == "trash bin":
                print("Ah I see the trash, my ultimate goal. Now I'll take out all the trash from the bin")
            print("......")
move_decide_act()
print("welcome to ai agent mastery")   
environment = ["walls", "open area","trash bin", "obstacles", "walls"]
def perceive(element):
    print(f"I see: {element}")
def move_decide_act():
    for element in environment:
        perceive(element)
        if element == "walls":
            print("I came across the wall, can't move straight")
        elif element == "open area":
            print("I am in open area, thus cam move freely")
        elif element == "trash bin":
            print("Ah I came across trash bin, now I'll remove trash from the bin")
        elif element == "obstacles":
            print("Due to this obstacle, I'll change my direction now")
        print("......")
move_decide_act()
environment = ["walls", "open area", "trash bin", "obstacles", "walls"]
memory = []
def perceive(element):
    print(f"I see: {element}")
    if element not in memory:
        memory.append(element)
    else:
        print("I remember seeing this before!")
def move_decide_act():
    for element in environment:
        perceive(element)
        if element == "walls":
            print("I came across the wall, hence can't move straight")
        elif element == "open area":
            print("I am in the open area, and can move freely")
        elif element == "trash bin":
            print("Saw the trash bin, I'll now take out all the trash")
        elif element == "obstacles":
            print("I came across this obstacle, hence I'll change my direction")
        print(".......")
move_decide_act()