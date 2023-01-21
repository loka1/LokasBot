# create page onject to remove or add template
 # add remove
 # add add
 # add check
import pywikibot

from bots.unreviewed_article.core import UnreviewedArticle

title =  "ابن حجر العسقلاني"
site = pywikibot.Site("ar", "wikipedia")
page = UnreviewedArticle(site)
page.title = title
page.load_page()
if not page.check():
    page.add_template()
else:
    page.remove_template()