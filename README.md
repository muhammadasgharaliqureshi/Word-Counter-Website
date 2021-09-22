# Word-Counter-Website

A simple Django website prototype with functionality for understanding django flow.

For running this site do following.

first make migrations by typing
python manage.py migrate.

migrations are not required in this project but to be on the safe side just do it.

then run it by followinng command.

python manage.py runserver

This will run your website on default ip and port i.e. 127.0.0.0:8000.

you can run it to your own choiced ip and port by following.

python manage.py runserver {ip}:{port}

for this you would also need to add you {ip} in allowed_ip list in settings.py.

Enjoy and feel free to reach me out on asgharaliq99@gmail.com
