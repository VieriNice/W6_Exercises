
sched1 = "Garbage pickup is Wednesday"
sched2 = "Recycling pickup is Wednesday"
sched3 = "Yard waste pickup is Friday"

print(f'''Schedule change! This week due to the holiday, 
      {sched1.replace("Wednesday", "Thursday")}
    {sched2.replace ("Wednesday ", "Thursday")}
        {sched3.replace("Firday", "Saturday")}''')
holiday_sched = sched1.replace("Wednesday", "Thursday")



test_range = range(31)
for x in test_range:
    print(x)








# inv_gar = 26
# inv_recy = 8
# inv_yw = 14

# total_bill = "Your total bill managment bill is: {total: .2f}"
# breakdown = "Total includes garbage {0:.2f}, reclycling {1:.2f}, and yard waste {2:.2f}". format(inv_gar, inv_recy, inv_yw)


# print(total_bill.format(total = inv_gar + inv_recy + inv_yw))
# print(breakdown)




# print(f'''Your total waste management bill is:
#       ${format(inv_gar + inv_recy + inv_yw, ".2f")}''')
      





# sched1 = "Garbage pickup is Wednesday"
# sched2 = "Recycling pickup is Wednesday"
# sched3 = "Yard waste pickup is Friday"

# print(sched2.upper().rfind('RECYCLING'))
# print(sched2.rfind('pickup'))
# print(sched2.find('Wednesday'))
# print(sched2.rfind('Wednesday'))