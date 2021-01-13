from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .analysis import *
# print(Output_RSD_notall)
from .DBinput import axis_RSD,Output_RSD,gps_RSD,can_RSD,AngularvelocityDfn
# from .DBinput import axis_RSD,a,df_s_h
# CanSteeringdf ,EquipStatusDf ,GeomagnetismDf ,LocationDf ,SatelliteDf,df,df1

# from .DBinput import AccelerationDf,axis_nonexistdate,axis_RSD,gps_nonexistdate,can_nonexistdate,AnaSummaryDf,AccelerationDf,axis_ana,gps_ana,can_ana,axis_data,gps_data,can_data,noaxis_date,nocan_date,gp_ca_ac,no_ca_ac_date

# print(AngularvelocityDfn())
# print(gp_ca_ac)
# print(no_ca_ac_date)
# print(rsd_axis)
#
# print(noaxis_date)
# print(nocan_date)
# # print(axis_ana)
# # print(axis_RSD)
# # print(b)
# # print(AccelerationDf)
# # print(merged)
# # print(AccelerationDf)
# # print(AnaSummaryDf)
# # print(axis_nonexistdate)
# # print(can_nonexistdate)
# # print(gps_nonexistdate)
#
# print(df_s_h)
# for item in axis_nonexistdate:
#     print(item)
#     print("-----")
# print(gps_ana)
# print(can_ana)
# print(axis_ana)
# print(gps_data)
# print(can_data)
# print(axis_data)
# # print(a)
# print(b)
# print(merged)
# print(df)
# print(df1)
# print(AccelerationDf)
# print(AngularvelocityDf)
# print(CanAccelDf)
# print(CanBrakeDf)
# print(CanPositionDf)
# print(CanSpeedDf)
# print(CanSteeringdf)
# print(EquipStatusDf)
# print(GeomagnetismDf)
# print(LocationDf)
# print(SatelliteDf)

# Create your views here.
def index (request):
   return HttpResponse("Hello World")