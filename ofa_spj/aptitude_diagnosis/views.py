from django.shortcuts import render

from django.http import HttpResponse
from .models import Score1, Summary1
import datetime
import pandas as pd
from sqlalchemy import create_engine
import json

import random #ダミー用

connection_config = {
    'database': 'aptitude_diagnosis_data',
    'user': 'postgres',
    'password': 'ofa',
    'host': 'localhost',
    'port': '5432',
}

engine = create_engine('postgresql://{user}:{password}@{host}:{port}/{database}'.format(**connection_config))


a=random.randint(0, 10)
b=random.randint(0, 10)
c=random.randint(0, 10)
d=random.randint(0, 10)
e=random.randint(0, 10)
f=random.randint(0, 10)
g=random.randint(0, 10)
h=random.randint(0, 10)
i=random.randint(0, 10)
j=random.randint(0, 10)
k=random.randint(0, 10)
l=random.randint(0, 10)
m=random.randint(0, 10)
n=random.randint(0, 10)
o=random.randint(0, 10)
p=random.randint(0, 10)
q=random.randint(0, 10)
r=random.randint(0, 10)
s=random.randint(0, 10)
t=random.randint(0, 10)
u=random.randint(0, 10)
v=random.randint(0, 10)
w=random.randint(0, 10)
x=random.randint(0, 10)
y=random.randint(0, 10)



# ave=df['point'].me
#デフォ値

car_id=4
office_id=1
run_start_date="2020-11-05 00:49:44.875575+09"
total_score='A'
shin_score='A'
gi_score='B'
tai_score='B'
comment='コメントコメントコメント'
updated_at=datetime.datetime.now()

cat_shin = ['1','2','3','4','5','6','7','8','思考性','支配性','社会性',]
pt_shin=[a,b,c,d,e,f,g,h,i,j,k,]
cat_gi = ['運転前後動作','運転姿勢','運転行動','基本走行','法規走行','安全行動',]
pt_gi=[l,m,n,o,p,q,]
cat_tai= ['上半身（押系動作）','上半身（引系動作）','下半身（押系動作）','下半身（引系動作）','認知','予知・判断','操作','眼・視覚機能']
pt_tai=[r,s,t,u,v,w,x,y]
pt=pt_shin+pt_gi+pt_tai
cat=cat_shin+cat_gi+cat_tai
trm=['Amenu','Bmenu','Cmenu','Dmenu','Emenu','Fmenu','Gmenu','Hmenu','Imenu','Jmenu','Kmenu','Lmenu','Mmenu','Nmenu',\
     'Omenu','Pmenu','Qmenu','Rmenu','Smenu','Tmenu','Umenu','Vmenu','Wmenu','Xmenu','Ymenu']



def index(request):


    id_cal = pd.DataFrame(list(Summary1.objects.all().values()))

    id_value = id_cal['id'].max() + 1


    for category,point in zip(cat,pt):

                         df_category = pd.DataFrame(list(Score1.objects.filter(score_category=category).values()))


                         df_score = pd.DataFrame(
                           {'summary_id': [id_value], 'score_category': [category], 'point': [point],  \
                           'office_id': [office_id], 'updated_at': [updated_at]})

                         df_rank_area = pd.concat([df_score, df_category])
                         df_rank_office = df_rank_area[df_rank_area['office_id'] == office_id]
                         df_score_std=df_rank_area['point'].std(ddof=0)#母分散・母標準偏差

                         average = df_rank_area['point'].mean()#平均点
                         # print(df_rank_area)
                         # print(average)
                         # print(df_score_std)
                         print(df_rank_area)
                         print(average)
                         print(df_score_std)

                         df_rank_area['deviation']=df_rank_area['point'].map(lambda x: round((x - average) / df_score_std * 10 + 50)).astype(int)
                         print(df_rank_area['deviation'].head(1).max())
                         deviation = df_rank_area['deviation'].head(1).max()
                         print('lineline')




                         df_rank_area['rank_area'] = df_rank_area['point'].rank(ascending=False, method='min')
                         rank_area = df_rank_area['rank_area'].head(1).max()

                         df_rank_office['rank_office'] = df_rank_office['point'].rank(ascending=False, method='min')
                         rank_office = df_rank_office['rank_office'].head(1).max()

                         num_area = len(df_rank_area)
                         num_office = (df_rank_area['office_id'] == office_id).sum()

                         df_score_save = pd.DataFrame(
                              {'summary_id': [id_value], 'score_category': [category], 'point': [point], 'average': [average], \
                              'num_area': [num_area], 'office_id': [office_id], 'updated_at': [updated_at], \
                              'rank_area': [rank_area], 'num_office': [num_office], 'rank_office': [rank_office],\
                               'deviation':[deviation]})
                         # df_score_save.to_sql('score1', con=engine, if_exists='append', index=False)


    # df_total = pd.DataFrame(list(Score1.objects.filter(summary_id=id_value).values()))
    # df_shin=df_total[df_total['score_category'].isin(['抑うつ','気分変化','神経質','客観性','協調性','攻撃性','活動性','のんきさ','思考性','支配性','社会性'])]
    # shin_score=df_shin['point'].sum()
    # df_gi=df_total[df_total['score_category'].isin(['運転前後動作','運転姿勢','運転行動','基本走行','法規走行','安全行動'])]
    # gi_score=df_gi['point'].sum()
    # df_tai=df_total[df_total['score_category'].isin(['上半身（押系動作）','上半身（引系動作）','下半身（押系動作）','下半身（引系動作）','認知','予知・判断','操作','眼・視覚機能'])]
    # tai_score=df_tai['point'].sum()
    # total_score=shin_score+gi_score+tai_score
    #
    # df_summary_save = pd.DataFrame({'car_id': [car_id], 'run_start_date': [run_start_date], 'total_score': [total_score], \
    #      'shin_score': [shin_score], 'gi_score': [gi_score], 'tai_score': [tai_score],\
    #      'comment': [comment], 'updated_at': [updated_at]})
    # df_summary_save.to_sql('summary', con=engine, if_exists='append', index=False)
    #
    # for category, training_menu,point in zip(cat, trm,pt):
    #     if point<5:#5point以上ならトレーニング不要
    #         df_training=pd.DataFrame({'training_id':[id_value],'training_category':[category],'training_menu':[training_menu], 'updated_at': [updated_at]})
    #         df_training.to_sql('training', con=engine, if_exists='append', index=False)

    return HttpResponse(json.loads(df_training.to_json(orient='records')))





