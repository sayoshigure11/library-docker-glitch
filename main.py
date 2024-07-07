from flask import Flask, jsonify, request

app = Flask(__name__)



# https://youtu.be/8dOUauu0Og4?si=BTch5OgCffnYSTR7&t=446
import datetime
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.trigger.interval import IntervalTrigger


last_run_time = None

@app.route("/demo")
def cron_status():
    global last_run_time
    client = request.args.get('client')
    if client == 'gas':
        return "Glitch woke up"
    return f"Last run time of the job: {last_run_time}"

def my_cron_job():
    global last_run_time
    last_run_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    app.logger.info(f"job run at: {last_run_time}")

scheduler = BackgroundScheduler()
scheduler.start()

scheduler.add_job(
    func=my_cron_job,
    trigger=IntervalTrigger(minutes=2),
    id='my_cron_job_id',
    name='Print every 2 minutes',
    replace_existing=True
)

atexit.register(lambda: scheduler.shutdown())

@app.route("/")
def hello():
    client = request.args.get('client')
    if client == 'gas':
        return "Glitch woke up"
    return jsonify({"msg":"hello deploy from flask glitch"})


if __name__ == "__main__":
    app.run()