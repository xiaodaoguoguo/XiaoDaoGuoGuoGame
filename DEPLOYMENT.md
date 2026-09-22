# 部署与发布完整指南

本文档详细说明如何将项目部署到GitHub并通过GitHub Actions自动构建发布APK。

## 📋 准备工作

### 1. 安装必要工具

- **Git**: https://git-scm.com/downloads
- **JDK 17**: https://adoptium.net/ （本地构建需要）
- **GitHub账号**: https://github.com/

### 2. 配置Git（如果还没配置）

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

## 🚀 第一步：创建GitHub仓库

### 方式A：通过GitHub网站创建

1. 登录 GitHub: https://github.com/
2. 点击右上角的 "+" → "New repository"
3. 填写仓库信息：
   - Repository name: `XiaoDaoGuoGuoGame`
   - Description: `小刀果果HTML5游戏的Android APP版本`
   - 选择 "Public"（公开仓库）
   - **不要** 勾选 "Add a README file"
   - **不要** 选择 ".gitignore" 和 "license"（项目已包含）
4. 点击 "Create repository"

## 📤 第二步：上传项目到GitHub

在项目根目录执行以下命令：

```bash
# 1. 进入项目目录
cd D:\project\XiaoDaoGuoGuoGame

# 2. 初始化Git仓库
git init

# 3. 添加所有文件
git add .

# 4. 创建首次提交
git commit -m "初始提交：小刀果果游戏Android APP"

# 5. 设置main分支
git branch -M main

# 6. 添加远程仓库（替换'xiaodaoguoguo'为你的用户名）
git remote add origin https://github.com/xiaodaoguoguo/XiaoDaoGuoGuoGame.git

# 7. 推送到GitHub
git push -u origin main
```

**如果推送失败**，可能需要配置GitHub认证：

```bash
# 方式1：使用GitHub CLI
gh auth login

# 方式2：使用Personal Access Token
# 在 https://github.com/settings/tokens 生成token
# 推送时使用token作为密码
```

## 🏷️ 第三步：创建Release发布

### 方式A：自动创建（推荐）

```bash
# 1. 创建Tag
git tag -a v1.0.0 -m "Release version 1.0.0"

# 2. 推送Tag到GitHub
git push origin v1.0.0

# 3. 等待GitHub Actions自动构建并发布（5-10分钟）
```

GitHub Actions会自动：
1. 构建Debug和Release版本的APK
2. 创建GitHub Release
3. 将APK文件上传到Release页面

### 方式B：手动创建

1. 等待GitHub Actions构建完成
2. 访问仓库的 "Releases" 页面
3. 点击 "Create a new release"
4. 填写信息：
   - Tag version: `v1.0.0`
   - Release title: `小刀果果游戏 v1.0.0`
   - Description: 填写更新说明
5. 从Actions下载APK并上传
6. 点击 "Publish release"

## 📥 分享下载链接

Release创建成功后，分享以下链接：

```
https://github.com/xiaodaoguoguo/XiaoDaoGuoGuoGame/releases
```

## 🔄 日常更新流程

### 修改代码后发布新版本

```bash
# 1. 修改代码后提交
git add .
git commit -m "修复：描述你的修改"
git push

# 2. 创建新版本Tag
git tag -a v1.0.1 -m "Release version 1.0.1"
git push origin v1.0.1

# 3. GitHub Actions自动构建并发布
```

### 版本号规范

遵循语义化版本（Semver）：`主版本.次版本.修订号`

- **主版本号**: 重大更新，不向下兼容
- **次版本号**: 新增功能，向下兼容
- **修订号**: Bug修复

例如：
- `v1.0.0` - 首次发布
- `v1.0.1` - 修复Bug
- `v1.1.0` - 新增功能
- `v2.0.0` - 重大更新

同时更新 `app/build.gradle` 中的版本：

```gradle
defaultConfig {
    versionCode 2        // 每次发布递增
    versionName "1.0.1"  // 对应Tag版本
}
```

## 🛠️ 本地测试构建

在推送到GitHub之前，建议先在本地测试构建：

### Windows

```bash
gradlew.bat clean
gradlew.bat assembleDebug
```

### Linux/Mac

```bash
chmod +x gradlew
./gradlew clean
./gradlew assembleDebug
```

构建成功后APK位于：
```
app/build/outputs/apk/debug/app-debug.apk
```

## 🔐 签名APK（可选）

### 为什么需要签名？

- 无签名APK可以安装和使用
- 签名APK更专业，适合正式发布
- 应用商店要求必须使用签名APK

### 生成密钥库

```bash
keytool -genkey -v -keystore keystore.jks -keyalg RSA -keysize 2048 -validity 10000 -alias xiaodaoguoguo-key
```

按提示输入密码和信息。

### 配置签名

编辑 `app/build.gradle`，在 `android` 块中添加：

```gradle
android {
    signingConfigs {
        release {
            storeFile file("../keystore.jks")
            storePassword "你的密码"
            keyAlias "xiaodaoguoguo-key"
            keyPassword "你的密码"
        }
    }

    buildTypes {
        release {
            signingConfig signingConfigs.release
            minifyEnabled true
            shrinkResources true
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}
```

### 构建签名APK

```bash
./gradlew assembleRelease
```

**重要**: 
- 将 `keystore.jks` 添加到 `.gitignore`
- **不要** 将密钥库提交到Git仓库
- 妥善保管密钥库和密码

## ✅ 发布检查清单

发布前确认：

- [ ] 代码已推送到GitHub
- [ ] GitHub Actions构建成功
- [ ] APK文件可以正常下载
- [ ] 在真机上测试安装和运行
- [ ] 游戏加载正常
- [ ] 所有功能测试通过
- [ ] README.md中的下载链接已更新
- [ ] Release说明已填写

## 📞 获取帮助

如果遇到问题：

1. 查看GitHub Actions构建日志
2. 在仓库中创建Issue
3. 查看Android开发文档: https://developer.android.com/

---

**祝发布顺利！** 🎉
