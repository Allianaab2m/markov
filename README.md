# マルコフ連鎖で文章をつくろう

## 注意事項
- この Project は `poetry` でパッケージ管理されています
  - 使わなくても多分問題ないけど，パッケージは先に入れといてね
- 生成される `model_data.json` はクソ重いので開くときは注意
  - 俺の nvim はこれで落ちました（クソ）

## Step 1 適当に文章データを取ってくる

```
echo '取ってきたやつ' >> ./data.txt
```

## Step 2 スクリプト群を実行して辞書データを作る

```
(venv) python main.py  // data.txt から new_data.txt を生成
(venv) python make_dictionary.py // new_data.txt から model_data.json を生成
```

## Step 3 Have fun!
```
(venv) python tweet.py
```

