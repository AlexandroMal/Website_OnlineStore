from flask import Flask, redirect, render_template, url_for

app = Flask("__name__")

@app.route('/')
def home_page():
    return render_template('index.html', title="Home Page", css_name='styles.css')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)