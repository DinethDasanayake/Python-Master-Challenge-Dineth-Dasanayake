# min=minutes
#h=hours
#dau=daughter
lady_min = 20
lady_day = 3

lord_min = 25
lord_day = 4

dau_min = 15
dau_day = 5

master_min = 30
master_day = 6

# week=minutes they exercise in a week
lady_week = lady_min*lady_day
lord_week = lord_min*lord_day
dau_week = dau_min*dau_day
master_week = master_min*master_day

all_one_week = lady_week+lord_week+dau_week+master_week
all_two_weeks = all_one_week*2

all_two_weeks_h = int(all_two_weeks/60)
all_two_weeks_min = all_two_weeks%60

print("Hours and minutes they all exercise during 2 weeks =",all_two_weeks_h, "hours and", all_two_weeks_min, "minutes")
