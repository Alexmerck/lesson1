def get_summ(one, two, delimiter='&'):
    return one.capitalize() + delimiter + two.capitalize()
a = get_summ("learn", "python")
print(a)
