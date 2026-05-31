# Health Prediction System
## 1. Project Overview
The Health Prediction System is a web-based application developed using Django, Django REST Framework (DRF), SQLite, Bootstrap, and Scikit-learn. The system allows healthcare staff to manage patient records and predict potential health risks based on blood test parameters such as glucose, haemoglobin and cholesterol levels.
The application combines CRUD operations, REST APIs, and Machine Learning predictions to provide a simple AI-powered healthcare solution.

## 2. Features
## Patient Management
- Add new patient records
- View all patient records
- Update patient information
- Delete patient records
## Health Prediction
- Predict health risk using Machine Learning
- Automatic risk classification
- Store prediction results in remarks field
## REST API
- Create patient via API
- Retrieve patient records
- Update patient records
- Delete patient records
## User Interface
- Bootstrap responsive design
- Simple navigation
- User-friendly forms
## Documentation
- Swagger API documentation
- DRF Browsable API

## 3. Technology Stack
## Frontend
- HTML5
- CSS3
- Bootstrap 5
- Django Templates
## Backend
- Python
- Django
- Django REST Framework
## Database
- SQLite
## Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Joblib
## API Documentation
- Swagger 
## Version Control
- Git
- GitHub

## 4. Installation Steps
cd healthpredictionsystem
## Create Virtual Environment
virtualenv venv
## Activate Virtual Environment
venv\Scripts\activate
## Install Dependencies
pip install -r requirements.txt
## Apply Migrations
- python manage.py makemigrations
- python manage.py migrate
## Train Machine Learning Model
python train_model.py
## Start Server
python manage.py runserver
## Open Browser
http://127.0.0.1:8000/

## Input Features
- Glucose Level
- Haemoglobin Level
- Cholesterol Level
## Algorithm Used
Decision Tree Classifier
## Model Training
python train_model.py
## Model File
health_model.pkl
## 7. API Endpoints
http://127.0.0.1:8000/api/
