import base64
from Datenbanken import settings.db
with open("settings.db", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
my_string = my_string.decode('utf-8')