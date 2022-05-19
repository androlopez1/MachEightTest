Test project for MachEight

# Create a virtualenv 
virtualenv env

# Activate the virtualenv
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install project requirements
pip install -r requirements.txt

# Run the migrations
python manage.py makemigrations

python manage.py migrate

# Run the server
python manage.py runserver

# URL
http://localhost:8000/nbaplayers

# Run test
python manage.py test
 
By Andrés López 
