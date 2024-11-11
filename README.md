# Django_Auction_Sc
Этот проект представляет из себя сайт на основе Django.
На главной странице проекта выводятся актуальные лоты для покупки, если такое есть на рынке.

Красный цвет лота - нет выгодных лотов. 

Оранжевый цвет лота - цена ниже средней цены по рынку на 23% - 39%

Зелёный цвет лота - цена ниже средней цены по рынку на price > 40%

# Настройка скрипта
Приложение auction -> scripts -> Api.py:

Изначально высчетанная средняя цена уменьшается на 10%
average_price = int(sum(price_one_item) / len(price_one_item)) * 0.90 

Это сделано в целях исключения влияния сверх-дорогих предложений на рынке.

# Метод get_item_price класса ApiClient
Переменные для изменения процента выгодности лота

DISCOUNT_YELLOW = 0.77  # Ниже средней цены на 23%

DISCOUNT_GREEN = 0.60  # Ниже средней цены на 40%

## Getting started
[DATABASE: Postgresql, Reddis, ENV: Poetry]

1. Download [Docker]([https://eapi.stalcraft.net](https://www.docker.com)).

2. DATABASES = {
    'HOST': 'db', # Для запуска докера необходимо указать db.
}
Остальные поля заполняются данными вашей БД.

3. Добавь свой токен [API STALCRAFT](https://eapi.stalcraft.net) в переменную API_KEY в главном приложении django в файле settgins.py


4. В docker-compose.yml так же необходимо заполнить данные своей БД. 
