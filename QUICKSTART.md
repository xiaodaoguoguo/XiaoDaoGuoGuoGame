# ⚡ 快速开始指南

完全没有Android开发经验？没关系！跟着这个5步指南，20分钟内完成发布。

## 📝 第一步：检查文件

你的项目现在在 `D:\project\XiaoDaoGuoGuoGame\`，包含以下内容：

```
XiaoDaoGuoGuoGame/
├── app/                 # 应用代码
├── .github/            # GitHub Actions配置
├── build.gradle        # 构建配置
├── settings.gradle     # 项目设置
├── README.md           # 说明文档
└── 各种文档和配置文件
```

## 🔑 第二步：创建GitHub仓库

### 方法1：网页操作（推荐新手）

1. 打开 https://github.com/ 并登录
2. 点击右上角 `+` → `New repository`
3. 填写：
   - Repository name: `XiaoDaoGuoGuoGame`
   - Description: `小刀果果游戏Android版`
   - 选择 `Public`（公开）
   - 其他都不选
4. 点击 `Create repository`

## 📤 第三步：上传项目

打开命令行（CMD或PowerShell），执行：

```bash
# 进入项目目录
cd D:\project\XiaoDaoGuoGuoGame

# 依次执行以下命令
git init
git add .
git commit -m "初始提交"
git branch -M main
git remote add origin https://github.com/xiaodaoguoguo/XiaoDaoGuoGuoGame.git
git push -u origin main
```

**注意**：将 `xiaodaoguoguo` 替换为你的GitHub用户名

### 如果推送失败

第一次使用Git需要配置身份：

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

## ⏳ 第四步：等待自动构建

1. 访问你的仓库页面
2. 点击 `Actions` 标签
3. 等待5-10分钟，直到变成绿色对勾 ✅

## 🎉 第五步：创建Release发布

构建成功后：

```bash
# 在项目目录执行
git tag -a v1.0.0 -m "首次发布"
git push origin v1.0.0
```

等待5分钟，GitHub Actions会自动创建Release并上传APK。

## 📥 下载和分享

发布成功后，从这个链接下载APK：

```
https://github.com/你的用户名/XiaoDaoGuoGuoGame/releases
```

## ⚠️ 重要提示：添加APP图标

在上传到GitHub之前，你需要添加图标！

使用在线工具：https://icon.kitchen/
1. 上传你的高清图标
2. 下载生成的zip
3. 解压后将 `mipmap-*` 文件夹内容复制到：
   `D:\project\XiaoDaoGuoGuoGame\app\src\main\res\`

详细步骤查看 `ICON_GUIDE.md`

---

**准备好了？现在就开始吧！** 🚀
