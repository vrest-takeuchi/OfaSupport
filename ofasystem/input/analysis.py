from django_pandas.io import *
from .DBinput import axis_RSD,Output_RSD,gps_RSD,can_RSD
import time as tim
import itertools
from django.http import HttpResponse
from output.models import AnaSummary
from .DBinput import AnaSummaryDfn,AngularvelocityDfn,CanBrakeDfn,CanPositionDfn,CanSpeedDfn,CanSteeringDfn,EquipStatusDfn,SatelliteDfn,LocationDfn,AccelerationDfn,CanAccelDfn,AccelerationDf


print('start_processing......')
"""アプリケーション起動時の処理"""
"""出力先のDB確認"""
Output_RSD_notall =Output_RSD[Output_RSD['comment'] != '0']['run_start_date'] #データ不足があるものを抽出
if len(Output_RSD_notall) == 0 :#データ不足のデータが1個以上あるとき
    for date in Output_RSD_notall:#不足のあるデータを再度新しいデータがあるか確認
        axis_data = axis_RSD[axis_RSD['run_start_date'] == 'date']
        gps_data = gps_RSD[gps_RSD['run_start_date'] == 'date']
        can_data = can_RSD[can_RSD['run_start_date'] == 'date']
        if len(axis_data)+len(gps_data)+len(can_data)==3: #すべてのデータが存在する場合解析処理をかける
            print(date,end='...exist_new_data...delete_old_data...and...starting_analysis')
            print('......')
            print(AngularvelocityDfn(date))
            print(CanBrakeDfn(date))
            print(CanPositionDfn(date))
            print(CanSpeedDfn(date))
            print(CanSteeringDfn(date))
            print(SatelliteDfn(date))
            print(LocationDfn(date))
            print(AccelerationDfn(date))
            print(CanAccelDfn(date))
        else:
            print(date,end='...not_new_data')
            print('......')
else:
    print('not_lack_data...start_application...')
# print(LocationDfn('2020-12-17 19:48:04+00:00'))

date='2020-12-17 19:48:04+00:00'
"""gps"""
Satelite_data=SatelliteDfn(date).loc[:,['equip_id','run_start_date','measurement_date','positioning_quality','used_satellites']]
Location_data=LocationDfn(date).loc[:,['measurement_date','latitude','longitude','velocity']]
Acceleration_data=AccelerationDfn(date).loc[:,['measurement_date','nine_axis_acceleration_x','nine_axis_acceleration_y','nine_axis_acceleration_z']]
Angularvelocity_data=AngularvelocityDfn(date).loc[:,['measurement_date','nine_axis_angular_velocity_x','nine_axis_angular_velocity_y','nine_axis_angular_velocity_z']]
CanBrake_data=CanBrakeDfn(date).loc[:,['measurement_date','can_brake']]
CanPosition_data=CanPositionDfn(date).loc[:,['measurement_date','can_turn_lever_position']]
CanSpeed_data=CanSpeedDfn(date).loc[:,['measurement_date','can_speed']]
CanSteering_data=CanSteeringDfn(date).loc[:,['measurement_date','can_steering']]
CanAccel_data=CanAccelDfn(date).loc[:,['measurement_date','can_accel']]

gps_data=pd.merge(Satelite_data,Location_data, on='measurement_date',  how='outer')
axis_data=pd.merge(Acceleration_data,Angularvelocity_data, on='measurement_date',  how='outer')
can1_data=pd.merge(CanBrake_data,CanPosition_data, on='measurement_date',  how='outer')
can2_data=pd.merge(CanSpeed_data,CanSteering_data, on='measurement_date',  how='outer')
can3_data=pd.merge(can1_data,can2_data, on='measurement_date',  how='outer')
can_data=pd.merge(can3_data,CanAccel_data, on='measurement_date',  how='outer')

gps_axis_data=pd.merge(gps_data,axis_data, on='measurement_date',  how='outer')
gps_axis_can_data=pd.merge(gps_axis_data,can_data, on='measurement_date',  how='outer')

gps_axis_can_data['measurement_date'] = pd.to_datetime(gps_axis_can_data['measurement_date'])

gps_axis_can_data.sort_values(by=['measurement_date'], inplace=True)

