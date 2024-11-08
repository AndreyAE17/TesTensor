from page.main_page import ContactsPage

link = "https://sbis.ru/"

def test_photos_chronologies_identical_height_width(browser):
    page = ContactsPage(browser, link)
    page.open()
    page.header_contacts().click()
    page.icon_header_contacts_more_offices().click()    
    page.banner().click()
    browser.switch_to.window(browser.window_handles[1])
    assert browser.current_url == "https://tensor.ru/"
    page.more_details_strength_people().click()
    assert browser.current_url == "https://tensor.ru/about"
    size_photosc = page.photo_chronology()
    for x in size_photosc:
        assert x.size['height'] == size_photosc[0].size['height'] or x.size['width'] == size_photosc[0].size['width']

def test_region(browser):
    page = ContactsPage(browser, link)
    page.open()
    page.header_contacts().click()
    page.icon_header_contacts_more_offices().click()    
    assert page.region().text == "Ярославская обл."
    page.region_list("Ярославль")
    page.region().click()
    page.change_region("Камчатский край").click()
    page.close_change_region_time("Камчатский край", 10)
    assert page.region().text == "Камчатский край"
    page.region_list("Петропавловск-Камчатский")



