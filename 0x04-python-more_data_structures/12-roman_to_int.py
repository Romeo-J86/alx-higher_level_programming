#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    answer = 0
    i = 0
    while (i < len(roman_string)):
        if roman_string[i] == "I":
            if i != len(roman_string) - 1:
                if roman_string[i + 1] == "I":
                    answer += 2
                    i += 2
                    continue
                elif roman_string[i + 1] == "V":
                    answer += 4
                    i += 2
                    continue
                elif roman_string[i + 1] == "X":
                    answer += 9
                    i += 2
                    continue
                else:
                    answer += 1
            else:
                answer += 1
        elif roman_string[i] == "V":
            answer += 5
        elif roman_string[i] == "X":
            if i != len(roman_string) - 1:
                if roman_string[i + 1] == "L":
                    answer += 40
                    i += 2
                    continue
                elif roman_string[i + 1] == "C":
                    answer += 90
                    i += 2
                    continue
                else:
                    answer += 10
            else:
                answer += 10
        elif roman_string[i] == "L":
            answer += 50
        elif roman_string[i] == "C":
            if i != len(roman_string) - 1:
                if roman_string[i + 1] == "D":
                    answer += 400
                    i += 2
                    continue
                elif roman_string[i + 1] == "M":
                    answer += 900
                    i += 2
                    continue
                else:
                    answer += 100
            else:
                answer += 100
        elif roman_string[i] == "D":
            answer += 500
        elif roman_string[i] == "M":
            answer += 1000
        else:
            return 0
        i += 1
    return answer
