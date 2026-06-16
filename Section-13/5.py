from translate import Translator

translator = Translator(to_lang="ja")

try:
    with open('./sample.txt', mode='r') as myfile:
        text = myfile.read()
        translation = translator.translate(text)
        print(translation)
        with open('./test-ja.txt', mode='w', encoding='utf-8') as myfile2:
            myfile2.write(translation)
except FileNotFoundError as e:
    print("File not found")
