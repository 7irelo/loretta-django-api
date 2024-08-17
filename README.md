# Loretta Bank - Server API

Welcome to Loretta Bank, an online banking application built with Django and PostgreSQL. This project is a backend API for managing various banking operations, providing a secure and robust platform for user authentication, account management, transactions, and more.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Folder Structure](#folder-structure)

## Features

- User Authentication (Sign Up, Log In, Log Out)
- Account Management (Create, View, Update, Delete Accounts)
- Fund Transfers (Internal and External)
- Transaction History
- Balance Inquiries

## Tech Stack

- **Backend**: Django
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)

## Installation

### Prerequisites

- Docker and Docker Compose installed
- Git installed

### Docker Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/7irelo/loretta-django-api.git
    cd loretta-django-api
    ```

2. Build and start the containers:

    ```bash
    docker-compose up --build
    ```

### Environment Variables

Ensure your environment variables are set correctly. Here are the default ones used in the Docker setup:

- Backend `.env`:

    ```env
    DJANGO_SECRET_KEY=your_django_secret_key
    DATABASE_URL=postgres://postgres:password@db:5432/loretta_bank
    JWT_SECRET=your_jwt_secret
    ```

## Usage

The API server will be running on `http://localhost:8000`. You can use a tool like Postman or cURL to interact with the API.

## API Endpoints

### Authentication

- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Log in a user
- `GET /api/auth/user/` - Get the authenticated user's details
- `POST /api/auth/logout/` - Log out a user

### Accounts

- `GET /api/accounts/` - Get all accounts for the authenticated user
- `POST /api/accounts/` - Create a new account
- `GET /api/accounts/<id>/` - Get a specific account
- `PUT /api/accounts/<id>/` - Update a specific account
- `DELETE /api/accounts/<id>/` - Delete a specific account

### Transactions

- `GET /api/transactions/` - Get all transactions for the specific account
- `POST /api/transactions/` - Create a new transaction
- `GET /api/transactions/<id>/` - Get a specific transaction
- `PUT /api/transactions/<id>/` - Update a specific transaction
- `DELETE /api/transactions/<id>/` - Delete a specific transaction

### Cards

- `GET /api/cards/` - Get all cards for the specific account
- `POST /api/cards/` - Create a new card
- `GET /api/cards/<id>/` - Get a specific card
- `PUT /api/cards/<id>/` - Update a specific card
- `DELETE /api/cards/<id>/` - Delete a specific card

### Loans

- `GET /api/loans/` - Get all loans for the specific account
- `POST /api/loans/` - Create a new loan
- `GET /api/loans/<id>/` - Get a specific loan
- `PUT /api/loans/<id>/` - Update a specific loan
- `DELETE /api/loans/<id>/` - Delete a specific loan

### Customer Support

- `GET /api/support/` - Get all support tickets for the specific user
- `POST /api/support/` - Create a new support ticket
- `GET /api/support/<id>/` - Get a specific support ticket
- `PUT /api/support/<id>/` - Update a specific support ticket
- `DELETE /api/support/<id>/` - Delete a specific support ticket

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or issues, please contact us at [support@lorettabank.com](mailto:support@lorettabank.com).

## Folder Structure

```
loretta-bank-api/
├── manage.py                  # Django project management script
├── loretta_bank/              # Main Django app
│   ├── settings.py            # Django settings
│   ├── urls.py                # URL routing
│   ├── wsgi.py                # WSGI application
│   ├── asgi.py                # ASGI application
│   ├── apps/                  # Django apps (e.g., accounts, transactions)
│   ├── models/                # Database models
│   ├── views/                 # Views (controllers)
│   ├── serializers/           # DRF serializers
│   ├── permissions/           # Custom permissions
│   └── admin.py               # Django admin configurations
├── docker-compose.yml         # Docker Compose configuration
├── Dockerfile                 # Dockerfile for Django app
└── README.md
```
