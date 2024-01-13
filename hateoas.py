from flask import Flask, redirect, request, render_template
import csv
import pandas as pd


class Contacts:
    def search(keyword):
        csv_file_path = 'contact_data.csv'
        target_keyword = keyword

        df = pd.read_csv(csv_file_path)

# Specify the columns you want to search in
        columns_to_search = ['First', 'Last', 'Phone', 'Email']

# Perform the search
        result = df[df[columns_to_search].apply(lambda row: target_keyword in row.values, axis=1)]

        print(result)
        return result

    def all():
        return


app = Flask(__name__)


@app.route("/")
def index():
    return redirect("/contacts")


@app.route("/contacts")
def contacts():
    search = request.args.get("q")
    if search is not None:
        contacts_set = Contacts.search(search)
    else:
        contacts_set = Contacts.all()
    return render_template("index.html", contacts=contacts_set)
