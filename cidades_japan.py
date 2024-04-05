Cidades = ['Tóquio','Yokohama','Osaka','Nagoya','Sapporo','Kobe','Kyoto','Fukuoka','Kawasaki','Saitama','Hiroshima','Sendai'
           'Kawaguchi','Nishinomiya','Himeji','Kurashiki','Ichikawa','Matsudo','Oita','Utsunomiya','Amagasaki','Kanazawa',
            'Toyama','Toyota','Nagasaki','Machida','Fukuyama','Yokosuka','Fujisawa','Hirakata','Gifu','Kitakyushu','Chiba',
            'Hamamatsu','Sakai','Niigata','Shizuoka','Okayama','Kumamoto','Sagamihara','Kagoshima','Hachioji','Funabashi',
            'Matsuyama','Higashiosaka']

grupo = dict()

for city in Cidades:
    letra = city[0]
    if letra not in grupo:
        grupo[letra] = [city]
    else:
        grupo[letra].append(city)

for g in grupo.keys():
    print(f'{g}:')
    for c in grupo[g]:
        print(f' - {c}')

       



