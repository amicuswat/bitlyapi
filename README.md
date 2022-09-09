# Обрезка ссылок с помощью Битли
Программа предназначена для формирования коротких ссылок
из длинных ссылок. Такие ссылки применяются в SMM.
Так же программа позволяет получить статистику кликов
по обрезанной ранее ссылке.

### Как установить
- Скачайте код.
- Установите витруальное окружение командой `python -m venv venv`
- Запустите виртуальное окружение командой `venv\Scripts\activate`
- Установите зависимости командой `pip install -r requirements.txt`
- Запустите программу командой `python main.py`

### Переменные окружения
Часть настроек проекта берётся из переменных окружения. 
Чтобы их определить, создайте файл `.env` рядом с `main.py` 
и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ="значение"`.

Доступна 1 переменная:
`BITLY_TOKEN` - токен для авторизации в сервисе bitly. Зарегистрируйтесь на сайте bitly.com и во вкладке API получите токен.

### Использование скрипта
- Для получение обрезанной ссылки используйте команду
`python main.py https://your_long_link`.
Ожидаемый результат: короткая ссылка bitly будет выведена в консоль.

- Для получение количества кликов по ссылке битли
`python main.py your_bittly_link`. 
Ожидаемый результат: количество кликов будет выведено в консоль.

### Цель проекта
Код написан в образовательных целях, 
на курсе для разработчиков [dvmn.org](https://dvmn.org/referrals/u4guYYiV5HjY6tnwtCShzP2cWFYE0EWnKeoJLEWP/)