# How to run

### Runs dockerized solution
```
docker-compose up
```

### Run to make migrations:
```
docker-compose run web python3 manage.py migrate
```

### Run to fill in data into database:
```
docker-compose run web python3 manage.py create_script
```

### Run to delete all data in database:
```
docker-compose run web python3 manage.py delete_script
```

Data is created programmatically via the create_script. It will add 3 users with 20 products and rating for each of them.

The .env.dev is placed for demonstration purposes only.