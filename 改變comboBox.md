# Python designer GUI 選取下拉式選單來改變LabelText

![image](https://github.com/user-attachments/assets/4bc88225-8d10-4cc7-9e2f-efc928405f20)

```python
        self.comboBox.currentIndexChanged.connect(self.change_item)
        self.comboBox_2.currentTextChanged.connect(self.check_order)
        
    def change_item(self):
        Group  = self.comboBox.currentText()
        if Group == "炸物":
            item = ["鹹酥雞", "薯條", "雞排"]
        elif Group == "飲料":
            item = ["紅茶", "綠茶", "可樂"]
        self.comboBox_2.clear() # 清空combobox
        
        for i in item:
            self.comboBox_2.addItem(i) # 新增item，文字是餐點品項
    
    def check_order(self):
        result = self.comboBox_2.currentText()
        self.label_3.setText(f"您點了{result}")
            
```
