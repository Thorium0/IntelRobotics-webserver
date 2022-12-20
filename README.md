# IntelRobotics-webserver

For at sætte projektet op:

Installér Python 3.9 eller nyere: https://www.python.org/downloads/
Installér Python biblioteker: 
pip install -r requirements-mssql.txt
For at bruge mysql istedet for mssql:
pip install -r requirements-mysql.txt


Gå ind i informatik_projekt/settings.py og instil database-indstillinger til hvad du bruger
Lav en fil i root mappen der hedder keys.py og put de sensitite database-informationer i den. Kald variablerne det som er angivet i settings.py
Kør denne kommando for at oprette databasen: python manage.py migrate
Start severen med: runserver.sh for Linux, eller runserver.bat for Windows

For at komme til login-siden:
tilføj /admin til slutningen af dit url:
example.com -> example.com/admin

For at oprette den første administrator-bruger:
Åben er terminal i projektmappen
Skriv python manage.py createsuperuser
Udfyld de angivne fælter
Du kan nu logge ind med den nye bruger


Hvis du har skrevet din kode forkert for mange gange og er blevet låst ud, så kan du låse om igen med denne kommando: python manage.py axes_reset Eller for en bestemt ip: python manage.py axes_reset_ip [ip ...] Eller for en bestemt bruger: python manage.py axes_reset_username [username ...]
