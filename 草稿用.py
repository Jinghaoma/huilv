import datetime


def return_next_day(t_str="20150101"):
    d = datetime.datetime.strptime(t_str, '%Y%m%d')
    d.strftime('%Y%m%d')
    delta = datetime.timedelta(days=1)
    d1 = d + delta
    return d1.strftime('%Y%m%d')

