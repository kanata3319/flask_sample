# flask_sample
## Python+flask Project

### サーバ起動
```
python run.py
```

### Migrete
#### 初期化
```
flask db init
```
#### migrations/env.pyにmodelのimportを追加
```
from models.models import *
```
#### migrationファイル作成
```
flask db migrate
```
#### migration実行
```
flask db upgrade
```