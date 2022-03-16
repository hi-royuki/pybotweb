from pybot_eto import eto_command
from pybot_random import choice_command, dice_command
from pybot_datetime import today_command, now_command, weekday_command
from pybot_event import event_command
from pybot_wikipedia import wikipedia_command

def len_command(command):
    cmd, text = command.split()
    length = len(text)
    response = f'文字列ノ長サハ {length} 文字デス。'
    return response

def wareki_command(command):
    wareki, year_str = command.split() # 文字列を空白で分割する。
    # try:       # tryを追加し、int()関数の処理からresponseを返す前までにtry節にする
    if year_str.isdigit(): # 数値に変換可能か確認
        year = int(year_str) # 文字列を数値に変換
        if year >= 2019:
            reiwa = year - 2018
            response = f'西暦{year}年ハ、令和{reiwa}年です。'
        elif year >= 1989:
            heisei = year - 1988
            response = f'西暦{year}年ハ、平成{heisei}年です。'
        else:
            response = f'西暦{year}年ハ、平成より前です'
    # except ValueError:
    else:
        response = '数値を指定してください'
    return response # 結果を返す



command_file = open('pybot.txt', encoding='utf-8')
raw_data = command_file.read()
command_file.close()
lines = raw_data.splitlines() #　改行で分割して行ごと文字列のリストを作成します

# あいさつの辞書データの作成
bot_dict = {} #　空の辞書データの変数を用意する
for line in lines:
    word_list = line.split(',') #　１行分の文字列をカンマで2つの文字列に分割
    key = word_list[0] # 分割した文字列の0番目を辞書のキーに
    response = word_list[1] # 分割した文字列の１番目をバリューに
    bot_dict[key] = response # 辞書データに値を追加



def pybot(command):
# input関数でユーザーからの入力を受付、入力された値をcommand変数に保存
    # command = input('pybot> ')
    # print(command)
    response = '' #空文字列で初期化する
    try:
        for message in bot_dict:
            if message in command:
                response = bot_dict[message]
                break

        #　年号の計算をする和暦コマンドを作成
        if '和暦' in command: # 和暦が含まれている場合
            response = wareki_command(command)
        # 長さを取得するコマンドを作成
        if '長さ' in command:
            response = len_command(command)
        # 干支コマンドを作成
        if '干支' in command:
            response = eto_command(command)
        # 選ぶコマンドを作成
        if '選ぶ' in command:
            response = choice_command(command)
        # さいころコマンドを作成
        if 'さいころ' in command:
            response = dice_command()
        # 今日の日付コマンドの作成
        if '今日' in command:
            response = today_command()
        # 現在日時のコマンド作成
        if '現在' in command:
            response = now_command()
        # 曜日コマンド作成
        if '曜日' in command:
            response = weekday_command(command)
        # イベント検索コマンド作成
        if 'イベント' in command:
            response = event_command(command)
        #事典コマンド作成
        if '事典' in command:
            response = wikipedia_command(command)
            # year = int(year_str)
            # if year >= 2019: # 令和の範囲か
            #     reiwa = year - 2018
            #     response = f'西暦{year}年ハ、令和{reiwa}年です。'
            # elif year >= 1989:
            #     heisei = year - 1988
            #     response = f'西暦{year}年ハ、平成{heisei}年です。'
            # else:
            #     response = f'西暦{year}年ハ、平成より前です'
            #


        if not response:
            response = '何ヲ言ッテイルカ、ワカラナイ'
        return response

        # if 'さようなら' in command:
        #     break
    except Exception as e:
        print('予期せぬエラーが発生しました')
        print(f'* 種類: {type(e)}')
        print(f'* 内容; {e}')
