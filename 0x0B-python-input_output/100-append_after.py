#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r') as f:
        t = f.read()
    l = t.split('\n')
    try:
        l.remove('')
    except:
        pass
    c = 1
    for n_line, line in enumerate(l[:]):
        if search_string in line:
            l = (l[:n_line + c] +
                     [new_string.replace('\n', '')] + l[n_line + c:])
            c += 1
    new_t = "\n".join(l)
    if t[-1] == '\n':
        new_t += '\n'
    with open(filename, 'w') as f:
        f.write(new_t)
