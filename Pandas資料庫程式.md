## apply()應用cost自訂函數裡return的數據
```python
import pandas as pd

df = pd.read_excel("資料/銷售資料.xlsx")
print(df)

df_group = df.groupby("貨品編號")

def cost(data):
    print(data) # 代表每個group的單價、數量欄位(DataFrame)
    print("--------")
    return data.mean() * 0.5

apply_result = df_group[["單價", "數量"]].apply(cost)
print(apply_result)

print(df_group[["單價", "數量"]].mean())
```
## concat 資料連接
```python
import pandas as pd

path = "資料/"
df_base = pd.read_excel(f"{path}銷售資料.xlsx") #原檔案
df_ex = pd.read_excel(f"{path}擴充銷售資料.xlsx") #擴充檔案

#左右連接，根據index相同進行連接
df = pd.concat( [df_base, df_ex]) 

df["銷售額"] = df["單價"] *df["數量"] #計算銷售額

df_group = df.groupby("客戶編號")
print(df_group[["銷售額"]].sum())
```
### 左右連接
```python
# 左右連接，根據index相同進行連接
df = pd.concat( [df_base, df_ex], axis = 1 )
print(df.shape)
```
![image](https://github.com/user-attachments/assets/6eed0402-dbf6-4e86-b2c5-1a75b0a35ac1)
## 兩筆資料合併後，列出每個客戶每年每月的總銷售額
```python
import pandas as pd

path = "資料/"
df_base = pd.read_excel(f"{path}銷售資料.xlsx") #原檔案
df_ex = pd.read_excel(f"{path}擴充銷售資料.xlsx") #擴充檔案
# 上下連接，根據column相同進行連接
df = pd.concat( [df_base, df_ex]) 
df.info() #確認日期格式是不是datetime，不是的話用pd.to_datetime轉換
df["銷售額"] = df["單價"] *df["數量"] #計算銷售額
df["年"] = df["日期"].dt.year
df["月"] = df["日期"].dt.month

df_group = df.groupby(["年","月","客戶編號"])

agg_dict = {"銷售額" : ["sum", "mean"] , "數量"  : ["sum", "mean"]}
print(df_group[["銷售額"]].sum())
result = df_group.agg(agg_dict)
print(result)
#result.to_excel("每年每月貨品銷售額_agg.xlsx") 生成一個excel
```
![image](https://github.com/user-attachments/assets/61de3428-524d-4776-af62-c6b3c42a0117)
![agg_dict的result](https://github.com/user-attachments/assets/7f733206-7464-47f3-8a84-dc4f16c41398)
