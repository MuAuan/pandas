import numpy as np # 数値計算
import pandas as pd # DataFrame
import matplotlib.pyplot as plt # グラフ描画
#import seaborn as sns # グラフ描画設定
from tqdm import tqdm # forループの進捗状況確認
import codecs # Shift-JIS読み込み用
#from fbprophet import Prophet # prophet
import pandas
import pandas as pd

#sns.set_style(style='ticks') # グラフスタイルの指定

years = range(1888, 2018, 10)

read_path = 'data/'

all_data = pd.DataFrame()

data1=pandas.read_csv(read_path+"data_1872.csv",encoding='Shift-JIS')

print(data1)

with codecs.open(read_path+"data_1878.csv", "r", 
                     "Shift-JIS", "ignore") as f:
    data2 = pd.read_table(
            f, delimiter=",", skiprows=5, index_col=0, 
            usecols=[0, 1, 4])
#data2.index = pd.to_datetime(data2.index)
data2.index = pd.RangeIndex(start=0, stop=len(data2), step=1)
print(data2)

data_ave = data2
data_ave.columns = ['temp', 'rain']

plt.figure(num=None, figsize=(30, 15), dpi=60)
print('Plotting Results')
plt.subplot(2, 1, 1)
plt.plot(data_ave['temp'])

plt.subplot(2, 1, 2)
plt.plot(data_ave['rain'])
plt.pause(3)
plt.savefig('plot_epoch_{0:03d}_temp.png'.format(1878), dpi=60)
plt.close()


for year in tqdm(years):
    data_file = 'data_{}.csv'.format(year)

    # 補足1：普通にpd.read_csvすると読み込めない
    with codecs.open(read_path+data_file, "r", 
                     "Shift-JIS", "ignore") as f:
        # 補足2：先頭数行のデータは使用しない．
        # また，不要なカラムは除外して利用する．
        data = pd.read_table(
            f, delimiter=",", skiprows=5, index_col=0, 
            usecols=[0, 1, 4])
        
    data.index = pd.RangeIndex(start=0, stop=len(data), step=1)
    data = data.dropna(how='all')
    data.columns = ['temp', 'rain']
    plt.figure(num=None, figsize=(30, 15), dpi=60)
    print('Plotting Results')
    plt.subplot(2, 1, 1)
    plt.plot(data['temp'])
    plt.subplot(2, 1, 2)
    plt.plot(data['rain'])
    plt.pause(3)
    plt.savefig('plot_epoch_{0:03d}_temp.png'.format(year), dpi=60)
    plt.close()

    # datetime形式に変換
    #data.index = pd.to_datetime(data.index)
    #data.index = pd.RangeIndex(start=0, stop=len(data), step=1)

    # all_dataを更新
    all_data = pd.concat([all_data, data])
    data_ave= data_ave + data
    data_ave.columns = ['temp', 'rain']
    data_ave.index = pd.RangeIndex(start=0, stop=len(data_ave), step=1)
    data_ave = data_ave.dropna(how='all')
    
    ##data.columns = ['temp', 'rain']
    plt.figure(num=None, figsize=(30, 15), dpi=60)
    print('Plotting Results')
    plt.subplot(2, 1, 1)
    plt.plot(data_ave['temp'])
    plt.subplot(2, 1, 2)
    plt.plot(data_ave['rain'])
    plt.pause(3)
    plt.savefig('plot_epoch_ave{0:03d}_temp.png'.format(year), dpi=60)
    plt.close()
    
    # カラム名を変更
    #data.columns = ['temp', 'rain']

