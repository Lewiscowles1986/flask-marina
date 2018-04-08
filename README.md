# Flask Marina

This is a repo for the web-frontend (using Flask) for John Rendell marina racing. It's a small project being worked on by https://www.soslug.org

This part of the system and any works contributed by Lewis Cowles are AGPL-3.0 in the absence of a license file. This means that anyone with access to the system must be entitled to this source code and any derrivative works.

## Download & Setup

```
git clone https://github.com/Lewiscowles1986/flask-marina
cd flask-marina
virtualenv .venv
. .venv/bin/activate
pip install -r requirements.txt
FLASK_APP=app.py flask run
```

## Using

* Setup an IP or DNS accessible machine
* Download & Setup the project (see above)
* Adjust your webserver to forward traffic for the desired hostname / IP to port 5000

> **Note:** You are responsible for security such as rolling the secret_key in app.py, setting up firewalls, adding authentication in-front of this service.

## Screenshot

![screenshot capture - 2018-04-09 - 00-48-51](https://user-images.githubusercontent.com/2605791/38473999-3d9f7a7a-3b90-11e8-9c94-30ec6db54df8.png)



