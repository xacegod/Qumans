# How to run

### Runs dockerized solution
```
docker-compose up
```

### Run to make migrations:
```
python3 manage.py makemigrations
```

### Run to migrate:
```
docker-compose run web python3 manage.py migrate
```

### Run to fill in dummy data into database:
```
docker-compose run web python3 manage.py create_script
```

### Run to delete all data from database:   
```
docker-compose run web python3 manage.py delete_script
```

Data is created programmatically via the create_script. It will add 3 users with 20 products and rating for each of them.

The .env.dev is placed for demonstration purposes only.

In the view code, there are examples of different approach to writing API, and this is for demonstration only.

Credentials for test users are in create_script, but also can be found here:
```
username: super
password: tesT123
```

This application will use default Django authentication method for user rating.

#### URLs are:
```
"http://127.0.0.1:8000/api/v1/product/": "Product list",
"http://127.0.0.1:8000/api/v1/product/create/": "Create product",
"http://127.0.0.1:8000/api/v1/product/update/<int:pk>/": "Update product",
"http://127.0.0.1:8000/api/v1/product/delete/<int:pk>/": "Delete product",
"http://127.0.0.1:8000/api/v1/product/<int:pk>/": "Get product with id",
"http://127.0.0.1:8000/api/v1/product/rate/": "Rating list",
"http://127.0.0.1:8000/api/v1/product/rate/create": "Create rating",
"http://127.0.0.1:8000/api/v1/product/rate/<int:pk>/": "All rating",
"http://127.0.0.1:8000/api/v1/product/rate/list/": "Ratings list",
```

#### API endpoint documentation
```
http://127.0.0.1:8000/api/v1/swagger/
```
```
http://127.0.0.1:8000/api/v1/redoc
```
