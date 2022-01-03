# JSON:javascript object notation.とくにwebでのデータ送受信によく使われる
# jsonモジュールを使う
import json

# json.load(f)：jsonファイルをpythonのデータ構造で読み込み
with open('example.json') as f:
    data = json.load(f)

print(data['glossary']['GlossDiv'])

# json.dump：pythonのデータ構造をjsonファイルに書き込み
new_json = {'key1': 'value1', 'key2': (1, 'value2')}
with open('new_json.json', 'w') as f:
    json.dump(new_json, f)

with open('new_json.json', 'r') as f:
    new_json_reload = json.load(f)

print(new_json_reload['key2'])

# json.dumps：pythonのデータ構造をjson文字列に変換
json_str = json.dumps(new_json)
print(type(json_str))

# json.loads：json文字列をpythonのデータ構造に変換
python_data = json.loads(json_str)
print(python_data)
print(type(python_data))