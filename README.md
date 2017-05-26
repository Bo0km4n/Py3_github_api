# github api issues

### import libarary
`pip install PyGithub`

### sample code

```py3:
from github import Github

g = Github("user", "password")

for repo in g.get_user().get_repos():
    print repo.name
    repo.edit(has_wiki=False)
```

### Githubオブジェクトの仕様
基本的に最初にGithubオブジェクトを作成し、そこからリポジトリの情報や各種サービスの情報を取得、
POSTやPUTといった処理を行うという流れ

### ライブラリのリファレンス
http://pygithub.readthedocs.io/en/latest/introduction.html
