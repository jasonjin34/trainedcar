f = open('cars.info', 'w+')
fbg = open('bg.txt', 'w+')

for i in range(550):
    f.write('pos/pos-' + str(i) + '.pgm 1 0 0 100 40\n')

for i in range(8144):
    temp_i = i + 1
    temp_i_len = len(str(temp_i))
    temp_str = ''
    
    for i in range(5 - temp_i_len):
        temp_str = temp_str + '0'

    temp_str = temp_str + str(temp_i)
    f.write('pos/' + temp_str + '.jpg 1 0 0 100 40\n')

for i in range(514):
    fbg.write('neg/neg-' + str(i) + '.pgm\n')
