with open("mmdcommands.csv") as mmd_expressions:
    with open("DivaDSC.txt") as DSC_Commands:
        for line in mmd_expressions:
            current_expression = line.split(",")
            Name = current_expression[0]
            Time = int(current_expression[1]) * 60
            Value = float(current_expression[2]) * 100
            
            
            if Name == "感嘆":
                output_command = str("TIME(" + str(Time) + "); \n" + "EXPRESSION(0, 5, " + str(str(round(Value))) + ", -1); ")
                
                print(output_command)
            elif current_expression[0] == "ヤル":
                output_command = str("TIME(" + str(Time) + "); \n" + "EXPRESSION(0, 20, " + str(str(round(Value))) + ", -1); ")
                
                print(output_command)