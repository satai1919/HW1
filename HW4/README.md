#  作業四
本作業共三個檔案
1. hw4.py：將作業一的ETF淨值重新下載至最新資料
2. output.csv：是hw4.py的output
3. HW4.ipynb：是作業的正式內容

## 討論
根據HW4.ipynb，
1. 分析結果：   
周資料  

|前三名/指標 | ASKSR | omega | Riskiness|  
|:----------- | :-----------:  | :-----------: | :-----------:|  
|1   | FXE  | URR | FXA|  
|2 | ULE | DRR | USDU|  
|3 | EUFX | YCL | CROC|

月資料

|前三名/指標 | ASKSR | omega | Riskiness|  
|:----------- | :-----------:  | :-----------: | :-----------:|  
|1  | SPFF  | CROC | USDU|  
|2 | CYB | DRR | FXE|  
|3 | PSK | IPFF | EUO|

2. Correlation ranking of cross展示了三種指標在周月資料之間的相似程度。   
可以發現omega是相似程度最高的一個指標，相關係數落在0.73；最不像的則是ASKSR，相關係數只有-0.14。

3. 三種指標所評出的排序結果並不相似。   
若用rank correlation評比評價的相似程度，則在周資料中，最相近的兩個評比指標為ASKSR以及riskiness，相關係數為-0.04；相差最遠的是ASKSR與omega，相關係數為-0.48。   
以同樣的方式檢驗月資料中指標評價的相似程度，最相近的兩個評比指標為ASKSR和omega，相關係數為0.07；相差最遠的是ASKSR與riskiness，相關係數為-0.19。   
雖然在周、月資料中分辨出最相似的指標，但可以發現其實他們之間的相關係數都很低。
