def repairMap(file_name):
    with open(file_name, 'r') as Read:
        distorted = Read.readlines()

    if len(distorted) != 1:
        row_start = []
        for i in range(len(distorted)):
            if distorted[i][0] == "[":
                row_start.append(i)
        row_start.append(len(distorted))
        true_form = []
        for i in range(len(row_start)-1):
            true_form.append(str(distorted[row_start[i]:row_start[i+1]]))
        fixed = true_form
        for i in range(len(fixed)):
            fixed[i] = fixed[i].split()
            for j in range(len(fixed[i])):
                fixed[i][j] = fixed[i][j].strip("[.]\n',\\n")
                if fixed[i][j] == "":
                    continue
                fixed[i][j] = int(fixed[i][j])

    else:
        distorted = (str(distorted))
        distorted = distorted[1:-1]
        fixed = distorted[1:-1]
        fixed = eval(fixed)
        for i in range(len(fixed)):
            for j in range(len(fixed[i])):
                fixed[i][j] = int(fixed[i][j])

    for i in range(len(fixed)):
        for j in range(len(fixed[i])):
            if fixed[i][j] == '':
                fixed[i] = fixed[i][:j] + fixed[i][j+1:]
                fixed[i].append("")
        while fixed[i][-1] == "":
            fixed[i] = fixed[i][:-1]

    return fixed
