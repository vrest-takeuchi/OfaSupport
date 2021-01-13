from .models import AccelerationTbl, AngularvelocityTbl, CanAccelTbl, CanBrakeTbl, CanPositionTbl, CanSpeedTbl, \
    CanSteeringTbl, EquipStatusTbl, GeomagnetismTbl, LocationTbl, SatelliteTbl
from output.models import AnaSummary
from django_pandas.io import *
import psycopg2


"""起動時のDBINPUT"""
"""出力DB"""
AnaSummaryDf = read_frame(AnaSummary.objects.all())
Output_RSD = AnaSummaryDf.drop_duplicates(subset='run_start_date')  # run_start_dateをソート

"""入力DB"""
AccelerationDf = read_frame(AccelerationTbl.objects.all())
axis_RSD = AccelerationDf.drop_duplicates(subset='run_start_date') #9軸センサrun_start_dateをソート
SatelliteDf = read_frame(SatelliteTbl.objects.all())
gps_RSD = SatelliteDf.drop_duplicates(subset='run_start_date')#gpsrun_start_dateをソート
CanAccelDf = read_frame(CanAccelTbl.objects.all())
can_RSD = CanAccelDf.drop_duplicates(subset='run_start_date')#canrun_start_dateをソート


"""比較DB※modelData"""

"""DBINPUT関数"""

def AnaSummaryDfn(x):
    AnaSummaryDf = read_frame(AnaSummary.objects.all())
    return AnaSummaryDf[AnaSummaryDf['run_start_date']==x]
def AccelerationDfn(x):
    AccelerationDf = read_frame(AccelerationTbl.objects.all())
    return AccelerationDf[AccelerationDf['run_start_date']==x]
def AngularvelocityDfn(x):
    AngularvelocityDf  = read_frame(AngularvelocityTbl.objects.all())
    return AngularvelocityDf[AngularvelocityDf['run_start_date']==x]
def CanBrakeDfn(x):
    CanBrakeDf = read_frame(CanBrakeTbl.objects.all())
    return CanBrakeDf[CanBrakeDf['run_start_date']==x]
def CanPositionDfn(x):
    CanPositionDf = read_frame(CanPositionTbl.objects.all())
    return CanPositionDf[CanPositionDf['run_start_date']==x]
def CanSpeedDfn(x):
    CanSpeedDf = read_frame(CanSpeedTbl.objects.all())
    return CanSpeedDf[CanSpeedDf['run_start_date']==x]
def CanSteeringDfn(x):
    CanSteeringDf = read_frame(CanSteeringTbl.objects.all())
    return CanSteeringDf[CanSteeringDf['run_start_date']==x]
def CanAccelDfn(x):
    CanAccelDf = read_frame(CanAccelTbl.objects.all())
    return CanAccelDf[CanAccelDf['run_start_date']==x]
def EquipStatusDfn(x):
    EquipStatusDf = read_frame(EquipStatusTbl.objects.all())
    return EquipStatusDf[EquipStatusDf['run_start_date']==x]
def SatelliteDfn(x):
    SatelliteDf = read_frame(SatelliteTbl.objects.all())
    return SatelliteDf[SatelliteDf['run_start_date']==x]
def LocationDfn(x):
    LocationDf = read_frame(LocationTbl.objects.all())
    return LocationDf[LocationDf['run_start_date']==x]




"""course情報取得"""
connection = psycopg2.connect(host='localhost', dbname='safety_mobility', user='postgres', password='ofa')
ms_driving_course_evaluationDf = pd.read_sql("SELECT * FROM ms_driving_course_evaluation", connection)

# print(ms_driving_course_evaluationDf)