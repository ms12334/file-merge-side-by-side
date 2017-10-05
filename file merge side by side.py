finame1 = 'source1.txt'
finame2 = 'source2.txt'
foname = 'result.log'

count = 1

with open(finame1) as fin1, open(finame2) as fin2:
    with open(foname,'a') as fout:
        for line1 in fin1:  # Loop through lines in fin1 as base
            line1 = line1.strip()
            line2 = fin2.readline().strip()
            if line2 != "":
                fout.write('Line ' + str(count) + ': ' + '<' + finame1 + '>' + line1 + '\t' + '<' + finame2 + '>' + line2 + '\n')
                count = count + 1
            else:
                fout.write('Line ' + str(count) + ': ' + '<' + finame1 + '>' + line1 + '\n')
                count = count + 1
        for line2 in fin2:  # print the rest of fin2 when fin2 is begger than fin1
            line2 = line2.strip()
            fout.write('Line ' + str(count) + ': ' + '<' + finame2 + '>' + line2 + '\n')
            count = count + 1

fin1.close()
fin2.close()
fout.close()
