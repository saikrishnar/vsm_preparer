#! /usr/bin/python
import os

def main():
     phone_array = []
     f = open('../dictionary/vectors.txt')
     for line in f:
         phone = line.split(' ')[0]
         phone_array.append(phone)
     f.close()
     vsm_array = []
     f = open('../dictionary/representation.txt')
     for line in f:
          representation = line.strip('\n')      
          vsm_array.append(representation)
     f.close()
     print phone_array     
     f = open('../lab/tel.quindur')
     g = open('../lab/tel_vsm.quindur','w')
     i = 0
     for line in f:
       try:
         chars = line.split(' ')
         dur = line.strip('\n').split(' ')[0]
         vsm = ' ' 
         print i 
         j = 0
         for phone in chars:
              if j == 0:
                  pass
              
              elif phone == '\n':
                  pass
              else:
                  phone = phone.strip('\n').split()[0]
                  print phone
                  phone_index = phone_array.index(phone)
                  vsm = vsm + vsm_array[phone_index]
              j = j  + 1
         g.write(phone  + ' ' + dur + ' ' + vsm + '\n')              
         i = i + 1
       except ValueError:
         pass        
 


if __name__ == '__main__':
    main()
