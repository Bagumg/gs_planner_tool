from bitrix24 import *
from dt_to_ut import *
from gen_cli_list import *
from vars import *

test_day = generate_day()

for i in range(len(test_day) - 1):
    client_and_comment = get_day()
    bx24 = Bitrix24(API_URL)
    cal = bx24.callMethod('calendar.event.add',
                          type='user',
                          ownerId='95',
                          name=f'{client_and_comment[0]}',
                          description=f'При визите обратить внимание на:\n{client_and_comment[1]}',
                          # description='[img]https://www.bbcode.org/images/lubeck_small.jpg[/img]',
                          from_ts=f'{test_day[i]}',
                          to_ts=f'{test_day[i + 1]}',
                          section=51,
                          importance='normal',
                          color='#9cbe1c',
                          text_color='#283033',
                          accessibility='busy',)
