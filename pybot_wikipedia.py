import wikipedia # ライブラリーをインポート

def wikipedia_command(command):
    cmd, keyword = command.split(maxsplit=1) # maxsplitで最大分割回数を指定
    wikipedia.set_lang('ja') # 対象となるwikipediaの言語を日本語に設定
    try:
        page = wikipedia.page(keyword) # wikipedia.page()関数にキーワードを指定し、ページの情報を取得
        title = page.title
        summary = page.summary
        response = f'タイトル: {title}\n{summary}'
    except wikipedia.exceptions.PageError:
        response = f'「{keyword}」の意味が見つかりません'
    return response
