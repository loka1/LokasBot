
 This repository contains code for generating leaderboard pages on a MediaWiki instance. The code is written in Python and makes use of the Pywikibot library.

The code consists of three main classes:

- Base: This class contains the shared logic for all other classes. It sets up the connection to the MediaWiki instance and defines the logic for calculating the start and end dates for the current week.

- SubPage: This class generates the leaderboard sub-pages for each activity (e.g. "articles created", "articles reviewed"). It takes a dictionary as input, containing the following keys:

  -  competition_page: The name of the main leaderboard page for the current week

  -  title_of_page: The name of the sub-page to be generated

  -  summary: The edit summary to be used when saving the page

  -  team: The name of the team being ranked (e.g. "top 5 article creators")

  -  activity: The activity being ranked (e.g. "articles created")

  -  query: The SQL query to be used to retrieve the rankings data from the database

- MainPage: This class generates the main leaderboard page for the current week. It takes the following arguments:

  - title_of_page: The name of the main leaderboard page
  - summary: The edit summary to be used when saving the page
  - stub: The name of the file containing the stub for the main leaderboard page
- The code also includes a TableGenerator class, which is used by the SubPage class to generate the table of rankings data to be included on the sub-pages.

## To use the code, you will need to:

* Clone this repository
* Install the required dependencies (Pywikibot and MySQL connector)
* Set up a user-config.py file in the root of the repository, as described in the Pywikibot documentation
* Edit the list_page_sub_pages variable in the data.py file to include the sub-pages you want to generate. Each sub-page should be represented as a dictionary with the keys described above.
* Run the daily.py script to generate the main leaderboard page and all sub-pages.
* You may also need to modify the Base class to specify the correct database connection details and the correct MediaWiki instance to connect to.

## المستخدمون الـ5 الأوائل في إنشاء المقالات 

~~~~sql
 SELECT actor_name as name, COUNT(*) as score 
    FROM revision r
    INNER JOIN actor ON r.rev_actor = actor.actor_id
    INNER JOIN page p on r.rev_page = p.page_id
    WHERE p.page_namespace=0
    and p.page_is_redirect=0
    and r.rev_timestamp between START_WEEK_DATE and END_WEEK_DATE
    and r.rev_parent_id=0
     and ucase(actor_name) not like ucase("%BOT") COLLATE utf8mb4_general_ci
  and actor_name not like "%بوت%" collate utf8mb4_general_ci
  and actor_name Not IN (SELECT user_name
                         FROM user_groups
                                  INNER JOIN user ON user_id = ug_user
                         WHERE ug_group = "bot")
                         and actor_name not in (SELECT replace(pl_title,"_"," ")
FROM pagelinks
where pagelinks.pl_from = 7352181
and pl_namespace = 2)
    GROUP BY actor_name
    having COUNT(*) > 1
    ORDER BY score DESC,name
    LIMIT 10;
~~~~

## أكثر 5 مستخدمين مراجعة للمقالات
~~~~sql
select
  actor_name as name,
  COUNT(*) as score
from
  logging
  INNER JOIN actor ON log_actor = actor.actor_id
where
  log_timestamp BETWEEN START_WEEK_DATE and END_WEEK_DATE
  and ucase(actor_name) not like ucase("%BOT") COLLATE utf8mb4_general_ci
  and actor_name not like "%بوت%" collate utf8mb4_general_ci
  and actor_name Not IN (SELECT user_name
                         FROM user_groups
                                  INNER JOIN user ON user_id = ug_user
                         WHERE ug_group = "bot")
  and log_action = "approve-i"
  and log_namespace = 0
  and actor_name not in (SELECT replace(pl_title,"_"," ")
FROM pagelinks
where pagelinks.pl_from = 7352181
and pl_namespace = 2)
group by actor_name
having COUNT(*) > 1
ORDER BY score DESC,name
LIMIT 10;
~~~~

        
        
        
## الإداريون الذين أجروا أكبر عدد من الأعمال الإدارية
~~~~sql
select actor_name as name, COUNT(*) as score
from logging
INNER JOIN actor on logging.log_actor = actor_id
where log_timestamp BETWEEN START_WEEK_DATE AND END_WEEK_DATE
and log_type in ("block", "protect", "delete", "rights")
and actor_name not in (SELECT replace(pl_title,"_"," ")
FROM pagelinks
where pagelinks.pl_from = 7352181
and pl_namespace = 2)
group by logging.log_actor
having COUNT(*)>1
ORDER BY score DESC,name
LIMIT 10;
~~~~

        
        
        
## المستخدمون الـ 5 الأوائل في إضافة نصوص
~~~~sql
SELECT actor_name as name, SUM(CAST(rev.rev_len as signed)-CAST(parent.rev_len as signed)) AS score, COUNT(rev.rev_id) as edit_count
FROM revision rev
INNER JOIN actor on rev.rev_actor = actor_id
JOIN revision parent
ON rev.rev_parent_id = parent.rev_id
INNER JOIN comment_revision on rev.rev_comment_id = comment_id
JOIN page
ON page_id = parent.rev_page
WHERE page_namespace = 0
and comment_text not like "%رجوع%"
and comment_text not like "%استرجاع%"
AND rev.rev_timestamp BETWEEN START_WEEK_DATE AND END_WEEK_DATE
AND parent.rev_timestamp BETWEEN START_WEEK_DATE AND END_WEEK_DATE
  and ucase(actor_name) not like ucase("%BOT") COLLATE utf8mb4_general_ci
  and actor_name not like "%بوت%" collate utf8mb4_general_ci
  and actor_name Not IN (SELECT user_name
                         FROM user_groups
                                  INNER JOIN user ON user_id = ug_user
                         WHERE ug_group = "bot")
