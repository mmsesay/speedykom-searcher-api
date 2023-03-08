from flask import (
    Flask, 
    jsonify
)
from fetcher import get_data_from_health_gov


app = Flask(__name__)


@app.route("/api/v1/search/<keyword>", methods=['GET'])
def search_keyword(keyword):
    return get_data_from_health_gov(keyword)


if __name__ == "__main__":
    app.run()