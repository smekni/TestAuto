import json
from jsonpath_ng import parse
from Elements.ElementPageContacter import PageContacterElements

class page_contacter(PageContacterElements):


    def __init__(self, search):
        self.driver = search

#--- methodes de page contacter ---

    def contact(self):
        contacter = self.driver.find_element_by_xpath(self.contacter_xpath)
        contacter.click()

    def field_nom(self):
        #parsing list
        with open("C:\\Users\\Mac\\PycharmProjects\\DemoTest\\Pages\\data.json", 'r') as json_file:
            json_data = json.load(json_file)
        parseName= parse('input[*].nom')
        for match in parseName.find(json_data):
            valueName= match.value

        name = self.driver.find_element_by_id(self.name_id)
        name.clear()
        name.send_keys(valueName)


    def field_email(self):
        # parsing list
        with open("C:\\Users\\Mac\\PycharmProjects\\DemoTest\\Pages\\data.json", 'r') as json_file:
            json_data = json.load(json_file)
        parseEmail = parse('input[*].email')
        for match in parseEmail.find(json_data):
            valueMail = match.value

        email = self.driver.find_element_by_id(self.email_id)
        email.clear()
        email.send_keys(valueMail)

    def field_phone(self):
        # parsing list
        with open("C:\\Users\\Mac\\PycharmProjects\\DemoTest\\Pages\\data.json", 'r') as json_file:
            json_data = json.load(json_file)
        parsePhone = parse('input[*].phone')
        for match in parsePhone.find(json_data):
            valuePhone = match.value

        phone = self.driver.find_element_by_id(self.phone_id)
        phone.clear()
        phone.send_keys(valuePhone)


    def field_entreprise(self):
        # parsing list
        with open("C:\\Users\\Mac\\PycharmProjects\\DemoTest\\Pages\\data.json", 'r') as json_file:
            json_data = json.load(json_file)
        parseEntreprise = parse('input[*].entreprise')
        for match in parseEntreprise.find(json_data):
            valueEntreprise = match.value

        entreprise = self.driver.find_element_by_id(self.entreprise_id)
        entreprise.clear()
        entreprise.send_keys(valueEntreprise)

    def field_message(self):
        # parsing list
        with open("C:\\Users\\Mac\\PycharmProjects\\DemoTest\\Pages\\data.json", 'r') as json_file:
            json_data = json.load(json_file)
        parseMessage = parse('input[*].message')
        for match in parseMessage.find(json_data):
            valueMessage = match.value

        message = self.driver.find_element_by_name(self.message_name)
        message.clear()
        message.send_keys(valueMessage)

    def btn_envoyer(self):
        envoyer = self.driver.find_element_by_id(self.envoyer_id)
        envoyer.click()