and actor_name IN (SELECT user_name FROM user_groups INNER JOIN user ON user_id = ug_user WHERE ug_group = 'editor' or 'autoreview') 
and actor_name not in (SELECT replace(pl_title,"_"," ")
FROM pagelinks
where pagelinks.pl_from = 7352181
and pl_namespace = 2)
GROUP BY actor_name
having score > 0
ORDER BY score DESC,name
LIMIT 10;
~~~~

        
        

## أكثر 5 مستخدمين مراجعة للتعديلات
~~~~sql
select actor_name as name, COUNT(*) as score
    from logging
    INNER JOIN actor ON actor.actor_id = logging.log_actor
    where log_timestamp BETWEEN START_WEEK_DATE AND END_WEEK_DATE
    and log_action = "approve"
    and log_namespace = 0

    and actor_name Not IN (SELECT user_name FROM user_groups INNER JOIN user ON user_id = ug_user WHERE ug_group = 'bot') 
     and ucase(actor_name) not like ucase("%BOT") COLLATE utf8mb4_general_ci
  and actor_name not like "%بوت%" collate utf8mb4_general_ci
and actor_name not in (SELECT replace(pl_title,"_"," ")
FROM pagelinks
where pagelinks.pl_from = 7352181
and pl_namespace = 2)
    group by logging.log_actor
    having COUNT(*)>1
    ORDER BY score DESC,name
	LIMIT 10;
~~~~

        
        
        
## المستخدمون الـ5 الأوائل بعدد التعديلات
~~~~sql
SELECT actor_name as name, COUNT(rev.rev_id) as score
FROM revision rev
INNER JOIN actor on rev.rev_actor = actor_id
INNER JOIN comment_revision on rev.rev_comment_id = comment_id
JOIN page ON page_id = rev.rev_page
AND comment_text NOT LIKE ucase ("%[[ميدياويكي:Gadget-Cat-a-lot|تعديل تصنيفات]]%") collate utf8mb4_general_ci 
    AND comment_text NOT LIKE ucase ("%[[Project:أوب|أوب]]%") collate utf8mb4_general_ci 
    AND comment_text NOT LIKE ucase ("%[[ويكيبيديا:أوب|أوب]]%") collate utf8mb4_general_ci 
AND rev.rev_timestamp BETWEEN START_WEEK_DATE AND END_WEEK_DATE
AND ucase(actor_name) NOT LIKE ucase("%BOT") COLLATE utf8mb4_general_ci
AND actor_name NOT LIKE "%بوت%" collate utf8mb4_general_ci
AND actor_name NOT IN (SELECT user_name FROM user_groups INNER JOIN user ON user_id = ug_user WHERE ug_group = "bot")
and actor_name not in (SELECT replace(pl_title,"_"," ")
FROM pagelinks
where pagelinks.pl_from = 7352181
and pl_namespace = 2)
GROUP BY actor_name
HAVING score > 0
ORDER BY score DESC,name
LIMIT 10;
~~~~
        
        
        
## أنشط 5 مستخدمين بين المستخدمين الواعدين
~~~~sql
SELECT actor_name as name, COUNT(revision.rev_id) AS score
FROM user
INNER JOIN actor ON user_id = actor_user
INNER JOIN revision ON rev_actor = actor_id
INNER JOIN page ON page.page_id = revision.rev_page
WHERE rev_timestamp BETWEEN START_WEEK_DATE AND END_WEEK_DATE
AND user_registration BETWEEN DATE_BEFORE_30_DAYS and START_WEEK_DATE
AND page.page_namespace = 0
AND ucase(actor_name) NOT LIKE ucase("%BOT") COLLATE utf8mb4_general_ci
AND actor_name NOT LIKE "%بوت%" collate utf8mb4_general_ci
and actor_name NOT IN (SELECT user_name FROM user_groups INNER JOIN user ON user_id = ug_user WHERE ug_group = 'editor' or 'autoreview' or 'bot')
and actor_name not in (SELECT replace(pl_title,"_"," ")
FROM pagelinks
where pagelinks.pl_from = 7352181
and pl_namespace = 2)
GROUP BY actor_name
ORDER BY score DESC,name
LIMIT 10;
~~~~