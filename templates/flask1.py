from flask import Flask, render_template
import datetime
import calendar
import pytz

run = Flask(__name__)

@test.route('/')
def index():
    currentTime = dateTime.dateTime.now(pytz.timezone)
    ctime = currentTime.strftime("%B %d %Y %H:%M:%S")
    return render_template('index.html', ctime = calendar.day_name[currentTime.weekday()] + ', ' + ctime)

if __name__ == '__main__':
    run.run()