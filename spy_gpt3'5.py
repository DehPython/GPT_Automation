from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from fake_useragent import UserAgent
from selenium.webdriver.support import expected_conditions as EC

prompt = str(input("Digite o prompt: "))

op = webdriver.ChromeOptions()
op.add_argument(f"user-agent={UserAgent.random}")
op.add_argument("user-data-dir=./")
op.add_experimental_option("detach", True)
op.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = uc.Chrome(chrome_options=op)

MAIL = "SEU_EMAIL
PASSWORD = "SUA_SENHA"

driver.get('https://chat.openai.com/auth/login')

sleep(3)

inputElements = driver.find_elements(By.TAG_NAME, "button")
inputElements[0].click()

sleep(2)

mail = driver.find_elements(By.TAG_NAME,"input")[1]
mail.send_keys(MAIL)

btn = driver.find_elements(By.TAG_NAME,"button")[0]
btn.click()

password = driver.find_elements(By.TAG_NAME,"input")[2]
password.send_keys(PASSWORD)

sleep(2)

wait = WebDriverWait(driver, 10)
btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "_button-login-password")))
btn.click()

sleep(6)

# Envia o prompt para o ChatGPT
input_box = driver.find_element(by=By.XPATH, value='//textarea[contains(@placeholder, "Message ChatGPT…")]')
driver.execute_script(f"arguments[0].value = '{prompt}';", input_box)
input_box.send_keys(Keys.RETURN)
input_box.submit()
sleep(15)

# Obter a conversa do ChatGPT
response_elements = driver.find_elements(by=By.CSS_SELECTOR, value='div.text-base')
last_response = response_elements[-1].text

# Opcional: Exibir a última resposta
print(last_response)
