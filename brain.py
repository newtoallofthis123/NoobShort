from time import strftime
from datetime import datetime, date
import random
import string
from requests.utils import requote_uri
import sqlite3

def time_cal():
    current_t = datetime.now()
    current_date = str(date.today())
    current_t_f = current_t.strftime("%H:%M:%S")
    timeAnddate = (f'{current_t_f} {current_date}')
    return timeAnddate

def url_gen():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    # symbols = string.punctuation
    whole =  lower + upper + digits
    pwd1 = random.sample(whole, 8)
    generated_url = "".join(pwd1)
    return generated_url

conn = sqlite3.connect('database.db', check_same_thread=False)
c = conn.cursor()

def check_db_health():
    try:
        c.execute("""CREATE TABLE urls(
            original text,
            short text,
            time_ text
        )""")
        conn.commit()
    except:
        pass

def add_engine(url, short_url):
    check_db_health()
    c.execute("INSERT INTO urls VALUES (:original, :short, :time_)",
        {
            'original': url,
            'short': short_url,
            'time_': time_cal()
        })
    conn.commit()

def check_engine(url):
    check_db_health()
    c.execute('SELECT * FROM urls WHERE original = :original', {
        'original': url
    })
    raw_db_content = c.fetchall()
    if raw_db_content == []:
        return "new"
    else:
        return "old"

def check_duplicate(short_url):
    check_db_health()
    c.execute('SELECT * FROM urls WHERE short = :short', {
        'short': short_url
    })
    raw_db_content = c.fetchall()
    if raw_db_content == []:
        return short_url
    else:
        new_short_url = url_gen()
        return new_short_url

def get_original(short_url):
    check_db_health()
    c.execute('SELECT * FROM urls WHERE short = :short', {
        'short': short_url
    })
    raw_db_content = c.fetchall()
    original = raw_db_content[0][0]
    return original

def debug_engine():
    check_db_health()
    c.execute('SELECT rowid, * FROM urls')
    raw_db_content = c.fetchall()
    print("INDEX \t   Original \t Short \t TIME")
    for thingy in raw_db_content:
        print(f'  {thingy[0]}   | {thingy[1]} | {thingy[2]} | {thingy[3]}')

def engine(url, short_url):
    check_db_health()
    if check_engine(url) == "new":
        final_original = url
        final_short = check_duplicate(short_url)
        add_engine(final_original, final_short)
    elif check_engine(url) == "old":
        check_db_health()
        c.execute('SELECT * FROM urls WHERE original = :original', {
            'original': url
        })
        raw_db_content = c.fetchall()
        final_original = raw_db_content[0][0]
        final_short = raw_db_content[0][1]
    final_list = [final_original, final_short]
    return final_list

def shorten(url):
    encoded_url = requote_uri(url)
    shortened_url = url_gen()
    encoded_shortened_url = requote_uri(shortened_url)
    short_list = engine(encoded_url, encoded_shortened_url)
    return short_list

# print(engine("https://youtube", "Hello"))
debug_engine()