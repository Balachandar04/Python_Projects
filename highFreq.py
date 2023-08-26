# def large_freq(str1):

#     dict1 = {}
#     for i in str1:
#         if i in dict1:
#             dict1[i] += 1
#         else:
#             dict1[i] = 1
#     dict1.pop(' ')
#     max_char = None
#     max_freq = 0
#     for x in dict1:
#         max_char, max_freq = (x, dict1.get(
#             x)) if dict1.get(x) >= max_freq else (max_char, max_freq)
#     return max_char


# print(large_freq("I am a barbie girl in the barbie world"))

# method 2

def max_freq(str1: str) -> chr:
    dict1 = {}

    for i in str1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1

    dict1.pop(' ')

    freq_char = sorted(dict1.items(), key=lambda kv: kv[1], reverse=True)
    max_val = freq_char[1][1]
    return list(filter(lambda val: val[1] == max_val, freq_char))


print(max_freq("I am a barbie girl in the barbie world"))
