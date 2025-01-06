# 要執行重複性工作，但不確定要執行次數時使用while
## while條件迴圈
```python
while 邏輯條件式:
  指令1
    ...
  指令n
```
### 累加1到n
```python
Sum = 0
n = 5
i = 1
while i < n + 1: #i<=n同理
 Sum = Sum + i
  print("第%d圈累加結果 = %d" %(i, Sum))
  i += 1
```
### 條件迴圈產生亂數
```python
import random
ran = 1
count = 0
list1 = []
i = 1
while ran != 0 :
    ran = random.randint(0,9)
    count += 1
    list1.append(ran)
    print("新亂數:%d字串目前第%d次:%s" %(ran,count,list1))
```
![image](https://github.com/user-attachments/assets/e3383c66-f8eb-428a-9799-ea1003f077dd)
## 巢狀條件迴圈while
```python
while 邏輯條件式:
  while 邏輯條件式:
    指令1
      ...
    指令n
```
### 九九乘法表
```python
i = 1
while i < 10:
  j = 1
  while j < 10:
    print("%d乘以%d等於%2d"%(i,j,i*j),end="")
    j += 1
  print( )
  i += 1
```
# 迴圈結合break continue
## continue回到原迴圈
```python
for i in range(1,21):
  if % 3 == 0:
    continue #跳過能被3整除的回到原迴圈
  if % 10 == 0:
    break #直接離開迴圈
print(i)
```
