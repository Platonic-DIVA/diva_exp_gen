with open("mmdcommands.csv") as mmd_expressions:
    for line in mmd_expressions:
            current_expression = line.split(",")
            Name = current_expression[0]
            Time = float(current_expression[1]) / 60 * 100000
            Value = float(current_expression[2]) * 100
            FrameValue = float(current_expression[2]) * 1000
            
            if Name == "まばたき": # Eye blink
                if Value >= 50:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EYE_ANIM(0, 1, " + "50" + "); ")
                    print(output_command)
                if Value <= 50:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EYE_ANIM(0, 2, " + "100" + "); ")
                    print(output_command)
            if Name == "感嘆":
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 5, " + "50, " + str(str(round(FrameValue))) + ");")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 3, " + "50" + ", 0);")
                    print(output_command)
            if Name == "ヤル":
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 20, " + "50, " + str(str(round(FrameValue))) + ");")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 3, " + "50" + ", 0);")
                    print(output_command)
            if Name == "笑い": # Eyes - Happy
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 1, " + "50, " + str(str(round(FrameValue))) + ");")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 3, " + "50" + ", 0);")
                    print(output_command)
            if Name == "明確にする":
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 11, " + "50, " + str(str(round(FrameValue))) + ");")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 3, " + "50" + ", 0);")
                    print(output_command)
            if Name == "クール":
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 34, " + "50, " + str(str(round(FrameValue))) + ");")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 3, " + "50" + ", 0);")
                    print(output_command)
            if Name == "眩しい":
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 8, " + "50, " + str(str(round(FrameValue))) + ");")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 3, " + "50" + ", 0);")
                    print(output_command)
            if Name == "元気":
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 19, " + "50, " + str(str(round(FrameValue))) + ");")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 3, " + "50" + ", 0);")
                    print(output_command)
            if Name == "優しい":
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 12, " + "50, " + str(str(round(FrameValue))) + ");")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 3, " + "50" + ", 0);")
                    print(output_command)
            if Name == "キリッ":
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 15, " + "50, " + str(str(round(FrameValue))) + ");")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 3, " + "50" + ", 0);")
                    print(output_command)
            if Name == "くもん":
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 36, " + "50, " + str(str(round(FrameValue))) + ");")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 3, " + "50" + ", 0);")
                    print(output_command)
            if Name == "くつう":
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 37, " + "50, " + str(str(round(FrameValue))) + ");")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 3, " + "50" + ", 0);")
                    print(output_command)
            if Name == "ながし":
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 13, " + "50, " + str(str(round(FrameValue))) + ");")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 3, " + "50" + ", 0);")
                    print(output_command)
            if Name == "なき":
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 38, " + "50, " + str(str(round(FrameValue))) + ");")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 3, " + "50" + ", 0);")
                    print(output_command)
            if Name == "なやみ":
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 39, " + "50, " + str(str(round(FrameValue))) + ");")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 3, " + "50" + ", 0);")
                    print(output_command)
            if Name == "考える":
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 17, " + "50, " + str(str(round(FrameValue))) + ");")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 3, " + "50" + ", 0);")
                    print(output_command)
            if Name == "悲しい":
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 0, " + "50, " + str(str(round(FrameValue))) + ");")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 3, " + "50" + ", 0);")
                    print(output_command)
            if Name == "せつな":
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 18, " + "50, " + str(str(round(FrameValue))) + ");")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 3, " + "50" + ", 0);")
                    print(output_command)
            if Name == "アイスマイル":
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 6, " + "50, " + str(str(round(FrameValue))) + ");")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 3, " + "50" + ", 0);")
                    print(output_command)
            if Name == "強い":
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 10, " + "50, " + str(str(round(FrameValue))) + ");")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 3, " + "50" + ", 0);")
                    print(output_command)
            if Name == "ぴっくり２":
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 40, " + "50, " + str(str(round(FrameValue))) + ");")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 3, " + "50" + ", 0);")
                    print(output_command)
            if Name == "ぴっくり":
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 3, " + "50, " + str(str(round(FrameValue))) + ");")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 3, " + "50" + ", 0);")
                    print(output_command)
            if Name == "ウツロ":
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 16, " + "50, " + str(str(round(FrameValue))) + ");")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "EXPRESSION(0, 3, " + "50" + ", 0);")
                    print(output_command)
            if Name == "あ": # Mouth_A
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "MOUTH_ANIM(0, 0, 0, " + "100" + ", 1000);")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "MOUTH_ANIM(0, 0, 8, " + "100" + ", 1000);")
                    print(output_command)
            if Name == "え": # Mouth_E
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "MOUTH_ANIM(0, 0, 1, " + "100" + ", 1000);")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "MOUTH_ANIM(0, 0, 8, " + "100" + ", 1000);")
                    print(output_command)
            if Name == "い": # Mouth_I
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "MOUTH_ANIM(0, 0, 10, " + "100" + ", 1000);")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "MOUTH_ANIM(0, 0, 8, " + "100" + ", 1000); ")
                    print(output_command)
            if Name == "お": # Mouth_O
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "MOUTH_ANIM(0, 0, 2, " + "100" + ", 1000);")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "MOUTH_ANIM(0, 0, 8, " + "100" + ", 1000);")
                    print(output_command)
            if Name == "う": # Mouth_U
                if Value >= 1:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "MOUTH_ANIM(0, 0, 11, " + "100" + ", 1000);")
                    print(output_command)
                if Value <= 0:
                    output_command = str("TIME(" + str(int(Time)) + "); \n" + "MOUTH_ANIM(0, 0, 8, " + "100" + ", 1000);")
                    print(output_command)