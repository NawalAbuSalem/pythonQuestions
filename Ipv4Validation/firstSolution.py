
def validate_ipv4(ip):
    segments = ip.split(".")
    if len(segments) != 4:
        return False
    for segment in segments:
        for char in segment:
            if not char.isdigit():
                return False

        if int(segment) > 255:
            return False

        if len(segment) > 1 and segment[0] == '0':
            return False

    return True


print(validate_ipv4("172.16.254.14"))
