with open("mmdcommands.csv") as mmd_expressions:
    with open("DivaDSC.txt") as DSC_Commands:
        for line in mmd_expressions:
            current_expression = line.split(",")
            if current_expression[0] == "感嘆":
                output_command = str("TIME(" + str(int(current_expression[1]) * 60) + "); \n" + "EXPRESSION(0, 5, " + str(float(current_expression[2]) * 100) + ", -1); ")
                
                print(output_command)
            elif current_expression[0] == "ヤル":
                output_command = str("TIME(" + str(int(current_expression[1]) * 60) + "); \n" + "EXPRESSION(0, 20, " + str(float(current_expression[2]) * 100) + ", -1); ")
                
                print(output_command)