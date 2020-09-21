a = "45673456877734967894055679340679340576945876"
result = str(a[0])
max_result = ""
last = str(a[0])
for i in a[1:]:
    if i == last:
        result += str(i)
        print(i, result)
    else:
        if len(result) > len(max_result):
            max_result = result
            last = i
            result = ""
    if len(result) > len(max_result):
        max_result = result
print(max_result)
