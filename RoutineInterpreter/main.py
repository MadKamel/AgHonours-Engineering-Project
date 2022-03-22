import action, time, configs, os

cfg = configs.Read("configs")

RoutineFile = open(cfg["routine"]+".routine")
RoutineList = RoutineFile.read().split("\n")
LogFile = open("logs.txt", "a")

def log(message):
	print(message)
	LogFile.write(message + "\n")

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
                                log("[#] LINE: " + RoutineList[i])
                        if SplitCommand[0] == "NOTE":
                                log("[@] NOTE: " + " ".join(SplitCommand[1:]))
                        elif SplitCommand[0] == "WAIT":
                                time.sleep(float(SplitCommand[1]))
                        elif SplitCommand[0] == "FLOW":
                                if SplitCommand[1] == "ON":
                                        log("[i] INFO: ATTEMPTING TO BEGIN FLOW")
                                        if action.Flow(int(cfg["output_pin"]), True):
                                                log("[i] INFO: FLOW NOW ACTIVE")
                                        else:
                                                log("[i] WARN: FLOW COULD NOT START!")
                                elif SplitCommand[1] == "OFF":
                                        log("[i] INFO: ATTEMPTING TO STOP FLOW")
                                        if action.Flow(int(cfg["output_pin"]), False):
                                                log("[i] INFO: FLOW NOW INACTIVE")
                                        else:
                                                log("[i] WARN: FLOW COULD NOT STOP!")
                                else:
                                        log("[i] WARN: INVALID FLOW CONTROL " + SplitCommand[1])
                        else:
                                log("[!] WARN: (" + RoutineList[i] + ") NOT RECOGNISED AS COMMAND.")
                                continue
except:
        log("[!] WARN: AN ERROR HAS OCCURRED, FINALISING SCRIPT PREMATURELY")
finally:
        log("[i] INFO: FINALISING ROUTINE")
        action.Finalize()
log("[i] INFO: ROUTINE FINISHED.\n\n")

os.system("./update_logs.sh")