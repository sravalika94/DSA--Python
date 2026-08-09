class Solution(object):
    def strongPasswordChecker(self, password):
        missing = 3
        if any(c.islower() for c in password):
            missing -= 1
        if any(c.isupper() for c in password):
            missing -= 1
        if any(c.isdigit() for c in password):
            missing -= 1

        arr = []
        i = 2
        while i < len(password):
            if password[i] == password[i-1] == password[i-2]:
                l = 2
                while i < len(password) and password[i] == password[i-1]:
                    l += 1
                    i += 1
                arr.append(l)
            else:
                i += 1

        if len(password) < 6:
            return max(missing, 6 - len(password))

        replace = sum(x // 3 for x in arr)

        if len(password) <= 20:
            return max(missing, replace)

        delete = len(password) - 20

        for k in [1, 2]:
            for i in range(len(arr)):
                if delete <= 0:
                    break
                if arr[i] < 3 or arr[i] % 3 != k - 1:
                    continue
                d = min(delete, k)
                arr[i] -= d
                delete -= d
                replace -= d // k

        for i in range(len(arr)):
            if delete <= 0:
                break
            if arr[i] >= 3:
                d = min(delete, arr[i] - 2)
                arr[i] -= d
                delete -= d
                replace -= d // 3

        return (len(password) - 20) + max(missing, replace)
        