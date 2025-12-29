# HeartRateMonitoring

### Setup
```
sudo apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev curl git libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
curl https://pyenv.run | bash
pyenv local 3.8
```

.bashrcに以下を追加
```
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init - bash)"
eval "$(pyenv virtualenv-init -)"
```

sudo でpythonを実行するために以下編集
```
$ sudo visudo 
```

開いたファイルを以下編集して保存
```
# Defaults    secure_path = /sbin:/bin:/usr/sbin:/usr/bin  コメントアウト
Defaults    env_keep += "PATH"
Defaults    env_keep += "PYENV_ROOT"
```

openantインストール
```
pip install openant
```

### Check

以下コマンドで機器確認
```
sudo openant scan
```

### 起動

