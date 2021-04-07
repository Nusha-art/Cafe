from django.db import models
from pages.models import menu

ADRESS = (
    ('не выбрано','не выбрано'),
    ('Россия, Москва, улица Арбат,1','Кафе "Анютина лавка" Главный офис Россия, Москва, улица Арбат,1'),
    ('Шараповский пр., вл, Мытищи Торговый Центр "Красный Кит"','Кафе "Анютина лавка" Шараповский пр., вл, Мытищи Торговый Центр "Красный Кит"'),
    ('1, район Новокуркино, 8-й микрорайон, Химки ТРЦ МЕГА', 'Кафе "Анютина лавка" 1, район Новокуркино, 8-й микрорайон, Химки ТРЦ МЕГА'),

)
class Order(models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    email = models.EmailField()
    phone = models.CharField( max_length=15)
    adress = models.CharField(max_length=200,choices=ADRESS, default="не выбрано")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    for_payment = models.CharField(max_length=50)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(menu, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
