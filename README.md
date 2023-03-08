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
   - `export FLASK_APP=app.py` to set the app for running
   - `flask run` to start the server

- **To run the tests please run the following commands on your terminal:**
    - `git clone https://github.com/mmsesay/speedykom-searcher-api.git` Only if you have cloned it in the previous step above
  

## App Endpoints
- GET: `/api/v1/search/<keyword>` the keyword is a string like: `health benefits` to query the records 


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

