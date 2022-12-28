def validate_ipv6(ip):
    segments = ip.split(":")

    if len(segments) != 8:
        return False

    for segment in segments:
        if len(segment) != 4:
            return False
        for char in segment:
            if not (char.isdigit() or 'a' <= char <= 'f' or 'A' <= char <= 'F'):
                return False

    return True


print(validate_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))
