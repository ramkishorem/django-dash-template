from django.utils.timezone import now, localtime
from datetime import timedelta, datetime, date, time as datetime_time
from collections import namedtuple

Month = namedtuple('Month',['month','year'])

def today():
    return now().date()

def previous_day(dayte):
    return dayte - timedelta(days=1)

def next_day(dayte):
    return dayte + timedelta(days=1)

def months_ago(months, dayte=today()):
    years = int(months/12)
    months = months%12
    month = (12 + dayte.month - months) % 12 or 12
    year = dayte.year - years - 1 if months>=dayte.month \
        else dayte.year - years
    return Month(month, year)

def months_from(months, dayte=today()):
    years = int(months/12)
    months = months%12
    month = (12 + dayte.month + months) % 12 or 12
    year = dayte.year + years
    if months > (12 - dayte.month):
        year += 1
    return Month(month, year)

def month_first_date(month):
    return date(month.year, month.month, 1)

def month_last_date(month):
    last_day = 31
    while last_day>27:
        try:
            return date(month.year, month.month, last_day)
        except ValueError:
            last_day = last_day - 1
            continue
    return None

def years_from(dayte, years):
    return dayte + timedelta(days=int(365*years))

def weeks_ago(dayte, weeks):
    return dayte - timedelta(days=int(7*weeks))

def years_ago(dayte, years):
    return dayte - timedelta(days=int(365*years))

def yesterday():
    return previous_day(today())

def tomorrow():
    return next_day(today())

def daydelta(start_date, end_date=today()):
    return int( (end_date-start_date).days )

def daterange(start_date, end_date=today(), backwards = False):
    for n in range( daydelta(start_date, end_date) ):
        if backwards:
            yield end_date - timedelta(n)
        else:
            yield start_date + timedelta(n)

def date_from_string(date_string):
    try:
        return datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        return None

def calculate_age(born):
    this_day = today()
    try:
        birthday = born.replace(year=this_day.year)
    except ValueError:
        # raised when birth date is February 29 and the 
        # current year is not a leap year
        birthday = born.replace(year=this_day.year,
            month=born.month+1, day=1)
    if birthday > this_day:
        return this_day.year - born.year - 1
    return this_day.year - born.year

def months_between_2_dates(starting_date, ending_date=now().date()):
    yield_date = date(starting_date.year,starting_date.month,1)
    while yield_date < ending_date:
        yield Month(yield_date.month, yield_date.year)
        if yield_date.month == 12:
            yield_date = date(
                yield_date.year+1,
                1,1)
        else:
            yield_date = date(
                yield_date.year,
                yield_date.month+1,
                1)

def oldest_dob_for_age(age):
    this_day = today()
    try:
        age_years_ago = this_day.replace(
            year=this_day.year - age - 1)
    except ValueError:
        age_years_ago = this_day.replace(
            year=this_day.year - age - 1,
            month=born.month + 1, day=1)
    return age_years_ago + timedelta(1)

def newest_dob_for_age(age):
    this_day = today()
    try:
        age_years_ago = this_day.replace(year=this_day.year-age)
    except ValueError:
        age_years_ago = this_day.replace(year=this_day.year-age,
            month=born.month+1, day=1)
    return age_years_ago

def local_now():
    return localtime(now())


def time_diff(start, end):
    if isinstance(start, datetime_time): # convert to datetime
        assert isinstance(end, datetime_time)
        start, end = [datetime.combine(datetime.min,t) \
            for t in [start, end]]
    if start <= end: # e.g., 10:33:26-11:15:49
        return end - start
    else: # end < start e.g., 23:55:00-00:25:00
        end += timedelta(1) # +day
        assert end > start
        return end - start

def minutes_from(tyme, minutes):
    return tyme + timedelta(minutes=minutes)

def less_than_minutes_ago(tyme, minutes):
    """
    see if the given datetime value is within 'minutes' ago from now
    """
    added_time = minutes_from(tyme, minutes)
    return added_time >= now()

def daterange(start_date, end_date):
    if start_date <= end_date:
        for n in range( ( end_date - start_date ).days + 1 ):
            yield start_date + timedelta( n )
    else:
        for n in range( ( start_date - end_date ).days + 1 ):
            yield start_date - timedelta( n )

def current_financial_year_start_date():
    this_day = today()
    this_year, this_month = this_day.year, this_day.month
    return date(
        year = this_year if this_month>=4 else (this_year - 1),
        month = 4,
        day = 1
        )
