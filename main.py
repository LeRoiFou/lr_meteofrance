from selenium import webdriver

"""Assignation d'un déclenchement du driver"""
driver = webdriver.Chrome(executable_path='chromedriver.exe')

"""Accès au site directement avec Chrome"""
driver.get('https://meteofrance.com/')

"""Accepter le cookies"""
btn_cookies = driver.find_element_by_id('didomi-notice-agree-button')

"""Clic sur le bouton accepter"""
btn_cookies.click()

"""Récupération de la barre de recherche pour saisir la ville"""
search_bar = driver.find_element_by_id('search_form_input')

"""Saisie de la ville dans la barre de recherche"""
search_bar.send_keys('Paris')

"""Récupération du bouton 'rechercher'"""
search_btn = driver.find_element_by_css_selector('#block-mfsearchform > form > button')

"""Clic sur le bouton 'rechercher'"""
search_btn.click()

"""Sélection de la ville affichée par le site"""
search_selection = driver.find_element_by_css_selector('#search_result_poi_682010 > a > p')

"""Clic sur la ville affichée par le site"""
search_selection.click()
