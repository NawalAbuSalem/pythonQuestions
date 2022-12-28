import re


def validate_ipv6(ip):
    result = re.fullmatch(r"^(([0-9 a-f A-F]{4})(:(?!$)|$)){8}$", ip)
    return result is not None


print(validate_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))
