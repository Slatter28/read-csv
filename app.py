from flask import Flask
from flask_api import status
import pandas as pd

app = Flask(__name__)


@app.route("/api/read-csv")
def csv():
    users = pd.read_csv("./users_spreadsheet.csv")
    return { "number of users": len(users)}, status.HTTP_200_OK


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9000, debug=True)