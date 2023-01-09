"""
This code is using the SubPage and MainPage classes from the module module to generate and save Wikipedia pages based on data from the list_page_sub_pages variable in the data module.

The list_page_sub_pages variable contains a list of dictionaries, each of which has data that is used to populate a Wikipedia page. For each dictionary in the list, the code creates an instance of the SubPage class and calls the save_page method to generate and save the page.

After all of the sub pages have been generated and saved, the code creates instances of the MainPage class and calls the read_file and save_page methods to generate and save the main page and archive page.

The read_file method reads the contents of a text file and sets the text attribute of the MainPage instance to the contents of the file. The save_page method connects to the Wikipedia site, gets a Page object for the page specified in the title_of_page attribute, sets the text of the page to the contents of the text attribute, and saves the page with the summary specified in the summary attribute.
"""
from module import SubPage,MainPage
from data import list_page_sub_pages

# Iterate through each page data in list_page_sub_pages
for page_data in list_page_sub_pages:
    # Create a SubPage object with the page data
    obj = SubPage(input_dict=page_data)
    # Save the page
    obj.save_page()

# Create a MainPage object for the main page
main_page = MainPage(
    title_of_page="DOMAIN_NAMEمستخدمو الأسبوع الأكثر نشاطا",
    summary="update",
    stub="stub/main_page.txt",
)
# Read the file for the main page
main_page.read_file()
# Save the main page
main_page.save_page()

# Create a MainPage object for the archive page
archive_page = MainPage(
    title_of_page="DOMAIN_NAMEمستخدمو الأسبوع الأكثر نشاطا/الأسبوع الWEEK_NUMBER YEAR_NUMBER",
    summary="update",
    stub="stub/archive.txt",
)
# Read the file for the archive page
archive_page.read_file()
# Save the archive page
archive_page.save_page()