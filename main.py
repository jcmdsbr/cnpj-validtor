def format_document(document: str):
    return ''.join(e for e in document.strip() if e.isalnum())


def cnpj_validator(cnpj: str):
    mult_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    mult_2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    document = format_document(cnpj)

    if len(document) != 14:
        return False
    temp_doc = document[0:12]
    sum_result = 0

    for i in range(12):
        sum_result += int(temp_doc[i]) * mult_1[i]

    result = sum_result % 11

    if result < 2:
        result = 0
    else:
        result = 11 - result

    digit = str(result)
    temp_doc = temp_doc + digit

    sum_result = 0

    for i in range(13):
        sum_result += int(temp_doc[i]) * mult_2[i]

    result = sum_result % 11

    if result < 2:
        result = 0
    else:
        result = 11 - result

    digit = digit + str(result)

    return cnpj.endswith(digit)


cnpj = '13.057.257/0001-21'

print(cnpj_validator(cnpj))
