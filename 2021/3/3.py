def get_decimal(binary_list):
    num = 0
    for b in binary_list:
        num = 2 * num + b
    return num


input_file_path = str(input())
diagnostic_report = []

with open(input_file_path, "r") as f:
    content = f.readlines()
    for line in content:
        diagnostic_report.append(line)
# assert len(diagnostic_report) == 12
assert len(diagnostic_report) == len(content)

mega_binary_list = []
for i in range(12):
    count_1 = 0
    count_0 = 0
    for number in diagnostic_report:
        if number[i] == "1":
            count_1 += 1
        else:
            count_0 += 1
    if count_0 > count_1:
        mega_binary_list.append(0)
    else:
        mega_binary_list.append(1)

epsilon_binary_list = []
for bit in mega_binary_list:
    epsilon_binary_list.append(1 if bit == 0 else 0)

mega_report = get_decimal(mega_binary_list)
epsilon_report = get_decimal(epsilon_binary_list)
power_consumption = mega_report * epsilon_report
print(mega_report)
print(mega_binary_list)
print(epsilon_report)
print(epsilon_binary_list)
print(power_consumption)
