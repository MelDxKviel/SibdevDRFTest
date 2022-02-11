from django.db import models


class Customer(models.Model):
    username = models.CharField(max_length=50, verbose_name='Имя покупателя')
    spent_money = models.IntegerField(default=0, verbose_name='Потраченные деньги')

    class Meta:
        verbose_name = 'Покупатель'
        ordering = ['-spent_money']

    def load_gems_list(self):
        customers = Customer.objects.all().exclude(username=self.username)[:4]
        deals_filter = Deals.objects.filter(customer__in=customers).values_list('item', flat=True)
        gems = set(self.deals.filter(item__in=deals_filter).values_list('item', flat=True))
        return gems

    def __str__(self):
        return self.username


class Deals(models.Model):
    customer = models.ForeignKey(Customer, related_name='deals', on_delete=models.CASCADE, verbose_name='Покупатель')
    item = models.CharField(max_length=25, verbose_name='Товар')
    total = models.IntegerField(default=0, verbose_name='Сумма')
    quantity = models.IntegerField(default=0, verbose_name='Количество')
    date = models.DateTimeField(verbose_name='Дата')

    class Meta:
        verbose_name = 'Сделка'
