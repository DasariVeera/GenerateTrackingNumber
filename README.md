# Tracking Number Generator

This project provides a Django-based RESTful API that generates unique tracking numbers for parcels. This API is scalable, efficient, and capable of handling high concurrency.

## Features

- Generates unique tracking numbers conforming to the regex pattern ^[A-Z0-9]{1,16}$

- Designed for scalability and high concurrency.
  
- Handled database lock OperationalErrors with retry mechanism. 

## Requirements (Prerequisites)

- Python 3.x 
- Django 3.x or later (Preferably 4.2.x)
- Django REST Framework 3.x or later

## Getting started

### Clone the repository:

```bash
git clone git@github.com:DasariVeera/GenerateTrackingNumber.git

# Create virtual environment
python -m venv venv

# Activate created virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Run Web server
python manage.py runserver

# Access web
http://127.0.0.1:8000/api/next-tracking-number/
                       or 
http://localhost:8000/api/next-tracking-number/

```

## Running the tests
#### Required query params
- **origin_country_id:** The order’s origin country code in ISO 3166-1 alpha-2 format (e.g., "MY").
- **destination_country_id:** The order’s destination country code in ISO 3166-1 alpha-2 format (e.g, "ID").
- **weight:** The order’s weight in kilograms, up to three decimal places (e.g., "1.234").
- **created_at:** The order’s creation timestamp in RFC 3339 format (e.g.,"2018-11-20T19:29:32+08:00").
- **customer_id:** The customer’s UUID (e.g.,"de619854-b59b-425e-9db4-943979e1bd49").
- **customer_name:** The customer’s name (e.g., "RedBox Logistics").
- **customer_slug:** The customer’s name in slug-case kebab-case (e.g., "redbox-logistics").
### 1. Via Web
#### Provide Query params to the web api
##### Example Request
- http://127.0.0.1:8000/api/next-tracking-number/?customer_id=ab619854-b59b-425e-9db4-943979e1bd49&origin_country_id=IN&destination_country_id=US&weight=1&customer_name=xx&customer_slug=veera_veera&created_at=2018-11-20T19:29:32+08:0

##### Response
```bash
HTTP 201 Created
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "tracking_number": "INUSKQZ3UFPHIF0U",
    "customer_id": "ab619854-b59b-425e-9db4-943979e1bd49",
    "origin_country_id": "IN",
    "destination_country_id": "US",
    "created_at": "2024-09-15T07:48:32.839279Z"
}
```
### 2. Using python requests module
#### Code Snippet
```bash
import requests

API_URL = 'http://127.0.0.1:8000/api/next-tracking-number/?customer_id=ab619854-b59b-425e-9db4-943979e1bd49&origin_country_id=IN&destination_country_id=US&weight=3&customer_name=xx&customer_slug=x-x'

response = requests.get(API_URL)

print(response.json())

```
#### Response
```bash
{'tracking_number': 'INUSNV4JU60TM9LN', 'customer_id': 'ab619854-b59b-425e-9db4-943979e1bd49', 'origin_country_id': 'IN', 'destination_country_id': 'US', 'created_at': '2024-09-15T10:33:22.395802Z'}
```
### 3. Using Postman
#### Make GET request providing Query Params
<img width="529" alt="image" src="https://github.com/user-attachments/assets/5cc5bab2-ea7d-484d-84fc-1c77742a7521">

#### response
<img width="527" alt="image" src="https://github.com/user-attachments/assets/abc1bd0f-25c7-4dc4-8ab7-f6225dfbe468">

