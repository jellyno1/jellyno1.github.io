import json
from datetime import date

# 写入日记内容
entry_date = input("请输入日期 (YYYY-MM-DD): ")
entry_title = input("请输入标题: ")
entry_content = input("请输入正文: ")

with open("diary.json", "r", encoding="utf-8") as f:
    data = json.load(f)

data[entry_date] = {
    "title": entry_title,
    "content": entry_content
}

with open("diary.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ 日记 {entry_date} 添加成功！")
