# 路徑
## w 寫入,"w"
## 絕對路徑
```python
#f = open("C:/Users/USER/Desktop/GamingTime/test2.txt", "w") 斜線/
#f = open("C:\\Users\\USER\\Desktop\\GamingTime\\test3.txt","w") 雙反斜線\\
```
# 相對路徑
```python
f = open("outputs/test.txt", "w")
f.write("第一行\n")
f.write("第二行")
f.close() # 關閉檔案
```
