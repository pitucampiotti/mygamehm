from flask import Flask
from csv import reader
import random

from views import views

def getcard():
    # open file
    with open("HerdMentality.csv", "r", encoding='utf-8') as my_file:
        # pass the file object to reader()
        file_reader = reader(my_file)
        rows = list(file_reader)

        num=random.uniform(1, 992)
        num=int(num)
        print(rows[num][0])
        return rows[num][0]

app = Flask(__name__)


# @app.route("/")
# def home():
#     return getcard()

app.register_blueprint(views, url_prefix="/")


if __name__ == "__main__":
    app.run(debug=True, port=7000)


