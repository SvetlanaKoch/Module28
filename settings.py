from faker import Faker

import string

"""Данные для авторизации в системе"""
valid_firstname = 'Светлана'
valid_lastname = 'Коч'
valid_email = 'svetlana.95@inbox.ru'
valid_pass = 'Q1q2q3q4q5q6'
valid_phone = '+79166106808'
valid_login = 'Svetlana_Koch'
valid_ls = '11111111'
from locators import AutoPageLoc
"""Неправильные данные для авторизации в системе"""
# ввод данных на русском языке
fake_ru = Faker('ru_RU')
fake_firstname = fake_ru.first_name()
fake_lastname = fake_ru.last_name()
fake_phone = fake_ru.phone_number()
#ввод данных на английском языке
fake = Faker()
fake_firstname_en = fake.first_name()
fake_lastname_en = fake.last_name()
fake_password = fake.password()
fake_email = fake.email()
fake_login = fake.user_name()
invalid_ls = '222222222'
region = 'Москова'