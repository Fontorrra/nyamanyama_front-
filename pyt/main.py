import asyncio
from vars import *
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import aiogram




def read_users():
    users = dict()
    with open('./users.txt', 'r') as file:
        for line in file:
            tg_id, vk_id = line.split(',')
            users[int(tg_id)] = int(vk_id)
    return users


def update_users(tg_id, vk_id):
    with open('./users.txt', 'a') as file:
        text = str(tg_id) + ',' + str(vk_id)
        file.write(text + '\n')


def read_groups():
    d = dict()
    with open('./normal_groups.txt', 'r', encoding='utf-8') as file:
        for line in file:
            groups = line.split(',')
            try:
                d[int(groups[0])] = groups[1:]
            except:
                pass
    return d


def update_groups(vk_id, groups):
    with open('./groups.txt', 'a') as file:
        text = str(vk_id) + ','
        text += ','.join(groups)
        file.write(text)


async def get_token():
    global VKs, vk_iter
    LOGIN = VKs[vk_iter][0]
    PASSWORD = VKs[vk_iter][1]
    try:
        temp = get_vk_official_token(LOGIN, PASSWORD)
        user_agent = str(temp['user_agent'])
        token = str(temp['token'])
    except:
        try:
            temp = get_kate_token(LOGIN, PASSWORD)
            user_agent = str(temp['user_agent'])
            token = str(temp['token'])
        except:
            vk_iter += 1

            if vk_iter == len(VKs):
                vk_iter = 0

            LOGIN = VKs[vk_iter][0]
            PASSWORD = VKs[vk_iter][1]

            try:
                temp = get_vk_official_token(LOGIN, PASSWORD)
                user_agent = str(temp['user_agent'])
                token = str(temp['token'])
            except:
                try:
                    temp = get_kate_token(LOGIN, PASSWORD)
                    user_agent = str(temp['user_agent'])
                    token = str(temp['token'])
                except:
                    return False
    return [token, user_agent]


async def get_vk_id(name) -> int:
    global token, user_agent
    if "https" in name:
        name = name[name.rfind('/') + 1:]
    if "@" in name:
        name = name[name.rfind('@') + 1:]

    async with aiohttp.ClientSession() as session:
        try:
            url = f'https://api.vk.com/method/utils.resolveScreenName?screen_name={name}&access_token={token}&v=5.131'
            session.headers.update({'User-Agent': str(user_agent)})
            async with session.get(url) as response:
                js = await response.json()
                user_id = str(js['response']['object_id'])
        except:
            try:
                token, user_agent = await get_token()
                url = f'https://api.vk.com/method/utils.resolveScreenName?screen_name={name}&access_token={token}&v=5.131'
                session.headers.update({'User-Agent': str(user_agent)})
                async with session.get(url) as response:
                    js = await response.json()
                    user_id = str(js['response']['object_id'])
            except:
                return False

    return int(user_id)


async def get_groups(vk_id):
    global token, user_agent
    groups = []
    async with aiohttp.ClientSession() as session:
        try:
            url = f'https://api.vk.com/method/groups.get?user_id={vk_id}&access_token={token}&v=5.131&extended=1&fields=name'
            session.headers.update({'User-Agent': str(user_agent)})
            async with session.get(url) as response:
                js = await response.json()
                js = js['response']['items']
                for i in range(len(js)):
                    groups.append(js[i]['name'])
        except:
            token, user_agent = await get_token()
            url = f'https://api.vk.com/method/groups.get?user_id={vk_id}&access_token={token}&v=5.131&extended=1&fields=name'
            session.headers.update({'User-Agent': str(user_agent)})
            async with session.get(url) as response:
                js = await response.json()
                js = js['response']['items']
                for i in range(len(js)):
                    groups.append(js[i]['name'])

    return groups


def get_soulmates(vk_id):
    global groups
    me = groups[vk_id]
    matches = dict()
    matches_size = dict()
    for key in groups:
        if key != vk_id:
            inter = set(me) & set(groups[key])
            matches[key] = list(inter)
            matches_size[key] = len(inter)
    sorted_matches_size = dict(sorted(matches_size.items(), key=lambda item: item[1], reverse=True))
    return (sorted_matches_size, matches)


async def get_names_by_ids(ids):
    def build_url(ids, token):
        api = 'API.users.get({{\'user_id\':{}}})'.format(ids[0])
        for i in range(1, len(ids)):
            api += ',API.users.get({{\'user_id\':{}}})'.format(ids[i])
        url = f'https://api.vk.com/method/execute?access_token={token}&v=5.131&code=return[{api}];'
        return url

    global token, user_agent
    names = []
    async with aiohttp.ClientSession() as session:
        try:
            url = build_url(ids, token)
            session.headers.update({'User-Agent': str(user_agent)})
            async with session.get(url) as response:
                js = await response.json()
                js = js['response']
                for el in js:
                    name = el[0]['first_name'] + ' ' + el[0]['last_name']
                    names.append(name)
        except:
            token, user_agent = await get_token()
            url = build_url(ids, token)
            session.headers.update({'User-Agent': str(user_agent)})
            async with session.get(url) as response:
                js = await response.json()
                js = js['response']
                for el in js:
                    name = el[0]['first_name'] + ' ' + el[0]['last_name']
                    names.append(name)
    return names


