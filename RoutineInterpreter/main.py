import action, time, configs

cfg = configs.Read("configs")

RoutineFile = open(cfg["routine"]+".routine")
RoutineList = RoutineFile.read().split("\n")

try:
        action.InitPump(int(cfg["output_pin"]))
        for i in range(len(RoutineList)):
                SplitCommand = RoutineList[i].split(" ")
                if SplitCommand[0] == "#":
                        continue
                elif SplitCommand[0] == "":
                        continue
                else:
                        if cfg["debug"] == "yes":
                                print("[#] LINE: " + RoutineList[i])
                        if SplitCommand[0] == "NOTE":
                                print("[@] NOTE: " + " ".join(SplitCommand[1:]))
                        elif SplitCommand[0] == "WAIT":
                                time.sleep(float(SplitCommand[1]))
                        elif SplitCommand[0] == "FLOW":
                                if SplitCommand[1] == "ON":
                                        print("[i] INFO: ATTEMPTING TO BEGIN FLOW")
                                        if action.Flow(int(cfg["output_pin"]), True):
                                                print("[i] INFO: FLOW NOW ACTIVE")
                                        else:
                                                print("[i] WARN: FLOW COULD NOT START!")
                                elif SplitCommand[1] == "OFF":
                                        print("[i] INFO: ATTEMPTING TO STOP FLOW")
                                        if action.Flow(int(cfg["output_pin"]), False):
                                                print("[i] INFO: FLOW NOW INACTIVE")
                                        else:
                                                print("[i] WARN: FLOW COULD NOT STOP!")
                                else:
                                        print("[i] WARN: INVALID FLOW CONTROL " + SplitCommand[1])
                        else:
                                print("[!] WARN: (" + RoutineList[i] + ") NOT RECOGNISED AS COMMAND.")
                                continue
except:
        print("[!] WARN: AN ERROR HAS OCCURRED, FINALISING SCRIPT PREMATURELY")
finally:
        print("[i] INFO: FINALISING ROUTINE")
        action.Finalize()
print("[i] INFO: ROUTINE FINISHED.")