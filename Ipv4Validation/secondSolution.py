import re


def validate_ipv4(ip):
    result = re.fullmatch(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}$", ip)
    return result is not None


print(validate_ipv4("172.16.254.14"))
