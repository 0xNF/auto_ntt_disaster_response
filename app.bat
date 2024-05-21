@ECHO OFF
set PYTHONHOME=C:\Users\nf\AppData\Local\Programs\Python\Python310
set PYTHONPATH=C:\Users\nf\AppData\Local\Programs\Python\Python310\Lib
set PATH=%PYTHONHOME%;%PATH%
@ECHO ON
py %~dp0\app.py