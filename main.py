
from seleniumbase import Driver
import time
from selenium.webdriver.common.by import By

user_data_dir = 'C:/Users/felic/AppData/Local/Google/Chrome/User Data/Profile 1'
#user_data_dir='C:/Users/felic/AppData/Local/Google/Chrome/User Data/Profile'

def if_error (driver, text):
    print ()
    print(text)
    driver.refresh()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)
    return driver
    
def login(user_data_dir):
    driver = Driver(uc=True, user_data_dir=user_data_dir) #mode inconnu + données de Chrome sont deja installées en local
    driver.get("https://www.vinted.fr/member/items/favourite_list")
    time.sleep(6)
    driver.set_window_size(1080,800)

    y = 0
    running = True  # Drapeau pour contrôler l'exécution des boucles
    while running:
        try:
            # Recherche de tous les boutons avec l'attribut aria-label="Remove from favourites"
            buttons = driver.find_elements("xpath", "//span[@data-icon-name='heart-filled']") 
            if not buttons:
                driver = if_error(driver, 'Bouton non visible, refresh de la page')
            # Sinon, il clique
            print("Clique sur le bouton...", y)
            try:
                buttons[0].click()
                time.sleep(0.2)
                y = y + 1
            except Exception as e:
                driver = if_error(driver, 'Bouton non visible, refresh de la page')

        except Exception as e:
            driver = if_error(driver, 'erreur chargement')


    # Ferme le navigateur à la fin
    driver.quit()

if __name__ == '__main__':
    print('Lancement')
    login(user_data_dir=user_data_dir)