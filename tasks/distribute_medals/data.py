list_of_distribute_medals = [
    {
        "number": 500,
        "query" : """
SELECT actor_name, sum_yc, sum_tc
FROM (
  SELECT actor.actor_name,
         SUM(yc_rev.cnt) + SUM(yc_arc.cnt) AS sum_yc,
         SUM(tc_rev.cnt) + SUM(tc_arc.cnt) AS sum_tc
  FROM actor
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision WHERE rev_timestamp < START_DATE GROUP BY rev_actor) yc_rev
  ON yc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive WHERE ar_timestamp < START_DATE GROUP BY ar_actor) yc_arc
  ON yc_arc.ar_actor = actor.actor_id
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision AND rev_timestamp > END_DATE GROUP BY rev_actor) tc_rev
  ON tc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive AND rev_timestamp > END_DATE GROUP BY ar_actor) tc_arc
  ON tc_arc.ar_actor = actor.actor_id
  WHERE actor_name not IN (SELECT REPLACE(pl_title, '_', ' ') FROM pagelinks WHERE  pl_from = 7519882)
  GROUP BY actor.actor_name
) sub
WHERE sum_yc < NUMBER_COUNT AND sum_tc >= NUMBER_COUNT
""",
        "template_stub": "{{وسام تعديلات|NUMBER|-- SIGNATURE}}"
    },
    {
        "number": 1000,
        "query" : """
SELECT actor_name, sum_yc, sum_tc
FROM (
  SELECT actor.actor_name,
         SUM(yc_rev.cnt) + SUM(yc_arc.cnt) AS sum_yc,
         SUM(tc_rev.cnt) + SUM(tc_arc.cnt) AS sum_tc
  FROM actor
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision WHERE rev_timestamp < START_DATE GROUP BY rev_actor) yc_rev
  ON yc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive WHERE ar_timestamp < START_DATE GROUP BY ar_actor) yc_arc
  ON yc_arc.ar_actor = actor.actor_id
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision AND rev_timestamp > END_DATE GROUP BY rev_actor) tc_rev
  ON tc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive AND rev_timestamp > END_DATE GROUP BY ar_actor) tc_arc
  ON tc_arc.ar_actor = actor.actor_id
  WHERE actor_name not IN (SELECT REPLACE(pl_title, '_', ' ') FROM pagelinks WHERE  pl_from = 7519882)
  GROUP BY actor.actor_name
) sub
WHERE sum_yc < NUMBER_COUNT AND sum_tc >= NUMBER_COUNT
""",
        "template_stub": "{{وسام تعديلات|NUMBER|-- SIGNATURE}}"
    },
    {
        "number": 2000,
        "query" : """
SELECT actor_name, sum_yc, sum_tc
FROM (
  SELECT actor.actor_name,
         SUM(yc_rev.cnt) + SUM(yc_arc.cnt) AS sum_yc,
         SUM(tc_rev.cnt) + SUM(tc_arc.cnt) AS sum_tc
  FROM actor
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision WHERE rev_timestamp < START_DATE GROUP BY rev_actor) yc_rev
  ON yc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive WHERE ar_timestamp < START_DATE GROUP BY ar_actor) yc_arc
  ON yc_arc.ar_actor = actor.actor_id
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision AND rev_timestamp > END_DATE GROUP BY rev_actor) tc_rev
  ON tc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive AND rev_timestamp > END_DATE GROUP BY ar_actor) tc_arc
  ON tc_arc.ar_actor = actor.actor_id
  WHERE actor_name not IN (SELECT REPLACE(pl_title, '_', ' ') FROM pagelinks WHERE  pl_from = 7519882)
  GROUP BY actor.actor_name
) sub
WHERE sum_yc < NUMBER_COUNT AND sum_tc >= NUMBER_COUNT
""",
        "template_stub": "{{وسام تعديلات|NUMBER|-- SIGNATURE}}"
    },
    {
        "number": 3000,
        "query" : """
SELECT actor_name, sum_yc, sum_tc
FROM (
  SELECT actor.actor_name,
         SUM(yc_rev.cnt) + SUM(yc_arc.cnt) AS sum_yc,
         SUM(tc_rev.cnt) + SUM(tc_arc.cnt) AS sum_tc
  FROM actor
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision WHERE rev_timestamp < START_DATE GROUP BY rev_actor) yc_rev
  ON yc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive WHERE ar_timestamp < START_DATE GROUP BY ar_actor) yc_arc
  ON yc_arc.ar_actor = actor.actor_id
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision AND rev_timestamp > END_DATE GROUP BY rev_actor) tc_rev
  ON tc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive AND rev_timestamp > END_DATE GROUP BY ar_actor) tc_arc
  ON tc_arc.ar_actor = actor.actor_id
  WHERE actor_name not IN (SELECT REPLACE(pl_title, '_', ' ') FROM pagelinks WHERE  pl_from = 7519882)
  GROUP BY actor.actor_name
) sub
WHERE sum_yc < NUMBER_COUNT AND sum_tc >= NUMBER_COUNT
""",
        "template_stub": "{{وسام تعديلات|NUMBER|-- SIGNATURE}}"
    },
    {
        "number": 5000,
        "query" : """
SELECT actor_name, sum_yc, sum_tc
FROM (
  SELECT actor.actor_name,
         SUM(yc_rev.cnt) + SUM(yc_arc.cnt) AS sum_yc,
         SUM(tc_rev.cnt) + SUM(tc_arc.cnt) AS sum_tc
  FROM actor
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision WHERE rev_timestamp < START_DATE GROUP BY rev_actor) yc_rev
  ON yc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive WHERE ar_timestamp < START_DATE GROUP BY ar_actor) yc_arc
  ON yc_arc.ar_actor = actor.actor_id
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision AND rev_timestamp > END_DATE GROUP BY rev_actor) tc_rev
  ON tc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive AND rev_timestamp > END_DATE GROUP BY ar_actor) tc_arc
  ON tc_arc.ar_actor = actor.actor_id
  WHERE actor_name not IN (SELECT REPLACE(pl_title, '_', ' ') FROM pagelinks WHERE  pl_from = 7519882)
  GROUP BY actor.actor_name
) sub
WHERE sum_yc < NUMBER_COUNT AND sum_tc >= NUMBER_COUNT
""",
        "template_stub": "{{وسام تعديلات|NUMBER|-- SIGNATURE}}"
    },
    {
        "number": 10000,
        "query" : """
SELECT actor_name, sum_yc, sum_tc
FROM (
  SELECT actor.actor_name,
         SUM(yc_rev.cnt) + SUM(yc_arc.cnt) AS sum_yc,
         SUM(tc_rev.cnt) + SUM(tc_arc.cnt) AS sum_tc
  FROM actor
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision WHERE rev_timestamp < START_DATE GROUP BY rev_actor) yc_rev
  ON yc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive WHERE ar_timestamp < START_DATE GROUP BY ar_actor) yc_arc
  ON yc_arc.ar_actor = actor.actor_id
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision AND rev_timestamp > END_DATE GROUP BY rev_actor) tc_rev
  ON tc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive AND rev_timestamp > END_DATE GROUP BY ar_actor) tc_arc
  ON tc_arc.ar_actor = actor.actor_id
  WHERE actor_name not IN (SELECT REPLACE(pl_title, '_', ' ') FROM pagelinks WHERE  pl_from = 7519882)
  GROUP BY actor.actor_name
) sub
WHERE sum_yc < NUMBER_COUNT AND sum_tc >= NUMBER_COUNT
""",
        "template_stub": "{{وسام تعديلات|NUMBER|-- SIGNATURE}}"
    },
    {
        "number": 20000,
        "query" : """
SELECT actor_name, sum_yc, sum_tc
FROM (
  SELECT actor.actor_name,
         SUM(yc_rev.cnt) + SUM(yc_arc.cnt) AS sum_yc,
         SUM(tc_rev.cnt) + SUM(tc_arc.cnt) AS sum_tc
  FROM actor
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision WHERE rev_timestamp < START_DATE GROUP BY rev_actor) yc_rev
  ON yc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive WHERE ar_timestamp < START_DATE GROUP BY ar_actor) yc_arc
  ON yc_arc.ar_actor = actor.actor_id
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision AND rev_timestamp > END_DATE GROUP BY rev_actor) tc_rev
  ON tc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive AND rev_timestamp > END_DATE GROUP BY ar_actor) tc_arc
  ON tc_arc.ar_actor = actor.actor_id
  WHERE actor_name not IN (SELECT REPLACE(pl_title, '_', ' ') FROM pagelinks WHERE  pl_from = 7519882)
  GROUP BY actor.actor_name
) sub
WHERE sum_yc < NUMBER_COUNT AND sum_tc >= NUMBER_COUNT
""",
        "template_stub": "{{وسام تعديلات|NUMBER|-- SIGNATURE}}"
    },
    {
        "number": 30000,
        "query" : """
SELECT actor_name, sum_yc, sum_tc
FROM (
  SELECT actor.actor_name,
         SUM(yc_rev.cnt) + SUM(yc_arc.cnt) AS sum_yc,
         SUM(tc_rev.cnt) + SUM(tc_arc.cnt) AS sum_tc
  FROM actor
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision WHERE rev_timestamp < START_DATE GROUP BY rev_actor) yc_rev
  ON yc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive WHERE ar_timestamp < START_DATE GROUP BY ar_actor) yc_arc
  ON yc_arc.ar_actor = actor.actor_id
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision AND rev_timestamp > END_DATE GROUP BY rev_actor) tc_rev
  ON tc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive AND rev_timestamp > END_DATE GROUP BY ar_actor) tc_arc
  ON tc_arc.ar_actor = actor.actor_id
  WHERE actor_name not IN (SELECT REPLACE(pl_title, '_', ' ') FROM pagelinks WHERE  pl_from = 7519882)
  GROUP BY actor.actor_name
) sub
WHERE sum_yc < NUMBER_COUNT AND sum_tc >= NUMBER_COUNT
""",
        "template_stub": "{{وسام تعديلات|NUMBER|-- SIGNATURE}}"
    },
    {
        "number": 40000,
        "query" : """
SELECT actor_name, sum_yc, sum_tc
FROM (
  SELECT actor.actor_name,
         SUM(yc_rev.cnt) + SUM(yc_arc.cnt) AS sum_yc,
         SUM(tc_rev.cnt) + SUM(tc_arc.cnt) AS sum_tc
  FROM actor
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision WHERE rev_timestamp < START_DATE GROUP BY rev_actor) yc_rev
  ON yc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive WHERE ar_timestamp < START_DATE GROUP BY ar_actor) yc_arc
  ON yc_arc.ar_actor = actor.actor_id
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision AND rev_timestamp > END_DATE GROUP BY rev_actor) tc_rev
  ON tc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive AND rev_timestamp > END_DATE GROUP BY ar_actor) tc_arc
  ON tc_arc.ar_actor = actor.actor_id
  WHERE actor_name not IN (SELECT REPLACE(pl_title, '_', ' ') FROM pagelinks WHERE  pl_from = 7519882)
  GROUP BY actor.actor_name
) sub
WHERE sum_yc < NUMBER_COUNT AND sum_tc >= NUMBER_COUNT
""",
        "template_stub": "{{وسام تعديلات|NUMBER|-- SIGNATURE}}"
    },
    {
        "number": 50000,
        "query" : """
SELECT actor_name, sum_yc, sum_tc
FROM (
  SELECT actor.actor_name,
         SUM(yc_rev.cnt) + SUM(yc_arc.cnt) AS sum_yc,
         SUM(tc_rev.cnt) + SUM(tc_arc.cnt) AS sum_tc
  FROM actor
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision WHERE rev_timestamp < START_DATE GROUP BY rev_actor) yc_rev
  ON yc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive WHERE ar_timestamp < START_DATE GROUP BY ar_actor) yc_arc
  ON yc_arc.ar_actor = actor.actor_id
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision AND rev_timestamp > END_DATE GROUP BY rev_actor) tc_rev
  ON tc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive AND rev_timestamp > END_DATE GROUP BY ar_actor) tc_arc
  ON tc_arc.ar_actor = actor.actor_id
  WHERE actor_name not IN (SELECT REPLACE(pl_title, '_', ' ') FROM pagelinks WHERE  pl_from = 7519882)
  GROUP BY actor.actor_name
) sub
WHERE sum_yc < NUMBER_COUNT AND sum_tc >= NUMBER_COUNT
""",
        "template_stub": "{{وسام تعديلات|NUMBER|-- SIGNATURE}}"
    },
    {
        "number": 60000,
        "query" : """
SELECT actor_name, sum_yc, sum_tc
FROM (
  SELECT actor.actor_name,
         SUM(yc_rev.cnt) + SUM(yc_arc.cnt) AS sum_yc,
         SUM(tc_rev.cnt) + SUM(tc_arc.cnt) AS sum_tc
  FROM actor
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision WHERE rev_timestamp < START_DATE GROUP BY rev_actor) yc_rev
  ON yc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive WHERE ar_timestamp < START_DATE GROUP BY ar_actor) yc_arc
  ON yc_arc.ar_actor = actor.actor_id
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision AND rev_timestamp > END_DATE GROUP BY rev_actor) tc_rev
  ON tc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive AND rev_timestamp > END_DATE GROUP BY ar_actor) tc_arc
  ON tc_arc.ar_actor = actor.actor_id
  WHERE actor_name not IN (SELECT REPLACE(pl_title, '_', ' ') FROM pagelinks WHERE  pl_from = 7519882)
  GROUP BY actor.actor_name
) sub
WHERE sum_yc < NUMBER_COUNT AND sum_tc >= NUMBER_COUNT
""",
        "template_stub": "{{وسام تعديلات|NUMBER|-- SIGNATURE}}"
    },
    {
        "number": 70000,
        "query" : """
SELECT actor_name, sum_yc, sum_tc
FROM (
  SELECT actor.actor_name,
         SUM(yc_rev.cnt) + SUM(yc_arc.cnt) AS sum_yc,
         SUM(tc_rev.cnt) + SUM(tc_arc.cnt) AS sum_tc
  FROM actor
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision WHERE rev_timestamp < START_DATE GROUP BY rev_actor) yc_rev
  ON yc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive WHERE ar_timestamp < START_DATE GROUP BY ar_actor) yc_arc
  ON yc_arc.ar_actor = actor.actor_id
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision AND rev_timestamp > END_DATE GROUP BY rev_actor) tc_rev
  ON tc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive AND rev_timestamp > END_DATE GROUP BY ar_actor) tc_arc
  ON tc_arc.ar_actor = actor.actor_id
  WHERE actor_name not IN (SELECT REPLACE(pl_title, '_', ' ') FROM pagelinks WHERE  pl_from = 7519882)
  GROUP BY actor.actor_name
) sub
WHERE sum_yc < NUMBER_COUNT AND sum_tc >= NUMBER_COUNT
""",
        "template_stub": "{{وسام تعديلات|NUMBER|-- SIGNATURE}}"
    },
    {
        "number": 80000,
        "query" : """
SELECT actor_name, sum_yc, sum_tc
FROM (
  SELECT actor.actor_name,
         SUM(yc_rev.cnt) + SUM(yc_arc.cnt) AS sum_yc,
         SUM(tc_rev.cnt) + SUM(tc_arc.cnt) AS sum_tc
  FROM actor
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision WHERE rev_timestamp < START_DATE GROUP BY rev_actor) yc_rev
  ON yc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive WHERE ar_timestamp < START_DATE GROUP BY ar_actor) yc_arc
  ON yc_arc.ar_actor = actor.actor_id
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision AND rev_timestamp > END_DATE GROUP BY rev_actor) tc_rev
  ON tc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive AND rev_timestamp > END_DATE GROUP BY ar_actor) tc_arc
  ON tc_arc.ar_actor = actor.actor_id
  WHERE actor_name not IN (SELECT REPLACE(pl_title, '_', ' ') FROM pagelinks WHERE  pl_from = 7519882)
  GROUP BY actor.actor_name
) sub
WHERE sum_yc < NUMBER_COUNT AND sum_tc >= NUMBER_COUNT
""",
        "template_stub": "{{وسام تعديلات|NUMBER|-- SIGNATURE}}"
    },
    {
        "number": 90000,
        "query" : """
SELECT actor_name, sum_yc, sum_tc
FROM (
  SELECT actor.actor_name,
         SUM(yc_rev.cnt) + SUM(yc_arc.cnt) AS sum_yc,
         SUM(tc_rev.cnt) + SUM(tc_arc.cnt) AS sum_tc
  FROM actor
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision WHERE rev_timestamp < START_DATE GROUP BY rev_actor) yc_rev
  ON yc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive WHERE ar_timestamp < START_DATE GROUP BY ar_actor) yc_arc
  ON yc_arc.ar_actor = actor.actor_id
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision AND rev_timestamp > END_DATE GROUP BY rev_actor) tc_rev
  ON tc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive AND rev_timestamp > END_DATE GROUP BY ar_actor) tc_arc
  ON tc_arc.ar_actor = actor.actor_id
  WHERE actor_name not IN (SELECT REPLACE(pl_title, '_', ' ') FROM pagelinks WHERE  pl_from = 7519882)
  GROUP BY actor.actor_name
) sub
WHERE sum_yc < NUMBER_COUNT AND sum_tc >= NUMBER_COUNT
""",
        "template_stub": "{{وسام تعديلات|NUMBER|-- SIGNATURE}}"
    },
    {
        "number": 100000,
        "query" : """
SELECT actor_name, sum_yc, sum_tc
FROM (
  SELECT actor.actor_name,
         SUM(yc_rev.cnt) + SUM(yc_arc.cnt) AS sum_yc,
         SUM(tc_rev.cnt) + SUM(tc_arc.cnt) AS sum_tc
  FROM actor
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision WHERE rev_timestamp < START_DATE GROUP BY rev_actor) yc_rev
  ON yc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive WHERE ar_timestamp < START_DATE GROUP BY ar_actor) yc_arc
  ON yc_arc.ar_actor = actor.actor_id
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision AND rev_timestamp > END_DATE GROUP BY rev_actor) tc_rev
  ON tc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive AND rev_timestamp > END_DATE GROUP BY ar_actor) tc_arc
  ON tc_arc.ar_actor = actor.actor_id
  WHERE actor_name not IN (SELECT REPLACE(pl_title, '_', ' ') FROM pagelinks WHERE  pl_from = 7519882)
  GROUP BY actor.actor_name
) sub
WHERE sum_yc < NUMBER_COUNT AND sum_tc >= NUMBER_COUNT
""",
        "template_stub": "{{وسام تعديلات|NUMBER|-- SIGNATURE}}"
    },
    {
        "number": 125000,
        "query" : """
SELECT actor_name, sum_yc, sum_tc
FROM (
  SELECT actor.actor_name,
         SUM(yc_rev.cnt) + SUM(yc_arc.cnt) AS sum_yc,
         SUM(tc_rev.cnt) + SUM(tc_arc.cnt) AS sum_tc
  FROM actor
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision WHERE rev_timestamp < START_DATE GROUP BY rev_actor) yc_rev
  ON yc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive WHERE ar_timestamp < START_DATE GROUP BY ar_actor) yc_arc
  ON yc_arc.ar_actor = actor.actor_id
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision AND rev_timestamp > END_DATE GROUP BY rev_actor) tc_rev
  ON tc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive AND rev_timestamp > END_DATE GROUP BY ar_actor) tc_arc
  ON tc_arc.ar_actor = actor.actor_id
  WHERE actor_name not IN (SELECT REPLACE(pl_title, '_', ' ') FROM pagelinks WHERE  pl_from = 7519882)
  GROUP BY actor.actor_name
) sub
WHERE sum_yc < NUMBER_COUNT AND sum_tc >= NUMBER_COUNT
""",
        "template_stub": "{{وسام تعديلات|NUMBER|-- SIGNATURE}}"
    },
    {
        "number": 150000,
        "query" : """
SELECT actor_name, sum_yc, sum_tc
FROM (
  SELECT actor.actor_name,
         SUM(yc_rev.cnt) + SUM(yc_arc.cnt) AS sum_yc,
         SUM(tc_rev.cnt) + SUM(tc_arc.cnt) AS sum_tc
  FROM actor
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision WHERE rev_timestamp < START_DATE GROUP BY rev_actor) yc_rev
  ON yc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive WHERE ar_timestamp < START_DATE GROUP BY ar_actor) yc_arc
  ON yc_arc.ar_actor = actor.actor_id
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision AND rev_timestamp > END_DATE GROUP BY rev_actor) tc_rev
  ON tc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive AND rev_timestamp > END_DATE GROUP BY ar_actor) tc_arc
  ON tc_arc.ar_actor = actor.actor_id
  WHERE actor_name not IN (SELECT REPLACE(pl_title, '_', ' ') FROM pagelinks WHERE  pl_from = 7519882)
  GROUP BY actor.actor_name
) sub
WHERE sum_yc < NUMBER_COUNT AND sum_tc >= NUMBER_COUNT
""",
        "template_stub": "{{وسام تعديلات|NUMBER|-- SIGNATURE}}"
    },
    {
        "number": 175000,
        "query" : """
SELECT actor_name, sum_yc, sum_tc
FROM (
  SELECT actor.actor_name,
         SUM(yc_rev.cnt) + SUM(yc_arc.cnt) AS sum_yc,
         SUM(tc_rev.cnt) + SUM(tc_arc.cnt) AS sum_tc
  FROM actor
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision WHERE rev_timestamp < START_DATE GROUP BY rev_actor) yc_rev
  ON yc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive WHERE ar_timestamp < START_DATE GROUP BY ar_actor) yc_arc
  ON yc_arc.ar_actor = actor.actor_id
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision AND rev_timestamp > END_DATE GROUP BY rev_actor) tc_rev
  ON tc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive AND rev_timestamp > END_DATE GROUP BY ar_actor) tc_arc
  ON tc_arc.ar_actor = actor.actor_id
  WHERE actor_name not IN (SELECT REPLACE(pl_title, '_', ' ') FROM pagelinks WHERE  pl_from = 7519882)
  GROUP BY actor.actor_name
) sub
WHERE sum_yc < NUMBER_COUNT AND sum_tc >= NUMBER_COUNT
""",
        "template_stub": "{{وسام تعديلات|NUMBER|-- SIGNATURE}}"
    },
    {
        "number": 200000,
        "query" : """
SELECT actor_name, sum_yc, sum_tc
FROM (
  SELECT actor.actor_name,
         SUM(yc_rev.cnt) + SUM(yc_arc.cnt) AS sum_yc,
         SUM(tc_rev.cnt) + SUM(tc_arc.cnt) AS sum_tc
  FROM actor
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision WHERE rev_timestamp < START_DATE GROUP BY rev_actor) yc_rev
  ON yc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive WHERE ar_timestamp < START_DATE GROUP BY ar_actor) yc_arc
  ON yc_arc.ar_actor = actor.actor_id
  JOIN (SELECT rev_actor, COUNT(rev_id) AS cnt FROM revision AND rev_timestamp > END_DATE GROUP BY rev_actor) tc_rev
  ON tc_rev.rev_actor = actor.actor_id
  JOIN (SELECT ar_actor, COUNT(ar_id) AS cnt FROM archive AND rev_timestamp > END_DATE GROUP BY ar_actor) tc_arc
  ON tc_arc.ar_actor = actor.actor_id
  WHERE actor_name not IN (SELECT REPLACE(pl_title, '_', ' ') FROM pagelinks WHERE  pl_from = 7519882)
  GROUP BY actor.actor_name
) sub
WHERE sum_yc < NUMBER_COUNT AND sum_tc >= NUMBER_COUNT
""",
        "template_stub": "{{وسام تعديلات|NUMBER|-- SIGNATURE}}"
    },
]
