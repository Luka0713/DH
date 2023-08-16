from ckiptagger import data_utils
data_utils.download_data_gdown("./") # gdrive-ckip

from ckiptagger import WS, POS, NER

# 创建分词对象

data_utils.download_data_gdown("./") # gdrive-ckip

ws = WS("./data")
pos = POS("./data")
ner = NER("./data")

# 读取本地文件
file_path = r"C:\Users\xue_k\iCloudDrive\DH\database_work\《明清之际西学文本》_work\第1册\天主實錄_cleaned1.txt"
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# 将整个文档内容作为一个句子
sentence_list = [content]

# 进行分词
word_sentence_list = ws(
    sentence_list,
    # sentence_segmentation=True, # To consider delimiters
    # segment_delimiter_set={",", "。", ":", "?", "!", ";"}, # This is the default set of delimiters
    # recommend_dictionary=dictionary1, # words in this dictionary are encouraged
    # coerce_dictionary=dictionary2, # words in this dictionary are forced
)

# 进行词性标注
pos_sentence_list = pos(word_sentence_list)

# 进行命名实体识别
entity_sentence_list = ner(word_sentence_list, pos_sentence_list)


# 输出分词结果
def print_word_pos_sentence(word_sentence, pos_sentence, file):
    assert len(word_sentence) == len(pos_sentence)
    for word, pos in zip(word_sentence, pos_sentence):
        print(f"{word}({pos})", end="\u3000", file=file)
    print(file=file)
    return

output_file_path = r"c:\Users\xue_k\iCloudDrive\DH\output\2"
with open(output_file_path, 'w', encoding='utf-8') as file:
    for i, sentence in enumerate(sentence_list):
        print(file=file)
        print(f"'{sentence}'", file=file)
        print_word_pos_sentence(word_sentence_list[i], pos_sentence_list[i], file)
        for entity in sorted(entity_sentence_list[i]):
            print(entity, file=file)