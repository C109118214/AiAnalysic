# For迴圈是給知道執行次數的重複結構
## 單一For迴圈
```python
for 計數器 in range (start, end, step):
  指令1
    ...
  指令n
```
### 範例
```python
for i in range(1,6): #1數到6
for i in range(7): #0數到7
  print(i) #0到7
  print(f"{i} / 6 = ", i / 6) #0除以6~~7除以6
for i in (25,0,-5) #從25到0遞減迴圈
print(sum(range(1,30,2)) #印出從1到30所有奇數的加總
```
## 印出從1到30所有奇數的加總
```python
#方法一
print(sum(range(1,30,2)) #印出從1到30所有奇數的加總 
#方法二
sum = 0
for i in range(1,30,2): #1數到30間隔2(所有奇數)
    sum += i 
    print ("%s累加%d為%s"%(sum-i,i,sum)) #前一個Sum,加的數字,加總為
#方法三
n = int(input("Input an integer:"))
sum = 0
for i in range(1 , n+1, 2):
    sum += i #sum *= i #N階乘
    print("%s累加%d為%s"%(sum-i,i,sum))
```
![image](https://github.com/user-attachments/assets/f5973f6d-5d8e-4e76-93f2-892f8860a6fd)
## 費式數列(for 迴圈)
```python
list = [1,1]
n = int(input("Input an integer:"))
for i in range(n-2): #原先已有第一第二項/i為次數沒用到i
    num = list[-1] + list[-2] #最後一項相加最後第二項
    list.append(num)  #相加結果加入到串列最後一項
    print(num ,list) #加入的最後一項, 串列狀況
```
![image](https://github.com/user-attachments/assets/46c4b56d-edc2-4b48-ac44-fa093483754c)
## 因數
```python
#方法一
num = 0 #數因數
count = 0 #數第幾項
list1=[] #先訂一個空串列
for i in range(1,100):
    if i % 5 == 0 and i % 7 == 0: #找5和7的共同倍數
        count += 1 #項數加一
        num += i #下一個公倍數
        list1.append(i) #增加到原本的串列
        print("串列為%s加總為%s第%s項"%(list1,num,count))
#方法二
list1=[]
for i in range(1,100):
    if i % 5 == 0 and i % 3 == 0:
        list1.append(i)
        #print("目前串列為%s加總為%s第%s項"%(list1,num,count))
print("最終串列為%s共有%s項加總為%s"%(list1,len(list1),sum(list1))) #len算長度=總數量sum算總和
```
![image](https://github.com/user-attachments/assets/a2d2e1fe-68ed-45cf-b9cd-662182f0a6ac)
## 字串反轉
```python
#方法一
String = list(input("Input a string:"))
length = len(String) #計算字串的長度
for i in range(length - 1,-1,-1): #字串-1為最後一位數位置(字串第一項為第0項),-1+1到0第一項,-1倒數
    print(String[i],end = "")
#方法二
Stringrev = id_list[::-1] #反轉串列
print(Stringrev) #印出結果
```
## 投骰子
```python
import random 
num = int(input("The times you roll the dice:"))
Dice = [0] * 6 #產生六個空位
#統計6個點數各自出現的次數和機率
for i in range(num):
    outcome = random.randint(1,6)
    #outcome出現過一次隨機亂數後-1次亂數產生要的次數並多印出一個串列結果
    Dice[outcome - 1] += 1
    #印出6點出現的次數與機率
    #print(Dice)
for i in range(len(Dice)):
    print("%d點,出現%d次,出線機率為%.2f"%(i+1,Dice[i],Dice[i]/num)) #四捨五入到小數點第二位
```
![image](https://github.com/user-attachments/assets/56435e9d-94ec-4ac3-aeae-e6b743ebeb19)
## CP值計算
```python
shop_name_list = ["M", "K", "B"]
score_list = [60, 85, 90]
price_list = [145, 200, 220]
CP_ratio_list = []

for i in range(len(shop_name_list)):
    CP_ratio = score_list[i] / price_list[i]
    CP_ratio_list.append(CP_ratio)

print(CP_ratio_list)

Max_CP = max(CP_ratio_list)
print(Max_CP)
# 查看CP值最高的索引號是多少
Max_CP_index = CP_ratio_list.index(Max_CP)
print(Max_CP_index)

print("CP值最高的速食店為", shop_name_list[Max_CP_index])
```
![image](https://github.com/user-attachments/assets/c5804021-b582-489b-bf16-69d06da8b265)
## 一番賞獎
```python
import random as rd

# 一番賞抽獎
prize_list = ["D"] * 5 + ["C"] * 3 + ["B"] * 2 + ["A"]
print(prize_list)

Num = int(input("請輸入抽幾次："))
get_prize_list = []
for i in range(Num):
    # 查看獎池裡面還有多少
    prize_len = len(prize_list)
    prize_index = rd.randint(0, prize_len-1)
    prize = prize_list.pop(prize_index)
    print(prize_list)
    print(prize_len , prize_index, prize)
    get_prize_list.append(prize)
print(get_prize_list)
```
![image](https://github.com/user-attachments/assets/0fdc8925-b6e0-4fc2-90bb-cae123e6811d)
# 巢狀for迴圈
```python
for 記數器1 in range(start,end,step)
  for 計數器2 in range(start,end,step)
    內圈指令區
  外圈指令區
```
## 九九乘法表
```python
for i in range(1,10): #外圈
  for j in range(1,10): #內圈
    print("%d乘上%d是%2d"%(i,j,i*j),end=" ") #不換行以空格間隔 %2d調整一位數成二位數位置
  print( ) #換行
```
![image](https://github.com/user-attachments/assets/4b5c03c2-7833-4862-ba09-7fb998384790)
## 金字塔
### 正金字塔
```python
n = int(input("How many levels does the triangle has:"))

for i in range(1,n+1): #1到(n+1)層 
    for j in range(i):
        print("%",end="") #以""為空格 
    print("#") #空格+換行
```
### 倒金字塔
```python
n = int(input("How many levels does the triangle has:"))

for i in range(n,0,-1): #1到(n+1)層 
    for j in range(i):
        print("%",end="") #以""為空格 
    print("#") #空格+換行
```
### 菱形
```python
#方法一
level = int( input("請輸入菱形要印出幾層 =") )
for i in range(level):
    for j in range(level - i - 1):
        print(" ", end = " ")
    for k in range((2 * i) + 1):
        print("+", end = " ")
    print()

# 程式與上一段相同，僅更改range的內容
for i in range(level - 2, -1, -1): #range改成從輸入數字-1到0倒數
    for j in range(level - i - 1): 
        print(" ", end = " ")
    for k in range((2 * i) + 1):
        print("+", end = " ")
    print()
#方法二
level = int( input("請輸入菱形要印出幾層 =") )

for i in range(1, level * 2):
    if i <= level:
        blank = "  " * (level - i)
        star = "+ " * (i * 2 - 1)
        
    else:
        blank = "  " * (i - level)
        star = "+ " * ( ( i - 2 * (i - level) ) * 2 - 1 )
        
    print(blank + star)
#方法三
level = int( input("請輸入菱形要印出幾層 =") )

for i in range(1, level + 1):
    blank = "  " * (level - i)
    star = "+ " * (i * 2 - 1)
       
    print(blank + star)
    
for i in range(level - 1, 0, -1):
    blank = "  " * (level - i)
    star = "+ " * (i * 2 - 1)
       
    print(blank + star)
#方法四
level = int( input("請輸入菱形要印出幾層 =") )

for i in range(1, level + 1):
    output = ""
    for k in range(1, level- i + 1):
        output+= "  "
    
    for k in range(1, i * 2):
        output+= "+ "
       
    print(output)
    
for i in range(level - 1, 0, -1):
    output = ""
    for k in range(1, level - i + 1):
        output+= "  "
    
    for k in range(1, i * 2):
        output+= "+ "
       
    print(output)
```
### 聖誕樹
```python
tree_layers = int( input("請輸入聖誕樹層數：") )

def tree_single_layer(current_layer, max_layer):
    # 第一層特別處理
    if current_layer == 1:
        for i in range(4):
            print(" " * (3-i+max_layer-current_layer) + "* " * i) # 用最大層數與現在的層數調整輸出結果
    # 其他層
    else:
        max_length = current_layer + 3 # 每層三層
        for i in range(current_layer, max_length):
            print(" " * (max_length -1 -i+max_layer- current_layer) + "* " * i)  # 用最大層數與現在的層數調整輸出結果
# 固定給三層的樹幹，並根據樹的層數調整位子
def tree_root(max_layer):
    for i in range(3):
        print(" " * max_layer +"*" * 3) # 樹幹粗固定3個*
        
# 用迴圈將每一層透過自訂函數輸出
for layer in range(1, tree_layers+1):
    tree_single_layer(layer, tree_layers)

tree_root(tree_layers) # 輸出樹幹

print("------------")
```
## 賽程表
```python
class_list = ["A", "B", "C"] # 班級列表
class_num = len(class_list) # 班級的數量
game_set_list = [] # 儲存組合的串列
# 班級之間兩兩配對
# i為0，j會跑過1,2
# i為1，j會跑過2
# i為2，j不會跑
for i in range(class_num): # 從第一個班級，列舉其他班級的配對
    # 配對的目標
    for j in range(i + 1, class_num):
        # 將每個班級的名稱，根據i,j取出，放入list中代表配對
        game_set = [ class_list[i], class_list[j] ]
        # 將配對放入game_set_list(儲存組合的串列)
        game_set_list.append(game_set)
print(game_set_list)

# 將每個組合輸出
for g_set in game_set_list:
    print(g_set[0], "班對上", g_set[1], "班")
```
![image](https://github.com/user-attachments/assets/61b3aa62-1ab2-41c5-a788-9c94d1288611)
