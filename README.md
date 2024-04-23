# House Inventory Management System

This Django project is designed to manage medicine, medicine schedule, and User name . Users can define name, medicine name, Descriptions, and associated Schedule details.

# Setup Instructions

Clone the repository:  git clone https://github.com/nutan-mal/Medical_management_system.git

Install dependencies:  cd medicine
pip install -r requirements.txt

Run migrations: python manage.py migrate


Create a superuser (admin) to access the admin panel:  python manage.py createsuperuser


Start the development server:   python manage.py runserver


Access the application at http://localhost:8000/ in your web browser.

# Check URLs :

 http://localhost:8000/
   http://localhost:8000/'login/
   
   http://localhost:8000/'logout/

   
   http://localhost:8000/user_profile/
   http://localhost:8000/medicine/
   
   http://localhost:8000/medicine/<int:medicine_id>//
   
  http://localhost:8000/room_report/ medicine_report/<int:medicine_id>//
    
  
# Directory Structure

Medicine/: Main project directory.

app1/: Django app for managing User, Medicine, and Schedule.

models.py: Contains models for User, Medicine, and Schedule.

views.py: Includes views for creating, listing, and managing Medicine, Details, and report.

forms.py: Django forms for creating and editing Medicine, Details, and Schedule details.

templates/: HTML templates for user interface.

admin.py: Admin panel configurations.

static/: Static files like CSS, JavaScript, images, etc.

requirements.txt: Lists project dependencies.

README.md: This file.



