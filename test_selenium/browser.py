from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    def __init__(self):
        # Inicia o browser chrome, mas pode ser feito com outros como Firefox, Safari e IE
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        # Define o tempo máximo para o carregamento da página
        self.browser.set_page_load_timeout(30)
        # Maximiza a janela do browser ao ser iniciado
        self.browser.maximize_window()
        # find element
        self.find = self.browser.find_element
        # find elements
        self.finds = self.browser.find_elements

    def browser_quit(self):
        # Fecha o browser
        self.browser.quit()

    def browser_clear(self):
        # Limpa o browser
        self.browser.delete_all_cookies()
        self.browser.execute_script('window.localStorage.clear()')
        self.browser.execute_script('window.sessionStorage.clear()')
        self.browser.refresh()
