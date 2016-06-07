

import threading
import time

from alarmbox import settings
from alarmbox.collector import Collector
from alarmbox.shaping import DataStore
from alarmbox.sms_send import Sms

temp_store = []
workers = []
data_store = DataStore()

mib2 = (settings.SNMP_MIB2_IF['ifIndex'],
        settings.SNMP_MIB2_IF['ifDescr'],
        settings.SNMP_MIB2_IF['ifHighSpeed'],
        settings.SNMP_MIB2_IF['ifHCInOctets'],
        settings.SNMP_MIB2_IF['ifHCOutOctets'],
        )

def job(host):
    col = Collector(host)
    # need to be implemented the exception for "col.run()"
    col.run(*mib2)
    temp_store.append(col.data_store)

def snmp_request():
    for host in settings.SNMP_HOSTS.keys():
        worker = threading.Thread(target=job, args=(host,))
        workers.append(worker)
        worker.start()
    for worker in workers:
        worker.join()
'''
def alarm_check(host, *ports):
    while True:
        for port in ports:
            id, desc, speed, inpacks, outpacks = data_store.get_iface(host, iface_name=port)
'''

def update():
    clear_temp_stored_list(workers, temp_store)
    snmp_request()
    data_store.merge_into_single_store(*temp_store)

def fetch_details(snmp_hosts):
    hosts_dict = {}
    new_data_store = DataStore()
    for host, ports in settings.SNMP_HOSTS.items():
        temp_list = []
        for port in ports:
            temp_list.append(data_store.get_iface(host, iface_name=port))
        hosts_dict[host] = temp_list
    new_data_store.set_data_store(hosts_dict)
    return new_data_store

def run():
    update()
    host_before = fetch_details(settings.SNMP_HOSTS)
    time.sleep(60*settings.INTERVAL)
    update()
    host_after = fetch_details(settings.SNMP_HOSTS)
    result_data = thold_check(host_before, host_after)
    send_result(result_date)

def thold_check(before, after):

    result_data = DataStore()
    res_dict = {}

    for host, ports in settings.SNMP_HOSTS.items():
        res_list = []
        for port in ports:
            ch1 = after.get_iface(host, iface_name=port)
            ch2 = before.get_iface(host, iface_name=port)
            if ch1 and ch2:
                in_pkts_1 = before.get_in_packets(host, port=port)
                in_pkts_2 = after.get_in_packets(host, port=port)
                out_pkts_1 = before.get_out_packets(host, port=port)
                out_pkts_2 = after.get_out_packets(host, port=port)
                res_in = (int(in_pkts_2) - int(in_pkts_1))//(60*settings.INTERVAL)
                res_out = (int(out_pkts_2) - int(out_pkts_1))//(60*settings.INTERVAL)
                id = after.get_iface(host, iface_name=port)[0]
                desc = after. get_iface(host, iface_name=port)[1]
                speed = after.get_iface(host, iface_name=port)[2]
                res_list.append((id, desc, speed, str(res_in), str(res_out)))

    res_dict[host] = res_list
    result_data.set_data_store(res_dict)

    return result_data

def send_result(result_data):
    sms = Sms()
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

        if thold_inpkts >= float(settings.THOLD_VALUE)/100 or thold_outpkts >= float(settings.THOLD_VALUE)/100:
            message = message_template %(host,
                                            id,
                                            desc,
                                            str(float(speed)/1000)+' Gb',
                                            format(inpkts),
                                            format(outpkts)
                                            )

            sms.send(message, *settings.TO_SMS)

def format(packets):
    bit = 1
    byte = 8*bit
    Kb = 1024*bit
    Mb = 1024*Kb
    Gb = 1024*Mb

    new_packets = int(packets)*byte

    if len(str(new_packets)) < 3:
        return str(float(new_oackets))+' bit'
    elif 3 <= len(str(new_packets)) < 6:
        return str(round(float(new_packets)/float(Kb), 2))+' Kb'
    elif 6 <= len(str(new_packets)) < 9:
        return str(round(float(new_packets)/float(Mb), 2))+' Mb'
    elif 9 <= len(str(new_packets)) < 12:
        return str(round(float(new_packets)/float(Gb), 2))+' Gb'

    return str(new_packets)+' bit'

def set_action(timer):
    while True:
        delta = diff_times(timer)
        if delta.seconds == 0:
            threading.Timer(delta+1, run).start()
            print('func')
        time.sleep(1)

def diff_times(timer):
    timer= timer.split(":")[0]
    tm_hour, tm_min, tm_sec = timer[0], timer[1], timer[2]
    now = datetime.datetime.now()
    new_timer = datetime.datetime(now.year, now.month, now,day, tm_hour, tm_min, tm_sec)
    return new_timer - now


def clear_temp_stored_list(*temp_lists):
    for temp_list in temp_lists:
        while True:
            if len(temp_list) == 0:
                break
            del temp_list[0]

if __name__ == '__main__':
   while True:
        run()
