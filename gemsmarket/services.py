import csv
import io
import datetime

from django.utils.timezone import make_aware

from .models import Customer, Deals


def import_deals(file):
    decoded_file = file.read().decode('utf-8')
    io_string = io.StringIO(decoded_file)
    reader = csv.DictReader(io_string)
    template = ['customer', 'item', 'total', 'quantity', 'date']
    if reader.fieldnames != template:
        return {'Status': 'Error',
                'Desc': 'Invalid column format (must be "customer", "item", "total", "quantity", "date")'}

    Customer.objects.all().delete()

    customers = dict()
    for row in reader:
        if row['customer'] not in customers:
            customers.update({f"{row['customer']}": 0})
        customers[row['customer']] += int(row['total'])

    customers_objects = dict()
    for row in customers:
        customer = Customer(username=row, spent_money=customers[row])
        customer.save(force_insert=True)
        customers_objects.update({f"{row}": customer})

    deals_io_string = io.StringIO(decoded_file)
    deals_reader = csv.DictReader(deals_io_string)
    for row in deals_reader:
        deal = Deals(
            customer=customers_objects[row['customer']],
            item=row['item'],
            total=int(row['total']),
            quantity=int(row['quantity']),
            date=make_aware(datetime.datetime.strptime(row['date'], '%Y-%m-%d %H:%M:%S.%f'))
        )
        deal.save(force_insert=True)

    return {'Status': 'OK'}
