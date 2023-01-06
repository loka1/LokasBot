from module import UpdatePage, ArticleTables,index

# Set the parameters for the update
query = """SELECT actor_name, COUNT(*) as q_user_editcount
FROM revision r
         INNER JOIN actor ON r.rev_actor = actor.actor_id
         INNER JOIN page p on r.rev_page = p.page_id
WHERE p.page_namespace = 12
  and p.page_is_redirect = 0
  and r.rev_parent_id = 0
  and actor_id NOT IN ("2579643")
  and actor_user not in (137877)
GROUP BY actor_name
having COUNT(*) > 1
ORDER BY COUNT(*) DESC
LIMIT 500;"""
file_path = 'stub/users_by_number_of_help_pages_creation_with_bot.txt'
page_name = "ويكيبيديا:إحصاءات/المستخدمين حسب عدد إنشاء صفحات المساعدة (متضمنة البوتات)"

# Create an instance of the ArticleTables class
tables = ArticleTables()


def username(row, result,index):
    username = str(row['actor_name'], 'utf-8')
    name = username.replace("__", "[LOKA]").replace("_", " ").replace("[LOKA]", "_")
    return "[[مستخدم:" + username + "|" + name + "]]"


def total_edits(row, result,index):
    username = str(row['actor_name'], 'utf-8')
    number = format(row['q_user_editcount'], ',').replace(',', '٬')
    return "[[خاص:مساهمات/" + username + "|" + number + "]]"


columns = [
    ("الرقم", None, index),
    ("المستخدم", None, username),
    ("عدد الصفحات المساعدة", None, total_edits),
]

tables.add_table("main_table", columns)

# Create an instance of the updater and update the page
updater = UpdatePage(query, file_path, page_name, tables)
updater.update()
