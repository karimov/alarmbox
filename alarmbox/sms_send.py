
import suds.client
import base64
import time

class Sms(object):
    wsdl_url = 'http://msender.uzbek-telecom.uz/scripts/soap/Banking.wsdl'
    client = suds.client.Client(wsdl_url)
    location = '' # web service url
    client.sd[0].service.setlocation(location)
    from_number = '6100'
    #message = 'Not Avialable'

    def send(self, message, *to_numbers):
        binary_data = base64.b64encode(message.encode())
        message = binary_data.decode()
        for to_number in to_numbers:
            self.client.service.message(self.from_number, to_number, message, 3)
            time.sleep(2)
