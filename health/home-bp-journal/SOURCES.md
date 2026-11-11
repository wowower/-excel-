# 医疗信息来源与实现边界

核对日期：2026-11-11。指南可能更新；发布后的持续临床审查尚未建立。

1. [American Heart Association — Home Blood Pressure Monitoring](https://www.heart.org/en/health-topics/high-blood-pressure/understanding-blood-pressure-readings/monitoring-your-blood-pressure-at-home)
   - 用于：家庭测量准备、复测间隔、高读数和症状提示、不得自行停药的提示。
   - 产品区别：源页面高读数表述为高于 180 或 120；本工具从等于边界就提示，以减少边界漏提醒。这是保守提示，不是诊断阈值，也不自行标注血压分级。
2. [NICE NG136 — Recommendations, 1.2.7](https://www.nice.org.uk/guidance/ng136/chapter/recommendations#diagnosing-hypertension)
   - 用于：为家庭监测提供 7 天记录窗口及首日排除选项。
   - 源网页直接访问返回 403；本次依据官方页面搜索索引和 [官方 PDF](https://www.nice.org.uk/guidance/ng136/resources/hypertension-in-adults-diagnosis-andmanagement-pdf-66141722710213) 的索引摘要核对。没有把应用的记录数量概览称为符合诊断方案的完整性检查。

## 已知限制

- 仅针对一般成人记录场景；儿童、孕期、产后及特殊疾病不适用统一风险规则。
- 无医疗器械连接、临床验证、诊断、用药建议或低血压风险分层。
- 全部统计是用户输入的描述性结果；不推断缺测数据。
- 窗口按所输入的日历日期计算，原始时间不带时区，不做跨时区推断。
- 同一时段超过两条仍全部等权纳入平均，用户应把具体测量方案交给医生解释。
- 不输出“血压安全”“不用就医”等结论；任何急症症状都不能由网页排除。
