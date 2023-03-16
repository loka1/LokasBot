import logging
import random
from datetime import datetime

from database.engine import webcite_engine, statistics_engine
from tasks.webcite.module import get_pages
from sqlalchemy.orm import Session
from database.models import Page, TaskName, Status, Statistic

LAST_QUERY_KEY = "webcite_last_query_time"  # Unique key for the last query time statistic


# def is_page_present(session: Session, page_title: str, task_name: TaskName) -> bool:
def is_page_present(session: Session, page_title: str) -> bool:
    """
    Checks if a page with the given title is already present in the database
    """
    # return session.query(Page).where(Page.title == page_title).where(Page.task_name == task_name).count() > 0
    return session.query(Page).where(Page.title == page_title).count() > 0


def main(*args: str) -> int:
    try:
        # todo: mereg with read.py in maintenance task
        # Update the last query time in the statistics table
        now = datetime.now()

        # Get the last query time from the statistics table, if it exists
        with Session(statistics_engine) as session:
            last_query = session.query(Statistic).filter(Statistic.key == LAST_QUERY_KEY).first()
            last_query_time = datetime.fromisoformat(last_query.value) if last_query else now
            logging.info(f"Last query time: {last_query_time}")


            # Calculate the time difference in minutes
            time_diff = (now - last_query_time).seconds // 60
            logging.info(f"time_diff: {time_diff}")
            pages = get_pages(time_diff + 3)

            with Session(webcite_engine) as webcite_session:
                for page_title in pages:
                    if not is_page_present(webcite_session, page_title=page_title):
                        logging.info("add : " + page_title)
                        temp_model = Page(
                            title=page_title,
                            thread=random.randint(1, 3),
                        )
                        webcite_session.add(temp_model)

                webcite_session.commit()

            # Update the last query time in the statistics table
            if last_query:
                last_query.value = now.isoformat()
            else:
                last_query = Statistic(key=LAST_QUERY_KEY, value=now.isoformat())
                session.add(last_query)
            session.commit()

        logging.info("Added pages to the database successfully.")
    except Exception as e:
        logging.error("Error occurred while adding pages to the database.")
        logging.exception(e)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
