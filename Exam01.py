# Importe le module time nécessaire pour les opérations de pause
import time
# Importe les modules nécessaires de selenium pour automatiser le navigateur
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
# Importe le module nécessaire pour gérer les pilotes du navigateur Chrome
from webdriver_manager.chrome import ChromeDriverManager

# Initialise une instance du navigateur Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# Accède à la page web spécifiée
driver.get("https://videotron.com/")
# Maximise la fenêtre du navigateur pour s'assurer que tous les éléments sont bien chargés
driver.maximize_window()
# Fait une pause de 5 secondes pour s'assurer que la page web est complètement chargée
time.sleep(5)

#2- Trouver le nombre d’images sur le site et l’afficher dans la console de votre éditeur de code.
images= driver.find_elements(By.XPATH, "//img")
# afficher le nombre total des images:
nbr_images=len(images)
print("Le nombre d’images sur le site : ",nbr_images )

#3- Afficher la valeur de l’attribut « alt » des images du site dans la console.

print("Voici la valeur de l'attribut «alt» de chaque image:")
i=1
for image in images:
    print("Image" ,i, ":", image.get_attribute('alt'))
    i = i + 1
#4- Trouver le nombre de liens sur le site et l’afficher dans la console.
liens = driver.find_elements(By.TAG_NAME, 'a')
nbr_liens=len(liens)
print("Le nombre des liens : ",nbr_liens )
#5- Trouver le nombre de liens dans la section « footer » du site et l’afficher dans la console.
footer=driver.find_element(By.XPATH,"//footer[@class='videotron-ui__main-footer']")
# Trouvez tous les éléments 'a' (liens) à l'intérieur du footer
liens_footer= footer.find_elements(By.TAG_NAME,"a")
nbr_liens_footer=len(liens_footer)
print("Le nombre des liens dans le footer : ",nbr_liens_footer )
#6- Récupérer la valeur de l’attribut « href » de chaque lien dans la section « footer » du site et l’afficher dans la console.
print("Voici la valeur de l'attribut «href» de chaque lien:")
i = 1
for lien in liens_footer:
    print("Lien", i, ":", lien.get_attribute('href'))
    i= i+1