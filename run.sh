source venv/bin/activate

export FLASK_APP=main.py
export FLASK_DEBUG=1
export FLASK_ENV=development

flask run -p 5000 --reload --eager-loading