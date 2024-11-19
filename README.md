# Contact Book

The **Contact Book** is a serverless application that allows users to store, manage, and retrieve contact information. It is built using Python, JSON, JSP, SASS, and SQL, and leverages AWS Lambda for serverless backend execution. This project integrates secure coding practices to protect user data.

---

## Features

- **Add Contacts**: Store contact details including name, email, and phone number.
- **View Contacts**: Fetch and display all stored contacts.
- **Input Validation**: Ensures proper format for email and phone numbers.
- **Authentication**: Protects API endpoints using JWT-based authentication.
- **Secure Frontend**: Implements security headers and sanitizes inputs.

---

## Technologies Used

### Backend
- **Python**: Main programming language for Lambda functions.
- **SQLite**: Lightweight SQL database for local development.
- **DynamoDB**: NoSQL database for scalable data storage in production.
- **Serverless Framework**: Deployment and configuration of AWS Lambda.

### Frontend
- **JSP**: Dynamic HTML rendering.
- **SASS**: For styling and responsive design.
- **JavaScript**: Handles form submissions and fetches API data.

### Security
- **JWT**: Authentication and authorization.
- **CORS**: Protects against cross-origin access.
- **Input Validation**: Ensures data integrity.
- **Content Security Policy**: Mitigates XSS attacks.

---

## Folder Structure

```plaintext
contact-book/
│
├── backend/                       # Backend files
│   ├── handler.py                 # Lambda function handlers
│   ├── database.py                # Database logic and connections
│   ├── auth.py                    # JWT authentication logic
│   ├── validation.py              # Input validation utilities
│   ├── middleware.py              # Security middleware
│
├── frontend/                      # Frontend files
│   ├── templates/                 # JSP templates
│   │   └── index.jsp              # Main frontend page
│   ├── static/                    # Static assets
│   │   ├── styles.scss            # SASS styles
│   │   ├── styles.css             # Compiled CSS
│   │   ├── app.js                 # JavaScript
│   │   ├── images/                # Optional images
│   ├── secure_headers.jsp         # JSP partial for security headers
│
├── serverless.yml                 # Serverless Framework configuration
├── README.md                      # Documentation
├── .gitignore                     # Git ignore file
├── tests/                         # Unit tests
│   ├── test_handler.py            # Test Lambda functions
│   ├── test_database.py           # Test database operations
│
└── scripts/                       # Utility scripts
    └── seed_data.py               # Script for seeding initial data
