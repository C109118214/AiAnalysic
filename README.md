
<img src="https://avatars.githubusercontent.com/u/113969919" width="48">
<img src="https://github.com/C109118214/AiAnalysic/blob/main/image.png" width="500">
# AiAnalysic  

`AiAnalysic` 是一個用於處理 Excel 檔案的 Python 程式庫。  

## 快速開始  

### 安裝  

```bash  
pip install pandas openpyxl
import pandas as pd  

file_path = 'C:/Users/USER/Downloads/2330.TW_stock_data.xlsx'  

try:  
    df = pd.read_excel(file_path)  
    display(df)  
except FileNotFoundError:  
    print(f"Error: File not found at {file_path}")  
except Exception as e:  
    print(f"An error occurred: {e}")
```
## 文件結構
ReadExcel.py: 讀取 Excel 的主要程式。
README.md: 本文件。
history.py: 其他歷史記錄（可選）。
image.png: 附加圖片（可選）。
