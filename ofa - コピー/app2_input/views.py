from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from app2_input.models import EquipMeasurementTbl

from django_pandas.io import *
import pandas as pd

from sympy.geometry import Point,Polygon

#リザルトデータ待ち関数（APIから取得）
# import requests
# url=''
# res=requests.get(url)
# data=res.json()
# df=pd.DataFrame(data,columns=['result'])
# result=df.head(1)
result= 1#resultをデフォで”取得済みへ”

def app2(requests):
    # setting=Post.objects.all()
    # dfs=read_frame(setting)
    # dfs['updated_at'] = pd.to_datetime(dfs['updated_at'])
    # setting_recent_date = dfs['updated_at'].max()
    # df_setting = dfs[dfs['updated_at'] == setting_recent_date]
    # latitude_setting=int(df_setting.iloc[0]['title'])

    #Setting直接入力

    latitude_setting_1_Ll=35411234
    longtitude_setting_1_Ll=139453234
    latitude_setting_1_Lr = 35411234
    longtitude_setting_1_Lr = 139453234
    latitude_setting_1_Ul = 35411234
    longtitude_setting_1_Ul = 139453234
    latitude_setting_1_Ur = 35411234
    longtitude_setting_1_Ur = 139453234
    block1 = [(1, 1), (2, 3), (3, 3), (3, 1)]
    point = Point(2, 5)
    poly = Polygon(*block1)
    poly.encloses_point(point)
    if ((poly.encloses_point(block1)) == True):
        block_no=1


    if result==1:

        result_data='解析中'
        gnss=EquipMeasurementTbl.objects.filter(type_id=1)#id=1GNSSの情報取得
        df1=read_frame(gnss) #データフレームに格納
        df1_s = pd.concat([df1, df1['data_val']\
            .str.split(',', expand=True)], axis=1)\
            .drop('data_val', axis=1)\
            .drop('equip_id', axis=1)\
            .drop('seqno', axis=1)\
            .drop('type_id', axis=1) \
            .drop('record_start_date', axis=1) \
            .drop('record_stop_date', axis=1) \
            .drop('measurement_date', axis=1) \
            .drop('run_start_date', axis=1) \
            .drop('run_stop_date', axis=1)#データカラムを分解不要カラム削除
        df1_s.rename(columns={0: 'data_type', 1: 'time',2:'status',3:'latitude',4:'N/S',5:'longitude',6:'W/E'\
            ,7: 'speed', 8: 'direction', 9: 'date', 10:'A',11:'B',12:'checksum'}, inplace=True)#分割時の命名をリネーム
        df1_s['reg_date'] = pd.to_datetime(df1_s['reg_date']) #reg_dateをタイムフレームに変換
        least_recent_date = df1_s['reg_date'].max() #最新のデータの登録に日時を抽出
        df_gnss=df1_s[df1_s['reg_date'] == least_recent_date]
        # df_gnss['latitude'].astype(Decimal)
        df_gnss['latitude']=df_gnss['latitude'].astype(float)*10000
        df_gnss['latitude']=df_gnss['latitude'].astype(int)
        df_gnss['longitude']=df_gnss['longitude'].astype(float)*10000
        df_gnss['longitude']=df_gnss['longitude'].astype(int)
        df_gnss['block_no'] = 'out_of_area'
        df_gnss.loc[((df_gnss['latitude']<latitude_setting_1)&(df_gnss['longitude']<longtitude_setting_1)),'block_no']=1
        df_gnss.loc[((df_gnss['latitude'] > latitude_setting_2) & (df_gnss['longitude'] > longtitude_setting_2)), 'block_no'] = 2
        print(df_gnss['longitude'])
        print(result_data)
        print(df_gnss)

        print(type(latitude_setting_1))
        return HttpResponse(df_gnss)
    elif result==0:
        result_data='データ待ち'
        print(result_data)
# Create your views here.

# #
