import os, sys

def convert(folder):
    for d, ds, fs in os.walk(folder):
        for fname in fs:
            if fname[-4:] != '.lab':
                continue
            fullfname = d + '/' + fname
            phone_array = []
            time_array = []
            fr = open(fullfname)
            for line in fr:
                if line.split('\n')[0] == '#':
                   continue
                [s, e, p] = line.rstrip('\n').split()
                time_array.append(s)
                phone_array.append(p)               
            fw = open(fullfname[:-4] + '.dur', 'w')
            i = 0
            for line in range(0, len(time_array) -1):
              try:
                print i
                current_time = time_array[i]
                next_time = time_array[i+1]
                phone = phone_array[i]
                s_ns = float(float(current_time)*16000 )
                e_ns = float(float(next_time)*16000 )
                dur = str(float((e_ns - s_ns)/16))
                fw.write( phone + ' ' + dur + '\n')
                i = i + 1
              except IndexError:
                pass
            fr.close()
            fw.close()
            print "Converted", fullfname


if __name__ == '__main__':
    folder = '../lab'
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    print "Converting and accomodating the dictionary", folder
    convert(folder)
