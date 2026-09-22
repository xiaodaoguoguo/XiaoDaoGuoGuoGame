# 🎨 APP图标替换指南

## 快速方法（推荐）

### 使用Icon Kitchen自动生成

1. **访问网站**：https://icon.kitchen/
2. **上传图标**：点击"Image"上传你准备的高清图标（建议1024x1024或更大）
3. **调整设置**：
   - 可以调整内边距（Padding）
   - 可以修改背景颜色
   - 预览效果
4. **下载文件**：点击"Download"下载zip包
5. **解压复制**：
   - 解压下载的zip文件
   - 找到所有 `mipmap-*` 文件夹
   - 将文件夹内的所有PNG文件复制到：
     ```
     D:\project\XiaoDaoGuoGuoGame\app\src\main\res\mipmap-mdpi\
     D:\project\XiaoDaoGuoGuoGame\app\src\main\res\mipmap-hdpi\
     D:\project\XiaoDaoGuoGuoGame\app\src\main\res\mipmap-xhdpi\
     D:\project\XiaoDaoGuoGuoGame\app\src\main\res\mipmap-xxhdpi\
     D:\project\XiaoDaoGuoGuoGame\app\src\main\res\mipmap-xxxhdpi\
     ```

完成！你的图标已经配置好了。

## 需要的图标尺寸

如果你要手动准备，需要这些尺寸：

| 文件夹 | 尺寸 | 用于 |
|--------|------|------|
| mipmap-mdpi | 48x48 | 低密度屏幕 |
| mipmap-hdpi | 72x72 | 中密度屏幕 |
| mipmap-xhdpi | 96x96 | 高密度屏幕 |
| mipmap-xxhdpi | 144x144 | 超高密度屏幕 |
| mipmap-xxxhdpi | 192x192 | 超超高密度屏幕 |

每个文件夹需要3个文件：
- `ic_launcher.png` - 方形图标
- `ic_launcher_round.png` - 圆形图标
- `ic_launcher_foreground.png` - 前景图层

## 其他在线工具

- **Android Asset Studio**：https://romannurik.github.io/AndroidAssetStudio/icons-launcher.html
- **App Icon Generator**：https://appicon.co/

## 验证图标

添加图标后：
1. 构建APK
2. 安装到手机
3. 检查桌面图标是否正常显示

## 常见问题

### Q: 图标显示模糊？
A: 确保原始图标分辨率足够高（至少1024x1024）

### Q: 需要所有尺寸吗？
A: 是的，不同手机需要不同尺寸

### Q: 可以只用一张图吗？
A: 可以用工具自动生成所有尺寸

---

**图标准备好了？继续查看 QUICKSTART.md 发布你的APP！**
