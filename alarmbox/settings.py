

INTERVAL = 5 # interval in minutes

MSG_SENDTIME = "20:29:59" # format of timer "%Hh:%Mm:%Ss"

TO_SMS = [
    '998909837130',
    '998946371359'
    '998903255556',
    ]

SNMP_HOSTS = {
        '10.255.0.254': ('xgei_2/1', 'xgei_2/2'),
        '10.255.0.253': ('xgei_2/1', 'xgei_2/2'),
      #  '10.255.0.250': ('geo_1/2', 'gei_1/3'),
      #  '10.255.0.251': ('geo_1/2', 'gei_1/3'),
      #  '10.255.0.247': ('geo_1/2', 'gei_1/3'),
      #  '10.255.0.248': ('geo_1/2', 'gei_1/3')

    }

THOLD_VALUE = '75' # 75% of threshold of interface

SNMP_MIB2_SYS = {
        'sysDescr': '1.3.6.1.2.1.1.1',
        'sysObjectID': '1.3.6.1.2.1.1.2',
        'sysUpTime': '1.3.6.1.2.1.1.3',
        'sysContact': '1.3.6.1.2.1.1.4',
        'sysName': '1.3.6.1.2.1.1.5',
        'sysLocation': '1.3.6.1.2.1.1.6',
        'sysServices': '1.3.6.1.2.1.1.7'
    }


'''
    SNMP MIB-2 Interfaces
'''

SNMP_MIB2_IF = {
        'ifTable': '1.3.6.1.2.1.2.2',
        'ifIndex': '1.3.6.1.2.1.2.2.1.1',
        'ifDescr': '1.3.6.1.2.1.2.2.1.2',
        'ifType' : '1.3.6.1.2.1.2.2.1.3',
        'ifMtu': '1.3.6.1.2.1.2.2.1.4',
        'ifSpeed': '1.3.6.1.2.1.2.2.1.5',
        'ifPhysAddress': '1.3.6.1.2.1.2.2.1.6',
        'ifAdminStatus': '1.3.6.1.2.1.2.2.1.7',
        'ifOperStatus': '1.3.6.1.2.1.2.2.1.8',
        'ifLastChange': '1.3.6.1.2.1.2.2.1.9',
        'ifInOctets': '1.3.6.1.2.1.2.2.1.10',
        'ifInUcastPkts': '1.3.6.1.2.1.2.2.1.11',
        'ifInNUcastPkts': '1.3.6.1.2.1.2.2.1.12',
        'ifInDiscards': '1.3.6.1.2.1.2.2.1.13',
        'ifInErrors' : '1.3.6.1.2.1.2.2.1.14',
        'ifInUnknownProtos': '1.3.6.1.2.1.2.2.1.15',
        'ifOutOctets': '1.3.6.1.2.1.2.2.1.16',
        'ifOutUcastPkts': '1.3.6.1.2.1.2.2.1.17',
        'ifOutNUcastPkts': '1.3.6.1.2.1.2.2.1.18',
        'ifOutDiscards': '1.3.6.1.2.1.2.2.1.19',
        'ifOutErrors': '1.3.6.1.2.1.2.2.1.20',
        'ifOutQLen': '1.3.6.1.2.1.2.2.1.21',
        'ifSpecific': '1.3.6.1.2.1.2.2.1.22',
        'ifHCInOctets': '1.3.6.1.2.1.31.1.1.1.6',      # (64-bit Octets in counter)
        'ifHCOutOctets': '1.3.6.1.2.1.31.1.1.1.10',    # (64-bit Octets out counter)
        'ifHCInUcastPkts': '1.3.6.1.2.1.31.1.1.1.7',   # (64-bit Packets in counter)
        'ifHCOutUcastPkts': '1.3.6.1.2.1.31.1.1.1.11', # (64-bit Packets out counter)
        'ifHighSpeed': '1.3.6.1.2.1.31.1.1.1.15'       # (An estimate of the interface's current bandwidth in units of 1Mbps) 

    }
