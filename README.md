# UserProfile

## Overview
This project is a simple Django application that provides user authentication and account management features, including pages for login, signup, forgot password, change password, dashboard, and profile. The application also restricts access to certain pages based on the user's authentication status.

## Features
1. **User Authentication**: Users can register, log in, change their password, and log out.
2. **Pages**:
   - **Login Page**: Allows users to log in using their username/email and password.
   - **Sign Up Page**: Provides fields for user registration.
   - **Forgot Password Page**: Sends an email with a link to reset the password.
   - **Change Password Page**: Allows authenticated users to change their password.
   - **Dashboard**: Accessible only to logged-in users, displaying a personalized greeting and navigation links.
   - **Profile Page**: Displays user information including username, email, and account details.


## How to Run the Project
1. Clone the repository from the provided GitHub link.
2. Install the required dependencies using `pip install .`.
3. Run the Django server using:
   ```bash
   python manage.py runserver
   ```
4. Access the application at `http://localhost:8000/`.