async def get_friends(vk_id):
    def build_url(vk_id, token):
        url = f'https://api.vk.com/method/friends.get?user_id={vk_id}&order=hints&count=25&access_token={token}&v=5.131'
        return url

    global token, user_agent

    friends = []
    async with aiohttp.ClientSession() as session:
        try:
            url = build_url(vk_id, token)
            session.headers.update({'User-Agent': str(user_agent)})
            async with session.get(url) as response:
                js = await response.json()
                js = js['response']['items']
                for i in range(len(js)):
                    friends.append(js[i])
        except:
            token, user_agent = await get_token()
            url = build_url(vk_id, token)
            session.headers.update({'User-Agent': str(user_agent)})
            async with session.get(url) as response:
                js = await response.json()
                js = js['response']['items']
                for i in range(len(js)):
                    friends.append(js[i])
    return friends


async def add_friends(friends):
    def build_url(ids, token):
        api = 'API.users.get({{\'user_id\':{}}})'.format(ids[0])
        for i in range(1, len(ids)):
            api += ',API.users.get({{\'user_id\':{}}})'.format(ids[i])
        url = f'https://api.vk.com/method/execute?access_token={token}&v=5.131&code=return[{api}];'
        return url

    global token, user_agent
    names = []
    async with aiohttp.ClientSession() as session:
        try:
            url = build_url(ids, token)
            session.headers.update({'User-Agent': str(user_agent)})
            async with session.get(url) as response:
                js = await response.json()
                js = js['response']
                for el in js:
                    name = el[0]['first_name'] + ' ' + el[0]['last_name']
                    names.append(name)
        except:
            token, user_agent = await get_token()
            url = build_url(ids, token)
            session.headers.update({'User-Agent': str(user_agent)})
            async with session.get(url) as response:
                js = await response.json()
                js = js['response']
                for el in js:
                    name = el[0]['first_name'] + ' ' + el[0]['last_name']
                    names.append(name)
    return names

async def process_new_user(tg_id, vk_id):
    global users, groups
    users[tg_id] = vk_id
    groups[vk_id] = await get_groups(vk_id)

    friends = await get_friends(vk_id)
    await add_friends(friends)




async def page_show_soulmates(m):
    global matches, vk_id, orders
    if not matches:
        orders, matches = get_soulmates(vk_id)
    ids = []
    length = 0
    for key in orders:
        length += 1
        ids.append(key)
        if length == 10:
            break

    names = await get_names_by_ids(ids)
    markup = InlineKeyboardMarkup()
    for i in range(len(names)):
        markup.add(InlineKeyboardButton(
            names[i],
            callback_data='soulmates ' + str(ids[i])
        ))

    await bot.send_message(m.chat.id, str_your_soulmates, reply_markup=markup)

async def page_show_intersections(m, vk_id: int):
    global matches
    inters = matches[vk_id]
    text = '-----\n\U000026AA '
    text += '\n\U000026AA '.join(inters)
    await m.answer(text, reply_markup=markup_back)

async def main_page():
    pass

bot = Bot(token="6219957896:AAEsE9E32mpLkM2L49ioc5ctEdnnTH5NR70")
dp = Dispatcher(bot)
users = read_users()
groups = read_groups()
previous_page = 'main'
vk_id = None
matches = None
orders = None


pages = {'page_show_intersections': page_show_intersections,
         'page_show_soulmates': page_show_soulmates,
         'main_page': main_page}

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(
        'ok',
        callback_data='welcome ok'
    ))
    await message.answer(str_start, reply_markup=markup)


@dp.message_handler(commands=['dev'])
async def dev(message: types.Message):
    await message.answer(u'\U000026AA')


@dp.callback_query_handler(lambda callback_query: True)
async def query_handler(query):
    global is_wait_for_link, previous_page
    callback = query.data
    if callback == 'welcome ok':
        await bot.send_message(query.message.chat.id, str_get_vk)
        is_wait_for_link = True
    elif callback == 'back':
        await pages[previous_page](query.message)
    elif callback.split()[0] == 'soulmates':
        temp_id = int(callback.split()[1])
        previous_page = 'page_show_soulmates'
        await page_show_intersections(query.message, temp_id)
    await query.answer()


@dp.message_handler(content_types=["text"])
async def text_handler(message):
    global is_wait_for_link, users, groups, vk_id
    text = message.text
    if is_wait_for_link:
        tg_id = message.chat.id
        vk_id = await get_vk_id(text)

        if tg_id not in users:
            await process_new_user(tg_id, vk_id)

        await page_show_soulmates(message)



async def main():
    await dp.start_polling(bot)


# groups = get_groups()
asyncio.run(main())
