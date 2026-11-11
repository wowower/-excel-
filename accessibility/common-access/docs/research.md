# 共达无障碍需求调研与五个软件方案

公开证据调研与原型选型报告

资料核对日期 2026年11月11日

本报告比较五个可落地的无障碍软件方案，并解释为何将其实现为一个本地工具箱。当前交付包括五个可运行模块；这表明技术流程可实现，不表明已经获得用户认可、临床有效性或市场验证。

主要建议是把表达板与一步任务卡作为首轮共同设计的主线，轻阅读作为阅读支持入口，字幕工作台与网页检查台面向内容制作和服务提供者。先与当事人验证具体任务，再决定哪些模块应长期维护。

证据分为机构研究、技术标准、现有产品和公开反馈。完整的 29 条来源记录见文末及 sources.json。尚未开展本项目的一手访谈、实际外接开关测试或专业屏幕阅读器测试。

<!-- page -->

## 一 调研方法与证据边界

检索覆盖沟通与言语表达、肢体操作、低视力与阅读困难、听觉信息、认知记忆，以及内容提供者的无障碍建设工作。使用了中文政策与公共服务关键词、英文 accessibility user needs、AAC switch scanning、reading customization、caption quality、step instructions 及公开 GitHub 问题检索。

保留来源优先级依次为当事人或使用者公开反馈、与当事人共同形成的机构需求、原始调查、标准及实现文档。现有产品说明用于判断替代品，不能证明用户愿意购买新产品。机构故事不冒充本项目访谈，单一 GitHub 问题也不代表普遍发生率。

本轮形成 29 条可追溯来源，涵盖 WHO、UNICEF、W3C、DAISY、RNID、Stagetext、WebAIM、政府公开文本和开源项目。部分资料通过检索摘要发现，再打开原页核实；文末标注每项的证据类型。未购买数据库或声称已完成系统综述。

| 可用证据 | 能支持什么 | 不能支持什么 |
| --- | --- | --- |
| 机构研究与用户需求 | 某类障碍及设计需要 | 中国付费用户总量 |
| 公开问题与使用场景 | 一个可复现的具体困难 | 所有同类用户都遇到它 |
| 技术标准与解释 | 设计和检查的参考要求 | 本项目已取得认证 |
| 已实现软件与测试 | 所列功能在测试环境可运行 | 真实辅助设备兼容及长期使用效果 |

