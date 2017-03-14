from flask import Flask, render_template, request, redirect, url_for
import data_manager

app = Flask(__name__)

@app.route("/request-counter", methods=['GET', 'POST'])
def increment():
    if request.method == "GET":
        get_counter = data_manager.show_get_counter()[0]
        return get_counter



if __name__ == "__main__":
    app.run(debug=True)