ana_data=gps_axis_can_data.reset_index(drop=True).fillna(method='ffill')
pd.set_option('display.max_rows', 100000)


print(ana_data)



# print()


# for i in itertools.count():  # 1秒ごとにループ実行
#      tim.sleep(1)
#
#      if len(Output_RSD_notall) == 1 :#データ不足のデータが1個以上あるとき
#          print('C')
#          for date in Output_RSD_notall:#不足のあるデータを再度新しいデータがあるか確認
#             axis_data = axis_RSD[axis_RSD['run_start_date'] == 'date']
#             gps_data = gps_RSD[gps_RSD['run_start_date'] == 'date']
#             can_data = can_RSD[can_RSD['run_start_date'] == 'date']
#             print('B')
#             if len(axis_data)+len(gps_data)+len(can_data)!=3: #すべてのデータが存在する場合解析処理をかける
#                 a=AnaSummaryDf(date)
#                 print('date')
#                 print(a)
#                 break
#          else:
#             continue
#      else:
#          break
# else:



"""データ確認"""
"""入力データと出力済みデータを比較"""
axis_ana = pd.merge(axis_RSD, Output_RSD, on='run_start_date', indicator=True, how='outer')
gps_ana = pd.merge(gps_RSD, Output_RSD, on='run_start_date', indicator=True, how='outer')
can_ana = pd.merge(can_RSD, Output_RSD, on='run_start_date', indicator=True, how='outer')

axis_data = axis_ana[axis_ana['_merge'] == 'left_only']
axis_nonexistdate = axis_data['run_start_date']

gps_data = gps_ana[gps_ana['_merge'] == 'left_only']
gps_nonexistdate = gps_data['run_start_date']

can_data = can_ana[can_ana['_merge'] == 'left_only']
can_nonexistdate = can_data['run_start_date']

axis_dp_merge=axis_data.drop('_merge', axis=1)
gps_dp_merge=gps_data.drop('_merge', axis=1)
can_dp_merge=can_data.drop('_merge', axis=1)

gps_axis = pd.merge(gps_dp_merge,axis_dp_merge, on='run_start_date', indicator=True, how='outer').assign(comment='1')
gps_can = pd.merge(gps_dp_merge,can_dp_merge, on='run_start_date', indicator=True, how='outer').assign(comment='2')

noaxis_date = gps_axis[gps_axis['_merge'] == 'left_only'].loc[:,['run_start_date','comment']]
nocan_date= gps_can[gps_can['_merge'] == 'left_only'].loc[:,['run_start_date','comment']]

# gps_can = pd.merge(noaxis_date,nocan_date, on='run_start_date', indicator=True, how='outer').assign(comment='3')
# onlygps_date= gps_can[gps_can['_merge'] == 'both'].loc[:,['run_start_date','comment']]
gp_ca_ac=pd.merge(noaxis_date, nocan_date,  on='run_start_date', indicator=True ,how='outer').assign(comment='101')
no_ca_ac_date= gp_ca_ac[gp_ca_ac['_merge'] == 'both'].loc[:,['run_start_date','comment']]


#
# df_s_h = pd.merge([rsd_axis, rsd_gps, rsd_can ], how='outer')

# AccelerationDf = read_frame(AccelerationTbl.objects.all())
# df=AccelerationDf.drop_duplicates(subset='run_start_date')
# AngularvelocityDf = read_frame(AngularvelocityTbl.objects.all())
# CanAccelDf = read_frame(CanAccelTbl.objects.all())
# CanBrakeDf = read_frame(CanBrakeTbl.objects.all())
# CanPositionDf = read_frame(CanPositionTbl.objects.all())
# CanSpeedDf = read_frame(CanSpeedTbl.objects.all())
# CanSteeringdf = read_frame(CanSteeringTbl.objects.all())
# EquipStatusDf = read_frame(EquipStatusTbl.objects.all())
# GeomagnetismDf = read_frame(GeomagnetismTbl.objects.all())
# LocationDf = read_frame(LocationTbl.objects.all())
# SatelliteDf = read_frame(SatelliteTbl.objects.all())
# df1=LocationDf.drop_duplicates(subset='run_start_date')
#