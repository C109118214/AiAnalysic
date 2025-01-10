## 計算此買賣方法是否獲利
```python
import pandas as pd
import pylab
pylab.show()
df = pd.read_excel("0050.xlsx")

# 買賣價格
df["隔日開盤價"] = df["開盤價"].shift(-1)
df["賣出收盤價"] = df["收盤價"].shift(-5) #幾天後賣出
# 刪除沒有買賣價格的資料
df = df.dropna(subset = ["隔日開盤價", "賣出收盤價"])

# 篩選符合進場條件的資料
df = df[(df["收盤價"] > 135) & (df["最低價"] > 133)]

# 計算買賣獲利
df["損益"] = (df["賣出收盤價"] - df["隔日開盤價"]) * 1000
print("總損益",df["損益"].sum())
print("平均損益",df["損益"].mean())
print("交易次數",df["損益"].count())
```
![image](https://github.com/user-attachments/assets/d5eaf5f9-943a-497b-a4d9-b7e6263d30bf)
## 加入台灣買股後的手續費
```python
import pandas as pd

df = pd.read_excel("0050.xlsx")

# 買賣價格
df["隔日開盤價"] = df["開盤價"].shift(-1)
df["賣出收盤價"] = df["收盤價"].shift(-5) #幾天後賣出
# 刪除沒有買賣價格的資料
df = df.dropna(subset = ["隔日開盤價", "賣出收盤價"])

# 篩選符合進場條件的資料
df = df[ df["收盤價"] < 130 ]
# 交易成本分成手續費與證交稅
# 台灣交易手續費：0.001425，最低20元，券商可以打折，假設打五折
# 證交稅：0.003
# 手續費在買賣都要付，交易稅只有在賣出時需要付
# 計算時，交易成本視為成本的加項，收入的減項
#df["隔日開盤價"] *= (1 + 0.001425 * 0.5)
#df["賣出收盤價"] *= (1 - 0.001425 * 0.5 - 0.003)

# 計算買賣獲利
df["損益"] = (df["賣出收盤價"] - df["隔日開盤價"]) * 1000
print(df["隔日開盤價"],df["賣出收盤價"],df["損益"])
print("總損益", df["損益"].sum())
print("平均損益", df["損益"].mean())
print("交易次數",df["損益"].count())
```
### 加入手續費
![image](https://github.com/user-attachments/assets/358a1be6-8510-441e-811d-301c525baf69)
### 沒有算手續費
![image](https://github.com/user-attachments/assets/c2586010-f430-4bd5-a233-edecea7ce9fd)
```python
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.size"] = 15
plt.rcParams["font.family"] = ["Arial","DFKai-SB"] #標楷體無法顯示負號，用list前面加英文字體

df = pd.read_excel("0050繪圖.xlsx")
#df.plot(x = "日期",y = "收盤價")
#df.plot(x = "日期",y = ["開盤價","收盤價"])

df["日期"] = pd.to_datetime( df["日期"] )
# %Y代表四位數的西元年
# %m代表月份，把月份補0到二位數
# %d代表日，補0到二位數
df["日期"] = df["日期"].dt.strftime("%m-%d")
df.info() 
df.plot(kind = "line",
#line折線圖 bar長條圖"barh"為長條圖橫向horizontal"hist", #直方圖"scatter"點分布
        x = "日期",
        y = ["開盤價","收盤價"]
        )
plt.title("開盤價與收盤價") #加上標題
plt.xlabel("日期") #x座標名稱顯示
plt.ylabel("價格") #y座標名稱顯示
#plt.show()
plt.show()
```
![image](https://github.com/user-attachments/assets/f5e44c45-fb61-4f26-b5e8-0f627c174279)
## 圓餅圖
```python
import pylab
import pandas as pd
pylab.show()
data_dict = {
    "項目" : ["0-19", "20-39", "40-64", "65以上"],
    "人數" : [20, 40, 50, 30]
    }

df = pd.DataFrame(data_dict )
# 因為會自動把index當成圖例，所以把index指定成項目欄位
df.index = df["項目"]
df["人數"].plot(kind = "pie",
              autopct='%1.2f%%') # 顯示百分比
```
![image](https://github.com/user-attachments/assets/e5d61f61-cfe5-474d-bddb-48e6be41374b)
## scatter
```python
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.size"] = 10
plt.rcParams["font.family"] = "DFKai-SB"

df = pd.read_excel("0050.xlsx")

df["日期"] = pd.to_datetime( df["日期"] )
# %Y代表四位數的西元年
# %m代表月份，把月份補0到二位數
# %d代表日，補0到二位數
df["日期"] = df["日期"].dt.strftime("%m-%d")
df.info()

df.plot(kind = "scatter",
        x = "開盤價",
        y = "收盤價"
        )
plt.title("開盤價與收盤價")
plt.xlabel("開盤價")
plt.ylabel("收盤價")
plt.show()
```
![image](https://github.com/user-attachments/assets/1a3e77d1-f658-4738-91b1-20ad90ab6f0e)
## K線圖
```python
import mplfinance as fplt
import pandas as pd

df= pd.read_excel("0050繪圖.xlsx")
df["日期"]=pd.to_datetime(df["日期"])
df.index = df["日期"]
#重新命名欄位，以符合fplt格式
df.rename(columns = 
{"開盤價":"Open","最高價":"High","最低價":"Low","收盤價":"Close","成交股數":"Volume"},inplace = True)
fplt.plot(df,type = "candle") #蠟燭K線圖
```
![image](https://github.com/user-attachments/assets/6511f740-f4fe-4e2b-9399-9f3dccaa177d)
## K線美化
```python
import mplfinance as fplt
import pylab
import pandas as pd
pylab.show()

df = pd.read_excel("0050繪圖.xlsx")
df["日期"] = pd.to_datetime(df["日期"])
df.index = df["日期"]
# 重新命名欄位，以符合fplt的格式
df.rename(columns = {"開盤價" : "Open",
                "最高價" : "High",
                "最低價" : "Low",
                "收盤價" : "Close",
                "成交股數" : "Volume"
                }, inplace = True)
# 調整圖表標示顏色
mc = fplt.make_marketcolors(
                            up = 'tab:red',down = 'tab:green', # 上漲為紅，下跌為綠
                            wick = {'up':'red','down':'green'}, # 影線上漲為紅，下跌為綠
                            volume = 'tab:blue', # 交易量顏色
                           )

# 定義圖表風格
s = fplt.make_mpf_style(marketcolors = mc,
                        rc = {
                            'font.size': 10, #文字大小
                            "font.family":['sans-serif', "Microsoft JhengHei"] # 字型
                        }
                    ) 

fplt.plot(
            df, # 開高低收量的資料
            type = 'candle', # 類型為蠟燭圖，也就是 K 線圖
            style = s, # 套用圖表風格
            title = "0050", # 設定圖表標題
            ylabel = '價格', # 設定 Y 軸標題
            volume = True,
            savefig='K線圖/stock_Kbar.png', # 儲存檔案
        )
```
![image](https://github.com/user-attachments/assets/cdfb6cb9-5b1c-4f1b-9200-15eabbd1cbdc)
