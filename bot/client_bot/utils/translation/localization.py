# Модуль для работы с переводами
class Localization:
    translations = {
        'none': {
            "welcome": "Assalomu alaykum! Xush kelibsiz. Iltimos, tilni tanlang. 🇺🇿\n\nЗдравствуйте! Добро пожаловать. Пожалуйста, выберите язык. 🇷🇺",
            "error": "Nimadir notog'ri ketdi. 🇺🇿\n\nЧто-то пошло не так. 🇷🇺"
        },
        'uz': {
            "greeting_registered": """
Botdan foydalanish uchun quidagi tugmalardan foydalaning:

Profil - profilingiz xaqida malumot
Yordam - administrator bilan bog'lanish
            """,
            "greeting_not_registered": """
Xayrli kun aziz foydalanuvchi! 

Biz sizga uyingizdan chiqmasdan maishiy chiqindilardan xalos bo'lishga yordam beradigan ECO AXL xizmatini taklif etamiz!

Biz xonadonlar va xususiy uylardan maishiy chiqindilarni olib chiqamiz.

Har qanday obuna uchun siz og'irligi 7 kg gacha bo'lgan 5 tadan ko'p bo'lmagan sumka olishingiz mumkin


Bizning xizmatimiz quyidagi toifadagi odamlar uchun javob beradi: 

Ish va band odamlar uchun.  🧑‍💻🧑‍🔧

Geymerlar va uydagilar uchun foydali.🎮

Biz tug'ruq ta'tilidagi onalarga yordam beramiz.👩‍👧‍👦

Katta yoshdagilarga obuna bo'ling🧑‍  👨‍  

Kasal bo'lib ko'chaga chiqmaydiganlar uchun😷

Harakati cheklangan odamlar uchun zarur👨‍  
            """,
            "confirmation": """
<b>Telegram boti uchun foydalanuvchi shartnomasi</b>

Eʼtibor bering, quyidagi foydalanuvchi shartnomasi xizmat koʻrsatish sohasida tijorat bilan shugʻullanuvchi Telegram botidan foydalanishning umumiy shartlari va shartlarini tashkil qiladi. Ushbu shartlar bot egasi va uning foydalanuvchilari o'rtasidagi munosabatlarni tavsiflaydi. Iltimos, botni ishlatishdan oldin ularni diqqat bilan o'qing.

<b>1. Xizmatlar</b>ni taqdim etish
         1.1. Bot egasi Telegram boti orqali xizmatlarni taklif qiladi va ularni botda taqdim etilgan xizmatlar tavsifiga muvofiq taqdim etish majburiyatini oladi.
         1.2. Bot egasi istalgan vaqtda foydalanuvchini oldindan ogohlantirmasdan istalgan xizmatlarni o'zgartirish, yangilash yoki to'xtatish huquqini o'zida saqlab qoladi.

<b>2. Mas'uliyatni cheklash</b>
         2.1. Botning egasi bot tomonidan taqdim etilgan xizmatlardan foydalanish natijasida foydalanuvchilarning bevosita yoki bilvosita zararlari uchun javobgar emas.
         2.2. Bot egasi botdan noto'g'ri foydalanish yoki taqdim etilgan ma'lumotlarni noto'g'ri talqin qilish natijasida yuzaga keladigan muammolar uchun javobgar emas.
         2.3. Bot egasi Telegram platformasi yoki boshqa botlar yoki uchinchi tomon xizmatlari bilan o‘zaro aloqalar bilan bog‘liq muammolar uchun javobgar emas.

<b>3. Maxfiylik</b>
         3.1. Bot egasi foydalanuvchilarning shaxsiy ma'lumotlarini amaldagi ma'lumotlarni himoya qilish qonunlariga muvofiq qayta ishlash majburiyatini oladi.
         3.2. Bot egasi, qonun hujjatlarida nazarda tutilgan hollar bundan mustasno, foydalanuvchilarning shaxsiy ma'lumotlarini ularning oldindan roziligisiz uchinchi shaxslarga o'tkazmaydi.

<b>4. Intellektual mulk</b>
         4.1. Bot bilan bog'liq barcha intellektual mulk huquqlari (jumladan, mualliflik huquqlari va savdo belgilari bilan cheklanmagan holda) bot egasiga tegishli.
         4.2. Foydalanuvchilar bot egasining yozma roziligisiz bot tarkibidan foydalanishi, nusxalashi, o‘zgartirishi yoki tarqatishi mumkin emas.

         <b>5. Suiiste'mol qilishni taqiqlash</b>
         5.1. Foydalanuvchilarga botdan noqonuniy, zararli yoki haqoratomuz kontentni tarqatish uchun foydalanishi taqiqlanadi.
         5.2. Foydalanuvchilarga botdan firibgarlik, spam yoki bot egasiga yoki boshqa foydalanuvchilarga zarar yetkazishi mumkin bo‘lgan boshqa harakatlar uchun foydalanishi taqiqlanadi.

<b>6. Foydalanuvchi shartnomasini o'zgartirish</b>
         6.1. Bot egasi istalgan vaqtda ushbu foydalanuvchi shartnomasi shartlarini o'zgartirish huquqini o'zida saqlab qoladi.
         6.2. O'zgartirilgan foydalanuvchi shartnomasi botda e'lon qilinadi yoki foydalanuvchilarga bildirishnoma sifatida taqdim etiladi. Foydalanuvchilar vaqti-vaqti bilan foydalanuvchi shartnomasidagi o'zgarishlarni tekshirish majburiyatini oladilar.

<b>7. Foydalanishni tugatish</b>
         7.1. Foydalanuvchilar istalgan vaqtda botdan foydalanishni to‘xtatishi mumkin.
         7.2. Agar foydalanuvchi ushbu foydalanuvchi shartnomasi shartlarini buzsa yoki foydalanuvchining harakatlari qonun yoki axloqiy va axloqiy me'yorlarga mos kelmasa, bot egasi foydalanuvchilarga xizmatlar ko'rsatishni to'xtatish huquqini o'zida saqlab qoladi.

<b>8. Amaldagi qonunchilik va nizolarni hal qilish</b>
         8.1. Ushbu foydalanuvchi shartnomasi bot egasi ro'yxatdan o'tgan mamlakat qonunlariga muvofiq tartibga solinadi va talqin qilinadi.
         8.2. Bot egasi va foydalanuvchilar o'rtasida yuzaga keladigan har qanday nizolar muzokaralar va hamkorlik orqali hal qilinadi. Agar kelishuvga erishishning iloji bo'lmasa, nizolar vakolatli sudga yuboriladi.

         Shuni yodda tutingki, ushbu foydalanuvchi shartnomasi faqat botdan foydalanishning umumiy qoidalari va shartlaridir. Bot egasi, shuningdek, bot ichida yoki uning veb-saytida mavjud bo'lishi mumkin bo'lgan qo'shimcha siyosat va shartlarga ega bo'lishi mumkin.
            """,
            "get_name": "Keling, ro'yxatdan o'tish jarayonini boshlaylik. Toʻliq ismingizni quyidagi formatda kiriting:\n\nFamiliya Ism otasining ismi\n\nBoʻsh joy bilan ajratilgan!",
            "get_contact": "Kontaktni yuboring.",
            "error_name_format": "Siz noto'g'ri formatda kiritdingiz❗️\n\nTo'liq ismingizni quidagi formatda kiriting:\n\nFamiliya Ism Ota ismi\n\nBo'sh joy bilan ajratilgan!",
            "get_location": """
Joylashuvni yuboring 

Muhim eslatma: Uy manzilingizni ko'rsatishingiz kerak, chunki bu manzilni aniqlash uchun muhim.
            """,
            "get_address": """
manzilingizni quyidagi formatda kiriting:

Uy/kvartira/kirish/qavat

Misol: 30/16/2/1
            """,
            "get_comment_to_address": "Manzilga sharhlar:",
            "error_address_format": """
Sizning formatingiz noto'g'ri❗️

manzilingizni quyidagi formatda kiriting:

Uy/kvartira/kirish/qavat

Misol: 30/16/2/1
            """,
            "complete_registration": "Roʻyxatdan oʻtganingiz uchun tashakkur!",
            "error": "Nimadir xato ketdi❗️",
            "register_btn": "Ro'yhatdan o'tish",
            "help_btn": "Yordam",
            "get_location_btn": "Joylashuvni yuborish",
            "get_place": "Hududni tanlang:",
            "get_rate": """
Juft va toq sanalarda maishiy chiqindilarni olib tashlash uchun boshlang'ich tarif mavjud.  

Tarif nomi "Start". 

To'lov formati Click yoki Payme. 

Xizmat narxi 200 000 ming so'm (bu oyiga 12 ta emissiyani o'z ichiga oladi)

To'lovni tasdiqlash uchun siz ilovada to'lov bildirishnomalarini olasiz.
            """,
            "already_registered": "Siz allaqachon ro'yxatdan o'tgansiz!",
            "profile_error": "siz hali ro'yxatdan o'tmagansiz",
            "profile_btn": "Profil",
            "create_order_btn": "Buyurtma yaratish",
            "actual_order_btn": "Joriy buyurtma",
            "name_btn": "Ism",
            "house_number_btn": "Uy raqami",
            "apartment_number_btn": "Kvartira raqami",
            "entrance_number_btn": "Kirish raqami",
            "floor_number_btn": "Qavat",
            "comment_btn": "Manzilga sharhlar",
            "change_profile": "O'zgartirmoqchi bo'lgan maydonni tanlang:",
            "change_name_message": "Yangi nom kiriting:",
            "change_house_message": "Uy raqamini kiriting:",
            "change_apartment_message": "Kvartira raqamini kiriting:",
            "change_entrance_message": "Kirish raqamini kiriting:",
            "change_floor_message": "Qavat raqamini kiriting:",
            "change_comment_message": "Manzil uchun sharhlarni kiriting:",
            "error_changing": "Tugmani bosing",
            "complete_changing": "Maʼlumotlar muvaffaqiyatli oʻzgartirildi!",
            "confirm_btn": "Tasdiqlash✅",
            "cancel_btn": "Rad etish❌",
            "delete_btn": "Akkaunt o'chirish❌",
            "edit_btn": "Profilni tahrirlash",
            "back_btn": "◀️Orqaga",
            "help_message": "Administrator bilan bog'lanish",
            "rate_count_error": "Buyurtmalaringiz tugadi, qolgan buyurtmalar soni 0 ta",
            "order_success": "Buyurtma yaratildi - sizning buyurtmalaringiz balansi:",
            "photo_load_error": "Surat yuklashda xatolik yuz berdi!",
            "name": "Ism:",
            "phone_number": "Kontakt:",
            "house_number": "Uy:",
            "apartment_number": "Kvartira",
            "entrance_number": "Kirish:",
            "floor": "Qavat:",
            "comment_to_address": "Izoh:",
            "active": "Faol🟢",
            "not_active": "Faol emas🔴",
            "status": "Holat:",
            "deleted_success": "Akkaunt muvaffaqiyatli o'chirildi!",
            "accept_photo": "Kuryer buyurtmangizni qabul qilishi uchun eshigingiz yaqinidagi paketlarning fotosuratini yuboring.",
            "not_ended_order_error": "Sizda tugallanmagan buyurtma bor, bizning kurerimiz buyurtmangizni tez orada tugatadi. Agar muammolar mavjud bo'lsa, 'Yordam' tugmasini bosing",
            "not_order_error": "Sizda hali hech qanday buyurtma yo'q, Buyurtma yaratish tugmasini bosing",
            "worker_status": "Kuryer holati:",
            "order_created_time": "Yaratilish vaqti:",
            "order_end": "Tugallandi🟢",
            "order_not_end": "Tugallanmagan🔴",
            "order_status": "Holat:",
            "default_message": "To'liq ma'lumot olish uchun buyruqni kiriting / help",
            "get_contact_btn": "Raqamni yuborish",
            "change_language_btn": "Tilni o'zgartirish",
            "change_language": "Tilni tanlang",
            "change_language_success": "Til muvaffaqiyatli o'zgartirildi✅",
            "back_message": """
Botdan foydalanish uchun quidagi tugmalardan foydalaning:

Profil - profilingiz xaqida malumot
Yordam - administrator bilan bog'lanish
            """,
            "active_customer": "Profilingiz muvofaqiyatli aktivlashtirildi, botni ishlatishingiz mumkin!",
            "activation_error": "Profilni aktivlashtirish jarayonida xatolik boldi",
            "not_registered_customer": "Siz ro'yhatga olinmagansiz iltimos administrator bilan bog'laning",
            "additions_message": "Qo'shimcha ma'lumot qo'shish uchun quyida tanlang.",
            "success_photo": "Rasim joylandi",
            "order_count": "Chiqarishlar soni:",
            "account_activation": "Akkauntni faolashtirish",
            "register_type": "Ro'yhatdan o'tish usulini tanlang",
            "buy_rate": "Tariflar"
        },


        'ru': {
            "greeting_registered": """
Добро пожаловать!

Для начала использования бота или его перезапуска используйте команду:

/start

Навигация по боту:

📋 Профиль - Полная информация о вашем аккаунте.

❓ Помощь - Связаться с администратором.

Приятного использования! 😊
                    """,
            "greeting_not_registered": """
Добрый день, дорогой пользователь! 🌟

Мы рады представить вам сервис ECO AXL, который поможет вам избавиться от бытового мусора, не выходя из дома!

🗑️ Что мы предлагаем:

    Вынос бытового мусора из квартир и частных домов.
    По любой подписке доступен вынос до 5 мешков весом до 7 кг.

📦 Наш сервис подходит для:

    Деловых и занятых людей 🧑‍💻🧑‍🔧
    Геймеров и домоседов 🎮
    Мам в декрете 👩‍👧‍👦
    Пожилых людей 🧑‍🦳👨‍🦳 (оформите подписку для своих близких)
    Тех, кто болеет и не выходит на улицу 😷
    Маломобильных граждан 👨‍🦽

Мы здесь, чтобы облегчить вашу жизнь. 🌿
                    """,
            "confirmation": """
<b>Пользовательское соглашение для Telegram бота</b>

Пожалуйста, обратите внимание, что следующее пользовательское соглашение представляет собой общие правила и условия использования Telegram бота, занимающегося коммерцией в сфере услуг. Эти условия описывают взаимоотношения между владельцем бота и его пользователями. Пожалуйста, внимательно прочитайте их перед использованием бота.

<b>1. Предоставление услуг</b>
        1.1. Владелец бота предлагает услуги через Telegram бота и обязуется предоставлять их в соответствии с описанием услуг, предоставленным в боте.
        1.2. Владелец бота оставляет за собой право изменять, обновлять или прекращать предоставление любых услуг в любое время без предварительного уведомления пользователя.

<b>2. Ограничение ответственности</b>
        2.1. Владелец бота не несет ответственности за любые прямые или косвенные убытки, понесенные пользователями в результате использования услуг, предоставляемых ботом.
        2.2. Владелец бота не несет ответственности за проблемы, возникающие из-за неправильного использования бота или неправильной интерпретации предоставленной информации.
        2.3. Владелец бота не несет ответственности за любые проблемы, связанные с Telegram платформой или взаимодействием с другими ботами или сторонними сервисами.

<b>3. Конфиденциальность</b>
        3.1. Владелец бота обязуется обрабатывать персональные данные пользователей в соответствии с применимым законодательством о защите данных.
        3.2. Владелец бота не будет передавать персональные данные пользователей третьим лицам без их предварительного согласия, за исключением случаев, предусмотренных законодательством.

<b>4. Интеллектуальная собственность</b>
        4.1. Все права на интеллектуальную собственность, связанную с ботом (включая, но не ограничиваясь, авторскими правами и товарными знаками), принадлежат владельцу бота.
        4.2. Пользователи не имеют права использовать, копировать, изменять или распространять содержимое бота без предварительного письменного согласия владельца бота.

        <b>5. Запрет на злоупотребление</b>
        5.1. Пользователям запрещено использовать бота для распространения незаконного, вредоносного или оскорбительного содержимого.
        5.2. Пользователям запрещено использовать бота для осуществления мошенничества, спама или любых других действий, которые могут повредить владельцу бота или другим пользователям.

<b>6. Изменение пользовательского соглашения</b>
        6.1. Владелец бота оставляет за собой право в любое время изменять условия данного пользовательского соглашения.
        6.2. Измененное пользовательское соглашение будет опубликовано в боте или предоставлено пользователямв виде уведомления. Пользователи обязуются периодически проверять пользовательское соглашение на наличие изменений.

<b>7. Прекращение использования</b>
        7.1. Пользователи могут прекратить использование бота в любое время.
        7.2. Владелец бота оставляет за собой право прекратить предоставление услуг пользователям в случае нарушения пользователем условий данного пользовательского соглашения или в случае несоответствия действиям пользователя законодательству или морально-этическим нормам.

<b>8. Применимое право и разрешение споров</b>
        8.1. Данное пользовательское соглашение регулируется и толкуется в соответствии с законодательством страны, в которой зарегистрирован владелец бота.
        8.2. Любые споры, возникающие между владельцем бота и пользователями, будут разрешаться путем переговоров и сотрудничества. В случае невозможности достижения согласия, споры будут переданы на рассмотрение компетентного суда.

        Пожалуйста, имейте в виду, что данное пользовательское соглашение является лишь общими правилами и условиями использования бота. Владелец бота может также иметь дополнительные политики и условия, которые могут быть доступны в боте или на его веб-сайте.
        """,
            "get_name": """
Давайте начнем процесс регистрации. 📝

Пожалуйста, введите ваше Ф.И.О. в формате:

Фамилия Имя Отчество

⚠️ Важно: Введите данные через пробел!
""",
            "get_contact": "📲 Пожалуйста, отправьте ваш контакт, используя кнопку ниже.",
            "error_name_format": """
❗️ У вас неправильный формат! ❗️

Пожалуйста, введите ваше Ф.И.О в формате:

Фамилия Имя Отчество

Через пробел!
""",
            "get_location": """
📍 Отправьте локацию

⚠️ Важное примечание: Пожалуйста, отправляйте ваш домашний адрес, так как это важно для определения точного местоположения.
                           """,
            "get_address": """
🏡 Введите ваш адрес в формате:

Дом/Квартира/Подъезд/Этаж

Пример: 30/16/2/1
""",
            "get_comment_to_address": """
📝 Комментарии к адресу:

Пожалуйста, укажите дополнительные детали, которые помогут нам найти вас быстрее и точнее. Например, ориентиры, особые инструкции по входу в здание или любые другие примечания, которые могут быть полезны курьеру.
""",
            "error_address_format": """
❗️ У вас неправильный формат!

Введите ваш адрес в формате:

Дом/Квартира/Подъезд/Этаж

📍 Пример: 30/16/2/1
    """,
            "complete_registration": """
🎉 Спасибо за регистрацию!

Мы рады приветствовать вас в сервисе ECO AXL!

Теперь вы можете воспользоваться нашим сервисом по вывозу бытового мусора. Если у вас возникнут вопросы или потребуется помощь, не стесняйтесь обращаться к нам.
""",
            "error": """
⚠️ Что-то пошло не так!

К сожалению, возникла ошибка во время обработки вашего запроса. Пожалуйста, попробуйте еще раз или свяжитесь с нашей службой поддержки для получения помощи.
""",
            "register_btn": "Пройти Регистрацию",
            "help_btn": "Помощь",
            "get_location_btn": "Отправить локацию",
            "get_place": """
🏙️ Выберите район:

Пожалуйста, укажите свой район для более точного обслуживания. Выбор района поможет нам лучше понять ваши потребности и предложить наиболее подходящие услуги.

Нажмите на кнопку ниже, чтобы сделать свой выбор!
""",
            "get_rate": """
💰 Доступный тариф: "Start"

Сейчас доступен тариф "Start" для выноса бытового мусора, который действует как по четным, так и по нечетным числам.

🛠️ Что включает тариф:

    Стоимость услуги: 200,000 сум
    В тариф входит 12 выбросов в месяц!

💳 Форматы оплаты:

    Click
    Payme
""",
            "already_registered": """
🚫 Вы уже зарегистрированы!

Похоже, что ваша регистрация уже была выполнена.

💬 Помощь:

Если у вас возникли вопросы или вам нужна поддержка, нажмите на кнопку Помощь.

🔧 Профиль:

Чтобы изменить информацию о вашем аккаунте, используйте кнопку Профиль.
""",
            "profile_error": """
🚫 Вы еще не зарегистрировались!

Пожалуйста, пройдите процесс регистрации, чтобы получить доступ к всем функциям нашего сервиса.
""",
            "profile_btn": "Профиль",
            "create_order_btn": "Создать заказ",
            "actual_order_btn": "Актуальный заказ",
            "name_btn": "Имя",
            "house_number_btn": "номер дома",
            "apartment_number_btn": "номер квартиры",
            "entrance_number_btn": "номер подьезда",
            "floor_number_btn": "этаж",
            "comment_btn": "комментарии к адресу",
            "change_profile": "🛠️ Выберите поле, которое хотите изменить:",
            "change_name_message": "✏️ Введите ваше новое имя:",
            "change_house_message": "🏠 Введите номер вашего дома:",
            "change_apartment_message": "🏢 Введите номер вашей квартиры:",
            "change_entrance_message": "🚪 Введите номер подъезда:",
            "change_floor_message": "🏢 Введите номер этажа:",
            "change_comment_message": """
📝 Введите комментарии к адресу:

Здесь вы можете оставить дополнительные сведения или указания, которые могут быть полезны для курьера.
""",
            "error_changing": "Нажмите на кнопку",
            "complete_changing": """
✅ Данные успешно изменены!

Ваши изменения были сохранены. Если вам нужно внести дополнительные правки, нажмите на кнопку Профиль
""",
            "confirm_btn": "Потвердить✅",
            "cancel_btn": "Отказать❌",
            "delete_btn": "Удалить аккаунт❌",
            "edit_btn": "Редакторовать профиль",
            "back_btn": "◀️Назад",
            "help_message": """
💬 Связаться с оператором:

Для получения дополнительной информации или помощи, пожалуйста, свяжитесь с нашим оператором: @jacurlive.
""",
            "rate_count_error": """
❗️ Внимание:
У вас исчерпаны все заказы. Осталось 0 заказов.
""",
            "order_success": """
✅ Заказ успешно создан!
Ваш текущий остаток заказов:
""",
            "photo_load_error": """
❌ Ошибка!

Не удалось загрузить фотографию.
""",
            "name": "имя:",
            "phone_number": "номер телефона:",
            "house_number": "номер дома:",
            "apartment_number": "номер квартиры:",
            "entrance_number": "номер подьезда:",
            "floor": "этаж:",
            "comment_to_address": "комментарии к адресу:",
            "active": "Активен🟢",
            "not_active": "Неактивен🔴",
            "status": "Статус:",
            "deleted_success": """
✅ Успех!
Ваш аккаунт был успешно удалён.
""",
            "accept_photo": """
📸 Отправьте фотографию пакетов, расположенных возле вашей двери.
Это поможет курьеру точно идентифицировать ваш заказ.
""",
            "not_ended_order_error": """
⚠️ У вас есть незавершённый заказ!
В ближайшее время наш курьер завершит его. Если у вас возникли вопросы или проблемы, нажмите на кнопку Помощь.
""",
            "not_order_error": """
📭 У вас ещё нет актуальных заказов.
Пожалуйста, нажмите на кнопку Создать заказ, чтобы оформить новый!
""",
            "worker_status": "Статус курьера:",
            "order_created_time": "Время создания:",
            "order_end": "Закончен🟢",
            "order_not_end": "Незакончен🔴",
            "order_status": "Статус:",
            "default_message": "сли у вас возникли вопросы или вам нужна поддержка, нажмите на кнопку Помощь.",
            "get_contact_btn": "Отправить контакт",
            "change_language_btn": "Изменить язык",
            "change_language": """
🌐 Выберите язык:
Пожалуйста, выберите язык, на котором вы хотите продолжить использование сервиса.
""",
            "change_language_success": """
🎉 Язык успешно изменён! ✅
Теперь вы можете продолжать использовать сервис на выбранном языке.
""",
            "back_message": """
Для начала использования бота или его перезапуска используйте команду:

/start

Навигация по боту:

📋 Профиль - Полная информация о вашем аккаунте.

❓ Помощь - Связаться с администратором.

Приятного использования! 😊
            """,
            "active_customer": """
🎉 Ваш профиль успешно активирован!
Теперь вы можете пользоваться ботом без ограничений. Приятного использования!
""",
            "activation_error": """
❗️ Произошла ошибка!
Пожалуйста, попробуйте снова позже. Если проблема не исчезнет, свяжитесь с администратором.
""",
            "not_registered_customer": """
❗️ Вы не зарегистрированы!
Пожалуйста, свяжитесь с администратором для регистрации.
""",
            "additions_message": "📋 Для добавления дополнительных сведений, пожалуйста, выберите ниже:",
            "success_photo": "🖼️ Фотография успешно добавлена!",
            "order_count": "Количество выносов:",
            "account_activation": "Активировать аккаунт",
            "register_type": """
📋 Выберите способ регистрации:

    1. Активировать аккаунт - если вы прошли регистрацию через оператора
    2. Пройти регистрацию - что бы пройти регистрацию в ручную
""",
            "buy_rate": "Тарифы"
        }
    }

    @staticmethod
    def get_translation(language, key):
        return Localization.translations.get(language, {}).get(key, key)


# Функция для отправки локализованных сообщений
async def get_localized_message(language, key):
    translation = Localization.get_translation(language, key)
    return translation
