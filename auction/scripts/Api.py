from StalcraftAuction.settings import API_KEY
import aiohttp


#Интеграция API-STALCRAFT
class ApiClient:

    def __init__(self, item):
        self.item = item
        self.token = API_KEY
        self._url = f'https://eapi.stalcraft.net/ru/auction/{self.item}/lots'
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }

    async def _relevant_lots(self) -> list[dict]:
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(self._url, headers=self.headers) as response:
                    response_data = await response.json()
                    return response_data.get('lots')
                
            except:
                return []

    async def _relevant_price(self) -> list[str]:
        data = await self._relevant_lots()
        if data:
            list_prices = [f"{lot['amount']}:{lot['buyoutPrice']}" for lot in data]  # ["1:15000", "2:25000", ...]
            return list_prices
        else:
            return []

    async def get_item_price(self) -> dict[str, str]:
        DISCOUNT_YELLOW = 0.77  # Ниже средней цены на 23%
        DISCOUNT_GREEN = 0.60  # Ниже средней цены на 40%
        try:
            list_amount_price = await self._relevant_price()
            if list_amount_price:
                price_one_item = sorted([int(price.split(':')[1]) / int(price.split(':')[0]) for price in list_amount_price])
                average_price = int(sum(price_one_item) / len(price_one_item)) * 0.90
                
                for item in list_amount_price:
                    quantity, price = item.split(':')
                    unit_price = int(price) / int(quantity)

                    if unit_price < (average_price * DISCOUNT_YELLOW):
                        return {'lot':f'Ниже средней цены... \n ЛОТ: Количество:{quantity}, \n Цена:{price} ', 'color': 'yellow'}
                    elif unit_price < (average_price * DISCOUNT_GREEN):
                        return {'lot':f'Ниже средней цены на 40%+ \n ЛОТ: Количество:{quantity}, \n Цена:{price} ', 'color': 'yellow'}

                    return {'lot': f'Поиск лота... \n Средняя цена:{int(average_price)}', "color": 'red'}
            else:
                return {'lot': 'Лоты отсутствуют...', "color": 'black'}
        except:
            return {'lot': 'Ошибка подключения! \n что то пошло не так...', "color": 'blue'}
