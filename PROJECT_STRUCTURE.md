# 📁 项目结构说明

本文档详细说明项目的文件结构和各文件的作用。

## 🌳 完整目录树

```
XiaoDaoGuoGuoGame/
├── .github/workflows/build.yml       # GitHub Actions自动构建配置
├── app/
│   ├── src/main/
│   │   ├── java/com/xiaodaoguoguo/game/MainActivity.java  # 核心代码
│   │   ├── res/
│   │   │   ├── layout/activity_main.xml          # 界面布局
│   │   │   ├── values/
│   │   │   │   ├── colors.xml                    # 颜色定义
│   │   │   │   ├── strings.xml                   # 文本字符串
│   │   │   │   ├── themes.xml                    # 主题样式
│   │   │   │   └── ic_launcher_background.xml    # 图标背景色
│   │   │   ├── mipmap-mdpi/          # 48x48 图标
│   │   │   ├── mipmap-hdpi/          # 72x72 图标
│   │   │   ├── mipmap-xhdpi/         # 96x96 图标
│   │   │   ├── mipmap-xxhdpi/        # 144x144 图标
│   │   │   ├── mipmap-xxxhdpi/       # 192x192 图标
│   │   │   └── mipmap-anydpi-v26/    # 自适应图标配置
│   │   └── AndroidManifest.xml       # 应用清单
│   ├── build.gradle                  # 应用级构建配置
│   └── proguard-rules.pro           # 代码混淆规则
├── build.gradle                      # 项目级构建配置
├── settings.gradle                   # Gradle项目设置
├── gradle.properties                 # Gradle全局属性
├── gradlew & gradlew.bat            # Gradle包装器脚本
├── .gitignore                       # Git忽略文件配置
├── README.md                        # 项目说明文档
├── QUICKSTART.md                    # 快速开始指南
├── DEPLOYMENT.md                    # 部署发布指南
├── ICON_GUIDE.md                    # 图标替换指南
├── PROJECT_STRUCTURE.md             # 本文件
└── LICENSE                          # MIT许可证
```

## 📄 核心文件详解

### 1. MainActivity.java
**位置**: `app/src/main/java/com/xiaodaoguoguo/game/MainActivity.java`
**作用**: 应用的主入口和核心逻辑

**关键代码段**:
```java
// 游戏URL配置
private static final String GAME_URL = "https://xiaodaoguoguo.github.io/xdg/";

// 关键功能：
- onCreate()              // 初始化应用
- enableFullscreenMode()  // 全屏沉浸式
- setupWebView()          // 配置WebView
- loadGame()              // 加载游戏
- onBackPressed()         // 返回键处理
```

**修改建议**:
- 修改游戏URL：改 `GAME_URL` 常量
- 调整双击退出间隔：改 `BACK_PRESS_INTERVAL`

### 2. AndroidManifest.xml
**位置**: `app/src/main/AndroidManifest.xml`
**作用**: 应用的配置清单

**关键内容**:
```xml
<!-- 权限声明 -->
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.WAKE_LOCK" />

<!-- 应用配置 -->
<application
    android:icon="@mipmap/ic_launcher"
    android:label="@string/app_name">
    
    <!-- Activity配置 -->
    <activity
        android:name=".MainActivity"
        android:screenOrientation="unspecified">  <!-- 屏幕方向 -->
```

**常见修改**:
- 锁定横屏：`android:screenOrientation="landscape"`
- 锁定竖屏：`android:screenOrientation="portrait"`

### 3. strings.xml
**位置**: `app/src/main/res/values/strings.xml`
**作用**: 所有文本字符串的集中管理

**内容**:
```xml
<string name="app_name">小刀果果游戏</string>
<string name="exit_confirm">再按一次退出游戏</string>
<string name="loading">加载中...</string>
<string name="network_error">网络连接失败，请检查网络设置</string>
<string name="retry">重试</string>
```

**修改说明**:
- 修改APP名称：改 `app_name`
- 修改提示文本：改对应字符串

### 4. build.gradle (app)
**位置**: `app/build.gradle`
**作用**: 应用的构建配置

**关键配置**:
```gradle
android {
    namespace 'com.xiaodaoguoguo.game'     // 包名
    compileSdk 34                           // 编译SDK版本
    
    defaultConfig {
        applicationId "com.xiaodaoguoguo.game"  // 应用ID
        minSdk 21                           // 最低支持Android 5.0
        targetSdk 34                        // 目标Android 14
        versionCode 1                       // 版本号（整数，递增）
        versionName "1.0.0"                 // 版本名（字符串）
    }
}
```

**常见修改**:
- 更新版本：改 `versionCode` 和 `versionName`
- 修改包名：改 `applicationId`

### 5. build.yml
**位置**: `.github/workflows/build.yml`
**作用**: GitHub Actions自动构建配置

**触发条件**:
- 推送到main/master分支
- 推送标签(v开头)
- Pull Request

**构建步骤**:
1. 检出代码
2. 设置JDK 17
3. 构建Debug APK
4. 构建Release APK
5. 上传构建产物
6. (如果是Tag) 创建Release

## 🎨 资源文件说明

### 图标文件（mipmap）

| 文件夹 | 尺寸 | 设备示例 |
|--------|------|----------|
| mipmap-mdpi | 48x48 | 老旧设备 |
| mipmap-hdpi | 72x72 | 低端设备 |
| mipmap-xhdpi | 96x96 | 普通设备 |
| mipmap-xxhdpi | 144x144 | 高端设备 |
| mipmap-xxxhdpi | 192x192 | 顶级设备 |

## 🛠️ 常见修改场景

### 场景1：更换游戏URL
1. 编辑 `MainActivity.java`
2. 修改 `GAME_URL` 常量
3. 提交并推送

### 场景2：修改APP名称
1. 编辑 `app/src/main/res/values/strings.xml`
2. 修改 `<string name="app_name">`
3. 提交并推送

### 场景3：替换图标
1. 准备各尺寸PNG图标
2. 放入对应 `mipmap-*` 文件夹
3. 文件命名为 `ic_launcher.png`
4. 提交并推送

### 场景4：锁定屏幕方向
1. 编辑 `AndroidManifest.xml`
2. 找到 `<activity>` 标签
3. 修改 `android:screenOrientation`:
   - `portrait`: 竖屏
   - `landscape`: 横屏
4. 提交并推送

### 场景5：发布新版本
1. 编辑 `app/build.gradle`
2. 递增 `versionCode`
3. 更新 `versionName`
4. 提交、推送、打Tag

## 📚 学习资源

- **Android开发文档**: https://developer.android.com/
- **WebView指南**: https://developer.android.com/guide/webapps/webview
- **Gradle文档**: https://docs.gradle.org/

---

**需要详细了解某个文件？** 可以直接打开查看，所有代码都有中文注释！
