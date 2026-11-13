import json
from datetime import datetime

now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
payload = {
    "msg": "这个文件由 GitHub Actions 自动生成",
    "last_run": now,
    "note": "push / 定时 / 手动点按钮都可以触发我"
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)

html = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>Auto Demo</title>
</head>
<body>
<pre>{json.dumps(payload, ensure_ascii=False, indent=2)}</pre>
</body>
</html>
"""
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
