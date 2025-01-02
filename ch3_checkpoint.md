<a href="https://colab.research.google.com/github/C109118214/AiAnalysic/blob/main/ch3_checkpoint.md" target="_parent">  
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>  
</a>  

# 數字運算  

```python  
# 計算 10000 乘以 (1 + 0.03)  
result = 10000 * (1 + 0.03)  
result  

執行結果：  
10300.0
```

接下來的程式碼示例：  

```python  
# 輸出 10000  
print(10000)  
執行結果：  
10000.0
```python
age = 18
result = "%s%d%s"%("Current age:",age,"years old.")
print (result)
```
```python
age = 18
result = "%s%d%s"%("Current age:",age,"years old.")
print (result)
```
|方法名稱|功能|
|-|-|
|append( )|加一個元素到字串尾端|
|extend( )|加一組元素到字串尾端|
|insert( )|加一組元素到字串中|
|remove( )|移除字串中的元素|
|pop( )|取出並回傳指定的元素|
|sort( )|字串元素從小到大排列|
|copy( )|複製字串元素|
|clear( )|清除字串所有元素|
```python
list1=[10,20,30,40,50]
 
list1.append(60)
list1.insert(1, 15)
list1.extend([70,80])
print(list1)
print (1**2,2**3)
```
 | # 優先順序| # 符號| # 作用| # 符號與變數|
|-|:-:|:-:|:-:|
|1|**|次方|a ** b|
|2|*|乘|a * b|
|2|/|除|a / b|
|2|//|整數除|a // b|
|2|%|取餘數|a % b|
|3|+|加|a + b|
|3|-|減|a - b|
```python
X,Y = 2,1
print (8*(X+Y)**2)
```
### 這是square ** 的進階power 如pow(x,y,z)有第三數則預設為MOD取餘數
```python
print (pow(1,2),pow(2,3,3))
#這是square **的進階power 如pow(x,y,z)有第三數則預設為MOD取餘數
```
```python
A = float(input("輸入整數A:").strip())
B = float(input("輸入整數B:").strip())
print (A % B == 0)
if A%B == 0 :
    print ("A 是 B 倍數")
else  :
    print ("A 不是 B 倍數")
```
### print (A % B == 0)直接判斷是否成立(True/False)
