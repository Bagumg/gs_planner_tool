import pandas as pd
import random
import csv


def generate_clients_dict():
    df = pd.read_excel('1-2020.xlsx')

    # писок клиентов для визитов
    cli_list = [i for i in df['Контрагент'][2:] if i != 0]
    # Список количества визитов к клиентам
    visits_list = [int(i) for i in df['План Кол-во визитов в месяц'][2:] if i != 0]
    # Список "Номенклатура развития" будет указан в качестве комментария в календаре.
    comments = [[i] for i in df['Номенклатура Развития'][2:] if i != 0]
    # Формируем словарь вида "клиент: [количество визитов, [комментарии(Номенклатура развития)]]"
    done_dict = dict()
    for i in range(len(cli_list)):
        done_dict[cli_list[i]] = visits_list[i], comments[i]

    return done_dict


def get_client():
    done_dict = generate_clients_dict()
    client = random.choice(list(done_dict.keys()))
    visits = done_dict[f'{client}'][0]
    comments = done_dict[f'{client}'][1]
    return client, visits, comments


def generate_month_file():
    df = pd.read_excel('2020.xlsx')
    contragent_list_all = [i for i in df['Контрагент'][2:] if i != 0]
    visits_list_all = [int(i) for i in df['План Кол-во визитов в месяц'][2:] if i != 0]
    comments_list_all = [i for i in df['Номенклатура Развития'][2:] if i != 0]
    # Формируем список клиентов на основе количества визитов к ним, т.е. если 4 визита,
    # то клиент фигурирует в этом списке 4 раза
    # for i in range(len(visits_list_all)):
    #     if visits_list_all[i] != 1:
    #         for j in range(visits_list_all[i] - 1):
    #             contragent_list_all.append(contragent_list_all[i])
    all_dict = dict()
    for i in range(len(comments_list_all)):
        all_dict[contragent_list_all[i]] = visits_list_all[i], comments_list_all[i]

    # Записываем полученный список в файл
    df = pd.DataFrame.from_dict(all_dict, orient='index')
    df.to_csv('month.csv')


def generate_week_file():
    try:
        df = pd.read_csv('month.csv', index_col=0)
        d = df.to_dict('split')
        d = dict(zip(d['index'], d['data']))
        contragent_list_week = []
        visits_list_week = []
        comments_list_week = []
        for k, v in d.items():
            if v[0] != 1:
                for j in range(v[0]):
                    contragent_list_week.append(k)
                    comments_list_week.append(v[1])
            else:
                contragent_list_week.append(k)
                comments_list_week.append(v[1])

        week_dict = dict()
        while len(week_dict) <= 50:
            random_list_week = random.choices(contragent_list_week, k=50)
            for i in range(len(random_list_week)):
                week_dict[random_list_week[i]] = d.get(random_list_week[i])[1]

        df = pd.DataFrame.from_dict(week_dict, orient='index')
        df.to_csv('week.csv')

    except:
        pass


def get_day():
    try:
        df = pd.read_csv('week.csv', index_col=0)
        dict_day = df.to_dict('split')
        dict_day = dict(zip(dict_day['index'], dict_day['data']))
        day_list = []

        for k in dict_day.keys():
            day_list.append(k)

        random_contragent = random.choice(day_list)
        desc = dict_day.pop(random_contragent)

        df = pd.DataFrame.from_dict(dict_day, orient='index')
        df.to_csv('week.csv')

        print(random_contragent)
        print(len(dict_day))

        return random_contragent, desc[0]
    except:
        pass