#plt.savefig('plot_epoch_{}_temp.png'.format("1878-2018"), dpi=60)
#plt.close()
all_data.index = pd.RangeIndex(start=0, stop=len(all_data), step=1)
# 補足3：すべてNanの行は削除
all_data = all_data.dropna(how='all')
print(data)
"""
plt.figure(num=None, figsize=(30, 15), dpi=60)
print('Plotting Results')
plt.subplot(2, 1, 1)
plt.plot(all_data["temp"])
#plt.ylim(-120, 120)
#plt.ylim(-5, 45)
#plt.xlim(0, 2000)
plt.subplot(2, 1, 2)
plt.plot(all_data["rain"])
#plt.ylim(-120, 120)
#plt.ylim(0, 100)
#plt.xlim(0, 2000)
plt.pause(3)
plt.savefig('plot_epoch_{}_temp.png'.format("all_data"), dpi=60)
plt.close()

plt.figure(num=None, figsize=(30, 15), dpi=60)
print('Plotting Results')
plt.subplot(2, 1, 1)
plt.plot(data_ave["temp"])
#plt.ylim(-120, 120)
#plt.ylim(-5, 45)
#plt.xlim(0, 2000)
plt.subplot(2, 1, 2)
plt.plot(data_ave["rain"])
#plt.ylim(-120, 120)
#plt.ylim(0, 100)
#plt.xlim(0, 2000)
plt.pause(3)
plt.savefig('plot_epoch_{}_temp.png'.format("data_ave"), dpi=60)
plt.close()
"""
plt.figure(num=None, figsize=(30, 15), dpi=60)
print('Plotting Results')
plt.subplot(2, 1, 1);
plt.plot(data_ave["temp"][:365])  #plt.ylim(-120, 120)
#plt.ylim(-5, 45)
#plt.xlim(0, 2000)
plt.subplot(2, 1, 2)
plt.plot(data_ave["rain"][:365])
#plt.ylim(-120, 120)
#plt.ylim(0, 100)
#plt.xlim(0, 2000)
plt.pause(3)
plt.savefig('plot_epoch_{}_temp.png'.format("data_ave365"), dpi=60)
plt.close()

plt.figure(num=None, figsize=(30, 15), dpi=60)
print('Plotting Results')
plt.subplot(2, 1, 1);
plt.plot(data_ave["temp"][366:730])  #plt.ylim(-120, 120)
#plt.ylim(-5, 45)
#plt.xlim(0, 2000)
plt.subplot(2, 1, 2)
plt.plot(data_ave["rain"][366:730])
#plt.ylim(-120, 120)
#plt.ylim(0, 100)
#plt.xlim(0, 2000)
plt.pause(3)
plt.savefig('plot_epoch_{}_temp.png'.format("data_ave730"), dpi=60)
plt.close()

data_ave_mon=pd.DataFrame()
data_ave_mon1=pd.DataFrame()
data_ave_mon1=data_ave[:365]/14
data_ave_mon2=pd.DataFrame()
data_ave_mon2=data_ave[366:730]/14
data_ave_mon3=pd.DataFrame()
data_ave_mon3=data_ave[731:1095]/14
data_ave_mon4=pd.DataFrame()
data_ave_mon4=data_ave[1096:1460]/14
data_ave_mon5=pd.DataFrame()
data_ave_mon5=data_ave[1461:1825]/14
data_ave_mon6=pd.DataFrame()
data_ave_mon6=data_ave[1826:2190]/14
data_ave_mon7=pd.DataFrame()
data_ave_mon7=data_ave[2191:2555]/14
data_ave_mon8=pd.DataFrame()
data_ave_mon8=data_ave[2556:2920]/14
data_ave_mon9=pd.DataFrame()
data_ave_mon9=data_ave[2921:3285]/14
data_ave_mon10=pd.DataFrame()
data_ave_mon10=data_ave[3286:3650]/14

