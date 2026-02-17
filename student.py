marks= [75,80,85,90,95]

total = 0

for mark in marks:
    total = total + mark
    print("Current total:", total)
print("Final total:", total)
average=total/len(marks)
print("average:",round(average,2))
highest=marks[0]
for mark in marks:
	if mark > highest:
		highest = mark
print(highest)
lowest=marks[0]
for mark in marks:
	if mark < lowest:
		lowest = mark
print(lowest)
count_above_75 = 0

for mark in marks:
    if mark > 75:
        count_above_75 = count_above_75 + 1

print(count_above_75)

