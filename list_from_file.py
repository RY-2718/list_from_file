def list_from_file(f):
    l = []
    with open(f,'r') as f:
        for row in f:
             s = row.strip()
             if len(s) > 0 and s[0] != "#":
                 l.append(".*" + s)
    return l
