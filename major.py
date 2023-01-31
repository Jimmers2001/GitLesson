attendanceList = [["Harry Tan", "tant2", "DarknessUnder"]]

## add your info here
attendanceList.append(["Gabriel Jacob", "jacobggit", "????"])
attendanceList.append(["Tingyi Tan", "tant", "ttan"])

## DO NOT CHANGE
printedList = open("attendanceListReal.txt", "w") 

for i in range(len(attendanceList)):
    printedList.write(str(i) + ". " + attendanceList[i][0] + "  RCS ID: " + attendanceList[i][1] + "  GitHub ID: " + attendanceList[i][2] + ";\n")

printedList.close() 