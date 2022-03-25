def convert_to_preferred_format(sec):
    sec = sec % (3600 * 86400)
    day = sec // 86400
    sec %= 86400
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min: int = sec // 60
    sec %= 60
    print("Значение секунд в днях:", day)
    print("Значение секунд в часах:", hour)
    print("Значение секунд в минутах:", min)
    print("Значение секунд в секундах :", sec)
    return "%02d:%02d:%02d:%02d" % (day, hour, min, sec)


n = 86463

print("Time in preferred format :-", convert_to_preferred_format(n))
