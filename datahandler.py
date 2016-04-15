from pandas import Series, DataFrame
import pandas as pd
print('input the URL of file')
URL = input()
chunker = pd.read_csv(URL, encoding='gbk', chunksize=1000)
flag = 1
d = DataFrame()
for f in chunker:
    for x in range(1000):
        if f.ix[x]['性别'] == '不详':
            f.ix[x]['性别'] = ''
        if isinstance(f.ix[x]['终端品牌'], str):
            f.ix[x]['终端品牌'] = f.ix[x]['终端品牌'].upper()
        if isinstance(f.ix[x]['终端型号'], str):
            f.ix[x]['终端型号'] = f.ix[x]['终端型号'].upper()
    if flag > 1:
        d = pd.merge(d, f, how='outer')
    else:
        d = f
    flag = flag + 1
    print('flag = %s' % flag)
print('input the URL of out')
URL = input()
d.to_csv(URL)
