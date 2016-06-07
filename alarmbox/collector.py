import sys

from alarmbox import settings
from shaping import DataStore

try:
    from pysnmp.entity.rfc3413.oneliner import cmdgen
except ImportError:
    print("Cannot import the module - pysnmp")
    sys.exit()

class Collector(object):
    def __init__(self, host):
        self.host = host
        self.port = '161'
        self.community = 'public'
        self.data_store = DataStore()

    def run(self, *args):
        self._cmdGen(*args)

    def _cmdGen(self, *args):
        transport = (self.host, self.port)
        cmdGen = cmdgen.CommandGenerator()
        authData = cmdgen.CommunityData(self.community)
        transportTarget = cmdgen.UdpTransportTarget(transport)

        errorIndication, errorStatus, errorIndex, varBindNbrTable = cmdGen.nextCmd(authData,
                                                                                    transportTarget, *args
                                                                                    # settings.SNMP_MIB2_IF['ifIndex'],
                                                                                    # settings.SNMP_MIB2_IF['ifDescr'],
                                                                                    # settings.SNMP_MIB2_IF['ifType'],
                                                                                    # settings.SNMP_MIB2_IF['ifHighSpeed']
                                                                                    )
        self.data_store.storing(varBindNbrTable, self.host)
