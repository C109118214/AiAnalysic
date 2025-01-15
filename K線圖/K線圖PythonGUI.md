
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
![image](https://github.com/user-attachments/assets/8193967c-8463-49e2-b787-afbfede58f02)
```python
import pandas as pd
import mplfinance as fplt
import yfinance as yf

def main(stock_id):
    # 下載近30天的資料
    df = yf.download(stock_id, period = "1mo",
                       interval="1d")
    df.columns = df.columns.get_level_values(0)
    print(df.columns)
    # 調整圖表標示顏色
    mc = fplt.make_marketcolors(
                                up = 'tab:red',down = 'tab:green', # 上漲為紅，下跌為綠
                                wick = {'up':'red','down':'green'}, # 影線上漲為紅，下跌為綠
                                volume = 'tab:blue', # 交易量顏色
                               )
    
    # 定義圖表風格
    s = fplt.make_mpf_style(marketcolors = mc,
                            rc = {
                                'font.size': 10, #文字大小
                                "font.family":['sans-serif', "Microsoft JhengHei"] # 字型
                            }
                        ) 
    
    fplt.plot(
                df, # 開高低收量的資料
                type = 'candle', # 類型為蠟燭圖，也就是 K 線圖
                style = s, # 套用圖表風格
                title = stock_id, # 設定圖表標題
                ylabel = '價格', # 設定 Y 軸標題
                volume = True,
                savefig='stock_Kbar.png', # 儲存檔案
            )
    
# 當這支程式被直接執行的時候，會執行測試的程式碼main("AAPL")
# 被匯入(import)的時候__name__就會變成檔案名稱Draw_plot，
# 就不會執行main("AAPL")
if __name__ == "__main__":

    main("GOOG")
```
