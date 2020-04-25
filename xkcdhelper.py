import logging
import requests
import bs4

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()


def start(update, context):
    logger.info("User {} started bot".format(update.effective_user["id"]))
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


xkcd_url = 'https://c.xkcd.com/random/comic/'


def getxkcd(update, context):
    res = requests.get(xkcd_url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem = soup.select('#comic img')
    comicUrl = 'https:' + comicElem[0].get('src')
    logger.info("User " + str(update.effective_user["id"]) + " obtained photo " + comicUrl)
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=comicUrl)


