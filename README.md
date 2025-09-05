#Rayoshop
> A Django-based e-commerce website with REST API support using Django REST Framework (DRF). It provides a full shopping experience, including item management, user authentication, and a customer cart system.


## Features
- Frontend Templates: Built with Django for a smooth shopping experience.
- API Endpoints: Powered by Django REST Framework (DRF) for integration and automation.
- Authentication: Token-based authentication for secure access.
- Role-Based Permissions:
  * Admins & Managers: Can add, update, or remove items.
  * Customers: Can browse items and manage a cart.
  * Shopping Cart: Customers can add/remove items and place orders.

## Tech Stack
- Django & Django REST Framework (DRF)
- SQLite
- HTML/CSS/JS for frontend templates

## API Endpoints
(/api/...)
| Method | Endpoint | Description | Authorization |
| --- | --- | --- | --- |
| POST | /signup | Sign up | no need | 
| POST | /login | Log in | no need | 
| GET | / | Retrieve all Items | no need |
| GET | /big/ExCat | ExCat lvl 1 Categorie page | no need |
| GET | /sml/ExCat | ExCat lvl 2 Categorie page | no need |
| GET | /search/sth | Items including sth in name | no need |
| GET | /ExItem | ExItem Item page | no need |
| POST | /ExItem | ExItem add to Cart | Token auth |
| POST | /create | Create Item  | Token auth(admin or manager) |
| GET | /cart | Users cart page | Token auth(customer) |

Body for SignUp
```json
{
"username" : "user",
"password" : "pass",
}
```
Body for LogIn
```json
{
    "username" : "user",
    "password" : "pass"
}
```
Body for Create Recipe
```json
{
{
    "name":"item name",
    "about":"some info about item",
    "price":100,
    "off":10,
    "categor":"items categorie"
}
}
```

Installation & Setup
- Clone the repository:
```bash
git clone https://github.com/Sina-Rayo/RayoShop
cd [PROJECT DIRECTORY]
```
- Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
- Install dependencies:
```bash
pip install -r requirements.txt
```
- Apply migrations:
```bash
python manage.py migrate
```
- Run the server:
```bash
python manage.py runserver
```
- API base URL: http://127.0.0.1:8000/api

## Usage
Consume the API using tools like Postman or cURL, passing Basic Authentication credentials for protected endpoints.
