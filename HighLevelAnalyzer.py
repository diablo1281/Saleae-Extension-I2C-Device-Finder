from saleae.analyzers import HighLevelAnalyzer, AnalyzerFrame, StringSetting, ChoicesSetting

class Hla(HighLevelAnalyzer):
    device_address = StringSetting()
    address_type = ChoicesSetting(choices=('binary', 'decimal', 'hex'))
    device_address_number = 0

    result_types = {
        'good': {
            'format': '[{{data.address}}]'
        },
        'bad': {
            'format': 'BAD [{{data.address}}] != [{{data.bad_address}}]'
        },
        'mismatch': {
            'format': 'MISMATCH'
        }
    }

    def __init__(self):
        print("Settings:", self.device_address, self.address_type)

        try:
            if self.address_type == 'binary':
                self.device_address_number = int(self.device_address, 2)
            elif self.address_type == 'hex':
                self.device_address_number = int(self.device_address, 16)
            else:
                self.device_address_number = int(self.device_address)
        except:
            self.device_address_number = int(self.device_address)

    def decode(self, frame: AnalyzerFrame):
        if frame.type == 'address':
            if frame.data['address'][0] == self.device_address_number:
                return AnalyzerFrame('good', frame.start_time, frame.end_time, {'address': self.device_address})
            else:
                return
        else:
            return
