class utilities():

    def __init__(self, browser):
        self.driver = browser

    def connection(self):   # se connecter au site kouka

        base_url = "https://kouka.io/"
        self.driver.get(base_url)
        assert "KOUKA, We are software crafts(wo)men! - Accueil" in self.driver.title