days = {
    'January': 31, 'February': 28, 'March': 31, 'April': 30,
    'May': 31, 'June': 30, 'July': 31, 'August': 31,
    'September': 30, 'October': 31, 'November': 30,
    'December': 31
}


user_input = input("월을 입력하세요: ")
if user_input.capitalize() in days:
    print(f"{user_input.capitalize()}의 일수는 {days[user_input.capitalize()]}입니다.")
else:
    
    abbreviations = {month[:3]: days[month] for month in days}
    if user_input.capitalize() in abbreviations:
        print(f"{user_input.capitalize()}의 일수는 {abbreviations[user_input.capitalize()]}입니다.")
    else:
        print("잘못된 입력입니다.")


print("알파벳 순서로 정렬된 월:")
for month in sorted(days):
    print(month)


print("일수가 31인 월:")
for month, day in days.items():
    if day == 31:
        print(month)


print("일수를 기준으로 오름차순 정렬된 월:")
for month in sorted(days, key=days.get):
    print(f"{month}: {days[month]}")
