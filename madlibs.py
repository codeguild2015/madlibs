madlib = "There was once a "
hero = input("Let's see a noun: ")
madlib += (hero + " that set out for a ")
goal = input("Another noun, please: ")
madlib += (goal + ".  But on the way past a ")
place = input("How about a place: ")
madlib += place
villain = input("A person this time: ")
action = input("A past tense verb: ")
madlib += ", {} ran out of {} with the {} first.".format(villain, place, goal)

print(madlib)