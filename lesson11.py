#第11回 最も身近なオープンデータ「郵便番号データベース」を活用しよう

# -*- coding: utf-8 -*-

#コマンドラインの引数を取得
import sys

#argvには0番目の要素にプログラムファイル名が、以降の要素にコマンドライン引数の値が設定されています
if len(sys.argv) <= 1 :
    print("以下のように入力してください")
    print("python findzip.py (住所)")
    exit()
    
#空白文字と改行除去
add = sys.argv[1].strip()

fp = open('KEN_ALL.CSV', 'rt', encoding = 'shift_jis')

for line in fp:
    line = line.replace(' ', '')
    line = line.replace('"', '')
    cells = line.split(",")
    zipno = cells[2] # 郵便番号
    ken = cells[6] # 都道府県
    shi = cells[7] # 市区
    cho = cells[8] # 市区以下
    title = ken + shi + cho
    if title.find(add) >= 0:
        print(title + 'の郵便番号 : ' + zipno)
fp.close()

