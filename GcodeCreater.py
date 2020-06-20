import os
import sys

filetype = [("", "*.gcode")]
pathlist = []
filedata = []
dirpath = os.path.abspath(os.path.dirname(__file__))
pathlist.append(dirpath + '\data\Printer_Config.txt')
pathlist.append(dirpath + '\data\Start_code.txt')
pathlist.append(dirpath + '\data\End_code.txt')

def get_PrinteConfig(Raw_data): #設定ファイル読み込み
    #プリンタ機種データをtextから取得し、関数代入
    if [s for s in Raw_data[0] if 'BedsizeX' in s] != "":
        print([s for s in Raw_data[0] if 'BedsizeX' in s])
        bedsize_X = ([s for s in Raw_data[0] if 'BedsizeX' in s])[0].replace("BedsizeX:","")
    else:
        print("ERROR/ Bedsize data X is not found.")
        sys.exit(1)

    if [s for s in Raw_data[0] if 'BedsizeY' in s] != "":
        print([s for s in Raw_data[0] if 'BedsizeY' in s])
        bedsize_Y = ([s for s in Raw_data[0] if 'BedsizeY' in s])[0].replace("BedsizeY:","")
    else:
        print("ERROR/ Bedsize data Y is not found.")
        sys.exit(1)

    if [s for s in Raw_data[0] if 'BedsizeZ' in s] != "":
        print([s for s in Raw_data[0] if 'BedsizeZ' in s])
        bedsize_Z = ([s for s in Raw_data[0] if 'BedsizeZ' in s])[0].replace("BedsizeZ:","")
    else:
        print("ERROR/ Bedsize data Z is not found.")
        sys.exit(1)

    if [s for s in Raw_data[0] if 'Nozzle_cross_section' in s] != "":
        print([s for s in Raw_data[0] if 'Nozzle_cross_section' in s])
        Nozzle_cross_section = ([s for s in Raw_data[0] if 'Nozzle_cross_section' in s])[0].replace("Nozzle_cross_section:","")
    else:
        print("ERROR/ Nozzle cross section is not found.")
        sys.exit(1)

    if [s for s in Raw_data[0] if 'Layer_Height' in s] != "":
        print([s for s in Raw_data[0] if 'Layer_Height' in s])
        Layer_Height = ([s for s in Raw_data[0] if 'Layer_Height' in s])[0].replace("Layer_Height:","")
    else:
        print("ERROR/ Layer Height is not found.")
        sys.exit(1)

    if [s for s in Raw_data[0] if 'Layer_Width' in s] != "":
        print([s for s in Raw_data[0] if 'Layer_Width' in s])
        Layer_Width = ([s for s in Raw_data[0] if 'Layer_Width' in s])[0].replace("Layer_Width:","")
    else:
        print("ERROR/ Layer Width is not found.")
        sys.exit(1)
    
    if [s for s in Raw_data[0] if 'Pump_MAX_RPM' in s] != "":
        print([s for s in Raw_data[0] if 'Pump_MAX_RPM' in s])
        Pump_MAX_RPM = ([s for s in Raw_data[0] if 'Pump_MAX_RPM' in s])[0].replace("Pump_MAX_RPM:","")
    else:
        print("ERROR/ Pump_MAX_RPM is not found.")
        sys.exit(1)

    if [s for s in Raw_data[0] if 'Pump_motor_deg/step' in s] != "":
        print([s for s in Raw_data[0] if 'Pump_motor_deg/step' in s])
        Pump_motor_deg = ([s for s in Raw_data[0] if 'Pump_motor_deg/step' in s])[0].replace("Pump_motor_deg/step:","")
    else:
        print("ERROR/ Pump_motor_deg/step is not found.")
        sys.exit(1)

    if [s for s in Raw_data[0] if 'Travel_Speed' in s] != "":
        print([s for s in Raw_data[0] if 'Travel_Speed' in s])
        Travel_Speed = ([s for s in Raw_data[0] if 'Travel_Speed' in s])[0].replace("Travel_Speed:","")
        Travel_Speed = Travel_Speed * 60
    else:
        print("ERROR/ Travel_Speed is not found.")
        sys.exit(1)

    #print("Printer size/X:",bedsize_X,"/Y:",bedsize_Y,"/Z:",bedsize_Z,"/Layer_Height:",Layer_Height,"/Layer_Width:",Layer_Width)
    #print("Nozzle_cross_section:",Nozzle_cross_section,"/Pump_MAX_RPM:",Pump_MAX_RPM,"/Pump_motor_deg/step:",Pump_motor_deg,"/Pump_motor_reduction_ratio:",Pump_motor_reduction_ratio)
    return bedsize_X,bedsize_Y,bedsize_Z,Layer_Height,Layer_Width,Nozzle_cross_section,Pump_MAX_RPM,Pump_motor_deg,Pump_motor_reduction_ratio,Travel_Speed

def line_print(bedsize_X,bedsize_Y,bedsize_Z,Layer_Height,Layer_Width,Nozzle_cross_section,Pump_MAX_RPM,Pump_motor_deg,Pump_motor_reduction_ratio,Travel_Speed):
    master_data = []
    master_data.append("")

for filename in pathlist:
    #ファイル読み込み→配列代入
    with open(filename,'r',encoding="utf-8") as f:
        filedata.append([s.strip() for s in f.readlines()])

bedsize_X,bedsize_Y,bedsize_Z,Layer_Height,Layer_Width,Nozzle_cross_section,Pump_MAX_RPM,Pump_motor_deg,Pump_motor_reduction_ratio,Travel_Speed = get_PrinteConfig(filedata) #プリント設定を取得
print("Printer size/X:",bedsize_X,"/Y:",bedsize_Y,"/Z:",bedsize_Z,"/Layer_Height:",Layer_Height,"/Layer_Width:",Layer_Width)
print("Nozzle_cross_section:",Nozzle_cross_section,"/Pump_MAX_RPM:",Pump_MAX_RPM,"/Pump_motor_deg/step:",Pump_motor_deg,"/Pump_motor_reduction_ratio:",Pump_motor_reduction_ratio)