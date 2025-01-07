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
|i|Sum|
|--|:--:|
|1|1|
|2|3|
|3|6|
|4|10|
|5|15|
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
## 判斷質數
```python
import datetime

Num_range = int(input("請輸入正整數："))
start_time = datetime.datetime.now()

result_list = [] # 儲存結果
# 驗證2到Num_range之間的質數
for Num in range(2, Num_range + 1):
    flag = True # 假設輸入的值是質數
    
    for i in range(2, Num):
        # 若2到Num-1之間有數字可以整除Num
        # 就不是質數
        if Num % i == 0:
            flag = False # 標註不是質數
            break # 結束迴圈
    
    # 直到最後，若Flag維持True，那這個數字就是質數
    if flag:
        result_list.append(Num)
print(result_list)
end_time = datetime.datetime.now()

print(end_time - start_time)
```
## 猜數字
```python
import random as rd
Bingo = rd.randint(1, 20) # 隨機產生1到20的答案
while True:
    Num = int(input("請輸入1到20的數字："))
    if Num == Bingo:
        print("Bingo，恭喜答對!")
        break # 答對就結束迴圈
    elif Num > Bingo:
        print("太大了，猜小一點")
    else:
        print("太小了，猜大一點")
    
```
## 樂透程式
```python
import random
Number_pool = list(range(1,43))
# 產生一個1到42的串列，模擬彩球池
result_list = []
for i in range(6):
    Number_len =  len(Number_pool)# 當下還有幾個彩球
    print(Number_pool)
    print(Number_len)
    # 抽出彩球對應的序列號(index)
    Number_index = random.randint(0, Number_len - 1)
    # 根據抽出來的序列號，選出號碼，取後不放回
    Num = Number_pool.pop(Number_index)
    #將號碼放入開獎結果
    result_list.append(Num)
print(result_list)
result_list.sort()
print(result_list)
```
## 讀書分配時間計算
```python
learning_rate = 0.4 #學習率
unknown_rate = 1 #從頭開始讀，不懂的比率
target = 0.1 #將不懂的地方降至0.1(10%)，到90%
time = 0 #準備的時間

while unknown_rate >= target:
    unknown_rate *= (1 - learning_rate)  
    time += 1 #時數加一
    
print("總共需要%.2f小時"%(time))
```
不懂的越來越少(1-學習率)
|unknown_rate|time|
|---|---|
|0.6|1|
|0.36|2|
|0.216|3|
|0.1296|4|
|0.07776|5|
## 計算存錢
```python
target = 1000000 #目標存到一百萬
annuaul_salary = 45000 * 12 #年薪
annuaul_cost = 30000*12 #每年支出
salary_growth_rate = 0.05 #薪水成長率
cost_growth_rate = 0.02 #支出漲幅
interest_rate = 0.01 #存款投資率

deposit = 0 #存入
year_count = 0 #存了的時間
#存款未達到目標就繼續存錢
while deposit < target:
    year_count += 1
    #年初的存款
    deposit += annuaul_salary - annuaul_cost
    
    #進行複利與成長
    annuaul_salary *= (1 + salary_growth_rate)
    annuaul_cost *= (1 + cost_growth_rate)
    deposit += (1 + interest_rate)
print("需要%d年達標"%(year_count))
```
