from selenium import webdriver


class Programme_TV:
    """Accès au site Programme TV"""

    """Assignation d'un déclenchement du driver"""
    driver = webdriver.Chrome(executable_path='chromedriver.exe')

    """Accès au site directement avec Chrome"""
    driver.get('https://www.programme-tv.net/')


class Meteo_france:
    """Accès au site Météo France"""

    """Assignation d'un déclenchement du driver"""
    driver = webdriver.Chrome(executable_path='chromedriver.exe')

    """Accès au site directement avec Chrome"""
    driver.get('https://meteofrance.com/')

    """Accepter le cookies"""
    btn_cookies = driver.find_element_by_id('didomi-notice-agree-button')
    btn_cookies.click()

    """Récupération de la barre de recherche pour saisir la ville"""
    search_bar = driver.find_element_by_id('search_form_input')
    search_bar.send_keys('XXXXX')

    """Récupération du bouton 'rechercher'"""
    search_btn = driver.find_element_by_css_selector('#block-mfsearchform > form > button')
    search_btn.click()

    """Sélection de la ville affichée par le site"""
    search_selection = driver.find_element_by_css_selector('#search_result_poi_XXXXX > a > p')
    search_selection.click()


programme_tv = Programme_TV()
meteo_france = Meteo_france()
