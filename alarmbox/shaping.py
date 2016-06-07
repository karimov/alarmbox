

class DataStore(object):
    def __init__(self):
        self.data_store = {}


    def set_data_store(self, data):
        self.data_store = data

    def storing(self, collected_data, host):
        innerList = []
        for rows in collected_data:
            innerTup = ()
            for item1, item2 in rows:
                innerTup = innerTup + (item2.prettyPrint(),)
            innerList.append(innerTup)
        self.data_store[host] = innerList


    def merge_into_single_store(self, *data_stores):
        result = {}
        for data_store in data_stores:
            result.update(data_store.data_store)

        self.data_store = result

    def __str__(self):
        return self.data_store

    def get_ipaddr_devices(self):
        return self.data_store.keys()

    def get_iface(self, dev_ip, **kwargs):
        retdata = None
        if kwargs.get('iface_id', False) and self.data_store.get(dev_ip, False):
            iface_id = kwargs['iface_id']
            index = 0
            for line in self.data_store[dev_ip]:
                if line != None and str(iface_id) in line:
                    break
                index = index + 1
            if index < len(self.data_store[dev_ip]):
                retdata = self.data_store[dev_ip][index]
            else:
                return None
        else:
            if kwargs.get('iface_name', False) and self.data_store.get(dev_ip, False):
                iface_name = kwargs['iface_name']
                index = 0
                for line in self.data_store[dev_ip]:
                    if line != None and iface_name in line[1]:
                        break
                    index = index + 1
                if index < len(self.data_store[dev_ip]):
                    retdata = self.data_store[dev_ip][index]
                else:
                    return None

        return retdata

    def get_in_packets(self, host, **kwargs):
        in_packets = -1
        if kwargs.get('port', False):
            iface = self.get_iface(host, iface_name=kwargs['port'])
            if iface:
                id, desc, speed, inpkts, outpkts = iface
                in_packets = int(inpkts)
        else:
            return None
        return in_packets

    def get_out_packets(self, host, **kwargs):
        out_packets = -1
        if kwargs.get('port', False):
            iface = self.get_iface(host, iface_name=kwargs['port'])
            if iface:
                id, desc, speed, inpkts, outpkts = iface
                out_packets = int(outpkts)
        else:
            return None
        return out_packets

    def get_port_speed(self, host, **kwargs):
        port_speed = -1
        if kwargs.get('port', False):
            iface = self.get_iface(host, iface_name=kwargs['port'])
            if iface:
                id,desc,speed, inpkts, outpkts = iface
                port_speed = speed
        else:
            return None
        return port_speed

    def get_port_id(self, host, **kwargs):
        port_id = -1
        if kwargs.get('port', False):
            iface = self.get_iface(host, iface_name=kwargs['port'])
            if iface:
                id,desc,speed,inpkts, outpkts  = iface
                port_id = id
        else:
            return None
        return port_id

    def __iter__(self):
        for host, ports in self.data_store.items():
            for port in ports:
                yield {host: port}

        '''


        if errorIndication:
            print(errorIndication)
            return
        # SNMPv1 response may contain noSuchName error *and* SNMPv2c exception,
        # so we ignore noSuchName error here
        if errorStatus and errorStatus != 2:
            print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBindTable[-1][int(errorIndex) - 1][0] or '?'))
            return  # stop on error
        for varBindRow in varBindTable:
            for oid, val in varBindRow:
                print('%s = %s' % (oid.prettyPrint(), val.prettyPrint()))

        return 1  # signal dispatcher to continue
        '''
