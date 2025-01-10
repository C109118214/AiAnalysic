# 以客戶編號分組
```python
import pandas as pd

df = pd.read_excel("資料/銷售資料.xlsx")
print(df)

df_group = df.groupby(by = ["客戶編號"]) 
print(df_group)
#分組
group_keys = df_group.groups.keys() 
print(group_keys)
for k in group_keys:
    print(k,df_group.get_group(k))
```
![image](https://github.com/user-attachments/assets/2b4dbe0b-2283-4ee4-8df8-3d71e33f65c0)
```python
import pandas as pd
df = pd.read_excel("資料/銷售資料.xlsx")
df_group = df.groupby(by = ["客戶編號"]) 
#分組
group_keys = df_group.groups.keys() 
df["總銷售額"] = df["單價"]*df["數量"]
print(df_group[["總銷售額", "數量"]].sum())
print(df_group[["總銷售額", "數量"]].mean()) #agg合併
```
## agg合併
```python
agg_dict = {"單價" : ['mean'],
            "數量" : ['sum','mean']
            }
agg_result = df_group.agg(agg_dict)
print(agg_result)
print("------------")
```
