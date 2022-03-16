def eto_command(command): # 関数にする
    eto, year_str = command.split() # 年を取得
    year = int(year_str)
    number_of_eto = (year + 8) % 12
    eto_tuple = ('子', '丑', '寅', '卯', '辰', '巳', '午', '末', '申', '酉', '戌', '亥',)
    eto_name = eto_tuple[number_of_eto]
    response = f'{year}年生マレノ干支ハ「{eto_name}」デス。'
    return response
