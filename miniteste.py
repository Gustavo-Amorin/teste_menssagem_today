import pywhatkit as pwk
import schedule
import time 

def tarefa():
    pwk.sendwhatmsg_instantly("+351934933650", "teste feito", 15, tab_close=True, close_time= 10)

schedule.every().day.at('13:11').do(tarefa)

while True:
    schedule.run_pending()
    time.sleep(1)
    