def get_line(path):
    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        print('Cannot open " ', path, ' ", plz check. ')
    else:
        with fp:
            lines = fp.readlines()
            i = 0
            while i < len(lines):
                # I will add i manually in some cases so I will not use 'for loops'
                line = lines[i].strip()
                lineList = list(line)
                # Transfer string into list, because list can simulate stack with its method pop()
                if not lineList:
                    continue
                # I do not a emtpy sequence to show up on my final output. (This happens, think about the final line!
                # Firstly I was trying to use break, because I know it is in the end, HOWEVER, I think continue is more logical.

                while '\\' == lineList[len(line) - 1]:
                    lineList.pop()
                    # '\' is at the end of each sequence, so do you remember there is an FILO structure called stack?
                    line = "".join(lineList)
                    line += lines[i + 1].strip()
                    lineList = list(line)
                    i += 1
                    # This i += 1 is for I sticking next line with present line together, so I cannot read next line again.

                i += 1
                # I put the final 'i += 1' because if I put it in the end, it might not execute. What is more, i will not be used below.

                for j in range(len(line)):
                    if '#' == line[j]:
                        j -= 1
                        # Offsets problems, think carefully with '[0: j + 1]'. I failed here mamy times.
                        break
                if j == -1:
                    # This -1 is so important.
                    continue
                else:
                    string = str(line[0: j + 1])
                    # I have to plus 1 because it is an open set.
                    yield string
