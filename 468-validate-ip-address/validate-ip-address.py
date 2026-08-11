class Solution(object):
    def validIPAddress(self, queryIP):
        def ipv4():
            parts = queryIP.split(".")
            if len(parts) != 4:
                return False
            for p in parts:
                if not p or (len(p) > 1 and p[0] == '0'):
                    return False
                if not p.isdigit():
                    return False
                if not (0 <= int(p) <= 255):
                    return False
            return True

        def ipv6():
            hexdigits = "0123456789abcdefABCDEF"
            parts = queryIP.split(":")
            if len(parts) != 8:
                return False
            for p in parts:
                if not (1 <= len(p) <= 4):
                    return False
                if any(c not in hexdigits for c in p):
                    return False
            return True

        if ipv4():
            return "IPv4"
        if ipv6():
            return "IPv6"
        return "Neither"
        