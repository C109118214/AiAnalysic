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
# 將分組的index，放入欄位，重新設定index為從0開始編號
# result = result.reset_index()
print(result)
#result.to_excel("每年每月貨品銷售額_agg.xlsx") 生成一個excel
```
![image](https://github.com/user-attachments/assets/61de3428-524d-4776-af62-c6b3c42a0117)
![agg_dict的result](https://github.com/user-attachments/assets/7f733206-7464-47f3-8a84-dc4f16c41398)
*上傳excel如果出現PermisionError可能為此Excel檔案尚未關閉，故資料無法寫入*
## 資料合併Merge
### 客戶名稱和銷售資料合併
```python
import pandas as pd

path = "資料/"
df_name = pd.read_excel(f"{path}客戶列表.xlsx") 
df_sell = pd.read_excel(f"{path}銷售資料.xlsx") 
# 上下連接，根據column相同進行連接
df = pd.merge(left = df_sell, right = df_name,
              left_on = "客戶編號", right_on = "編號") 

print(df)
#只保留客戶編號，編號刪除
df = df.drop(["編號"],axis = 1) #刪除為列
```
![image](https://github.com/user-attachments/assets/d7bfae3d-c722-4156-a925-507710b5d12d)

```python
import pandas as pd

path = "資料/"
df_name = pd.read_excel(f"{path}客戶列表.xlsx") 
df_sell = pd.read_excel(f"{path}銷售資料.xlsx") 

df_sell["年"] = df_sell["日期"].dt.year
df_sell["月"] = df_sell["日期"].dt.month
df_sell["銷售額"] = df_sell["單價"] * df_sell["數量"] #df_sell裡增加年月銷售額
df_sell_group = df_sell.groupby(["年", "月", "客戶編號"]) #df_sell合成group
result_df = df_sell_group["銷售額"].sum()

result_df = result_df.reset_index() #年/月/客戶編號加入到df

df = pd.merge(left = result_df, # 左邊放Df
              right = df_name, # 右邊放客戶姓名
              left_on = "客戶編號", # 查表對應的欄位
              right_on = "編號"
              )

print(df) # 將貨品名稱溶入進銷售資料中了

# 因為重複，所以只保留客戶編號，刪除編號
df = df.drop(["編號"], axis = 1)
```
![image](https://github.com/user-attachments/assets/10bdd489-f166-4c81-8f0b-ad9807557c5d)
## 外部合併
```python
# -*- coding: utf-8 -*-
import pandas as pd

path = "資料/"
df_sell = pd.read_excel(f"{path}銷售資料.xlsx")
df_good = pd.read_excel(f"{path}商品資料.xlsx")

df = pd.merge(left = df_sell,
              right = df_good,
              left_on = "貨品編號",
              right_on = "貨品編號"
              )

# 假設df_good中沒有A
df_good_non_A = df_good[df_good["貨品編號"] != "A"] #先去除掉A
# 預設為內部合併，兩邊有資料沒有對上，就不會被合併進來
# 只剩下875筆資料
df_2 = pd.merge(left = df_sell,
              right = df_good_non_A,
              left_on = "貨品編號",
              right_on = "貨品編號"
              )

# 以左邊的資料為準，沒有對應上的，還是保留
df_3 = pd.merge(left = df_sell,
              right = df_good_non_A,
              left_on = "貨品編號",
              right_on = "貨品編號",
              how = "left"
              )

# 以右邊的資料為準，沒有對應上的，還是保留
df_4 = pd.merge(left = df_sell,
              right = df_good_non_A,
              left_on = "貨品編號",
              right_on = "貨品編號",
              how = "right"
              )

# 以兩邊沒有對應上的都保留
df_5 = pd.merge(left = df_sell,
              right = df_good_non_A,
              left_on = "貨品編號",
              right_on = "貨品編號",
              how = "outer"
              )
```
