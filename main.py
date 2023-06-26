from utils import load_data, if_executed, sender_format, date_format, receiver_format

FILENAME = 'operations.json'

data = load_data(FILENAME)

last_executed_operations = if_executed(data, 5)

sorted_operations = sorted(last_executed_operations, key=lambda x: x.get('date'), reverse=True)

for operation in sorted_operations:
    date = date_format(operation.get('date'))
    description = operation.get('description')
    sender = sender_format(operation.get('from', 'Empty account'))
    receiver = receiver_format(operation.get('to', 'Empty account'))
    amount = operation.get('operationAmount')['amount']
    currency_name = operation.get('operationAmount')['currency']['name']
    print(f"{date} {description}\n"
          f"{sender} -> {receiver}\n"
          f"{amount} {currency_name}\n")
