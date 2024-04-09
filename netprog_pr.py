
def parse_string_to_dict(query_string, delimiter1, delimiter2):
    result_dict = {}
    pairs = query_string.split(delimiter1)
    for pair in pairs:
        try:
            key, value = pair.split(delimiter2)
            result_dict[key] = value
        except ValueError:
            print(f"잘못된 형식이 포함되어 있습니다: {pair}")
            continue
    return result_dict

query_string = input("쿼리를 입력해주세요: ")
parsed_dict = parse_string_to_dict(query_string, '&', '=')

print("\n문자열을 딕셔너리로 변환한 결과:")
print(parsed_dict)
