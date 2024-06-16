# Urine Strip Analyzer

This is a full-stack application for analyzing urine strips. The frontend is built with React, and the backend is built with Django. The application allows users to upload images of urine strips, processes the images, and returns the RGB values of specific colors on the strip.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x and pip
- Node.js and npm
- Django
- Django REST framework
- OpenCV for Python
- `django-cors-headers` package

## Installation

### Backend (Django)

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/urinestrip-analyzer.git
    cd urinestrip-analyzer
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations and start the server:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```

### Frontend (React)

1. Navigate to the `frontend` directory:
    ```sh
    cd frontend
    ```

2. Install the required npm packages:
    ```sh
    npm install
    ```

3. Start the React development server:
    ```sh
    npm start
    ```

## Usage

1. Start the Django backend server:
    ```sh
    python manage.py runserver
    ```

2. Start the React frontend development server:
    ```sh
    cd frontend
    npm start
    ```

3. Open your web browser and navigate to `http://localhost:3000`.

4. Upload an image of a urine strip and get the RGB values for analysis.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.
