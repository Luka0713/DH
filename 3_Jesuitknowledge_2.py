import os
from ckiptagger import WS, POS, NER

# 数据文件的路径（假设已经提前把model download到本地）
data_path = r"C:\Users\xue_k\AppData\Local\Programs\Python\Python311\data"

# 创建分词、词性标注和命名实体识别对象
ws = WS(data_path)
pos = POS(data_path)
ner = NER(data_path)

# 输入文件夹路径
input_folder_path = r"C:\Users\xue_k\DH\input"
# 输出文件夹路径
output_folder_path = r"C:\Users\xue_k\DH\output"

# 遍历指定文件夹中的所有.txt文件
for filename in os.listdir(input_folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(input_folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 将整个文档内容按换行符分割为多个句子
        sentence_list = content.split('\n')

        # 进行分词
        word_sentence_list = ws(sentence_list)

        # 进行词性标注
        pos_sentence_list = pos(word_sentence_list)

        # 进行命名实体识别
        entity_sentence_list = ner(word_sentence_list, pos_sentence_list)

        # 输出分词结果
        def print_word_pos_sentence(word_sentence, pos_sentence, file):
            assert len(word_sentence) == len(pos_sentence)
            for word, pos in zip(word_sentence, pos_sentence):
                print(f"{word}({pos})", file=file)  # 每个词在新的一行（这里是避免文件过大时，分词结果被放在同一行输出，导致最后的.txt文档中间缺少空格）
            print(file=file)  # 句子结束后换行

        output_file_path = os.path.join(output_folder_path, os.path.splitext(filename)[0] + "_1.txt")
        with open(output_file_path, 'w', encoding='utf-8') as file:
            for i, sentence in enumerate(sentence_list):
                print(f"'{sentence}'", file=file)
                print_word_pos_sentence(word_sentence_list[i], pos_sentence_list[i], file)
                for entity in sorted(entity_sentence_list[i]):
                    print(entity, file=file)
