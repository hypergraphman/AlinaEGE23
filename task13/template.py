g = {
    'А': 'БГ',
    'Б': 'Д',
    'В': 'АБДГ',
    'Ж': 'Е',
    'Л': 'ЖК',
    'К': 'Ж',
    'И': 'Л',
    'Е': 'ЛВ',
    'Д': 'ИЛЕ',
    'Г': 'ЕЖ',
}


def f(s, p):
    if len(p) > 1 and p[0] == p[-1]:
        return 1
    if len(p) != len(set(p)):
        return 0
    return sum([f(x, p + x) for x in g[s]])


print(f('Е', 'Е'))
