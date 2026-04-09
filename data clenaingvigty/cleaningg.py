Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

=============== RESTART: C:/Users/LAW LIBRARY/Desktop/cleaning.py ==============
      PatientId  AppointmentID Gender  ... Handcap SMS_received  No-show
0  2.987250e+13        5642903      F  ...       0            0       No
1  5.589978e+14        5642503      M  ...       0            0       No
2  4.262962e+12        5642549      F  ...       0            0       No
3  8.679512e+11        5642828      F  ...       0            0       No
4  8.841186e+12        5642494      F  ...       0            0       No

[5 rows x 14 columns]
<class 'pandas.DataFrame'>
RangeIndex: 110527 entries, 0 to 110526
Data columns (total 14 columns):
 #   Column          Non-Null Count   Dtype  
---  ------          --------------   -----  
 0   PatientId       110527 non-null  float64
 1   AppointmentID   110527 non-null  int64  
 2   Gender          110527 non-null  str    
 3   ScheduledDay    110527 non-null  str    
 4   AppointmentDay  110527 non-null  str    
 5   Age             110527 non-null  int64  
 6   Neighbourhood   110527 non-null  str    
 7   Scholarship     110527 non-null  int64  
 8   Hipertension    110527 non-null  int64  
 9   Diabetes        110527 non-null  int64  
 10  Alcoholism      110527 non-null  int64  
 11  Handcap         110527 non-null  int64  
 12  SMS_received    110527 non-null  int64  
 13  No-show         110527 non-null  str    
dtypes: float64(1), int64(8), str(5)
memory usage: 11.8 MB
None
PatientId         0
AppointmentID     0
Gender            0
ScheduledDay      0
AppointmentDay    0
Age               0
Neighbourhood     0
Scholarship       0
Hipertension      0
Diabetes          0
Alcoholism        0
Handcap           0
SMS_received      0
No-show           0
dtype: int64
Traceback (most recent call last):
  File "C:/Users/LAW LIBRARY/Desktop/cleaning.py", line 22, in <module>
    df.to_csv("cleaned_data.csv", index=False)
  File "C:\Users\LAW LIBRARY\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\generic.py", line 3988, in to_csv
    return DataFrameRenderer(formatter).to_csv(
  File "C:\Users\LAW LIBRARY\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\formats\format.py", line 1025, in to_csv
    csv_formatter.save()
  File "C:\Users\LAW LIBRARY\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\formats\csvs.py", line 251, in save
    with get_handle(
  File "C:\Users\LAW LIBRARY\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\common.py", line 926, in get_handle
    handle = open(
PermissionError: [Errno 13] Permission denied: 'cleaned_data.csv'
>>> 
=========================================================================================== RESTART: C:/Users/LAW LIBRARY/Desktop/cleaning.py ==========================================================================================
      PatientId  AppointmentID Gender  ... Handcap SMS_received  No-show
0  2.987250e+13        5642903      F  ...       0            0       No
1  5.589978e+14        5642503      M  ...       0            0       No
2  4.262962e+12        5642549      F  ...       0            0       No
3  8.679512e+11        5642828      F  ...       0            0       No
4  8.841186e+12        5642494      F  ...       0            0       No

[5 rows x 14 columns]
<class 'pandas.DataFrame'>
RangeIndex: 110527 entries, 0 to 110526
Data columns (total 14 columns):
 #   Column          Non-Null Count   Dtype  
---  ------          --------------   -----  
 0   PatientId       110527 non-null  float64
 1   AppointmentID   110527 non-null  int64  
 2   Gender          110527 non-null  str    
 3   ScheduledDay    110527 non-null  str    
 4   AppointmentDay  110527 non-null  str    
 5   Age             110527 non-null  int64  
 6   Neighbourhood   110527 non-null  str    
 7   Scholarship     110527 non-null  int64  
 8   Hipertension    110527 non-null  int64  
 9   Diabetes        110527 non-null  int64  
 10  Alcoholism      110527 non-null  int64  
 11  Handcap         110527 non-null  int64  
 12  SMS_received    110527 non-null  int64  
 13  No-show         110527 non-null  str    
dtypes: float64(1), int64(8), str(5)
memory usage: 11.8 MB
None
PatientId         0
AppointmentID     0
Gender            0
ScheduledDay      0
AppointmentDay    0
Age               0
Neighbourhood     0
Scholarship       0
Hipertension      0
Diabetes          0
Alcoholism        0
Handcap           0
SMS_received      0
No-show           0
dtype: int64
Traceback (most recent call last):
  File "C:\Users\LAW LIBRARY\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'age'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:/Users/LAW LIBRARY/Desktop/cleaning.py", line 10, in <module>
    df['age'] = df['age'].fillna(df['age'].median())
  File "C:\Users\LAW LIBRARY\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\LAW LIBRARY\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'age'
