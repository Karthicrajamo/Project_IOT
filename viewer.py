from flask import Flask

app = Flask(__name__)
basename = /

@app.route(basename+"viewer")
def view():
    return render_template("viewer.html")

if __name__ == '__main__':
    app.run()