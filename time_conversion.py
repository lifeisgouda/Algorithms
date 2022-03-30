# https://www.hackerrank.com/challenges/time-conversion/problem

# 1
time = input().strip()
h, m, s = map(int, time[:-2].split(':'))
p = time[-2:]
h = h % 12 + (p.upper() == 'PM') * 12
print(('%02d:%02d:%02d') % (h, m, s))

# 2
def timeConversion(s):
    tc = []

    tc.append(s[0:2])
    tc.append(s[3:5])
    tc.append(s[6:8])
    tc.append(s[8:])

    if tc[3] == "AM":
        if tc[0] == "12":
            tc[0] = "00"
            return str(tc[0] + ":" + tc[1] + ":" + tc[2])
        else:
            return str(tc[0] + ":" + tc[1] + ":" + tc[2])
    elif tc[3] == "PM":
        if tc[0] == "12":
            tc[0] = "12"
            return str(tc[0] + ":" + tc[1] + ":" + tc[2])
        else:
            tc[0] = str(int(tc[0]) + 12)
            return str(tc[0] + ":" + tc[1] + ":" + tc[2])
