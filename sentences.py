import os
import jieba


def load_data(path, ban_stop_words=False, stop_words_path='', add_words=False, add_words_path=''):
    data = []
    names = []
    stop_words = set()
    stop_txt = os.listdir(stop_words_path)
    for file in stop_txt:
        with open(stop_words_path + '/' + file, 'r', encoding='ANSI') as f:
            for j in f.readlines():
                stop_words.add(j.strip('\n'))
    replace = '[a-zA-Z0-9’!"#$%&\'()（）；：‘“？、》。《，*+,-./:：;「<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+\n\u3000 '

    add_txt = os.listdir(add_words_path)
    if add_words:
        for file in add_txt:
            with open(add_words_path + '/' + file, 'r', encoding='ANSI') as f:
                for j in f.readlines():
                    jieba.add_word(j.strip('\n'))

    files = os.listdir(path)
    for file in files:
        with open(path + '/' + file, 'r', encoding='ANSI') as f:
            t = f.read()
            for i in replace:
                t = t.replace(i, '')

            c = jieba.lcut(t)
            if ban_stop_words:
                for i in range(len(c)-1, -1, -1):
                    if c[i] in stop_words:
                        del c[i]
            data.append(c)
        f.close()
        print("{} loaded".format(file))
        names.append(file.split(".txt")[0])
    return data, names


if __name__ == '__main__':
    ban_stop_words = True
    add_words = True
    data, text_names = load_data("./data", ban_stop_words, "./stop", add_words, './words')
    text_num = len(data)

    with open('./sentences.txt', 'w', encoding='utf-8') as f:
        for i in range(len(text_names)):
            for j in data[i]:
                f.write(j)
                f.write(' ')
            f.write('\n')

