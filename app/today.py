import oseti
import sys, codecs, io

print("今日の気分を入力してください")
kibun = input()

analyzer = oseti.Analyzer()
analized_kibun = analyzer.analyze(kibun)

score_for_today = analized_kibun[0]
if score_for_today >= 1.0:
    print("楽しそうで良かったです！")

elif score_for_today < 0.0:
    print("猫画像をどうぞ！")

else:
    print("良い日が続きますように。Have a nice day!")