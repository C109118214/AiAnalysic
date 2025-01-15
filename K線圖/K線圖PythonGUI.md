
![image](https://github.com/user-attachments/assets/06c3eb14-9d0b-41c4-ba96-0ba6d8027070)
```python
        # 連結自訂函數
        self.pushButton.clicked.connect(self.onclick)
        
    def onclick(self):
        # 取的使用者輸入的股票代號
        stock_id = self.lineEdit.text()
        try:
            dp(stock_id)
            # 替換成畫好的圖
            self.label_2.setText("此K線圖如下")
            self.label.setPixmap(QtGui.QPixmap("stock_Kbar.png"))
        except:
            self.label_2.setText("沒有這個股票代號")
            self.label.setPixmap(QtGui.QPixmap("起始圖.png"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
```
