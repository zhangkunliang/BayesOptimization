with open('Thermal_conductivity.txt', 'r') as read_to_avg:
    readline = read_to_avg.readlines()
    with open('Thermal_conductivity.txt', 'w') as write_to_avg:
        sum = 0
        count = 0
        len_readline = len(readline)
        print(len_readline)
        for line in range(0, len_readline):
            len_array = len(readline[line].strip().split())
            print(len_array)
            for i in range(0, len_array):
                sum += float(readline[line].strip().split()[i])
                count += 1
        # print(count)
        res = "%1.5f" % (sum / count)
        write_to_avg.write(res)
print(30 * '-', 'Done!', 30 * '-')