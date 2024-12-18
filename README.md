# Python CRUD console app PSYCOPG2 and POSTGRES
#### Description
Well this is a practice to create a simple crud using python, psycopg2, postgres, sql scripts, email-validator, dotenv and for displaying data prettytables library.
With this practice you can make a solid foundation of python libraries, imports, and how can you interact with databases easily.

### How to run it
Note: You will need docker installed on your machine
Note: The data you save will not be preserved in time, after you close postgres image you will lose your data

1. Clone this repository
2. Define db.env at the root of the project (use db.env.example file)
3. Run:
   
```
docker compose up -d
```

5. In your terminal, init a virtualenv with python
6. Execute in your terminal:
   
```
pip install -r requirements.txt
```

#### To Do
Implement hashing of passwords
