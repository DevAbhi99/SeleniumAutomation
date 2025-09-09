#To run a BDD selenium script using pytest
pytest main.py

#To generate report in html
pytest -q --html=reports/report.html --self-contained-html (Make sure the runable file is in the name format test_<filename>.py)