WHO 所述全球辅助产品需求涵盖大量物理与数字产品，不能把该数字作为工具箱的市场规模。[S01](https://www.who.int/news-room/fact-sheets/detail/assistive-technology)

## 二 共通问题

需求往往发生在具体任务中：想表达但无法及时输入、想接着阅读却找不到位置、看见字幕却无法跟上、离开任务后忘记下一步。设计应当保留用户控制权，提供清晰反馈和恢复路径，并允许个人偏好不同。工具之间可以共享大按钮、可见焦点、备份及本地处理能力，但不能假定一种界面适合所有障碍类型。

<!-- page -->

## 三 方案一 可自定义的单开关表达板

### 需求与场景

目标用户是愿意采用文字短语沟通、且可以点击、键盘操作或使用键盘模拟开关的成人。协助者可以参与首次设置，日常表达应由使用者自己选择。典型任务是选出“我需要帮助”“请等一下”等短语，组合后展示给旁人或朗读。

Cboard 的公开问题中有人希望在顺序扫描之外用方向键空间导航；AsTeRICS 的另一条反馈讨论平板空间和操作模式，但该问题已关闭并有关联修复。两者说明需要多样输入和低干扰界面，不证明市场没有成熟 AAC 产品。[S18](https://github.com/cboard-org/cboard/issues/1828) [S20](https://github.com/asterics/Asterics-AAC/issues/859)

### 已实现的软件流程

默认短语位置固定；支持自定义 1至36 个短语、句子组合、撤回、大字展示、本地语音和可调速度的自动扫描。扫描也轮到朗读、撤回、清空与停止动作，按键长按不会重复选择，Esc、Tab、失焦或切换模块会停止。只有主动保存短语才写入本机，临时句子不保存。

### 替代方案与定位

Cboard 和 AsTeRICS 已提供成熟的符号沟通及丰富适配能力。共达采用原创文字界面，适用于短语沟通试验和教学演示；需要符号系统、眼控、复杂页面层级或专业语言干预的用户，应首先评估成熟方案与专业支持。[S17](https://github.com/cboard-org/cboard) [S19](https://github.com/asterics/Asterics-AAC)

### 验证与风险

拟请 5至6 名相关使用者在自选短语上完成表达任务，记录能否独立启动、误选、恢复和是否愿意继续使用。目标不是让每人说同样的话。应允许不使用语音、不披露个人内容和随时退出。外接开关、视觉注意能力及触发位置仍需实测，不能承诺适合所有运动能力。

后续优先级是触发键可配置、单开关循环等待优化、个性化版式及共同设计；不在当前阶段加入未经验证的眼控或自动诊断。建议投入 2至3 周做设备与当事人测试，再判断是否扩展。

<!-- page -->

## 四 方案二 可调显示与逐段朗读的轻阅读

### 需求与场景

面向有低视力、阅读困难或需要降低视觉负担的人，提供纯文本材料的个人化阅读入口。场景包括社区通知、课程讲义和工作说明，用户已经拥有文字，不需要把私密材料上传服务器。

DAISY 发布的用户故事涉及字号、间距、背景、语音及位置切换等不同偏好；这是机构整理的需求故事，不是本项目招募访谈。它支持“可调整而非统一处方”的设计原则。[S14](https://daisy.org/activities/standards/reading-apps-user-requirements/user-stories/)

### 已实现的软件流程

粘贴文字或导入 UTF-8 TXT，逐段阅读，调整字号、行距、列宽、字间距和纸面颜色。可切换全文与单段显示、前后导航、逐段本地朗读。用户主动选择后才保存原文与位置，取消保存会删除已记住的原文；未应用的编辑草稿不会覆盖正在阅读的已存内容。

### 替代方案与定位

Thorium Reader 已有出版物格式支持和更完整的阅读能力。共达仅支持短至中等长度的纯文本，不处理 DRM、EPUB 结构、扫描 PDF、公式或 OCR。完整读物应优先选择成熟阅读器。这里的机会是假设：某些短材料无需复杂文库流程，用户更愿意即时粘贴并调整。[S16](https://daisy.org/guidance/info-help/guidance-training/reading-systems/thorium-epub-reader-quick-start-guide/)

### 验证与风险

拟用参与者自选、无敏感内容的文字比较其原有阅读方式与自选显示设置，观察定位、段落切换和恢复位置是否有阻碍。不能用阅读速度单独判断体验，也不以字体或背景颜色声称治疗阅读障碍。

技术风险是本地语音的语言和声音质量不一致、纯文本损失原文结构，以及过量设置造成认知负担。后续应简化初次设置、加入清晰的原文结构导入，并与实际屏幕阅读器核对。建议先花 2 周确认最常用的三项偏好，而不是增加全部阅读格式。

<!-- page -->

## 五 方案三 便于人工复核的字幕工作台

### 需求与场景

目标使用者包括听障受众的内容协作者、学校及公益讲座制作人员。首轮任务是打开已有字幕和本地媒体，找到错位或遗漏，人工修改并导出可交付文件。

Stagetext 报道的一项 2025 年调查包含 94 名 RNID panel 成员，其中 85% 认为字幕质量重要。该小样本仅支持质量值得关注，不能推算全球需求或中国市场规模。[S22](https://www.stagetext.org/news/research-shows-85-of-deaf-people-say-that-the-quality-of-subtitles-is-important-to-them/)

### 已实现的软件流程

读取 SRT 或 WebVTT，搜索正文、逐条修改毫秒级时间与文字、整体偏移、检查重叠及自选速度阈值，配合本地视频显示当前字幕，导出 SRT、WebVTT 与纯文本。非法整体偏移会整体拒绝而不损坏当前字幕。导入中的样式、位置和标记不保留，并明确提示。

### 替代方案与定位

Subtitle Edit 已有成熟桌面与在线功能。共达不宣称算法优势，定位是中文、少量功能、可离线的入门校对路径。需要波形、批量格式转换、语音识别或专业字幕制作时，应优先考虑成熟软件。[S24](https://www.nikse.dk/subtitleedit)

### 验证与风险

字幕不仅是对白，还可能需要说话人及关键声音说明。自动时序规则不能判断准确性。建议由 3至4 名听障参与者及 2 名内容制作者共同复核合成素材，记录漏检、误报和播放器操作困难。[S23](https://www.w3.org/WAI/media/av/captions/)

不得把自动识别当成最终交付，不录制或上传未获同意的音视频。当前已用本地合成静音音频验证播放与字幕同步；真实视频、全部格式和多设备兼容仍待测试。字幕解析及导出流程已有算法和浏览器检查，后续再细化检查规则。

<!-- page -->

## 六 方案四 可以暂停恢复的一步任务卡

### 需求与场景

面向在注意、记忆或任务组织方面需要支持的人，以及愿意共同准备任务卡的协助者。任务应由使用者选择，适合收拾出门物品、准备学习材料等低风险生活场景，不承担服药剂量或其他医疗决定。

W3C 的认知无障碍补充指导建议提供清楚的步骤并减少记忆依赖。这支持分步可见、状态保留与暂停恢复的设计；这些指导不能证明本软件对某类疾病有效。[S10](https://www.w3.org/WAI/WCAG2/supplemental/patterns/o4p07-step-instructions/) [S12](https://www.w3.org/WAI/WCAG2/supplemental/objectives/o6-memory/)

### 已实现的软件流程

每行一个步骤，最多 80 步；开始后一步一屏，支持完成、退回、暂停及继续。主动保存后记录进度，完成全部步骤时不会循环开始。可选计时不自动推进步骤，暂停任务会暂停计时，切换工具会取消计时。清理本机数据后不再隐式保存进度。

### 替代方案与定位

纸卡、手机备忘录、系统提醒和成熟日程工具都是替代品。本项目不是完整日程系统；差异假设在于低刺激、单任务、没有账号以及能够随时看到当前步骤。是否优于纸卡，要由具体使用者判断。

### 验证与风险

建议邀请 5至6 名使用者自选任务，与其原有方式比较恢复位置、误操作和主观负担。不把“完成更多任务”设成唯一指标，不以照护者满意替代使用者意愿。

状态恢复比功能数量更重要：需要检验关闭页面、备份恢复、意外清理和共用设备的影响。计时器没有后台通知承诺；高风险任务禁止据此自动执行。后续优先研究更易读的步骤、可选图片和协助者编辑边界，再考虑跨设备同步。

<!-- page -->

## 七 方案五 面向内容建设者的网页检查台

### 需求与场景

面向网页维护者、学生和小型公益机构的内容人员，帮助他们发现容易忽略的源码问题，并知道下一步要做哪些人工检查。最终受益者是使用键盘、屏幕阅读器或其他辅助方式访问这些网页的人。

WebAIM Million 2026 对一百万主页的自动检查报告了大量可检测问题，包含标签、替代文本等。样本是热门网站主页，方法有限，不能直接代表中国互联网整体或证明本项目检测能力。[S25](https://webaim.org/projects/million/)

### 已实现的软件流程

对粘贴的静态 HTML 提供语言、标题、图片替代文本、表单名称、按钮及链接名称、重复 ID 和标题结构的检查线索。源码保持在未挂载的 template 中，既不执行脚本，也不请求输入里的图片或 iframe。另可计算两种不透明颜色的对比度，并导出本次记录。

### 替代方案与定位

WAVE、浏览器工具及其他成熟检查器具有更完整的能力。共达不是替代审计引擎，适用于教学、源码片段复核和理解常见问题。它不计算实际 CSS、不运行组件、不实现完整可访问名称算法，也不宣布“通过 WCAG”。

### 验证与风险

验收应使用有预期结果的好坏 HTML 样本，明确每条规则的误报和漏报边界；结合实际键盘任务、专业辅助技术及当事人测试。测试工具自身也要检查标签、焦点和缩放，防止把发现问题的工具做成新的障碍。[S09](https://www.w3.org/WAI/test-evaluate/tools/selecting/)

当前最值得投入的是报告可理解性和可复核性。不得给出合规保证、无障碍认证或法律意见。后续如面向机构采购，应采用经验证的检查引擎并与人工评估服务结合。

<!-- page -->

## 八 比较与优先级

下表是本项目的定性判断，不是统计评分。优先级体现小团队在当前约束下的验证顺序，不表示某类障碍更重要。

| 方案 | 需求证据 | 原型范围可控性 | 主要剩余风险 | 建议验证顺序 |
| --- | --- | --- | --- | --- |
| 表达板 | 公开具体反馈与成熟产品 | 较高 | 输入与语音适配 个体差异 | 首轮主线 |
| 轻阅读 | 机构整理用户需求 | 高 | 偏好和语音质量差异 | 首轮配套 |
| 字幕工作台 | 听障组织调查及内容指导 | 较高 | 内容准确性与媒体兼容 | 第二轮 |
| 一步任务卡 | 认知无障碍需求与模式 | 高 | 实际接受度和恢复体验 | 首轮主线 |
| 网页检查台 | 研究与标准 | 较高 | 误报漏报及错误合规推断 | 教学与配套 |

保留而未实现的备选方向包括无障碍路线导航、环境声音识别和自动手语翻译。前者依赖可信设施数据及实时维护；后两者存在识别覆盖、语言差异、误报及隐私风险。当前资源下先不承担可能被误认为安全保障的功能。

## 九 共同设计计划

拟在获得同意后招募 20至24 名参与者，尽量覆盖相关使用方式，提供可选择的访谈形式、交通或远程参与支持与合理补偿。首次访谈先问具体任务和现用替代品，不先推销软件。允许辅助人员参与，但单独确认使用者意愿，不要求披露诊断或健康记录。

先记录现有任务路径，再测试用户自己选择的模块。优先记录阻断、误选、恢复是否成功、能否完成自主选择、主观负担与继续使用意愿；对比的目标是发现谁受益、谁不适合，而非追求统一效果。每轮测试后按阻断严重度修复，再请相关参与者复核。

## 十 仍未知的关键问题

目前没有用户留存、付费意愿、机构采购周期或长期维护成本的实际数据。真实开关、NVDA 或其他专业屏幕阅读器、多浏览器与触屏设备尚需验证。若当事人更愿意使用成熟替代品，应停止对应模块扩张，转为文档、适配或贡献现有开源项目。

<!-- page -->

## 十一 来源索引 上

以下均于 2026年11月11日核对；公开反馈的状态仅指核对时页面状态。每项简述保留其限制，完整可机读记录见 sources.json。

| 编号 | 来源与类型 | 主要用途 |
| --- | --- | --- |
| S01 | [WHO Assistive technology](https://www.who.int/news-room/fact-sheets/detail/assistive-technology) | 全球背景 不作软件市场规模 |
| S02 | [WHO UNICEF 全球报告](https://www.unicef.org/reports/global-report-assistive-technology) | 辅助产品及服务背景 |
| S03 | [无障碍环境建设法官方转载](https://gxca.miit.gov.cn/zwgk/zcwj/flfg/art/2024/art_340a68cb6a8e45ae81c121630dd37346.html) | 中国信息交流政策背景 |
| S04 | [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/) | 技术参考 不宣称认证 |
| S05 | [W3C Keyboard](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html) | 键盘操作 |
| S06 | [W3C Target Size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) | 控件目标与间距 |
| S07 | [W3C Text Spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html) | 用户调整显示 |
| S08 | [W3C Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) | 两色计算参考 |
| S09 | [W3C Evaluation Tools](https://www.w3.org/WAI/test-evaluate/tools/selecting/) | 工具与人工评估边界 |
| S10 | [W3C Clear Instructions](https://www.w3.org/WAI/WCAG2/supplemental/patterns/o4p07-step-instructions/) | 分步说明 |
| S11 | [W3C Separate Instructions](https://www.w3.org/WAI/WCAG2/supplemental/patterns/o3p09-separated-instructions/) | 指令分离 |
| S12 | [W3C Memory](https://www.w3.org/WAI/WCAG2/supplemental/objectives/o6-memory/) | 减少记忆依赖 |
| S13 | [W3C Focus](https://www.w3.org/WAI/WCAG2/supplemental/objectives/o5-user-focus/) | 减少干扰 |
| S14 | [DAISY User Stories](https://daisy.org/activities/standards/reading-apps-user-requirements/user-stories/) | 机构用户故事 |
| S15 | [DAISY Requirements](https://daisy.org/activities/standards/reading-apps-user-requirements/executive-summary/) | 需求汇总 |

<!-- page -->

## 十二 来源索引 下

| 编号 | 来源与类型 | 主要用途 |
| --- | --- | --- |
| S16 | [DAISY Thorium Guide](https://daisy.org/guidance/info-help/guidance-training/reading-systems/thorium-epub-reader-quick-start-guide/) | 成熟阅读器对照 |
| S17 | [Cboard](https://github.com/cboard-org/cboard) | 成熟 AAC 对照 |
| S18 | [Cboard 1828](https://github.com/cboard-org/cboard/issues/1828) | 方向键需求 核对时 Open |
| S19 | [AsTeRICS AAC](https://github.com/asterics/Asterics-AAC) | 成熟 AAC 对照 |
| S20 | [AsTeRICS 859](https://github.com/asterics/Asterics-AAC/issues/859) | 历史场景反馈 核对时 Closed |
| S21 | [RNID Research](https://rnid.org.uk/what-we-do/evidence-hub/social-research-reports/) | 听障组织研究 |
| S22 | [Stagetext 字幕质量调查](https://www.stagetext.org/news/research-shows-85-of-deaf-people-say-that-the-quality-of-subtitles-is-important-to-them/) | 94人样本 保留地域限制 |
| S23 | [W3C Captions](https://www.w3.org/WAI/media/av/captions/) | 内容准确与声音信息 |
| S24 | [Subtitle Edit](https://www.nikse.dk/subtitleedit) | 成熟字幕工具对照 |
| S25 | [WebAIM Million 2026](https://webaim.org/projects/million/) | 自动检测现状与限制 |
| S26 | [Microsoft Adaptive Accessories](https://support.microsoft.com/en-us/surface/accessories/adaptive/) | 外接输入范围 |
| S27 | [MDN localService](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesisVoice/localService) | 本地语音选择 |
| S28 | [MDN template](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template) | 惰性源码解析 |
| S29 | [MDN Service Workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers) | 离线缓存条件 |

本轮只收集公开材料，没有联系这些机构或用户，没有获得背书、合作承诺或采购意向。任何对外申请均应保留这一事实，并在取得新的证据后更新本报告。
