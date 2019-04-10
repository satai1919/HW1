import pandas as pd
wordtype=dict()
path = 'wordtype.csv'
table = pd.read_csv(path).fillna('')
for i in range(table.shape[0]):
    if table.loc[i,'種類']!='':
        wordtype[table.loc[i,'單詞']]=table.loc[i,'種類']

filename = 'funds_info.csv'
f = pd.read_csv(filename)

content = f["投資策略"].tolist()

trainfilename = 'train_data'
trainfile = open(trainfilename, 'w')

for article in content[:1500]:
    article=str(article)
    l = len(article)
    now = 0
    while now<l:
        labeled=False
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
            now += 1
trainfile.close()

testfilename = 'test_data'
testfile = open(testfilename, 'w')

for article in content[1500:]:
    article=str(article)
    l = len(article)
    now = 0
    while now<l:
        labeled=False
        for key in wordtype.keys():
            lkey = len(key)
            if now+lkey<=l:
                if article[now:now+lkey]==key:
                    labeled=True
                    testfile.write(article[now]+'\t'+'B-'+wordtype[key]+'\n')
                    for i in range(1,lkey):
                        testfile.write(article[now+i]+'\t'+'I-'+wordtype[key]+'\n')
                    now += lkey
                    break
        if not labeled:
            testfile.write(article[now]+'\t'+'O'+'\n')
            now += 1
testfile.close()         