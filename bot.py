#импортный телебот
#конфигурация импорта
# случайный импорт
 
#от telebot импортных  типов
 
бот = телебот. TeleBot ( конфиг . TOKEN )
 
@ бот. message_handler ( commands = [ 'начало' ] )
def добро пожаловать ( сообщение ) :
    sti =  open ( 'static / welcome.webp' ,  'rb' )
    бот. send_sticker ( сообщение. чат . id , sti )
 
    # клавиатура
    разметка =  типы . ReplyKeyboardMarkup ( resize_keyboard = True )
    item1 =  типы . KeyboardButton ( "🎲 Рандомное число" )
    item2 =  типы . KeyboardButton ( «😊 Как дела?» )
 
    разметка. добавить ( item1 , item2 )
 
    бот. send_message ( message. chat . id ,  "Добро пожаловать, {0.first_name}! \ n Я - <b> {1.first_name} </b>, бот созданный для того, чтобы быть подопытным кроликом." . format ( message. from_user , бот. get_me ( ) ) ,
        parse_mode = 'html' , reply_markup = разметка )
 
@ бот. message_handler ( content_types = [ 'текст' ] )
def lalala ( сообщение ) :
    если сообщение. чат . type  ==  'private' :
        если сообщение. text  ==  '🎲 Рандомное число' :
            бот. send_message ( сообщение. чат . идентификатор ,  str ( случайный . randint ( 0 , 100 ) ) )
        сообщение elif . text  ==  '😊 Как дела?' :
 
            разметка =  типы . InlineKeyboardMarkup ( row_width = 2 )
            item1 =  типы . InlineKeyboardButton ( "Хорошо" , callback_data = 'хорошо' )
            item2 =  типы . InlineKeyboardButton ( "Не очень" , callback_data = 'плохо' )
 
            разметка. добавить ( item1 , item2 )
 
            бот. send_message ( сообщение. чат . id ,  'Отлично, сам как?' , reply_markup = разметка )
        еще :
            бот. send_message ( сообщение. чат . id ,  'Я не знаю что ответить 😢' )
 
@ бот. callback_query_handler ( func = лямбда- вызов: True )
def callback_inline ( вызов ) :
    попробуйте :
        если звоните. сообщение :
            если звоните. data  ==  'хорошо' :
                бот. send_message ( звонок. сообщение . чат . id ,  'Вот и отличненько 😊' )
            elif call. data  ==  'плохо' :
                бот. send_message ( звонок. сообщение . чат . id ,  'Бывает 😢' )
 
            # удалить встроенные кнопки
            бот. edit_message_text ( chat_id = call. message . chat . id , message_id = call. message . message_id , text = "😊 Как дела?" ,
                reply_markup = Нет )
 
            # показать оповещение
            бот. answer_callback_query ( callback_query_id = call. id , show_alert = False ,
                text = "ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ !! 11" )
 
    кроме  исключения  как e:
        печать ( repr ( e ) )
 
# БЕЖАТЬ
бот. опрос ( none_stop = True )