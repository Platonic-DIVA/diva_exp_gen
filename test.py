with open("mmdcommands.csv") as mmd_expressions:
    with open("DivaDSC.txt") as DSC_Commands:
        for line in mmd_expressions:
            current_expression = line.split(",")
            Name = current_expression[0]
            Time = int(current_expression[1]) * 600
            Value = float(current_expression[2]) * 100
            
            if Name == "まばたき":
                if Value >= 50:
                    output_command = str("TIME(" + str(Time) + "); \n" + "EYE_ANIM(0, 1, " + str(round(float(Time / (Value + 1)) / 10)) + "); ")
                    print(output_command)
                if Value <= 50:
                    output_command = str("TIME(" + str(Time) + "); \n" + "EYE_ANIM(0, 2, " + str(round(float(Time / (Value + 1)) / 1000)) + "); ")
                    print(output_command)
            if Name == "感嘆":
                output_command = str("TIME(" + str(Time) + "); \n" + "EXPRESSION(0, 5, " + str(str(round(Value))) + ", -1); ")
                
                print(output_command)
            if Name == "ヤル":
                output_command = str("TIME(" + str(Time) + "); \n" + "EXPRESSION(0, 20, " + str(str(round(Value))) + ", -1); ")
                
                print(output_command)
            if Name == "笑い":
                output_command = str("TIME(" + str(Time) + "); \n" + "EXPRESSION(0, 1, " + str(str(round(Value))) + ", -1); ")
                
                print(output_command)
            if Name == "明確にする":
                output_command = str("TIME(" + str(Time) + "); \n" + "EXPRESSION(0, 11, " + str(str(round(Value))) + ", -1); ")
                
                print(output_command)
            if Name == "クール":
                output_command = str("TIME(" + str(Time) + "); \n" + "EXPRESSION(0, 34, " + str(str(round(Value))) + ", -1); ")
                
                print(output_command)
            if Name == "眩しい":
                output_command = str("TIME(" + str(Time) + "); \n" + "EXPRESSION(0, 8, " + str(str(round(Value))) + ", -1); ")
                
                print(output_command)
            if Name == "元気":
                output_command = str("TIME(" + str(Time) + "); \n" + "EXPRESSION(0, 19, " + str(str(round(Value))) + ", -1); ")
                
                print(output_command)
            if Name == "優しい":
                output_command = str("TIME(" + str(Time) + "); \n" + "EXPRESSION(0, 12, " + str(str(round(Value))) + ", -1); ")
                
                print(output_command)
            if Name == "キリッ":
                output_command = str("TIME(" + str(Time) + "); \n" + "EXPRESSION(0, 15, " + str(str(round(Value))) + ", -1); ")
                
                print(output_command)
            if Name == "くもん":
                output_command = str("TIME(" + str(Time) + "); \n" + "EXPRESSION(0, 36, " + str(str(round(Value))) + ", -1); ")
                
                print(output_command)
            if Name == "くつう":
                output_command = str("TIME(" + str(Time) + "); \n" + "EXPRESSION(0, 37, " + str(str(round(Value))) + ", -1); ")
                
                print(output_command)
            if Name == "ながし":
                output_command = str("TIME(" + str(Time) + "); \n" + "EXPRESSION(0, 13, " + str(str(round(Value))) + ", -1); ")
                
                print(output_command)
            if Name == "なき":
                output_command = str("TIME(" + str(Time) + "); \n" + "EXPRESSION(0, 38, " + str(str(round(Value))) + ", -1); ")
                
                print(output_command)
            if Name == "なやみ":
                output_command = str("TIME(" + str(Time) + "); \n" + "EXPRESSION(0, 39, " + str(str(round(Value))) + ", -1); ")
                
                print(output_command)
            if Name == "考える":
                output_command = str("TIME(" + str(Time) + "); \n" + "EXPRESSION(0, 17, " + str(str(round(Value))) + ", -1); ")
                
                print(output_command)
            if Name == "悲しい":
                output_command = str("TIME(" + str(Time) + "); \n" + "EXPRESSION(0, 0, " + str(str(round(Value))) + ", -1); ")
                
                print(output_command)
            if Name == "せつな":
                output_command = str("TIME(" + str(Time) + "); \n" + "EXPRESSION(0, 18, " + str(str(round(Value))) + ", -1); ")
                
                print(output_command)
            if Name == "アイスマイル":
                output_command = str("TIME(" + str(Time) + "); \n" + "EXPRESSION(0, 6, " + str(str(round(Value))) + ", -1); ")
                
                print(output_command)
            if Name == "強い":
                output_command = str("TIME(" + str(Time) + "); \n" + "EXPRESSION(0, 10, " + str(str(round(Value))) + ", -1); ")
                
                print(output_command)
            if Name == "ぴっくり２":
                output_command = str("TIME(" + str(Time) + "); \n" + "EXPRESSION(0, 40, " + str(str(round(Value))) + ", -1); ")
                
                print(output_command)
            if Name == "ぴっくり":
                output_command = str("TIME(" + str(Time) + "); \n" + "EXPRESSION(0, 3, " + str(str(round(Value))) + ", -1); ")
                
                print(output_command)
            if Name == "ウツロ":
                output_command = str("TIME(" + str(Time) + "); \n" + "EXPRESSION(0, 16, " + str(str(round(Value))) + ", -1); ")
                
                print(output_command)