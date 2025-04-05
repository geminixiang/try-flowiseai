![Image](https://github.com/user-attachments/assets/c7776a56-7ff7-4408-a817-a4e52d50a3fa)

### 啟動
```shell
docker compose up -d
```

### 後台
http://localhost:3965/

帳密
```shell
your-username / your-username
```

### 腳本測試

```shell
uv sync
uv run main.py
```

### 預期成果
```
❯ uv run main.py
{'text': '四月份最高的單筆消費是在 4 月 11 號於台北的 Costco，金額為 11,250 元。', 'usedTools': [{'tool': 'april_expense_record', 'toolInput': {'input': 'highest single expense'}, 'toolOutput': 'date: 04/11\nlocation: taipei\nstore: Costco\nprice: 11250\n_0: \n_1: \n_2: \n_3: \n_4: \n_5: \n\ndate: 04/15\nlocation: taipei\nstore: 飯店\nprice: 3250\n_0: \n_1: \n_2: \n_3: \n_4: \n_5: \n\ndate: 04/15\nlocation: taipei\nstore: 7-11\nprice: 25\n_0: \n_1: \n_2: \n_3: \n_4: \n_5: \n\ndate: \nlocation: \nstore: \nprice: \n_0: \n_1: \n_2: \n_3: \n_4: \n_5: '}], 'question': '請問四月份最高的單筆消費是?', 'chatId': '36441915-a75a-4471-872a-036517b59d39', 'chatMessageId': '76eef61d-dae3-4ede-9d70-c14b64c427f2', 'isStreamValid': False, 'sessionId': '36441915-a75a-4471-872a-036517b59d39', 'memoryType': 'Buffer Memory'}
```
