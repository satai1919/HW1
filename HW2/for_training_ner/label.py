import pandas as pd
wordtype=dict()
path = 'wordtype.csv'
table = pd.read_csv(path).fillna('')
for i in range(table.shape[0]):
    if table.loc[i,'種類']!='':
        wordtype[table.loc[i,'單詞']]=table.loc[i,'種類']
lastword={'。','？','！'}

filename = 'funds_info.csv'
f = pd.read_csv(filename)

content = f["投資策略"].tolist()

trainfilename = 'train_data'
trainfile = open(trainfilename, 'w', encoding = 'utf-8')
testfilename = 'test_data'
testfile = open(testfilename, 'w', encoding = 'utf-8')


for i in range(len(content)):
    article=str(content[i])
    l = len(article)
    if i%3==0:    #用來決定是否該文章是test data
        now = 0    #指針，標示目前的位置
        while now<l:    #如果目前的位置不是文章最後一個字
            labeled=False    #先標記該字體為還未被label的
            
            #如果是空白字，則不寫入
            if article[now] == ' ':   
                now += 1
                continue
                
            
            #看看是否有以now為第一個字，來與關鍵字是符合的
            for key in wordtype.keys():
                lkey = len(key)
                if now+lkey<=l:
                    if article[now:now+lkey]==key:    #如果與關鍵字吻合
                        labeled=True    #標記它
                        testfile.write(article[now]+'\t'+'B-'+wordtype[key]+'\n')
                        for i in range(1,lkey):
                            testfile.write(article[now+i]+'\t'+'I-'+wordtype[key]+'\n')
                        now += lkey
                        break
            if not labeled:
                testfile.write(article[now]+'\t'+'O'+'\n')
                if article[now] in lastword:
                    testfile.write('\n')
            now += 1
        if article[-1] not in lastword:
            testfile.write('\n')
    else: 
        now = 0
        while now<l:
            labeled=False
            
            #如果是空白字，則不寫入
            if article[now] == ' ':   
                now += 1
                continue
            
            for key in wordtype.keys():
                lkey = len(key)
                if now+lkey<=l:
                    if article[now:now+lkey]==key:
                        labeled=True
                        trainfile.write(article[now]+'\t'+'B-'+wordtype[key]+'\n')
                        for i in range(1,lkey):
                            trainfile.write(article[now+i]+'\t'+'I-'+wordtype[key]+'\n')
                        now += lkey
                        break
            if not labeled:
                trainfile.write(article[now]+'\t'+'O'+'\n')
                if article[now] in lastword:
                    trainfile.write('\n')
            now += 1
        if article[-1] not in lastword:
            trainfile.write('\n')
trainfile.close()
testfile.close()

