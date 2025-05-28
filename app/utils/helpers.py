# utils/helpers.py
import datetime

def check_subscription_expired(subscription):
    end_date = subscription.start_date + datetime.timedelta(days=subscription.plan.duration)
    if datetime.datetime.utcnow() > end_date:
        return True
    return False