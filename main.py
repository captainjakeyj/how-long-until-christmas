from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    date_today = datetime.date.today()
    date_today_uk = date_today.strftime("%d/%m/%Y")
    christmas_day = datetime.date(2025, 12, 25)
    days_until_christmas = (christmas_day - date_today).days
    if days_until_christmas == 0:
        christmas_message = "Merry christmas!"
    else:
        christmas_message = f"There are {days_until_christmas} days until Christmas!"
    return render_template("index.html",
                           today=date_today_uk,
                           days=days_until_christmas,
                           message=christmas_message)

if __name__ == "__main__":
    app.run(debug=True)