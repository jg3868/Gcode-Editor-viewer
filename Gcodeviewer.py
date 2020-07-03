import tkinter, tkinter.filedialog, tkinter.messagebox
import os
import csv

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

filetype = [("", "*.gcode")]
dirpath = os.path.abspath(os.path.dirname(__file__))
filepath = tkinter.filedialog.askopenfilename(filetypes = filetype, initialdir = dirpath)
g_line = []

def get_gcode_profile(dirpath): #CSVファイルを読み込み、Gcodeコマンド名と説明を配列で返す
    
    profile_path = (dirpath + '\data\gcode_list.csv')
    with open(profile_path,'r',encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        gcode_command = []
        gcode_mean = []
        for row in reader:
            #print(row)
            gcode_command.append(row[0])
            gcode_mean.append(row[1])
    return gcode_command,gcode_mean

def check_index(l, x, default=False): #配列検索用、一致する配列行数を返す。一致しないときはFalseを返す。　check_index(検索配列,検索文字)
    if x in l:
        return l.index(x)
    else:
        return default

#defここまで---

with open(filepath) as f:
    for temp_line in f:
        #print(temp_line)
        g_line.append(temp_line.strip())

lineNo = 0
gcode_com,gcode_mean = get_gcode_profile(dirpath)

g_line_mean = []
move_point= []
temp_point_data = [0,0,0,0,0] #(X,Y,Z,E,F)

for gcode in g_line:   #Gcodeデータ各行ごとにループ
    lineNo+=1
    if (check_index(gcode_com,(gcode.split())[0])) is not False :    #Gcode説明文をリスト化して作成。読み込んだGcodeに対応し、g_line_mean[行数]で各Gcodeの説明を取得できる。
        #print("No. ",lineNo," ",gcode," - ",gcode_mean[check_index(gcode_com,(gcode.split())[0])])
        g_line_mean.append(gcode_mean[check_index(gcode_com,(gcode.split())[0])])
    else :
        #print("No. ",lineNo,gcode)
        g_line_mean.append("")

    if (gcode.split())[0] == "G28": #G28 オートホーム時にはゼロ代入
        temp_point_data[0] = 0  #X
        temp_point_data[1] = 0  #Y
        temp_point_data[2] = 0  #Z
        move_point.append(list(temp_point_data))
    
    if (gcode.split())[0] == "G92": #G92 吐出量リセット
        temp_point_data[3] = 0  #X
        move_point.append(list(temp_point_data))

    if (gcode.split())[0] == "G0" or (gcode.split())[0] == "G1": #G0 G1の移動データから必要データを分割
        #例：G0 X12   ; move to 12mm on the X axis // G0 F1500 ; set the feedrate to 1500mm/m // G1 X90.6 Y13.8 ; move to 90.6mm on the X axis and 13.8mm on the Y axis 
        move_data = gcode.split() #一行のG1,G2データを分離する
        for data in move_data:  #各分離データに対して検討
            if data.startswith("X"):
                temp_point_data[0] = data.replace("X","")
            elif data.startswith("Y"):
                temp_point_data[1] = data.replace("Y","")
            elif data.startswith("Z"):
                temp_point_data[2] = data.replace("Z","")
            elif data.startswith("E"):
                temp_point_data[3] = data.replace("E","")
            elif data.startswith("F"):
                temp_point_data[4] = data.replace("F","")
        #print("一時データ：",temp_point_data)
        move_point.append(list(temp_point_data)) #収集した座標データを配列として保存
    #if len(move_point) is not 0:
        #print("X:",move_point[-1][0],"/ Y:",move_point[-1][1],"/ Z:",move_point[-1][2],"/ E:",move_point[-1][3],"/ F:",move_point[-1][4]) #収集した座標データを表示

x = []
y = []
z = []
#収集した座標データから重複するものを消去
for data in range(len(move_point)):
    if move_point[data] == move_point[-1]:  #最後かどうかを判別
        break

    if move_point[data] == move_point[data+1] :     #重複した場合、消去
        move_point.pop(data+1)
    
    x.append(float(move_point[data][0]))
    y.append(float(move_point[data][1]))
    z.append(float(move_point[data][2]))
    print("X:",move_point[data][0],"/ Y:",move_point[data][1],"/ Z:",move_point[data][2],"/ E:",move_point[data][3],"/ F:",move_point[data][4]) #収集した座標データを表示

# 3Dでプロット
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(x, y, z, "o-", color="red")
# 軸ラベル
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
# 表示
plt.show()