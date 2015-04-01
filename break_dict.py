from itertools import islice

with open('cltk_latin_pos_dict.txt') as f:
    whole_dict = eval(f.read())

def chunks(data, size=40000):
    # http://stackoverflow.com/a/22878842
    it = iter(data)
    for i in range(0, len(data), size):
        file_counter = i + 1
        file_name = 'pos_lemma_' + str(file_counter) + '.py'
        print(file_name)
        new_dict = {k:data[k] for k in islice(it, size)}
        #with open(file_name, 'w') as f:
        #    f.write(str(new_dict))

if __name__ == '__main__':
    chunks(whole_dict)