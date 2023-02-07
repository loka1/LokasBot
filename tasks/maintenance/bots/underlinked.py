import re

import pywikibot
import re


class WikiLinkExtractor:
    def __init__(self, text):
        self.text = text
        self.links = []

    def extract_links(self):
        pattern = re.compile(r'\{\{.*?\}\}', re.IGNORECASE | re.DOTALL)
        templates = re.findall(pattern, self.text)

        for template in templates:
            self.text = self.text.replace(template, "")

        pattern = re.compile(r'\[\[([^:]*?)\]\]', re.IGNORECASE)

        matches = re.findall(pattern, self.text)
        for match in matches:
            if "تصنيف:" not in match.lower() and "Category:" not in match.lower():
                if "|" in match:
                    link = match.split("|")[0]
                else:
                    link = match
                site = pywikibot.Site()
                page_title = link
                tmp_page = pywikibot.Page(site,page_title)
                if tmp_page.exists() and (not tmp_page.isRedirectPage()) and (tmp_page.namespace() == 0):
                    self.links.append(link)
        return list(set(self.links))


class Underlinked:
    def __init__(self, page, text, summary):
        self.page = page
        self.text = text
        self.summary = summary

    def __call__(self):
        if "(توضيح)" in self.page.title() or "{{توضيح" in self.text:
            return self.text, self.summary

        if self.check():
            self.add_template()
        else:
            self.remove_template()
        return self.text, self.summary

    def add_template(self):
        """
        This method adds the {{وصلات قليلة}} template to the page if it doesn't already exist.
        """
        template = re.compile(r"{{وصلات قليلة(?:\|[^}]+)?}}")
        if not template.search(self.text):
            text = "{{وصلات قليلة|تاريخ ={{نسخ:شهر وسنة}}}}"
            text += "\n"
            text += self.text

            self.text = text
            self.summary += "، أضاف  وسم [[ويكيبيديا:وصلات قليلة|وصلات قليلة]]"

    def remove_template(self):
        """
           This method removes the {{وصلات قليلة}} template from the page if it exists.
           """
        template = re.compile(r"{{وصلات قليلة(?:\|[^}]+)?}}")
        new_text = template.sub("", self.text)
        if new_text != self.text:
            self.text = new_text
            self.summary += "، حذف  وسم [[ويكيبيديا:وصلات قليلة|وصلات قليلة]]"

    def check(self):
        extractor = WikiLinkExtractor(self.text)
        links = extractor.extract_links()
        num_of_links = len(links)
        if 1 <= num_of_links < 4:
            return True
        return False