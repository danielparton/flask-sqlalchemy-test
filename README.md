= Overview =

Turns out one can simply replace the master.db file from the shell while the Flask server is running. If the database file is not present, the Flask app will return an error message, but will not crash. As soon as the database file is present, the Flask app will function again.

= Instructions =

python stage-first.py
cp stage.db master.db
python run.py
curl localhost:5000/getdata
python stage-second.py
curl localhost:5000/getdata
cp stage.db master.db
curl localhost:5000/getdata
