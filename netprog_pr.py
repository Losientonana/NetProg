d = [
    {'name': 'Todd', 'phone': '555-1414', 'email': 'todd@mail.net'},
    {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
    {'name': 'Princess', 'phone': '555-3141', 'email': ''},
    {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@mail.net'}
]


def print_users_with_phone_ending_in_8():
    for person in d:
        if person['phone'].endswith('8'):
            print(person['name'])


def print_users_without_email():
    for person in d:
        if not person['email']:
            print(person['name'])


def print_contact_info(name):
    for person in d:
        if person['name'] == name:
            print(f"전화번호: {person['phone']}, 이메일: {person['email']}")
            return
    print("이름이 없습니다")


def parse_string_to_dict(query_string, delimiter1, delimiter2):
    result_dict = {}
    pairs = query_string.split(delimiter1)
    for pair in pairs:
        key, value = pair.split(delimiter2)
        result_dict[key] = value
    return result_dict


print("전화번호가 8로 끝나는 사용자:")
print_users_with_phone_ending_in_8()

print("\n이메일이 없는 사용자:")
print_users_without_email()

user_input = input("\n사용자 이름을 입력하세요: ")
print_contact_info(user_input)
