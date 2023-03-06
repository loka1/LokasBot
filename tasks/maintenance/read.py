import sys

from core.utils.sqlite import create_database_table, maintenance_db_name, save_pages_to_db
from module import get_pages
import traceback


def main(*args: str) -> int:
    # todo: mereg with read.py in webcite task
    try:
        thread_number = 1
        time_before_start = int(sys.argv[1])
        if time_before_start == 2540:
            thread_number = 3
        elif time_before_start == 500:
            thread_number = 2
        pages = get_pages(time_before_start)
        conn, cursor = create_database_table(maintenance_db_name)
        save_pages_to_db(pages, conn, cursor, thread_number=thread_number)
        conn.close()
    except Exception as e:
        print(f"An error occurred: {e}")
        just_the_string = traceback.format_exc()
        print(just_the_string)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
