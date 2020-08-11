# diva_exp_gen
a hacky python script to convert a csv format MMD morph animation into divascript for use in the project diva series of games
Update: HUGE Thanks to YukiKami for improving the output of this tool (seriously, the changes he made makes the expressions look absolutely amazing)

# How to Use:
Load your model and motion in MMD, click on the arrow with line " >l" to go to the last keyframe from the motion, then copy paste the last frame number into the empty box above "expand". Click on expand, type 2 in "magnification" and press OK. That will expand the frames from 30 fps to 60. Then afterwards choose All facial option from the dropdown, click on range-sel and export as VMD from File > save motion data.
After you exported your facials to VMD, convert them into a CSV file using "VMDConverterGraphical".
When it has been converted, you will need to edit the CSV, so open it into for example Notepad++ and remove the first 3 lines and last 3 lines. If any of the facials have special characters like "▲" in it, that line should be deleted too, because the script can't read that character.
After you modified the CSV, save it and rename it to "mmdcommands" and make a DSC.txt. Copy paste both into the folder with test.py.
Open CMD, type "cd folder location with diva_exp_gen.py" then type "diva_exp_gen.py > DSC.txt"
Open a random .DSC file using Script Editor and copy paste everything in it into Notepad++ then remove everything after Time(0); until "PV_END();" . EXPRESSION and MOUTH_ANIM have to be deleted as well inside Time(0);. Afterwards copy the output from DSC.txt and paste it into your file in Notepad++. You will see multiple Time(0); with either EXPRESSION, MOUTH_ANIM and EYE_ANIM, so delete the duplicates and leave only one of them. After that, select all, copy paste the new content into Script Editor and save as DSC file.
