import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt 
import warnings
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
from fbprophet import Prophet
from matplotlib import pyplot as plt
import logging
logging.getLogger('fbprophet').setLevel(logging.WARNING) 


path_file = "本年度每日尖峰備轉容量率.csv"
data = pd.read_csv(path_file)
data = pd.DataFrame(data)
data = data.loc[:,['date','capacity']]
#data.columns=['date','capacity']

'''change datetime format'''
for index in range(len(data['date'])):
    index_time = str(data['date'][index])
    time_change = datetime.strptime(index_time,"%Y/%m/%d").date()
    data['date'][index] = time_change
data['capacity'] *= 10


path_file = "近三年每日尖峰備轉容量率.csv"
data_1 = pd.read_csv(path_file)
data_1 = pd.DataFrame(data_1)
data_1 = data_1.loc[:,['日期','備轉容量(MW)']]
data_1.columns=['date','capacity']

'''change datetime format'''
for index in range(len(data_1['date'])):
    index_time = str(data_1['date'][index])
    time_change = datetime.strptime(index_time,"%Y/%m/%d").date()
    data_1['date'][index] = time_change
data_1['capacity'] *= 10

df_cat =  pd.concat([data_1,data])
df_cat.columns=['ds','y']

a = df_cat[0:90]
b = df_cat[365:90+365]
c = df_cat[731:90+731]
d = df_cat[731+365:-15]
train =  pd.concat([a,b,c,d])

prophet = Prophet()

prophet.fit(train)
future = prophet.make_future_dataframe(freq='D' ,periods=14)
forecasts = prophet.predict(future)

pred = forecasts[-14:]
pred = pred.loc[:,['ds','yhat']]
pred.columns=['date','operating_reserve(MW)']
pred.to_csv("submission.csv",index=False)

