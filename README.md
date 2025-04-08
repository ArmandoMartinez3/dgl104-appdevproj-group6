# Gym Project

This is a Django project for gym management.

## Prerequisites

- Python 3.8 or higher
- Node.js (for django-tailwind)
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone [REPOSITORY_URL]
cd [DIRECTORY_NAME]
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure the database:
```bash
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python create_superuser.py
```

## Running the Project

1. Make sure the virtual environment is activated.

2. Start the development server:
```bash
python manage.py runserver
```

3. Access the application:
   - Open your browser and go to: `http://127.0.0.1:8000/`

## Project Structure

- `gymapp/`: Main gym application
- `User_Gymproject/`: Project configuration
- `Images_sujal/`: Images directory
- `STMS/`: Student management system
- `Gym_Project/`: Additional project components

## Database Configuration

The project uses SQLite by default. To configure a different database:

1. Modify the `settings.py` file in `User_Gymproject/`
2. Run migrations:
```bash
python manage.py migrate
```

## Additional Notes

- Make sure you have the correct database permissions
- The `init_local_db.py` file can be used to initialize the local database
- For development, it's recommended to use Django's development server
- For production, it's recommended to use gunicorn as specified in `render.yaml`

## Support

For any issues or inquiries, please contact the development team. 