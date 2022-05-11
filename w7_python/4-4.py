from googletrans import Translator

translator = Translator()

sentence = "안녕하세요 코드라이언입니다."

result = translator.translate(sentence,'en')
print(result)