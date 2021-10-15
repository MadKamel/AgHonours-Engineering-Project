import action, time, configs

cfg = configs.Read("configs")

RoutineFile = open(cfg["routine"]+".routine")
RoutineList = RoutineFile.read().split("\n")

for i in range(len(RoutineList)):
        print("[#] LINE: " + RoutineList[i])
        SplitCommand = RoutineList[i].split(" ")
        if SplitCommand[0] == "#":
                continue
        elif SplitCommand[0] == "":
                continue
        else:
                if SplitCommand[0] == "NOTE":
                        print("[@] NOTE: " + " ".join(SplitCommand[1:]))
                elif SplitCommand[0] == "WAIT":
                        time.sleep(int(SplitCommand[1]))
                elif SplitCommand[0] == "FLOW":
                        if SplitCommand[1] == "ON":
                                print("[i] INFO: ATTEMPTING TO BEGIN FLOW")
                                if action.Flow(True):
                                        print("[i] INFO: FLOW NOW ACTIVE")
                                else:
                                        print("[i] WARN: FLOW COULD NOT START!")
                        elif SplitCommand[1] == "OFF":
                                print("[i] INFO: ATTEMPTING TO STOP FLOW")
                                if action.Flow(False):
                                        print("[i] INFO: FLOW NOW INACTIVE")
                                else:
                                        print("[i] WARN: FLOW COULD NOT STOP!")
                        else:
                                print("[i] WARN: INVALID FLOW CONTROL " + SplitCommand[1])
                else:
                        print("[!] WARN: (" + RoutineList[i] + ") NOT RECOGNISED AS COMMAND.")
                        continue
