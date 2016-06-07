

import run, threading
import datetime, time

def run_timer():
    run.update()
    host_before = run.fetch_details(run.settings.SNMP_HOSTS)
    time.sleep(60*run.settings.INTERVAL)
    run.update()
    host_after = run.fetch_details(run.settings.SNMP_HOSTS)
    result_data = run.thold_check(host_before, host_after)
    send_result(result_data)

def send_result(result_data):
    sms = run.Sms()
    message_template = '''<Alarmbox Report>
    Device: %s
    Port_ID: %s
    Port: %s
    PortSpeed: %s
    InPkts: %s
    OutPkts: %s
    '''
    for record in result_data:
        host = record.keys()[0]
        id = record[host][0]
        desc = record[host][1]
        speed = record[host][2]
        inpkts = record[host][3]
        outpkts = record[host][4]

        thold_inpkts = float(inpkts)*8/(int(speed)*(1000**2))
        thold_outpkts = float(outpkts)*8/(int(speed)*(1000**2))

        message = message_template %(host,
                                        id,
                                        desc,
                                        str(float(speed)/1000)+' Gb',
                                        run.format(inpkts),
                                        run.format(outpkts)
                                        )

        sms.send(message, *run.settings.TO_SMS)


def timer_action(timer):
    while True:
        delta = diff_times(timer)
        if delta.seconds == 0:
            threading.Timer(delta.seconds+1, run_timer).start()
            print(time.ctime(), "Action has been started in time!")
        time.sleep(1)

def diff_times(timer):
    timer= timer.split(":")
    tm_hour, tm_min, tm_sec = timer[0], timer[1], timer[2]
    now = datetime.datetime.now()
    new_timer = datetime.datetime(now.year, now.month, now.day, int(tm_hour), int(tm_min), int(tm_sec))
    return new_timer - now

if __name__ == '__main__':
    timer_action(run.settings.MSG_SENDTIME)


