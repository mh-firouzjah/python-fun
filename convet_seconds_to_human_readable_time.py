def make_readable(seconds):
    min, sec = divmod(seconds, 60)
    hr, min = divmod(min, 60)
    return f"{hr:02}:{min:02}:{sec:02}"


print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))
