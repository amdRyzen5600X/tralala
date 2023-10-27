import os

from aiogram import Bot, types
from aiogram.utils.callback_data import CallbackData

choose_cb = CallbackData('vote', 'choose')

bot = Bot(token=os.environ['API_TOKEN'], parse_mode=types.ParseMode.HTML)

WELLCOME_TEXT = '''<b>Привет! Я Лу</b><i>, твой помощник по поступлению в Astana IT University!</i>

Я готова помочь тебе с любыми вопросами, связанными с поступлением: от выбора программы до подачи документов. Astana IT University предоставляет высококачественное образование в области информационных технологий, и я готова помочь тебе стать частью цифровой истории Казахстана со мной. 

просто <b>выбери то что тебе интереснo узнать</b>

По всем вопросам к функционалу и работе бота обращаться к создателю: <a href = 'https://t.me/AMD_RYZEN_5_7600X'>Арнур</a> 
По всем вопросам к информации и её достоверности обращаться к: <a href = 'https://t.me/mxwltg'>Максим</a> '''

HOW_TO_GRADUATE = '''asdfasdfasdfasdfasdf w'''

AET = '''suchka'''

ABITUR = '''abitur'''

GRANTS = '''granty huyanty'''

DOCS = '''idi nahui'''

DISCOUNT = '''skidki huidki'''

EP = '''epepepepepepepepe'''

COLLEDGE = '''ahahahahaha'''

BACHELOR = '''heheheheheheh'''

MASTER = '''hohohohohohoho'''

PHD = '''hphphphphphphphp'''

BACHELOR_ABITUR = '''bachabachabacha'''

MAGA_ABITUR = '''magamamgamamgamgmagmagmagm'''

BACHELOR_GRANTS = '''dfdfdfdfdfdffd'''

MAGA_GRANTS = '''lklklklklklklkl'''

BACHELOR_DISCOUNT = '''disdisdisidisdisdisd'''

MAGA_DISCOUNT = '''magadisdiadiaidaidi'''

BACHELOR_EP = '''bepbepebepbepebpebppepeb'''

MAGA_EP = '''mepempmempempempep'''

