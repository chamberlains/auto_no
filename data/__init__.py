from faker import Faker
from faker.providers import BaseProvider

import datetime

fake = Faker("zh_CN")


def gen_datetime(fmt="%y-%m-%d", offset=0):
    return (datetime.datetime.now() + datetime.timedelta(days=offset)).strftime(fmt)


class MyProvider(BaseProvider):
    def id_card(self):
        return f"{fake.random.randint(100000, 999999)}{gen_datetime(fmt='%Y%m%d')}{str(fake.random.randint(0, 9999)).zfill(4)} "


fake.add_provider(MyProvider)
