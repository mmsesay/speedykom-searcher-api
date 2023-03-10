# speedykom-searcher-api

A simple web api that enable users to search for health related topics and a couple of articles to read

## Built With

- Flask
- Request

## Getting Started

- **To get a local copy of the repository please run the following commands on your terminal:**

  - `git clone git@github.com:mmsesay/speedykom-searcher-api.git`
  - `cd speedykom-searcher-api`
  - `python3 -m venv venv` to create a virtual environment
  - `source venv/bin/activate` to activate the virtual environment
  - `pip install -r requirements.txt` to intall the project dependencies

- **Please run the following commands on your terminal to setup the db:**

  - `cd project` to access the project main directory
  - `python` or `python3` to access the interactive shell
  - `from app import db, app` this commands starts references the db and flask app
  - `with app.app_context():` press enter after
  - `db.create_all()` press enter again
  - press `ctl + d` to exit the shell

- **Please run the following commands on your terminal to start the app:**

  - `cd ..` to come out of the main directory
  - `export FLASK_APP=project/server.py` to set the app for running
  - `flask run` to start the server

- **To run the tests please run the following commands on your terminal:**
  - `git clone https://github.com/mmsesay/speedykom-searcher-api.git` Only if you have cloned it in the previous step above
  - `pytest -v`

## App Endpoints

**Note: These are protected routes that needs an authorization header**

- GET: `/api/v1/records/search/<keyword>` the keyword is a string like: `health benefits` to query the records.
- GET: `/api/v1/records/<id>` to get a single record
- GET: `/api/v1/records` to get all the records for health

**Note: These routes doesn't needs an authorization header**

- POST: `/api/v1/register` Creates a new user with payload `{"email":"test@test.com", "password":"test"}`
- POST: `/api/v1/login` Login a user with payload `{"email":"test@test.com", "password":"test"}`

## Author

👤 **Muhammad Sesay**

- GitHub: [@mmsesay](https://github.com/mmsesay)
- Twitter: [@DeeMaejor](https://twitter.com/DeeMaejor)
- LinkedIn: [LinkedIn](https://linkedin.com/in/muhammad-m-sesay)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

## Show your support

Give a ⭐️ if you like this project!

## Acknowledgments

- Datasource from [Health.gov](https://health.gov/our-work/national-health-initiatives/health-literacy/consumer-health-content/free-web-content/apis-developers/api-documentation)
