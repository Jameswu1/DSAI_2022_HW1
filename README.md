目前使用到的 data 包含 2019 - 2022 年的備轉容量

這次作業常是三種方式
分別為 LSTM , ARIMA 以及 fbprophet
以目前的測試成績，fbprophet 成績最高
因此以這個模型當作最終解答

Train
由於資料量過多對於預測值趨於平均，因此在訓練過程中會將data減量，分別針對各年份的春天當作資料進行訓練

Test
執行 python app.py 即可，會直接寫入submission.csv

