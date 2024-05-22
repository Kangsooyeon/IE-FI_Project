#!/bin/bash
pip install -r requirements.txt

python manage.py migrate

python manage.py loaddata fixtures/depositproducts.json

python manage.py loaddata fixtures/savingproducts.json

python manage.py loaddata fixtures/depositoptions.json

python manage.py loaddata fixtures/savingoptions.json

python manage.py loaddata fixtures/exchangerate.json

python manage.py loaddata fixtures/countryflag.json

python manage.py loaddata fixtures/location.json

python manage.py loaddata fixtures/user.json

python manage.py loaddata fixtures/article.json

python manage.py loaddata fixtures/comment.json

# python manage.py loaddata fixtures/subscribeddepositproducts.json

# python manage.py loaddata fixtures/subscribedsavingproducts.json