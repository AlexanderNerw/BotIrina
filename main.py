# - *- coding: utf- 8 - *-

from aiogram import Bot, Dispatcher, executor, types
from random import randint 

bot = Bot(token='5596728441:AAFtwdOdxyOzNjHLbD3q13QBw9z50Q5KuaA')
dp = Dispatcher(bot)

prosto = ['Я понял, что в жизни мне не хватает двух вещей — кофе и тебя.',
'Ты так красиво улыбнулась, что я забыл, куда шел.',
'Никогда не улыбайся! Вдруг кто-то еще влюбится в твою улыбку.',
'Кто-то должен позвонить в полицию. Ты украла мое сердце.',
'Классно выглядишь! Мне кажется, ты очень позитивный человек. Я тоже. У нас много общего',
'У тебя такой очаровательный и волшебный взгляд, что невозможно пройти мимо.',
'Когда увидел тебя, то очень обрадовался, что не женат и у меня нет девушки.',
'Интересно, какого дракона надо убить, чтобы добиться сердца такой принцессы, как ты?',
'По шкале от 1 до 10 ты выглядишь на 20.',
'Ты лучшее, что я видел до сих пор.',
'Твоя красота обезоруживает.',
'Твои глаза! Хочу в них утонуть… Когда ты смотришь на меня, я забываю, что умею плавать.',
'Не знаю, что красивее сегодня — вода, небо или твои глаза.',
'Хочу признаться, лишь тебе: ты самая-самая лучшая на этой Земле!',
'Столько лет все мучаются вопросом, в чем смысл жизни, и никто до сих пор не нашел ответа. А я все знаю: для меня и ответ, и смысл жизни — это ты, моя любимая!',
'Только с тобой я чувствую себя самым счастливым, ты вдохновляешь меня!',
'Ты та, для кого бьется мое сердце!',
'Моя любовь к тебе космическая, без конца и края!',
'Ты больше, чем мечта!',
'Когда в небе гроза и капает дождь я вспоминаю тебя. и сразу же в моем сердце летают бабочки, светит солнце.',
'Я схожу с ума от твоей красоты! Твои губы, глаза… смотрел бы на них вечно!',
'И кто же сказал, что Ангелы есть только на небе?! Это не правда, ведь я вижу Ангела на земле!',
'Каждая девушка хочет услышать в свой адрес комплимент, но заслужить их по праву можешь только ты!',
'Мне кажется, что ты способна на многое, даже спасти мир своей красотой!',
'Наверное, твои подруги тебе всегда завидуют?! А по-другому невозможно, ведь ты лучшая по всем параметрам!',
'Жизнь без тебя не жизнь , это выживание',
'Ты видишь в небе солнце? Так знай, твоя улыбка светит гораздо ярче!',
'Красивая фигура, очаровательный взгляд, блестящий ум, солнечная улыбка – и это всё ты!',
'Хочу чтобы ты знала, твоя красота показалась мне самым главным украшением этого мира!',
'Ты похожа на жемчужину, которая на дне моря и мне не доступна…',
'Быть может, я не слишком красноречив, но я скажу одно и самое главное – ты прекрасна!',
'Быть с тобой рядом хотя бы минуту, это дороже вечности без тебя!',
'ВЫГЛЯДИШЬ КАК ВСЕГДА НЕОТРАЗИМО — ТЫ ЗВЕЗДА!',
'Твои глаза это лазурное море, и главное что сейчас хочется, это разучиться плавать!',
'Знаешь,я сам по себе атеист,но при виде тебя начинаю верить в Афродиту',
'Сказать что ты просто красивая, это не сказать ничего… Ты просто совершенство!',
'Ты луч солнца в пасмурный день!',
'Самая лучшая!!! Божественна, неотразимая, модная, веселая,самая лучшая !!!',
'Даже если мне закроют глаза, я найду тебя среди миллионов женщин, потому что ты особенная!',
'Бесконечно можно смотреть на три вещи:как горит огонь,как течёт вода,и на тебя..',
'Ты стройная, красивая, умная, нежная, блистательная, яркая.',
'Если в мире и есть идеальная девушка, так это только ты!',
'Ты знала, что, когда улыбаешься, то у тебя на щеках появляются ямочки? Они такие милые.',
'Улыбайся, пожалуйста, почаще. У тебя сразу начинают глаза блестеть, и ты выглядишь потрясающе.',
'У тебя такая красивая талия. Мне очень нравится твоя женственность.',
'Потрясающая фигура! Тебя легко принять за фитнес-тренера или спортсменку.',
'Ты настолько изумительна, что мне хочется стать художником и запечатлеть все твои линии, ямочки, тени на холсте.',
'Ты очень красива без макияжа, а твоя естественная красота видна сразу. Это большая редкость.',
'Прости, засмотрелся на тебя и потерял мысль.',
'Как, по-твоему, я должен держать себя в руках, если ты так сногсшибательно выглядишь?',
'Я не умею делать сальто, а вот мое сердце научилось, когда увидело тебя.',
'Ну ты хотя бы огнетушитель с собой носила, раз так выглядишь.',
'Говорят, нужно брать от жизни только самое лучшее. Так что я тебя забираю.',
'Ты вот просто улыбнулась, а у меня капитуляция мозга произошла.',
'Я, конечно, не Ричард Гир, но ты та еще красотка.',
'Это не ты играла главную роль в «Чудо-женщине»? Странно, а фильм явно о тебе.',
'Твои глаза и улыбка просто обворожительны.',
'В твоих глазах кусочек неба.',
'У тебя удивительная улыбка — ты уходишь, а она остается.',
'Ты самая обаятельная и привлекательная девушка.',
'Ты — неповторима! Ты — неотразима! Ты — непревзойденная!',
'Твоя лучезарная улыбка восхищает даже небо!',
'Сногсшибательно выглядишь! Ты когда по улице будешь идти, постарайся не наступать на упавших в обморок мужиков.',
'Ты до невозможности красива и очаровательна, обаятельна и привлекательна!',
'Ты особенная и необыкновенная. Я никогда не встречал девушек, хоть немного похожих на тебя.',
'Я бы присвоил тебе титул «Самой красивой девушки мира».',
'Ты самая пиздатая блять',
'Ты выглядишь как супер-модель перед важной фотосессией!',
'Блеск! Потрясающе! Превосходно выглядишь!',
'Ты меня улыбаешь!',
'Твоей фигуре могут позавидовать даже супермодели.',
'Ты – самый яркий пример того, что красота – это могущественная сила.',
'Твой стиль в одежде очень элегантный и продуманный. Ты действительно умеешь подчеркнуть свою красоту и индивидуальность.',
'Ты – одна из самых интересных людей в моем окружении, с тобой время летит незаметно.',
'Ты талантлива во всем, чем занимаешься.',
'Любая девушка может взять с тебя пример.',
'Ты словно Google или Яндекс. В тебе есть все, что я искал.',
'Твои родители, наверное, кулинары, раз у них вышла такая великолепная крошка.',
'Как тебе удается с каждым разом выглядеть все лучше и лучше?',
'Мое утро начинается не с кофе, а мысли о тебе.',
'В средние века тебя бы сожгли на костре, из-за волшебной красоты.',
'Все, что мне нужно для счастья – это ты.',
'Ты внутри еще красивее, чем снаружи',
'Мне нравится твой стиль',
'Ты как солнце в дождливый день',
'Ничего в себе не меняй. Ты великолепна',
'Ты всегда будешь поводом моей улыбки',
'Ты обаятельная, очаровательная и привлекательная',
'Ты доставляешь больше удовольствие, чем лопать пленку с пупырышками',
'Если бы ты жила на Кавказе, тебя бы уже украли давным-давно',
'Ты нравишься даже перфекционистам',
'Любая одежда идеально сидит на тебе. Я ей даже завидую.',
'Ты лучшая староста.',
'Ты – уникальная! В тебя нельзя не влюбиться.',
'Всякий раз, когда мне грустно, мысль о тебе сразу поднимает настроение.']

@dp.message_handler(commands=['start'])
async def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Коплимент 😏"]
    keyboard.add(*buttons)
    await message.answer("Это бот для комплиментов на, понял на?", reply_markup = keyboard )


@dp.message_handler(commands=['compliment'])
async def compliment(message):
    rand = randint(0, 94)
    await message.answer(prosto[rand])

@dp.message_handler(content_types=['text'])
async def reaction(message):
    if message.text == "Коплимент 😏":
        rand = randint(0, 94)
        await message.answer(prosto[rand])


if __name__ == '__main__':
    #************************************ ЗАПУСК *************************************
    executor.start_polling(dp, skip_updates=True)