from decimal import Decimal

import factory
import factory.fuzzy
from factory.django import DjangoModelFactory
from orders.models import Order, OrderItem
from pytest_factoryboy import register
from tests.users.factories import UserFactory


@register
class OrderFactory(DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    amount = Decimal("100")

    class Meta:
        model = Order


@register
class OrderItemFactory(DjangoModelFactory):
    order = factory.SubFactory(OrderFactory)
    quantity = factory.Faker("pyint")

    class Meta:
        model = OrderItem
