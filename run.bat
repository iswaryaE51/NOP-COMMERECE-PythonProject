REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Run pytest
pytest -v -s --html=./Reports/report.html testcases
