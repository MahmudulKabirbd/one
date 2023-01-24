mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here
exchange_rate = mobile_data.get('exchange_rate', 1)
for item in mobile_data['data']:
    name = item['name']
    made = item['made']
    price = float(item['price'].split(" ")[0])
    bdt_price = price * exchange_rate
    print(f"Here is the new {name} which is made in {made}. The price of this awesome phone is {price} USD which is almost equal to {bdt_price} BDT")