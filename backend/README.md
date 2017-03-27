The Waterfall Backend
=====================

Install
-------
Create virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Run
---
Start server:
```bash
python3 manage.py runserver
```
Login: admin
Password: qazwsxedc

Scripts
-------
In scripts/ folder.
Use data_loader.py for creating waterfall images from raw data:
```bash
python data_loader.py d3data.h5
```
The image is saved in the same folder.
