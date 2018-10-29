from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from pymongo import MongoClient
from time import sleep

client = MongoClient('' , )
db = client['']
db.authenticate('' , '')
data = db['']

options = Options()
options.add_argument("--headless")


driver = webdriver.Firefox(firefox_options=options)
driver.get('https://www.facebook.com/')

email = driver.find_element_by_id('email')
email.send_keys('')

password = driver.find_element_by_id('pass')
password.send_keys('')

login = driver.find_element_by_id('loginbutton')
login.click()

driver.get('')
for article in data.find():
	post = driver.find_element_by_css_selector("div[role='textbox']")
	post.send_keys(article['url'])
	post.send_keys(Keys.ENTER)
	sleep(17)
	post.send_keys(Keys.BACKSPACE)
	sleep(5)
	post.send_keys(Keys.COMMAND, 'a')
	post.send_keys(Keys.BACKSPACE)
	if article['opening_text'] is None:
		post.send_keys(article['title'].strip('\n').strip())
	else:
		post.send_keys(article['opening_text'].strip('\n').strip())
	post.send_keys(Keys.COMMAND, Keys.DOWN)
	post.send_keys(Keys.COMMAND, Keys.RIGHT)
	post.send_keys('" - ' + article['news_source'])
	post.send_keys(Keys.COMMAND, Keys.LEFT)
	post.send_keys(Keys.COMMAND, Keys.UP)
	post.send_keys('"')
	publish = driver.find_element_by_css_selector('button[data-testid="react-composer-post-button"]')
	publish.send_keys(Keys.ENTER)
	sleep(17)
	article['posted'] = True
	fashion_articles.update({'_id':article['_id']}, article)
