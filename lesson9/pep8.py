# выровнено по открывающему разделителю
# foo = long_function_name(var_one, var_two,
#                          var_three, var_four)

# больше отступов включено для отличения его от остальных
def long_function_name(var_one, var_two, var_three,
                       var_four):
    print(var_one)


with open("path/read") as file_1, \
     open("path/write", "w") as file_2:
     file_2.write(file_1.read())

# import os стандартные библиотеки
# import сторонней библиотеки
# import модуля проекта
