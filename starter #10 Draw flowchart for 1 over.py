import random

sl_r = 0
sl_t = 0
sl_w = 0
sl_b = 0
'''
1:wicket
2:runs
3:extras
'''
print("SL BATTING")
while sl_b < 6:
    type = random.randint(1, 3)
    if type == 1:
        sl_b += 1
        sl_w += 1
        print(sl_b, "balls |", sl_r, "runs |",
              sl_w, "wickets | 0 extras | total", sl_t)
    elif type == 2:
        sl_b += 1
        sl_r = random.randint(0, 6)
        sl_t += sl_r
        print(sl_b, "balls |", sl_r, "runs |", sl_w,
              "wickets | 0 extras | total", sl_t)
    else:
        sl_t += 1
        print(sl_b, "balls |", sl_r, "runs |", sl_w,
              "wickets |", 1, "extras | total", sl_t)
print("total", sl_t)

ind_r = 0
ind_t = 0
ind_w = 0
ind_b = 0
'''
1:wicket
2:runs
3:extras
'''
print("\n\nINDIA BATTING")
while ind_b < 6:
    type = random.randint(1, 3)
    if type == 1:
        ind_b += 1
        ind_w += 1
        print(ind_b, "balls |", ind_r, "runs |",
              ind_w, "wickets | 0 extras | total", ind_t)
    elif type == 2:
        ind_b += 1
        ind_r = random.randint(0, 6)
        ind_t += ind_r
        print(ind_b, "balls |", ind_r, "runs |", ind_w,
              "wickets | 0 extras | total", ind_t)
    else:
        ind_t += 1
        print(ind_b, "balls |", ind_r, "runs |", ind_w,
              "wickets |", 1, "extras | total", ind_t)
print("total", ind_t)

if sl_t > ind_t:
    print("\nSri Lanka won the match by", sl_t-ind_t, "runs.")
elif ind_t > sl_t:
    print("\nIndia won the match by", ind_t-sl_t, "runs.")
else:
    print("\nMatch was drawn.")
