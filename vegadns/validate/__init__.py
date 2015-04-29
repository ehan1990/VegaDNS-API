from vegadns.validate.ip import ValidateIPAddress
from vegadns.validate.dns import ValidateDNS


class Validate(object):

    def ipv4(self, ipv4_address):
        return ValidateIPAddress.ipv4(ipv4_address)

    def ipv6(self, ipv6_address):
        return ValidateIPAddress.ipv6(ipv6_address)

    def record_hostname(self, name):
        return ValidateDNS.record_hostname(name)