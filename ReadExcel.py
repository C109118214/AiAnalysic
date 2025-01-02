# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd


file_path = 'C:/Users/USER/Downloads/2330.TW_stock_data.xlsx' # Replace with your actual file path

try:
  # Read the Excel file into a pandas DataFrame
  df = pd.read_excel(file_path)

  # Display the DataFrame (which represents the Excel sheet)
  display(df)
  
except FileNotFoundError:
  print(f"Error: File not found at {file_path}")
except Exception as e:
  print(f"An error occurred: {e}")