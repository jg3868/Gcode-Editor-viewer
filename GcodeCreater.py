import os
import sys


filetype = [("", "*.gcode")]
pathlist = []
filedata = []
dirpath = os.path.abspath(os.path.dirname(__file__))
pathlist.append(dirpath + '\data\Printer_Config.txt')
pathlist.append(dirpath + '\data\Start_code.txt')
pathlist.append(dirpath + '\data\End_code.txt')

def get_PrinteConfig(Raw_data) -> float: #設定ファイル読み込み
    #プリンタ機種データをtextから取得し、関数代入
    return_data = []
    print("####プリンタ設定値####")
    if [s for s in Raw_data[0] if 'BedsizeX' in s] != "":
        print([s for s in Raw_data[0] if 'BedsizeX' in s])
        return_data.append(([s for s in Raw_data[0] if 'BedsizeX' in s])[0].replace("BedsizeX:",""))
    else:
        print("ERROR/ Bedsize data X is not found.")
        sys.exit(1)

    if [s for s in Raw_data[0] if 'BedsizeY' in s] != "":
        print([s for s in Raw_data[0] if 'BedsizeY' in s])
        return_data.append(([s for s in Raw_data[0] if 'BedsizeY' in s])[0].replace("BedsizeY:",""))
    else:
        print("ERROR/ Bedsize data Y is not found.")
        sys.exit(1)

    if [s for s in Raw_data[0] if 'BedsizeZ' in s] != "":
        print([s for s in Raw_data[0] if 'BedsizeZ' in s])
        return_data.append(([s for s in Raw_data[0] if 'BedsizeZ' in s])[0].replace("BedsizeZ:",""))
    else:
        print("ERROR/ Bedsize data Z is not found.")
        sys.exit(1)

    if [s for s in Raw_data[0] if 'Nozzle_cross_section' in s] != "":
        print([s for s in Raw_data[0] if 'Nozzle_cross_section' in s])
        return_data.append(([s for s in Raw_data[0] if 'Nozzle_cross_section' in s])[0].replace("Nozzle_cross_section:",""))
    else:
        print("ERROR/ Nozzle cross section is not found.")
        sys.exit(1)

    if [s for s in Raw_data[0] if 'Layer_Height' in s] != "":
        print([s for s in Raw_data[0] if 'Layer_Height' in s])
        return_data.append(([s for s in Raw_data[0] if 'Layer_Height' in s])[0].replace("Layer_Height:",""))
    else:
        print("ERROR/ Layer Height is not found.")
        sys.exit(1)

    if [s for s in Raw_data[0] if 'Layer_Width' in s] != "":
        print([s for s in Raw_data[0] if 'Layer_Width' in s])
        return_data.append(([s for s in Raw_data[0] if 'Layer_Width' in s])[0].replace("Layer_Width:",""))
    else:
        print("ERROR/ Layer Width is not found.")
        sys.exit(1)
    
    if [s for s in Raw_data[0] if 'Pump_MAX_RPM' in s] != "":
        print([s for s in Raw_data[0] if 'Pump_MAX_RPM' in s])
        return_data.append(([s for s in Raw_data[0] if 'Pump_MAX_RPM' in s])[0].replace("Pump_MAX_RPM:",""))
    else:
        print("ERROR/ Pump_MAX_RPM is not found.")
        sys.exit(1)

    if [s for s in Raw_data[0] if 'Pump_motor_deg/step' in s] != "":
        print([s for s in Raw_data[0] if 'Pump_motor_deg/step' in s])
        return_data.append(([s for s in Raw_data[0] if 'Pump_motor_deg/step' in s])[0].replace("Pump_motor_deg/step:",""))
    else:
        print("ERROR/ Pump_motor_deg/step is not found.")
        sys.exit(1)

    if [s for s in Raw_data[0] if 'Pump_motor_reduction_ratio' in s] != "":
        print([s for s in Raw_data[0] if 'Pump_motor_reduction_ratio' in s])
        return_data.append(([s for s in Raw_data[0] if 'Pump_motor_reduction_ratio' in s])[0].replace("Pump_motor_reduction_ratio:",""))
    else:
        print("ERROR/ Pump_motor_reduction_ratio is not found.")
        sys.exit(1)

    if [s for s in Raw_data[0] if 'Travel_Speed' in s] != "":
        Travel_Speed = ([s for s in Raw_data[0] if 'Travel_Speed' in s])[0].replace("Travel_Speed:","")
        Travel_Speed = float(Travel_Speed)
        Travel_Speed = round((Travel_Speed * 60),2)
        print("Travel_Speed:",Travel_Speed)
        return_data.append(Travel_Speed)
    else:
        print("ERROR/ Travel_Speed is not found.")
        sys.exit(1)
    
    if [s for s in Raw_data[0] if 'Min_Layer_Height' in s] != "" :
        print([s for s in Raw_data[0] if 'Min_Layer_Height' in s])
        return_data.append(([s for s in Raw_data[0] if 'Min_Layer_Height' in s])[0].replace("Min_Layer_Height:",""))
    else:
        print("ERROR/ Min_Layer_Height is not found.")
        sys.exit(1)
    
    if [s for s in Raw_data[0] if 'Pump_Steps_per_unit' in s] != "":
        print([s for s in Raw_data[0] if 'Pump_Steps_per_unit' in s])
        return_data.append(([s for s in Raw_data[0] if 'Pump_Steps_per_unit' in s])[0].replace("Pump_Steps_per_unit:",""))
    else:
        print("ERROR/ Pump_Steps_per_unit is not found.")
        sys.exit(1)
    return return_data

