import time
import datetime


# Генерирует дату дд/мм/гггг в заданном диапазоне.
def get_dates_list(ds, df, ms, mf):
    days = []
    months = []
    year = '2020'
    date_list = []
    # Генерируем день с ds по df. Тут проверку на 31 день не воткнуть, поэтому будет в месяцах
    for day in range(ds, df + 1):
        if day < 10:
            days.append(f'0{day}')
        else:
            days.append(f'{day}')
    #  Генерируем месяц с ms по mf
    for month in range(ms, mf + 1):
        if month < 10:
            months.append(f'0{month}')
        else:
            months.append(f'{month}')
    # Генерируем всю дату. Если месяц чётный, то добавляем 31 число. TODO февраль
    for d in days:
        for m in months:
            if m != '02' and int(m) % 2 == 0 and int(d) == 30:
                date_list.append(f'31/{m}/{year}')
            date_list.append(f'{d}/{m}/{year}')
    # Возвращаем список дат в формате [01/01/2020, 01/02/2020, ... 31/12/2020]
    return date_list


# Генерирует дни рабочей недели в UNIX времени.
# На выход подаёт список дат с 9:00(начало рабочего дня) в заданном диапазоне.
def generate_week():
    gtl = get_dates_list(
        int(input('Введите дату начала планирования: ')),
        int(input('Введите дату конца планирования: ')),
        int(input('Введите месяц начала планирования: ')),
        int(input('Введите месяц конца планирования: ')))

    utl = []
    # Приводим даты к UNIX формату.
    for i in gtl:
        utl.append(time.mktime(datetime.datetime.strptime(i, '%d/%m/%Y').timetuple()))
    # Плюсуем 32400 т.к. день в полученной дате стартует с 0:00, а нам надо с 9:00 планироваться
    wh = [i + 32400 for i in utl]

    return wh


def generate_day():
    work_day = []
    test_day = generate_week()

    for j in test_day:
        for i in range(11):
            work_day.append(j)
            j += 3600

    return work_day
