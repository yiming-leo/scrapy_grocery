import random

# 日语五十音图
hiragana_list = ['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ', 'た', 'ち',
                 'つ', 'て', 'と', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ひ', 'ふ', 'へ', 'ほ', 'ま', 'み', 'む', 'め',
                 'も', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん']
katakana_list = ['ア', 'イ', 'ウ', 'エ', 'オ', 'カ', 'キ', 'ク', 'ケ', 'コ', 'サ', 'シ', 'ス', 'セ', 'ソ', 'タ', 'チ',
                 'ツ', 'テ', 'ト', 'ナ', 'ニ', 'ヌ', 'ネ', 'ノ', 'ハ', 'ヒ', 'フ', 'ヘ', 'ホ', 'マ', 'ミ', 'ム', 'メ',
                 'モ', 'ヤ', 'ユ', 'ヨ', 'ラ', 'リ', 'ル', 'レ', 'ロ', 'ワ', 'ヲ', 'ン']
romaaji_list = ['a', 'i', 'u', 'e', 'o', 'ka', 'ki', 'ku', 'ke', 'ko', 'sa', 'shi', 'su', 'se', 'so', 'ta', 'chi',
                'tsu', 'te', 'to', 'na', 'ni', 'nu', 'ne', 'no', 'ha', 'hi', 'fu', 'he', 'ho', 'ma', 'mi', 'mu', 'me',
                'mo', 'ya', 'yu', 'yo', 'ra', 'ri', 'ru', 're', 'ro', 'wa', 'wo', 'n']

# 将列表打包为字典的列表
five_ten_dict_list = [{'hiragana': h, 'katakana': k, 'romaaji': r} for h, k, r in
                      zip(hiragana_list, katakana_list, romaaji_list)]

mode_result = input("choose mode: 1:hiragana 2:katakana 3:romaaji  : ")
if mode_result == '1':
    while True:
        choice_result = random.choice(five_ten_dict_list)
        print(f"hiragana: {choice_result['hiragana']}")

        while True:
            romaaji_input = input("romaaji: ")
            if romaaji_input == '':
                print(f"× {choice_result['romaaji']} {choice_result['hiragana']} {choice_result['katakana']}")
                break
            if romaaji_input == choice_result['romaaji']:
                print(f"√ {choice_result['romaaji']} {choice_result['hiragana']} {choice_result['katakana']}")
                break

elif mode_result == '2':
    while True:
        choice_result = random.choice(five_ten_dict_list)
        print(f"katakana: {choice_result['katakana']}")

        while True:
            romaaji_input = input("romaaji: ")
            if romaaji_input == '':
                print(f"× {choice_result['romaaji']} {choice_result['hiragana']} {choice_result['katakana']}")
                break
            if romaaji_input == choice_result['romaaji']:
                print(f"√ {choice_result['romaaji']} {choice_result['hiragana']} {choice_result['katakana']}")
                break

elif mode_result == '3':
    while True:
        choice_result = random.choice(five_ten_dict_list)
        print(f"romaaji: {choice_result['romaaji']}")

        while True:
            hiragana_input = input("hiragana: ")
            if hiragana_input == '':
                print(f"× {choice_result['romaaji']} {choice_result['hiragana']} {choice_result['katakana']}")
                break
            if hiragana_input == choice_result['hiragana']:
                print(f"√ {choice_result['romaaji']} {choice_result['hiragana']} {choice_result['katakana']}")
                break

        while True:
            katakana_input = input("katakana: ")
            if katakana_input == '':
                print(f"× {choice_result['romaaji']} {choice_result['hiragana']} {choice_result['katakana']}")
                break
            if katakana_input == choice_result['katakana']:
                print(f"√ {choice_result['romaaji']} {choice_result['hiragana']} {choice_result['katakana']}")
                break