def line_print(config_list): #壁Gcode生成
    print("####印刷設定値入力####")
    message = "直線長さ設定<mm>"+"(X_MAX:"+str(config_list[0])+"/Y_MAX:"+str(config_list[1])+"):"
    Line_length = float(input(message))
    message = "高さ設定<mm>"+"(Z_MAX:"+str(config_list[2])+"):"
    Line_hight = float(input(message))
    print("####印刷設定値####")
    print("Wall Length:",Line_length,"   Wall Hight",Line_hight)
    master_data = []

    if Line_hight > config_list[2]:#印刷長さがベッドサイズより大きくないか確認
        print("ERROR:Printing dimensions exceed the Zbed size.")  
        sys.exit(1)

    if Line_length <= config_list[0]: #印刷長さがX軸より小さい時は、X=Line_Xに
        Line_X = "X"
    elif  Line_length <= config_list[1]: #印刷長さがY軸より小さい時は、Y=Line_Xに
        Line_X = "Y"
    else:
        print("ERROR:Printing dimensions exceed the XYbed size.")
        sys.exit(1)

    if (Line_hight % config_list[5]) != 0: #レイヤー数(Total_layer_No)、最終レイヤー高さを算出(Last_layer_hight)
        #合計レイヤー数算出(割り切れない場合)
        if (Line_hight % config_list[5]) >= (config_list[5]*0.2) and not (Line_hight % config_list[5]) < config_list[10]:
            #余り高さが、設定レイヤー高さ*20%より大きい場合、レイヤー最低高さより大きい場合は、もう１レイヤー印刷する。
            Last_layer_hight = Line_hight % config_list[5]
            Total_layer_No = (Line_hight // config_list[4]) + 1 
        else:
            #余り高さが、設定レイヤー高さ*20%より小さい場合、レイヤー最低高さより小さい場合は、最終レイヤーを厚くする。
            Last_layer_hight = config_list[5]+(Line_hight % config_list[5])
            Total_layer_No = Line_hight // config_list[4]
    else:   #合計レイヤー数算出(割り切れる場合)
        Total_layer_No = Line_hight // config_list[4]   
        Last_layer_hight = config_list[4]
    
    print("Total number of layers:",Total_layer_No,"    Last Layer Hight:",Last_layer_hight)
    
    if Line_X == "X": #スタート地点にノズルを移動
        master_data.append("G0 F"+str(config_list[9])+" X"+str((config_list[0]/2)+(Line_length/2))+" Y"+str(config_list[1]/2)+" Z"+str(config_list[4])+" ;スタート地点に移動") #初期位置に移動
    else:
        master_data.append("G0 F"+str(config_list[9])+" X"+str(config_list[0]/2)+" Y"+str((config_list[1]/2)+(Line_length/2))+" Z"+str(config_list[4])) #初期位置に移動

    #設定値計算可憐
    gear_rps_max = (config_list[6]/config_list[8])/60 #ポンプ自転_RPS_最大値
    NOSteps_per_rotation = gear_rps_max*360 #一秒あたり自転角度
    Discharge_length_per_second = NOSteps_per_rotation/config_list[7]/config_list[11] #一秒間あたりの最大吐出長さ[mm]
    Dispensing_volume_per_second = config_list[3] * Discharge_length_per_second #１秒あたり最大吐出量[mm^3]
    Line_Print_Pump_Length = (config_list[4]*config_list[5]*Line_length)/config_list[3] #１レイヤーあたりの吐出長さ
    Nozzle_FEEDRATE = Dispensing_volume_per_second/(config_list[4]*config_list[5]) #ノズル移動速度[mm/s]
    #切り捨て
    Nozzle_FEEDRATE = round(Nozzle_FEEDRATE,3)
    Line_Print_Pump_Length = round(Line_Print_Pump_Length,3)
    Nozzle_FEEDRATE = Nozzle_FEEDRATE * 60 #ノズル移動速度[mm/min]
    print("ポンプ自転_回転数[RPS]:",gear_rps_max,"   一秒あたり自転角度[deg]:",NOSteps_per_rotation,"   一秒あたり吐出長さ[mm]:",Discharge_length_per_second,"     １秒あたり最大吐出量[mm^3]:",Dispensing_volume_per_second)
    print("１レイヤーあたりの吐出長さ[mm]:",Line_Print_Pump_Length,"    ノズル移動速度[mm/min]:",Nozzle_FEEDRATE,"  ノズル移動速度[mm/sec]:",Nozzle_FEEDRATE/60)

    if Line_X == "X":   #２点PointA,Bの座標を入力
        pointA = " X"+str(round((config_list[0]/2)-(Line_length/2),2))+" Y"+str(round(config_list[1]/2,2))
        pointB = " X"+str(round((config_list[0]/2)+(Line_length/2),2))+" Y"+str(round(config_list[1]/2,2))
    else:
        pointA = " X"+str(round(config_list[0]/2,2))+" Y"+str(round(config_list[1]/2-(Line_length/2),2))
        pointB = " X"+str(round(config_list[0]/2,2))+" Y"+str(round(config_list[1]/2+(Line_length/2),2))
    
    last_point = ""

    for layer in range(int(Total_layer_No)): #印刷Gcode書き出し
        if last_point == "pointA":
            master_data.append("G1 F"+str(Nozzle_FEEDRATE)+str(pointB)+" E"+str(Line_Print_Pump_Length)+" ;PointB")
            master_data.append("G0 F"+str(config_list[9])+" Z"+str((layer+2)*config_list[4])+" ;Layer "+str(layer+1))
            master_data.append("G92 E0")
            last_point = "pointB"
        else:
            master_data.append("G1 F"+str(Nozzle_FEEDRATE)+str(pointA)+" E"+str(Line_Print_Pump_Length)+" ;PointA")
            master_data.append("G0 F"+str(config_list[9])+" Z"+str((layer+2)*config_list[4])+" ;Layer "+str(layer+1))
            master_data.append("G92 E0")
            last_point = "pointA"

    print("Line_Master: ",master_data)
    return master_data

for filename in pathlist:
    #ファイル読み込み→配列代入
    with open(filename,'r',encoding="utf-8") as f:
        filedata.append([s.strip() for s in f.readlines()])

Printer_Config = get_PrinteConfig(filedata) #プリント設定を取得
#[0]=bedsize_X   [1]=bedsize_Y  [2]=bedsize_Z [3]=Nozzle_cross_section    [4]=Layer_Height     [5]=Layer_Width    [6]=Pump_MAX_RPM:   [7]=Pump_motor_deg/step:    [8]=Pump_motor_reduction_ratio  [9]=Travel_Speed [10]=Min_Layer_Height [11]=Pump_Steps_per_unit
Printer_Config =list(map(float,Printer_Config)) #プリント設定値をすべてfloatに変換

#書き出し

with open((dirpath + "\output.gcode"), mode='w') as f:
    f.write('\n'.join(filedata[1]))
    f.write('\n')
    f.write('\n'.join(line_print(Printer_Config)))
    f.write('\n')
    f.write('\n'.join(filedata[2]))