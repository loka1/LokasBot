import re

import pywikibot


class HasCategories:
    def __init__(self, page, text, summary):
        self.page = page
        self.text = text
        self.summary = summary

    def __call__(self):
        if "(توضيح)" in self.page.title():
            return self.text, self.summary
        """
            true mean has category -> remove
            false mean not have category -> add
        :return:
        """
        if not self.check():
            self.add_template()
        else:
            self.remove_template()
        return self.text, self.summary

    def add_template(self):
        """
        This method adds the {{بذرة غير مصنفة}} template to the page if it doesn't already exist.
        """
        template = re.compile(r"{{بذرة غير مصنفة(?:\|[^}]+)?}}")
        if not template.search(self.text):
            text = self.text
            text += "\n"
            text += "{{بذرة غير مصنفة|تاريخ ={{نسخ:شهر وسنة}}}}"

            self.text = text
            self.summary += "، أضاف  وسم [[:تصنيف:مقالات غير مصنفة|غير مصنفة]]"

    def remove_template(self):
        """
           This method removes the {{بذرة غير مصنفة}} template from the page if it exists.
           """
        template = re.compile(r"{{بذرة غير مصنفة(?:\|[^}]+)?}}")
        new_text = template.sub("", self.text)
        if new_text != self.text:
            self.text = new_text
            self.summary += "، حذف  وسم [[:تصنيف:مقالات غير مصنفة|غير مصنفة]]"

    def check(self):
        categories = self.page.categories()
        has_category = False
        for category in categories:
            tem = pywikibot.Category(self.page.site, category.title())
            if not tem.isHiddenCategory():
                has_category = True
                break
        return has_category
