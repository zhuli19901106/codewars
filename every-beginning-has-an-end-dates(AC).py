from datetime import datetime, timedelta

def week_start_date(dt):
    wd = dt.weekday()
    return dt + timedelta(days=-wd)

def week_end_date(dt):
    wd = dt.weekday()
    return dt + timedelta(days=6-wd)
