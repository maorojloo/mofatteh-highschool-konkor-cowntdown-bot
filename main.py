# University entrance exam date

import time
import schedule
import requests

def telegram_bot_sendtext(bot_message):
    bot_token = '1398678446:AAHEs_kIp3C78R8XYrNHKKydoNkbnFcVk54'
    bot_chatID = '-1001318501223'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def report():

    from datetime import datetime
    import pytz

    tz_te = pytz.timezone('Asia/Tehran')
    datetime_te = datetime.now(tz_te)
    IranDatetime = datetime_te.strftime("%Y/%m/%d %H:%M:%S")

    dt_string = IranDatetime
    dt_string1 = datetime.strptime(dt_string, "%Y/%m/%d %H:%M:%S")

    KonkoorDate = datetime(year=2021, month=7, day=1, hour=7, minute=0, second=0)

    result = KonkoorDate - dt_string1

    my_message = "کشکص چاقال  تا کنکور کیری فقط و فقط {}مونده به جای کصچرخ کیری تو تلگرام برو اون کتاب کیرو باز کن درستو بخون نترس کتابه نمیخورت . شو بخیر".format(result)
    telegram_bot_sendtext(my_message)


schedule.every(3600).seconds.do(report)

while True:
    schedule.run_pending()
    time.sleep(1)


# Finish :D
