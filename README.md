# 小刀果果游戏 Android APP

一个基于WebView封装的HTML5游戏Android应用，加载并运行托管在GitHub Pages上的游戏。

## 📱 功能特性

- ✅ **在线加载游戏** - 通过WebView加载 https://xiaodaoguoguo.github.io/xdg/
- ✅ **全屏沉浸式体验** - 隐藏状态栏和导航栏，提供完整游戏视图
- ✅ **返回键双击退出** - 防止误触，2秒内双击返回键退出游戏
- ✅ **屏幕常亮** - 游戏过程中保持屏幕不熄灭
- ✅ **支持横竖屏** - 自动适配不同屏幕方向
- ✅ **加载指示器** - 友好的加载进度提示
- ✅ **网络错误处理** - 网络异常时显示错误页面并支持重试

## 📥 下载安装

### 方式一：直接下载APK（推荐）

1. 访问 [Releases页面](https://github.com/xiaodaoguoguo/XiaoDaoGuoGuoGame/releases)
2. 下载最新版本的 `app-debug.apk` 文件
3. 在Android设备上安装APK（需要开启"允许安装未知来源应用"）

### 方式二：自己构建

详见下方"开发者指南"部分。

## 🎮 使用说明

1. 打开APP后会自动加载游戏
2. 游戏需要网络连接才能正常运行
3. 首次加载可能需要几秒时间
4. 按返回键可以返回上一页，在首页时双击退出

## 🛠️ 技术栈

- **开发语言**: Java
- **最低Android版本**: Android 5.0 (API 21)
- **目标Android版本**: Android 14 (API 34)
- **核心组件**: WebView
- **构建工具**: Gradle 8.0
- **CI/CD**: GitHub Actions

## 📂 项目结构

```
XiaoDaoGuoGuoGame/
├── .github/
│   └── workflows/
│       └── build.yml           # GitHub Actions自动构建配置
├── app/
│   ├── src/
│   │   └── main/
│   │       ├── java/com/xiaodaoguoguo/game/
│   │       │   └── MainActivity.java    # 主Activity
│   │       ├── res/
│   │       │   ├── layout/
│   │       │   │   └── activity_main.xml
│   │       │   ├── values/
│   │       │   │   ├── colors.xml
│   │       │   │   ├── strings.xml
│   │       │   │   └── themes.xml
│   │       │   └── mipmap-*/          # 应用图标
│   │       └── AndroidManifest.xml    # 应用清单
│   ├── build.gradle                   # 应用级Gradle配置
│   └── proguard-rules.pro            # 代码混淆规则
├── build.gradle                       # 项目级Gradle配置
├── settings.gradle                    # Gradle设置
├── gradle.properties                  # Gradle属性
└── README.md                          # 本文件
```

## 👨‍💻 开发者指南

### 环境要求

- JDK 17 或更高版本
- Android Studio 2022.3.1 或更高版本（可选，用于IDE开发）
- Git

### 克隆项目

```bash
git clone https://github.com/xiaodaoguoguo/XiaoDaoGuoGuoGame.git
cd XiaoDaoGuoGuoGame
```

### 本地构建

#### 方式一：使用命令行（推荐）

```bash
# Windows
gradlew.bat assembleDebug

# Linux/Mac
chmod +x gradlew
./gradlew assembleDebug
```

构建完成后，APK文件位于：
`app/build/outputs/apk/debug/app-debug.apk`

#### 方式二：使用Android Studio

1. 用Android Studio打开项目
2. 等待Gradle同步完成
3. 点击菜单 Build → Build Bundle(s) / APK(s) → Build APK(s)
4. 构建完成后点击通知中的"locate"查看APK

### 修改游戏URL

编辑 `app/src/main/java/com/xiaodaoguoguo/game/MainActivity.java`：

```java
private static final String GAME_URL = "你的游戏URL";
```

### 修改APP名称

编辑 `app/src/main/res/values/strings.xml`：

```xml
<string name="app_name">你的APP名称</string>
```

### 替换APP图标

你需要准备以下尺寸的图标（PNG格式）：

- mipmap-mdpi: 48x48
- mipmap-hdpi: 72x72
- mipmap-xhdpi: 96x96
- mipmap-xxhdpi: 144x144
- mipmap-xxxhdpi: 192x192

将图标文件命名为 `ic_launcher.png` 和 `ic_launcher_foreground.png`，放置到对应的 `mipmap-*` 文件夹中。

推荐使用在线工具生成：
- https://romannurik.github.io/AndroidAssetStudio/icons-launcher.html
- https://icon.kitchen/

### 生成签名APK

1. 生成密钥库：

```bash
keytool -genkey -v -keystore keystore.jks -keyalg RSA -keysize 2048 -validity 10000 -alias my-key
```

2. 配置签名（编辑 `app/build.gradle`）：

```gradle
android {
    signingConfigs {
        release {
            storeFile file("../keystore.jks")
            storePassword "你的密码"
            keyAlias "my-key"
            keyPassword "你的密码"
        }
    }

    buildTypes {
        release {
            signingConfig signingConfigs.release
            // ... 其他配置
        }
    }
}
```

3. 构建签名APK：

```bash
./gradlew assembleRelease
```

**注意**: 不要将 `keystore.jks` 提交到Git仓库！

## 🚀 GitHub Actions自动构建

项目已配置GitHub Actions，每次推送代码或创建Tag时会自动构建APK。

### 自动触发构建

- 推送到main/master分支时自动构建
- 创建Release Tag时自动构建并发布

### 创建Release

```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

GitHub Actions会自动：
1. 构建Debug和Release版本的APK
2. 创建GitHub Release
3. 将APK文件上传到Release页面

## 📝 常见问题

### 1. APK安装失败

- 确保开启了"允许安装未知来源应用"
- 如果之前安装过，卸载后重新安装

### 2. 游戏加载失败

- 检查设备网络连接
- 确认游戏URL可以在浏览器中正常访问
- 点击"重试"按钮重新加载

### 3. 编译错误

- 确保使用JDK 17
- 清理Gradle缓存：`./gradlew clean`
- 重新构建：`./gradlew assembleDebug`

### 4. 图标显示异常

- 确保图标文件命名正确
- 确保图标尺寸符合要求
- 清理项目后重新构建

## 📄 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📧 联系方式

- GitHub: [@xiaodaoguoguo](https://github.com/xiaodaoguoguo)
- 游戏地址: https://xiaodaoguoguo.github.io/xdg/

---

**享受游戏！** 🎮
