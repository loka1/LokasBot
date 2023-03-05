import random
import sqlite3

from threading import Timer

import pymysql
import pywikibot
from pywikibot import config as _config
import os
import datetime
import traceback

from tasks.webcite.modules.parsed import Parsed
from core.utils.wikidb import Database


def create_database_table():
    home_path = os.path.expanduser("~")
    database_path = os.path.join(home_path, "webcite.db")
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Create the table with a status column
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS pages (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, status INTEGER, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,thread INTEGER)''')

    return conn, cursor


def get_pages(start):
    query = """SELECT pl_2_title
FROM (
    SELECT DISTINCT page.page_title AS "pl_2_title"
    FROM revision
    INNER JOIN page ON revision.rev_page = page.page_id
    WHERE page.page_namespace IN (0)
    AND rev_timestamp > DATE_SUB( now(), INTERVAL MINUTE_SUB_NUMBER MINUTE ) and page_is_redirect = 0
) AS pages_list"""
    database = Database()
    database.query = query.replace("MINUTE_SUB_NUMBER", str(start))
    database.get_content_from_database()
    gen = []
    for row in database.result:
        title = str(row['pl_2_title'], 'utf-8')
        gen.append(title)

    gen = set(gen)
    return gen


def save_pages_to_db(gen, conn, cursor, thread_number):
    for entry in gen:
        try:
            title = entry
            cursor.execute("SELECT * FROM pages WHERE title = ?", (title,))
            if cursor.fetchone() is None:
                print("added : " + title)
                cursor.execute("INSERT INTO pages (title, status,thread) VALUES (?, 0,?)",
                               (title, int(thread_number)))
            conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred while inserting the title {entry.title()} into the database: {e}")


def get_articles(cursor, thread_number):

    query1 = """
        SELECT id, title, thread
        FROM pages
        WHERE status = 0 AND thread = 1
        ORDER BY date ASC
        LIMIT 200 OFFSET ?;
    """

    query2 = """
        SELECT id, title, thread
        FROM pages
        WHERE status = 0 AND thread = 2
        ORDER BY date ASC
        LIMIT 150 OFFSET ?;
    """

    query3 = """
        SELECT id, title, thread
        FROM pages
        WHERE status = 0 AND thread = 3
        ORDER BY date ASC
        LIMIT 100 OFFSET ?;
    """

    cursor.execute(query1, (thread_number,))
    result1 = cursor.fetchall()

    cursor.execute(query2, (thread_number,))
    result2 = cursor.fetchall()

    cursor.execute(query3, (thread_number,))
    result3 = cursor.fetchall()

    rows = result1 + result2 + result3
    return rows


def check_status():
    site = pywikibot.Site()
    title = "مستخدم:LokasBot/الإبلاغ عن رابط معطوب أو مؤرشف"
    page = pywikibot.Page(site, title)
    text = page.text
    if text == "لا":
        return True
    return False


def process_article(site, cursor, conn, id, title, thread_number,limiter):
    def handle_timeout():
        print(f"Timeout while processing {title}")
        raise TimeoutError()

    try:
        cursor.execute("SELECT status FROM pages WHERE id = ? LIMIT 1", (id,))
        row = cursor.fetchone()
        if row is not None:
            status = row[0]
            if status == 0:
                cursor.execute("UPDATE pages SET status = 1 WHERE id = ?", (id,))
                conn.commit()
                page = pywikibot.Page(site, title)

                if page.exists() and (not page.isRedirectPage()):
                    summary = ""
                    bot = Parsed(page.text, summary,limiter)

                    # Set the timeout here with Timer
                    t = Timer(1600, handle_timeout)
                    t.start()

                    new_text, new_summary = bot()
                    # write processed text back to the page
                    if new_text != page.text and check_status():
                        print("start save " + page.title())
                        page.text = new_text
                        page.save(new_summary)
                    else:
                        print("page not changed " + page.title())
                    t.cancel()
                # todo add option to not update page if have one or more links not archived
                cursor.execute("DELETE FROM pages WHERE id = ?", (id,))
                conn.commit()

    except TimeoutError:
        delta = datetime.timedelta(hours=6)
        new_date = datetime.datetime.now() + delta
        cursor.execute("UPDATE pages SET status = 0, date = ? WHERE id = ?",
                       (new_date, id))
        conn.commit()
    except Exception as e:
        print(f"An error occurred while processing {title}: {e}")
        just_the_string = traceback.format_exc()
        print(just_the_string)
        delta = datetime.timedelta(hours=1)
        new_date = datetime.datetime.now() + delta
        cursor.execute("UPDATE pages SET status = 0, date = ? WHERE id = ?",
                       (new_date, id))
        conn.commit()
