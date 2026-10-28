# Contributing

Read [README.md](README.md) or [README.zh-CN.md](README.zh-CN.md) for the project scope. Keep changes focused and explain the observed problem, the change and how you checked it.

After configuring a disposable local database, run `python manage.py check` and the relevant Django tests. Use synthetic accounts, orders and addresses; do not test writes against a database you need to keep.

Keep the English and Chinese READMEs consistent when behavior or setup changes. Preserve third-party attribution and submit only material you have permission to share. Security and private-data reports follow [SECURITY.md](SECURITY.md).

## 中文说明

先阅读 README，说明实际问题、修改内容和验证方式，尽量让每次提交围绕同一项变更。

配置可丢弃的本地测试数据库后，运行 `python manage.py check` 及相关 Django 测试。账号、订单和地址使用虚构数据，不要对需要保留的数据库执行测试写入。

运行方式或功能变化时同步更新中英文说明。保留第三方署名，仅提交有权分享的内容；安全和私人数据问题按 [SECURITY.md](SECURITY.md) 处理。
