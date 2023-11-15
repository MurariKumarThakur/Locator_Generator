from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re


def remove_special_characters(input_string):
    # Remove all characters that are not alphanumeric or whitespace
    if input_string:
        result_string = re.sub(r'[^a-zA-Z0-9\s]', '', input_string)

        # Replace spaces with underscores
        result_string = result_string.replace(" ", "").lower()
        return result_string

    else:
        print("INPUT_STRING NOT RECEIVED")


def find_links_on_web_page(cls):
    print("FIND ALL LINKS FROM WEB PAGE")
    find_by_element = ""
    element_text = ""

    time.sleep(5)  # Use sleep instead of Thread.sleep

    links = cls.driver.find_elements(By.TAG_NAME, "a")

    if links:
        for link in links:
            link_text = link.text
            href_value = link.get_attribute("href")
            link_text_variable = remove_special_characters(link_text)
            # Locate By linkText
            print("***************************")
            print("// Locate By linkText java supported locator")
            find_by_element = f"@FindBy(linkText=\"{link_text}\")"
            element_text = f"public WebElement {link_text_variable}_linkText"
            print(find_by_element)
            print(element_text)
            print("------------OR------------------")
            print("// Locate By partialLinkText java supported locator")
            find_by_element = f"@FindBy(partialLinkText=\"{link_text}\")"
            element_text = f"public WebElement {link_text_variable}_partialLinkText"
            print(find_by_element)
            print(element_text)

            if href_value:
                print("------------OR------------------")
                print("// Locate By xpath using href attribute java supported locator")
                find_by_element = f"@FindBy(xpath=\"//a[@href='{href_value}']\")"
                element_text = f"public WebElement {link_text_variable}_usingHref_xpath"
                print(find_by_element)
                print(element_text)

    else:
        print("+++++++++++++++++++++++++++")
        print("NO LINKS FOUND ON WEB PAGE")
        print("+++++++++++++++++++++++++++")


def find_button_on_web_page(cls):
    print("FIND ALL BUTTONS FROM WEB PAGE")
    find_by_element = ""
    element_text = ""

    time.sleep(5)  # Use sleep instead of Thread.sleep

    buttons = cls.driver.find_elements(By.TAG_NAME, "button")

    if buttons:
        for button in buttons:
            button_text = button.text
            id_loc = button.get_attribute("id")
            name_loc = button.get_attribute("name")
            class_loc = button.get_attribute('class')
            button_text_variable = ""
            if button_text:
                button_text_variable = remove_special_characters(button_text)
            else:
                button_text_variable = remove_special_characters("no_text_found")

            print("xpath by text")
            if button_text:
                find_by_element = f"@FindBy(xpath=\"//button[text()='{button_text}']\")"
                element_text = f"public WebElement {button_text_variable}_text_xpath"
                print(find_by_element)
                print(element_text)

            if id_loc:
                # Locate By id
                print("***************************")
                print("// Locate By id java supported locator")
                find_by_element = f"@FindBy(id=\"{id_loc}\")"
                element_text = f"public WebElement {button_text_variable}_id"
                print(find_by_element)
                print(element_text)
                print("------------OR------------------")
                print("// Locate By css selector")
                find_by_element = f"@FindBy(css=\"button[id='{id_loc}']\")"
                element_text = f"public WebElement {button_text_variable}_id_css"
                print(find_by_element)
                print(element_text)
                print("------------OR------------------")
                print("// Locate By xpath selector")
                find_by_element = f"@FindBy(xpath=\"//button[@id='{id_loc}']\")"
                element_text = f"public WebElement {button_text_variable}_id_xpath"
                print(find_by_element)
                print(element_text)

            if name_loc:
                # Locate By id
                print("***************************")
                print("// Locate By name")
                find_by_element = f"@FindBy(name=\"{name_loc}\")"
                element_text = f"public WebElement {button_text_variable}_name"
                print(find_by_element)
                print(element_text)
                print("------------OR------------------")
                print("// Locate By css selector")
                find_by_element = f"@FindBy(css=\"button[name='{name_loc}']\")"
                element_text = f"public WebElement {button_text_variable}_name_css"
                print(find_by_element)
                print(element_text)
                print("------------OR------------------")
                print("// Locate By xpath selector")
                find_by_element = f"@FindBy(xpath=\"//button[@name='{name_loc}']\")"
                element_text = f"public WebElement {button_text_variable}_name_xpath"
                print(find_by_element)
                print(element_text)

            if class_loc and button_text:
                # Locate By id
                print("***************************")
                print("// Locate By class")
                find_by_element = f"@FindBy(class=\"{class_loc}\")"
                element_text = f"public WebElement {button_text_variable}_class"
                print(find_by_element)
                print(element_text)
                print("------------OR------------------")
                print("// Locate By css selector")
                find_by_element = f"@FindBy(css=\"button[class='{class_loc}']\")"
                element_text = f"public WebElement {button_text_variable}_class_css"
                print(find_by_element)
                print(element_text)
                print("------------OR------------------")
                print("// Locate By xpath selector")
                find_by_element = f"@FindBy(xpath=\"//button[@class='{class_loc}']\")"
                element_text = f"public WebElement {button_text_variable}_class_xpath"
                print(find_by_element)
                print(element_text)

    else:
        print("+++++++++++++++++++++++++++")
        print("NO BUTTONS FOUND ON WEB PAGE WHERE TAG IS BUTTON")
        print("+++++++++++++++++++++++++++")


class GetTheLocatorFromWebPage:
    driver = None

    @classmethod
    def main(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://sfdev.walkingtree.tech/")

        # Finding Links on Web Page
        find_links_on_web_page(cls)
        find_button_on_web_page(cls)


if __name__ == "__main__":
    GetTheLocatorFromWebPage.main()
