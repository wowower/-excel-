# 维护说明

## 目录与依赖

应用使用原生 HTML/CSS/JavaScript，按模块拆分，没有第三方运行时依赖。core.js 保持可在 Node 中导入的纯函数；common.js 提供本机存储、文件、下载和本地语音适配；其余模块仅处理各自的界面状态。

start.py 仅使用 Python 标准库，并只绑定 127.0.0.1。不要改为向公网监听后声称具备认证或多用户隔离。

## 验证

`node test-core.cjs`；启动服务后打开 browser-tests.html。测试环境使用 `?test=1` 和独立存储键，避免污染正常数据。新增导入格式或保存状态时，应先增加边界及损坏数据用例，确认失败不会部分覆盖。

## 文档

docs 中 Markdown 为可编辑原文，运行 `python build_docs.py` 生成 HTML。页面用显式分页和语义化标题构成，表格采用重复表头与可读列宽。正式 PDF 使用 Windows 的本机 Edge 无头打印，生成脚本为 print_docs.py。普通使用者无需运行这些开发脚本。

PDF 逐页 QA 使用 render_pdf.py，需要开发环境中的 Pillow 和专用 PDFium DLL；它们不是应用依赖，不随应用运行。此次渲染器来自 GitHub bblanchon/pdfium-binaries 的 chromium/8152 发布，pdfium-win-x64.tgz 的 SHA-256 为 cee2b0e9990bc67c0721774932961b9dbf2766046c10eec925acd4cfba6fdfe3。下载与临时图像位于被忽略的 .qa 中，不进入交付仓库。

## 安全与无障碍约定

不把输入文本写入 innerHTML。唯一源码解析入口是未挂载 template；不要把该内容插入活动 DOM。新功能不得自动增加上传、遥测、云端语音或识别 API。当前所有保存均应保留明确用户选择和删除路径。

不要拦截全局键盘快捷键。扫描只在专用区域工作，必须保留 Esc、Tab、失焦与页面切换退出。任何配色、字号或布局修改都应复测焦点、标签、窄屏和用户文本缩放。

维护者不应把自检通过称为认证，不应把公开用户故事当成本项目访谈。发布前更新真实测试范围和已知问题，保留对成熟替代品的说明。
