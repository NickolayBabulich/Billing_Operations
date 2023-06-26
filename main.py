from utils import load_data, if_executed, sender_format, date_format, receiver_format

FILENAME = 'operations.json'
data = load_data(FILENAME)
last_executed_operations = if_executed(data, 5)

new = sorted(last_executed_operations, key=lambda x: x.get('date'), reverse=True)

for i in new:
    date = date_format(i.get('date'))
    description = i.get('description')
    sender = sender_format(i.get('from', 'Empty account'))
    receiver = receiver_format(i.get('to', 'Empty account'))
    amount = i.get('operationAmount')['amount']
    currency_name = i.get('operationAmount')['currency']['name']
    print(f"{date} {description}\n"
          f"{sender} -> {receiver}\n"
          f"{amount} {currency_name}\n")
