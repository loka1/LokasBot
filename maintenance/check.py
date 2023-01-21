# create page onject to remove or add template
 # add remove
 # add add
 # add check
import datetime

import pywikibot
from pywikibot import pagegenerators

from bots.unreviewed_article.core import UnreviewedArticle

import pywikibot

site = pywikibot.Site()

start = pywikibot.Timestamp.fromISOformat('2022-01-10T00:00:00Z')
end = pywikibot.Timestamp.fromISOformat('2023-01-20T00:00:00Z')


# end = pywikibot.Timestamp.now() - datetime.timedelta(minutes=5)


gen = pagegenerators.RecentChangesPageGenerator(site=site, start=start, end=end, namespaces=[0],reverse=True)

# To remove duplicate pages from the generator
gen = set(gen)

# To remove deleted pages from the generator,
gen = filter(lambda page: page.exists(), gen)

for entry in gen:
    page1 = pywikibot.Page(site, entry.title())
    if not page1.isRedirectPage():
        print(entry.title())
        try:
            title = entry.title()
            page = UnreviewedArticle(site)
            page.title = title
            page.load_page()
            if not page.check():
                page.add_template()
            else:
                page.remove_template()
        except Exception as e:
            print(f"An error occurred while processing {entry.title()}: {e}")
