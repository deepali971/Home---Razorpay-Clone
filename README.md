Project Title


Description

This project is a Flask web application designed to provide users with a platform to manage their contact submissions and user authentication. It allows users to sign up, log in, and submit contact forms, which are stored in a SQLite database. The application features a user-friendly interface with multiple pages, including home, contact, features, pricing, and checkout.

Key Features

- User authentication (sign up, log in, log out)
- Contact form submission with data storage
- Dynamic rendering of HTML templates
- SQLite database for data management
- Responsive design for various devices

Technologies Used

- Flask: A lightweight WSGI web application framework in Python.
- SQLite: A C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.
- Werkzeug: A comprehensive WSGI web application library.

Working

The application operates as follows:

1. User Authentication:

   - Users can sign up by providing a username and password. The password is securely hashed before being stored in the SQLite database.
   - After signing up, users can log in using their credentials. If the credentials are valid, a session is created, allowing the user to access authenticated features.

2. Contact Form Submission:

   - Authenticated users can navigate to the contact page, where they can fill out a form with their name, email, and message.
   - Upon submission, the data is sent to the server, where it is processed and stored in the SQLite database. Users receive a confirmation message upon successful submission.

3. Dynamic Pages:

   - The application features multiple pages, including:
     - **Home**: The landing page that introduces the application and its purpose.
     - **Contact**: A page with a form for users to submit their inquiries.
     - **Features**: A page that outlines the application's features and benefits.
     - **Pricing**: A page that details pricing information for services offered.
     - **Checkout**: A page that requires user authentication to access, ensuring that only logged-in users can proceed with purchases.

4. Navigation:

   - Users can easily navigate between different pages using links provided in the application. The application is designed to be responsive, ensuring a seamless experience across various devices.

Installation Instructions

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

Usage

Instructions on how to run the application:
```
python app.py
```

License

This project is licensed under the MIT License.
