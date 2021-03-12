# Conversation API
A very original application based off of nothing in particular.
Utilizes Django, and the powerful [DRF](https://www.django-rest-framework.org/).

The API supports CRUD operations on three resources:
- Conversation
  - Has a *title*, and a *start date*
  - Related to many Message resources
  
- Message
  - Keyed to a single Conversation via *conversation_id*
  - Has *text*, *datetime_sent*
  - Related to many Thought resources
  
- Thought
  - Keyed to a single Message via *message_id*
  - Has *text*, *datetime_sent*
  
## Installation

### Virtual Environment
1. Navigate to the project root
2. Make sure Python > 3.5 is installed on your system
    - Also install [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
2. Create your virtual environment: `python3 -m venv env`
3. Follow the steps listed [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#activating-a-virtual-environment)
to activate your virtual environment.
4. Install required packages: `pip3 install -r requirements.txt`

### Setup Django database (sqlite3)
1. Navigate to the project root
2. Run `python manage.py migrate`. This will set up the structure of the database.

### Test Data (optional)
1. Navigate to the project root
2. run `python manage.py loaddata starter_data` to preload a few examples

## Running
Now that the project is set up, running it is easy.
1. Navigate to the project root
2. Activate your virtualenv
3. Run `python manage.py runserver 8000`

## Tests
Run unit tests by first navigating to the project root, then run:

`python manage.py test`

