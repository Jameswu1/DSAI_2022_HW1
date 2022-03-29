目前使用到的 data 包含 2019 - 2022 年的備轉容量

這次作業常是三種方式
分別為 LSTM , ARIMA 以及 fbprophet
以目前的測試成績，fbprophet 成績最高
因此以這個模型當作最終解答
針對這次的實作，主要是從季節，月份，星期去做分析
分別針對不同的特徵提取可以看到明顯的不同
![image](https://user-images.githubusercontent.com/41716487/160602422-bf515305-1235-4636-a0bd-47908ea7ed09.png)
![image](https://user-images.githubusercontent.com/41716487/160601977-bd11531e-5624-45bb-8931-2d0526f31e99.png)
![image](https://user-images.githubusercontent.com/41716487/160602021-bbbb9df3-a455-4376-9c78-42e83cbdf37b.png)
![image](https://user-images.githubusercontent.com/41716487/160602045-1b5f304a-84f5-4a06-beed-6d598eec9f62.png)
並且隨著時序的變化，可以看出來不同年份的相同月份意識不同的趨勢
因此最後決定透過每年固定季節的資料
使模型訓練的過程中能將年與年之間的變化學習，並透過不同的波行的趨勢圖題取出來月份之間的變化

Train
由於資料量過多對於預測值趨於平均，因此在訓練過程中會將data減量，分別針對各年份的春天當作資料進行訓練


Test
執行 python app.py 即可，會直接寫入submission.csv

