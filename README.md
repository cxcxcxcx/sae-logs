# sae-logs
利用 Python 脚本下载 SAE 日志。用 goaccess 分析日志文件。

```
 python get_sae_logs.py --appname=SAE应用名 --from_date=20150626 --to_date=20150626 --secret_key=密钥
```

SAE 的日志可用如下 goaccess 命令分析：
```
goaccess  --log-format='%^ %h %^ %T [%d:%t %^] %^ %^ %^ %m %U %H %s %b "%R" "%u" %^' --date-format='%d/%b/%Y' --time-format='%H:%M:%S' -a
```
