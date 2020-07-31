mkdir data data/raw data/train data/test data/validation
mkdir app app/blueprints app/blueprints/home_page
touch app/blueprints/__init__.py app/blueprints/home_page/__init__.py app/blueprints/home_page/blueprint.py
mkdir app/static
touch app/static/style.css app/static/index.js
mkdir app/templates
touch app/templates/base.html app/templates/home.html
touch app/app.py app/.gitignore
mkdir scripts
touch scripts/preprocess.py scripts/model.py scripts/train.py
mkdir notebooks 
