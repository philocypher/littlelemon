# Restaurant API Documentation

This documentation provides information about the endpoints available in the Restaurant API.


### Prerequisites

Before you begin, make sure you have Pipenv installed on your system. If you don't have Pipenv installed, you can do so with the following command:

`pip install pipenv`

### Navigate to the root directory of your Django project (where Pipfile is located).
## Setting Up a Virtual Environment and Installing Dependencies

To ensure that your Restaurant API project is isolated and that all dependencies are properly managed, you can use Pipenv, a popular Python dependency management tool. Here's how to set up a virtual environment and install project dependencies:

```bash

pipenv shell

pipenv install

cd littlelemon

python3 manage.py runserver

```

### Now you should be able to go to http://localhost:8000/ and greeted with a simple welcome page
## Menu Endpoints

### Browse Menu Items
- **URL:** `/api/menu`
- **Method:** `GET`
- **Description:** Retrieve a list of menu items.

### Add New Menu Item
- **URL:** `/api/menu`
- **Method:** `POST`
- **Description:** Add a new menu item.
- **Request Body:** JSON data with `title`, `price`, and `inventory` fields.

### Get Specific Menu Item
- **URL:** `/api/menu/{pk}`
- **Method:** `GET`
- **Description:** Retrieve information about a specific menu item identified by `{pk}`.

## Booking Endpoints

### Secure Table Booking
- **URL:** `/booking/tables`
- **Method:** `POST`
- **Description:** Secure a table booking (Requires authentication token).

## Authentication Endpoints

### Register New User
- **URL:** `/auth/users`
- **Method:** `POST`
- **Description:** Register a new user by providing `username` and `password` as JSON data or form data.

### Get Authentication Token
- **URL:** `/auth/token/login`
- **Method:** `POST`
- **Description:** Obtain an authentication token by providing valid credentials.

### Get Authentication Token (Alternative)
- **URL:** `/api-token-auth/`
- **Method:** `POST`
- **Description:** Obtain an authentication token by providing `username` and `password`.

### Logout User
- **URL:** `/auth/token/logout`
- **Method:** `POST`
- **Description:** Log out the user (Requires authentication token).

## Authentication

To access endpoints that require authentication, you must include the authentication token in the request headers using the `Authorization` header. The token should be in the format: `Bearer <token>`.
- Header exapmle 'Authorization: Bearer <your_token_here>'


## Running Unit Tests

To ensure the reliability and functionality of the Restaurant API, you can run unit tests locally using Django's testing framework.


### Running Tests

To run the unit tests, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the root directory of your Django project (where `manage.py` is located).

3. Run the following command to execute the tests located in the `tests` directory:

   ```bash
   python3 manage.py test tests
   ```



