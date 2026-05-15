from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def run_matching():
    print("Running AI matching...")

    # fetch CVs + jobs
    # calculate scores
    # send alerts if score > threshold

scheduler.add_job(run_matching, "interval", minutes=10)
scheduler.start()