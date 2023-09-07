
### 10_seconds_batch_static_eq =[('GDX', 'GVWY', 42, 1858), ('ZIP', 'ZIC', 1821, 79), ('ZIP', 'SHVR', 1390, 510), ('GDX', 'AA', 1763, 137), ('GDX', 'SHVR', 1771, 129), ('ZIP', 'GVWY', 2, 1898), ('ZIP', 'AA', 1620, 280), ('AA', 'GVWY', 2, 1898), ('ZIC', 'GVWY', 0, 1900), ('ZIC', 'AA', 482, 1418), ('GDX', 'ZIP', 739, 1161), ('GDX', 'ZIC', 1805, 95), ('ZIC', 'SHVR', 145, 1755), ('GVWY', 'SHVR', 1863, 37), ('AA', 'SHVR', 267, 1633)]
### 2_seconds_batch_static_eq =[('GDX', 'GVWY', 91, 1809), ('ZIP', 'ZIC', 1898, 2), ('ZIP', 'SHVR', 1510, 390), ('GDX', 'AA', 1345, 555), ('GDX', 'SHVR', 715, 1185), ('ZIP', 'GVWY', 36, 1864), ('ZIP', 'AA', 1774, 126), ('AA', 'GVWY', 8, 1892), ('ZIC', 'GVWY', 0, 1900), ('ZIC', 'AA', 526, 1374), ('GDX', 'ZIP', 333, 1567), ('GDX', 'ZIC', 1796, 104), ('ZIC', 'SHVR', 40, 1860), ('GVWY', 'SHVR', 1477, 423), ('AA', 'SHVR', 857, 1043)]
### 0.5_seconds_batch_static_eq =[('GDX', 'GVWY', 824, 1076), ('ZIP', 'ZIC', 1899, 1), ('ZIP', 'SHVR', 1244, 656), ('GDX', 'AA', 1299, 601), ('GDX', 'SHVR', 1233, 667), ('ZIP', 'GVWY', 720, 1180), ('ZIP', 'AA', 1589, 311), ('AA', 'GVWY', 159, 1741), ('ZIC', 'GVWY', 4, 1896), ('ZIC', 'AA', 638, 1262), ('GDX', 'ZIP', 875, 1025), ('GDX', 'ZIC', 1881, 19), ('ZIC', 'SHVR', 110, 1790), ('GVWY', 'SHVR', 1038, 862), ('AA', 'SHVR', 756, 1144)]

### 10_seconds_batch_dynamic_eq =[('GDX', 'GVWY', 7, 1893), ('ZIP', 'ZIC', 1862, 38), ('ZIP', 'SHVR', 1572, 328), ('GDX', 'AA', 1738, 162), ('GDX', 'SHVR', 1659, 241), ('ZIP', 'GVWY', 2, 1898), ('ZIP', 'AA', 1836, 64), ('AA', 'GVWY', 0, 1900), ('ZIC', 'GVWY', 0, 1900), ('ZIC', 'AA', 605, 1295), ('GDX', 'ZIP', 139, 1761), ('GDX', 'ZIC', 1654, 246), ('ZIC', 'SHVR', 153, 1747), ('GVWY', 'SHVR', 1877, 23), ('AA', 'SHVR', 504, 1396)]
### 2_seconds_batch_dynamic_eq =[('GDX', 'GVWY', 13, 1887), ('ZIP', 'ZIC', 1889, 11), ('ZIP', 'SHVR', 1234, 666), ('GDX', 'AA', 994, 906), ('GDX', 'SHVR', 926, 974), ('ZIP', 'GVWY', 75, 1825), ('ZIP', 'AA', 1800, 100), ('AA', 'GVWY', 8, 1892), ('ZIC', 'GVWY', 0, 1900), ('ZIC', 'AA', 599, 1301), ('GDX', 'ZIP', 92, 1808), ('GDX', 'ZIC', 1679, 221), ('ZIC', 'SHVR', 46, 1854), ('GVWY', 'SHVR', 1668, 232), ('AA', 'SHVR', 730, 1170)]
### 0.5_seconds_batch_dynamic_eq =[('GDX', 'GVWY', 399, 1501), ('ZIP', 'ZIC', 1895, 5), ('ZIP', 'SHVR', 1196, 704), ('GDX', 'AA', 940, 960), ('GDX', 'SHVR', 1336, 564), ('ZIP', 'GVWY', 534, 1366), ('ZIP', 'AA', 1802, 98), ('AA', 'GVWY', 98, 1802), ('ZIC', 'GVWY', 3, 1897), ('ZIC', 'AA', 720, 1180), ('GDX', 'ZIP', 443, 1457), ('GDX', 'ZIC', 1799, 101), ('ZIC', 'SHVR', 82, 1818), ('GVWY', 'SHVR', 1225, 675), ('AA', 'SHVR', 1148, 752)]

data=[('GDX', 'GVWY', 399, 1501), ('ZIP', 'ZIC', 1895, 5), ('ZIP', 'SHVR', 1196, 704), ('GDX', 'AA', 940, 960), ('GDX', 'SHVR', 1336, 564), ('ZIP', 'GVWY', 534, 1366), ('ZIP', 'AA', 1802, 98), ('AA', 'GVWY', 98, 1802), ('ZIC', 'GVWY', 3, 1897), ('ZIC', 'AA', 720, 1180), ('GDX', 'ZIP', 443, 1457), ('GDX', 'ZIC', 1799, 101), ('ZIC', 'SHVR', 82, 1818), ('GVWY', 'SHVR', 1225, 675), ('AA', 'SHVR', 1148, 752)]


wins = {'AA': 0, 'GVWY': 0, 'SHVR': 0, 'GDX': 0, 'ZIC': 0, 'ZIP': 0}
beats = {'AA': 0, 'GVWY': 0, 'SHVR': 0, 'GDX': 0, 'ZIC': 0, 'ZIP': 0}
dominates = {'AA': [], 'GVWY': [], 'SHVR': [], 'GDX': [], 'ZIC':[], 'ZIP': []}

for d in data:
    wins[d[0]] += d[2]
    wins[d[1]] += d[3]
    
    if d[2] > d[3]:
        beats[d[0]] += 1
        dominates[d[0]]+=[d[1]]
    else:
        beats[d[1]] += 1
        dominates[d[1]]+=[d[0]]




wins = dict(sorted(wins.items(), key=lambda x: x[1], reverse=True))
beats = dict(sorted(beats.items(), key=lambda x: x[1], reverse=True))

# Print the results
print("\n")
print('Total number of wins for each trading algorithm:')
print(wins)
print('\nNumber of algorithms beaten by each trading algorithm:')
print(beats)
print('\nNumber of algorithms dominated by each trading algorithm:')
print(dominates)
