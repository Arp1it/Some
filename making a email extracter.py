import re

strop = """53yht@gamil.com, erfgbueogbuoeqrgubeuebuebegbqui
qergeqgoqueyrghqetgq\regqergegburgyerg
egewirfbuwefbuwef
fwqfiuhwfikjfiurfgrwjbnrwer
fgwqfrfiwerfrhffdf
wefwfbjkfnjwfh
wfwjfwfwieruh akshaNSH@gmail.com eghyefhufgbuyfg
egeughe
eguyehrfgieqf]
eqfuyeghufgoweugyt8t807ywet7
geugyeghe8hger
.+_%lmma@gmail.com dfsghbedgbiebge
\egefgeuwfede
gedguyegfuiesfadr
fgergfuyeferfgre
_3fg546bfvuiEd@gmail.com"""

pla = re.compile(r'[a-zA-Z0-9_.+%$#!^&*]+@[a-zA-Z0-9_.+%]+[.][a-zA-Z0-9_.]+')
d = pla.finditer(strop)

m = []

for i in range(len(strop)):
    for l in d:
        f = l.span()
        m.append(strop[f[0]:f[1]])

for i, t in enumerate(m):
    print(f"email {i} ", m[i])

g = re.findall(r'[a-zA-Z0-9_.+%$#!^&*]+@[a-zA-Z0-9_.+%]+[.][a-zA-Z0-9_.]+', strop)
print(g)
