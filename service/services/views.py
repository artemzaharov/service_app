from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Subscription
from .serializers import SubscriptionsSerializer
from django.db.models import Prefetch
from clients.models import Client


class SubscriptionView(ReadOnlyModelViewSet):
    """Этот класс - это представление Django REST Framework для модели Subscription,
        которое наследуется от класса ReadOnlyModelViewSet.
        Он предоставляет только операции чтения (GET), но не позволяет выполнять изменения данных.

        queryset - это набор данных, который будет использоваться для получения подписок из базы данных.
        В данном случае, используется Subscription.objects.all() - для получения всех записей из таблицы Subscription.
        Кроме того, используется prefetch_related, чтобы заранее загрузить связанные объекты client, 
        т.е. клиента, на которого оформлена подписка, используя метод Prefetch.
        Это может улучшить производительность, т.к. будет выполнено меньше запросов к базе данных.

        Prefetch принимает два аргумента: lookup, который определяет имя связанного поля, 
        которое должно быть заранее загружено, и queryset, который указывает, какие связанные объекты следует выбрать.
        В данном случае, используется Client.objects.all().select_related('user').only('company_name', 'user__email'), 
        чтобы выбрать всех клиентов и связанные с ними объекты User,
        загруженные заранее (select_related), и выбрать только поля 'company_name' и 'user__email'.
        serializer_class - это класс сериализатора, который будет использоваться для преобразования объектов Subscription в формат JSON и наоборот.
        В данном случае, используется SubscriptionsSerializer, который должен быть определен где-то в коде проекта и 
        содержать логику преобразования объектов модели Subscription в JSON и наоборот."""

    queryset = Subscription.objects.all().prefetch_related(
        Prefetch(
            "client",
            queryset=Client.objects.all()
            .select_related("user")
            .only("company_name", "user__email"),
        )
    )
    serializer_class = SubscriptionsSerializer
