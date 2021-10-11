import unittest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from Pages.PageContacter import page_contacter
from Pages.utilities import utilities


class formulaire_contact(unittest.TestCase):

    @classmethod
    @allure.severity(allure.severity_level.CRITICAL)
    def setUp(cls): # Ouvrir navigateur
        with allure.step("ouvrir le navigator"):
            chrome_options = webdriver.ChromeOptions()
            chrome_options.headless = True
            chrome_options.add_argument("--headless")
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument("--window-size=1366x768")
            #cls.driver = webdriver.Chrome(chrome_options=chrome_options)
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
            browser = cls.driver
            browser = utilities(browser)
            browser.connection()

        allure.attach(cls.driver.get_screenshot_as_png(), name="accès site kouka",
                        attachment_type=AttachmentType.PNG)

    @allure.severity(allure.severity_level.BLOCKER)
    def test_1_verifier_accès_page_contact(self): # acceder a la page nous contacter
        with allure.step("ouvrir la page contact"):
            search = self.driver
            search = page_contacter(search)
            search.contact()

        allure.attach(self.driver.get_screenshot_as_png(), name="accès page contact",
                        attachment_type=AttachmentType.PNG)

    allure.severity(allure.severity_level.NORMAL)
    def test_2_remplir_formulaire_contact(self): # remplir formulaire avec les valleur correcte
        with allure.step("ouvrir la page contact"):
            search = self.driver
            search = page_contacter(search)
            search.contact()
        with allure.step("remplir le formulaire"):
            search.field_nom()
            search.field_email()
            search.field_phone()
            search.field_entreprise()
            search.field_message()
        with allure.step("envoyer le formulaire"):
            search.btn_envoyer()
            self.expected_text = "Nous avons bien reçu votre message, notre équipe vous contactera sous peu."
            self.assertEqual(self.expected_text, "Nous avons bien reçu votre message, notre équipe vous contactera sous peu.")

        allure.attach(self.driver.get_screenshot_as_png(), name="formulaire contact",
                      attachment_type=AttachmentType.PNG)

    allure.severity(allure.severity_level.BLOCKER)
    def test_3_envoyer_formulaire_vide(self):  # remplir formulaire avec les valleur correcte
        with allure.step("ouvrir la page contact"):
            search = self.driver
            search = page_contacter(search)
            search.contact()
        with allure.step("envoyer le formulaire"):
            search.btn_envoyer()
            self.expected_text = "Nous avons bien reçu votre message, notre équipe vous contactera sous peu."
            self.assertEqual(self.expected_text, "Veuillez renseigner tous les champs obligatoires et réessayer.")

        allure.attach(self.driver.get_screenshot_as_png(), name="formulaire vide",
                      attachment_type=AttachmentType.PNG)


    @classmethod
    def tearDown(cls):  # Fermer le navigateur
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')