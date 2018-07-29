import numpy as np # 数値計算
import pandas as pd # DataFrame
import matplotlib.pyplot as plt # グラフ描画
from tqdm import tqdm # forループの進捗状況確認
import codecs # Shift-JIS読み込み用
import pandas


years = range(1878, 2018, 10)
read_path = 'data/temp/'
all_data = pd.DataFrame()

data1=pandas.read_csv(read_path+"data_1872.csv",encoding='Shift-JIS')
print(data1)

for year in tqdm(years):
    data_file = 'data_{}.csv'.format(year)

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
           
    # all_dataを更新
    data_ave= data
    data_ave.columns = ['temp', 'rain']
    data_ave.index = pd.RangeIndex(start=0, stop=len(data_ave), step=1)
    data_ave = data_ave.dropna(how='all')
    
    data_mon=pd.DataFrame()
    data_mon1=pd.DataFrame()
    data_mon1=data_ave[:365]
    data_mon2=pd.DataFrame()
    data_mon2=data_ave[366:730]
    data_mon3=pd.DataFrame()
    data_mon3=data_ave[731:1095]
    data_mon4=pd.DataFrame()
    data_mon4=data_ave[1096:1460]
    data_mon5=pd.DataFrame()
    data_mon5=data_ave[1461:1825]
    data_mon6=pd.DataFrame()
    data_mon6=data_ave[1826:2190]
    data_mon7=pd.DataFrame()
    data_mon7=data_ave[2191:2555]
    data_mon8=pd.DataFrame()
    data_mon8=data_ave[2556:2920]
    data_mon9=pd.DataFrame()
    data_mon9=data_ave[2921:3285]
    data_mon10=pd.DataFrame()
    data_mon10=data_ave[3286:3650]

    data_mon2.index = pd.RangeIndex(start=0, stop=len(data_mon2), step=1)
    data_mon3.index = pd.RangeIndex(start=0, stop=len(data_mon3), step=1)
    data_mon4.index = pd.RangeIndex(start=0, stop=len(data_mon4), step=1)
    data_mon5.index = pd.RangeIndex(start=0, stop=len(data_mon5), step=1)
    data_mon6.index = pd.RangeIndex(start=0, stop=len(data_mon6), step=1)
    data_mon7.index = pd.RangeIndex(start=0, stop=len(data_mon7), step=1)
    data_mon8.index = pd.RangeIndex(start=0, stop=len(data_mon8), step=1)
    data_mon9.index = pd.RangeIndex(start=0, stop=len(data_mon9), step=1)
    data_mon10.index = pd.RangeIndex(start=0, stop=len(data_mon10), step=1)
    
    data_mon=(data_mon1 + data_mon2 + data_mon3 + data_mon4 + data_mon5 + data_mon6 + data_mon7 + data_mon8+ data_mon9+ data_mon10 )/10
    
    all_data = pd.concat([all_data, data_mon])
    
    plt.figure(num=None, figsize=(30, 15), dpi=60)
    print('Plotting Results')
    plt.subplot(2, 1, 1);
    plt.plot(data_mon1["temp"])  #plt.ylim(-120, 120)
    plt.plot(data_mon2["temp"])  #plt.ylim(-120, 120)
    plt.plot(data_mon3["temp"])  #plt.ylim(-120, 120)
    plt.plot(data_mon4["temp"])  #plt.ylim(-120, 120)
    plt.plot(data_mon5["temp"])  #plt.ylim(-120, 120)
    plt.plot(data_mon6["temp"])  #plt.ylim(-120, 120)
    plt.plot(data_mon7["temp"])  #plt.ylim(-120, 120)
    plt.plot(data_mon8["temp"])  #plt.ylim(-120, 120)
    plt.plot(data_mon9["temp"])  #plt.ylim(-120, 120)
    plt.plot(data_mon10["temp"])  #plt.ylim(-120, 120)
    plt.ylim(0, 40)
    #plt.xlim(0, 365)
    plt.subplot(2, 1, 2)
    plt.plot(data_mon1["rain"])
    plt.plot(data_mon2["rain"])
    plt.plot(data_mon3["rain"])
    plt.plot(data_mon4["rain"])
    plt.plot(data_mon5["rain"])
    plt.plot(data_mon6["rain"])
    plt.plot(data_mon7["rain"])
    plt.plot(data_mon8["rain"])
    plt.plot(data_mon9["rain"])
    plt.plot(data_mon10["rain"])
    
    plt.ylim(0, 200)
    #plt.xlim(0, 365)
    plt.pause(3)
    plt.savefig('plot_epoch_{}_year_temp.png'.format(year), dpi=60)
    plt.close()
    

    plt.figure(num=None, figsize=(30, 15), dpi=60)
    print('Plotting Results')
    plt.subplot(2, 1, 1);
    plt.plot(data_mon["temp"])  #plt.ylim(-120, 120)
    plt.ylim(0, 40)
    #plt.xlim(0, 365)
    plt.subplot(2, 1, 2)
    plt.plot(data_mon["rain"])
    plt.ylim(0, 50)
    
    plt.pause(3)
    plt.savefig('plot_epoch_{}_ave_year.png'.format(year), dpi=60)
    plt.close()

print(all_data[:365])    
all_data[:365].plot("temp")
plt.figure(num=None, figsize=(30, 15), dpi=60)
print('Plotting Results')
plt.subplot(2, 1, 1);
plt.plot(all_data["temp"])  #plt.ylim(-120, 120)
plt.ylim(0, 40)
#plt.xlim(0, 365)
plt.subplot(2, 1, 2)
plt.plot(all_data["rain"])
#plt.ylim(-120, 120)
plt.ylim(0, 50)
#plt.xlim(0, 365)
plt.pause(3)
plt.savefig('plot_epoch_{}_allpandas_year.png'.format(year), dpi=60)
plt.close()
#plt.savefig('plot_epoch_{0:03d}_pandas.png'.format(1878), dpi=60)
