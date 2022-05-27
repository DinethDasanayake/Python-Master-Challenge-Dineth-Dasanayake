# d=distance
dw = 100
dl = 300
dr_from_l = 1.2

dr_from_l *= 1000
dr_nest = dr_from_l + dl

day = dw+dl+dr_nest
three_days=day*3
three_days_km=three_days/1000

print("Kilometers they fly in 3 days =",three_days_km)