data_ave_mon2.index = pd.RangeIndex(start=0, stop=len(data_ave_mon2), step=1)
data_ave_mon3.index = pd.RangeIndex(start=0, stop=len(data_ave_mon3), step=1)
data_ave_mon4.index = pd.RangeIndex(start=0, stop=len(data_ave_mon4), step=1)
data_ave_mon5.index = pd.RangeIndex(start=0, stop=len(data_ave_mon5), step=1)
data_ave_mon6.index = pd.RangeIndex(start=0, stop=len(data_ave_mon6), step=1)
data_ave_mon7.index = pd.RangeIndex(start=0, stop=len(data_ave_mon7), step=1)
data_ave_mon8.index = pd.RangeIndex(start=0, stop=len(data_ave_mon8), step=1)
data_ave_mon9.index = pd.RangeIndex(start=0, stop=len(data_ave_mon9), step=1)
data_ave_mon10.index = pd.RangeIndex(start=0, stop=len(data_ave_mon10), step=1)

data_ave_mon=(data_ave_mon1 + data_ave_mon2 + data_ave_mon3 + data_ave_mon4 + data_ave_mon5 + data_ave_mon6 + data_ave_mon7 + data_ave_mon8+ data_ave_mon9+ data_ave_mon10 )/10
#data_ave_mon.columns = ['temp', 'rain']
#data_ave_mon=data_ave_mon+data_ave[366:730]
#data_ave_mon["rain"]=data_ave["rain"][:365]+data_ave["rain"][366:730]
#data_ave_mon.index = pd.RangeIndex(start=0, stop=len(data_ave_mon), step=1)
#data_ave_mon.columns = ['temp', 'rain']
plt.figure(num=None, figsize=(30, 15), dpi=60)
print('Plotting Results')
plt.subplot(2, 1, 1);
plt.plot(data_ave_mon1["temp"])  #plt.ylim(-120, 120)
plt.plot(data_ave_mon2["temp"])  #plt.ylim(-120, 120)
plt.plot(data_ave_mon3["temp"])  #plt.ylim(-120, 120)
plt.plot(data_ave_mon4["temp"])  #plt.ylim(-120, 120)
plt.plot(data_ave_mon5["temp"])  #plt.ylim(-120, 120)
plt.plot(data_ave_mon6["temp"])  #plt.ylim(-120, 120)
plt.plot(data_ave_mon7["temp"])  #plt.ylim(-120, 120)
plt.plot(data_ave_mon8["temp"])  #plt.ylim(-120, 120)
plt.plot(data_ave_mon9["temp"])  #plt.ylim(-120, 120)
plt.plot(data_ave_mon10["temp"])  #plt.ylim(-120, 120)
plt.ylim(0, 40)
#plt.xlim(0, 2000)
plt.subplot(2, 1, 2)
plt.plot(data_ave_mon1["rain"])
plt.plot(data_ave_mon2["rain"])
plt.plot(data_ave_mon3["rain"])
plt.plot(data_ave_mon4["rain"])
plt.plot(data_ave_mon5["rain"])
plt.plot(data_ave_mon6["rain"])
plt.plot(data_ave_mon7["rain"])
plt.plot(data_ave_mon8["rain"])
plt.plot(data_ave_mon9["rain"])
plt.plot(data_ave_mon10["rain"])
#plt.ylim(-120, 120)
plt.ylim(0, 50)
#plt.xlim(0, 2000)
plt.pause(3)
plt.savefig('plot_epoch_{}_temp.png'.format("data_ave_mon1"), dpi=60)
plt.close()

plt.figure(num=None, figsize=(30, 15), dpi=60)
print('Plotting Results')
plt.subplot(2, 1, 1);
plt.plot(data_ave_mon["temp"])  #plt.ylim(-120, 120)
plt.ylim(0, 40)
#plt.xlim(0, 2000)
plt.subplot(2, 1, 2)
plt.plot(data_ave_mon["rain"])
#plt.ylim(-120, 120)
plt.ylim(0, 50)
#plt.xlim(0, 2000)
plt.pause(3)
plt.savefig('plot_epoch_{}_temp.png'.format("data_ave_mon2"), dpi=60)
plt.close()
