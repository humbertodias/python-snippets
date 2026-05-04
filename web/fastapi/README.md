```shell
python3 -m venv $HOME/venv
source $HOME/venv/bin/activate
python3 -m pip install fastapi uvicorn
uvicorn main:app --reload
```

Access
http://127.0.0.1:8000/docs