#! /usr/bin/python
import os

def main(folder):
     #vectors = [] 
     #f = open('../dictionary/vectors.txt')
     #for line in f:
     #    representation = line.strip('\n')
     #    vectors.append(representation)
     #f.close()
     for d, ds, fs in os.walk(folder):
        for fname in fs:
            if fname[-4:] != '.dur':
                continue
            fullfname = d + '/' + fname
            phone_array = []
            dur_array = []
            fr = open(fullfname)
            for line in fr:
                if line.split('\n')[0] == '#':
                   continue
                [phone, dur] = line.rstrip('\n').split()
                phone_array.append(phone)
                dur_array.append(dur)
            fw = open(fullfname[:-4] + '.quindur', 'w')
            for i in range(2, len(dur_array) - 2 ): 
                     phoneme_2p = phone_array[i-2]
                     #phoneme_2p_index = uniquephone_list.index(phoneme_2p)

                     phoneme_1p = phone_array[i-1]
                     #phoneme_1p_index = uniquephone_list.index(phoneme_1p)

                     phoneme = phone_array[i]
                     #phoneme_index = uniquephone_list.index(phoneme)

                     phoneme_1n = phone_array[i+1]
                     #phoneme_1n_index = uniquephone_list.index(phoneme_1n)

                     phoneme_2n = phone_array[i+2]
                     #phoneme_2n_index = uniquephone_list.index(phoneme_2n)

                     duration = dur_array[i]
                     fw.write( str(float(duration)) + ' ' + phoneme_2p + ' ' + phoneme_1p + ' ' + phoneme + ' ' + phoneme_1n + ' ' + phoneme_2n + '\n')
            fw.close()
            fr.close()


if __name__ == '__main__':
    folder = '../lab'
    main(folder)
