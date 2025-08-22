from selenium import webdriver

class infow():
    def __init__(self):
        self.driver = webdriver.Chrome(https://www.google.com/search?q=chrome&rlz=1C1ONGR_enIN1079IN1079&oq=chrome&gs_lcrp=EgZjaHJvbWUyDAgAEEUYORixAxiABDIKCAEQABixAxiABDIKCAIQABixAxiABDINCAMQABiDARixAxiABDIGCAQQBRhAMgYIBRAFGEAyBggGEAUYQDIGCAcQBRhA0gEIMjc0M2owajeoAgiwAgE&sourceid=chrome&ie=UTF-8)
        
    def get_info(self, query):
        self.query = query
        self.driver.get(url= "https://www.wikipedia.org")
        
        
        
assist = infow()
assist.get_info("hello")            