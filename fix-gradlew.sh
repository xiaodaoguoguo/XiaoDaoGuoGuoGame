#!/bin/bash

# 修复gradlew文件的换行符问题
# 将Windows格式(CRLF)转换为Unix格式(LF)

echo "正在修复gradlew文件..."

# 检查是否存在gradlew文件
if [ ! -f "gradlew" ]; then
    echo "错误: 找不到gradlew文件"
    exit 1
fi

# 转换换行符
dos2unix gradlew 2>/dev/null || sed -i 's/\r$//' gradlew

# 设置执行权限
chmod +x gradlew

echo "修复完成！"
echo "请重新提交并推送:"
echo "  git add gradlew"
echo "  git commit -m \"修复gradlew换行符问题\""
echo "  git push origin main"
