import action

RoutineFile = open(input("Please input the routine file to use: "), "r")
RoutineList = RoutineFile.read().split('\n')

for i in range(len(RoutineList)):
	if RoutineList[i] == "#":
		continue
	else:
		continue
