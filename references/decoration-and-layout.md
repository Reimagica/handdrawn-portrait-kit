# 手绘装饰与拼接

## 生成装饰

将用户提供的 1–3 组短内容分别绘制。文字用清晰的马克笔手写笔画，保留原文语言、措辞和大小写。短词组优先一行，长词组可在自然词界换行。图标用少量有笔压变化的轮廓线和必要结构线。参考随包的[马克笔线稿示意](../assets/decoration-style.png)取用笔、线重和留白。

每组文字与图标可用同一种线色。从人物衣着、背景或风景主色中取较深的同色系，例如深橄榄、墨棕或石板蓝，也可沿用近黑墨色。以成品尺寸和纸底上的对比度为准。装饰只画线稿，图标内部、字的封闭空隙和周围保留透明，省去色块、点染和阴影。若用户要求下划线，用同色的短马克笔线。

```text
Draw one isolated hand-lettered phrase, outline icon, or both as marker linework on a true transparent PNG. Render [exact user-supplied phrase with original language and case, icon, or both]. Use [a dark ink hue derived from the subject's clothes, scenery or background] for every stroke within this group, with enough contrast on the intended poster. Use readable marker handwriting and a few pressure-varied contour or structural strokes. Keep the icon interiors and the counters in letters transparent. Use strokes only, with no color fill, shading, marker dabs, extra marks or background. Leave a clear margin. Add a single line in the same ink only if an underline is requested.
```

逐字核对文字，并在纸底上预览检查线色对比度。用透明通道确认图标内部和字的空隙是空的。若生图错字，单独修正该组；必要时用独立文字层确保字对。姓名只在用户提供并要求展示时加入。

## 选择框线模板

按阶段 2 的风景选择和阶段 3 的装饰选择查表。可先看[五款总览](../assets/layout-templates/overview.png)，再打开对应的 SVG。

| 风景 | 装饰 | 框线模板 |
| --- | --- | --- |
| 无 | 无 | [01 单人物](../assets/layout-templates/01-portrait.svg)，人物居中贴底。 |
| 无 | 有 | [02 人物＋装饰](../assets/layout-templates/02-portrait-decoration.svg)，人物靠一侧，装饰放对侧。 |
| 有 | 无 | [03 人物＋半幅风景](../assets/layout-templates/03-portrait-landscape-half.svg)，风景从底边铺到中线附近。 |
| 有 | 无 | [04 人物＋高位风景](../assets/layout-templates/04-portrait-landscape-tall.svg)，树冠、山形或建筑适合向上延伸时使用。图中 68% 为示例。 |
| 有 | 有 | [05 人物＋风景＋装饰](../assets/layout-templates/05-portrait-landscape-decoration.svg)，风景约半幅，装饰放在风景上方。 |

01–05 均示意约 7 寸竖幅。按用户指定的画幅和实际人物比例调整位置与尺寸。可以左右互换摆放位置，保留人物和地标的原朝向。框线圆点标出双肩，虚线辅助对齐。需要裁切外伸手臂时，沿用对应模板，将手臂裁口落在画框边缘。导出成品前隐藏框线。

## 安排画面

- 始终同时交付透明图层与拼接 PNG。默认用暖白底（`#fcf8f4`）。画幅先试 7 寸竖版（127:178，约 1500 × 2102 px）。用户明确指定的尺寸、比例或方向优先。其余情况可以缩短竖幅（例如 4:5）、改方幅或改横幅（例如 4:3），以头肩大小和留白决定。
- 先定人物，再安排风景和装饰。人物核心是发顶、头颈、肩线与躯干；伸出的胳膊、手和肩包不计入核心。缩到预览尺寸时，**人物上半身应占约 50–70% 的视觉分量**。用核心宽约占画宽 50–70% 作参考，再检查纵向。发顶靠近上边框并保留适度呼吸空间：无装饰时以画高的 5–10% 为目标，最多约 12%；有装饰时以 6–14% 为目标，最多约 16%。装饰放侧边，头顶也无需专门留出装饰区。若贴底、发顶留白与双肩完整难以兼顾，先调整位置和等比缩放，再按需要调整未指定的画幅。
- 人物按指定侧放左下或右下；未指定时优先面朝画内。**人物的躯干截边和风景的岸线、地面或可见底部都贴画面下缘**，各自离底边约 0–3% 画高。风景由对侧进入，可延伸至人物身后并被人物大幅遮挡。画框也可以裁去景物伸出画幅的部分。以露出的树冠、枝干、地标或基底传达场景。摆放时先去掉图层空透明边，再对齐实际内容底部。
- 有装饰时，风景可见主体约占画高的 **45–55%**，从底边延伸到中线附近。跳过装饰时，风景仍从底边起，可按构图伸到更高的位置。适合画高的树冠、建筑或山形可利用原本给装饰留出的空间，保持人物为视觉中心。以实际露出的主体和基底估算，透明边和零散云朵不计入。若遮挡使风景难辨或露出的主体明显低于中线，优先移动风景。横向景色太矮时等比放大，或用较窄、前后错落的取景重画风景，保留主要地标和基底。
- 如有装饰，将 1–3 组放在人物对侧、风景上方的空白处。两组或三组做错落摆放；三组按从上到下的顺序，第一、第三组靠外侧安全线，第二组向内靠近人物。人物换边时，装饰的摆放方向随之对调。给文字、图标和脸留出间距，装饰完整落在画内，头顶保持干净。
- 默认让双侧肩缘和肩到上臂的转折都留在画内，并在侧边留出少量空隙。肩部碰到画框时，先把人物往画内移，可以多盖住一些后方风景。空间仍不足时，可等比缩放人物或加宽未指定的画幅。确需侧裁时只裁外伸手臂，让裁口处的袖子或皮肤连续接到边框。用户明确指定的裁切优先。
- 默认叠放顺序是纸底、风景、人物、装饰。用户可只取部分图层，自行缩放排版。输出新的合成 PNG 和使用过的独立 PNG，必要时保存布局参数，方便重拼。

## 构图验收

交稿前看缩略图，逐项确认：

1. 头肩和躯干是第一视觉落点，完整的发顶和双侧肩缘都在画内，头顶空白符合上述留边。无装饰时尤其检查顶部有没有预留的大块空区。
2. 人物截边与风景基底分别贴底。风景经人物遮挡和画框裁切后，露出的片段仍可辨认，可见主体从底部达到中线附近，无装饰时可延伸到中线以上。
3. 有侧裁时，确认人物只有外伸手臂与画框相交，肩到上臂的转折仍可辨认。若肩缘被切到，先重新摆放。若袖子在纸面中间突然收口，先修复连续形体。
4. 三组装饰从上到下呈外、内、外错落，文字在成品尺寸下清晰可读。

## 本地拼接

图层素材均就绪时，可用任意图层编辑器或本包的 `scripts/compose.py`，需 Python 和 Pillow。人物、风景和装饰标注对应的 `role`，人物与风景用 `bottom` 指定底部留边。下面以竖版 05 为例。风景从左边入画，人物在前，三组装饰按外、内、外排列。按实际素材的宽高调整尺寸及位置，保留双肩和发顶留白。

```json
{
  "canvas": [1500, 2102],
  "background": "#fcf8f4",
  "layers": [
    {"file": "landscape.png", "role": "landscape", "x": -160, "bottom": 0, "height": 1051, "clip_sides": ["left"]},
    {"file": "portrait.png", "role": "portrait", "x": 470, "bottom": 0, "height": 1910},
    {"file": "decoration-01.png", "role": "decoration", "x": 75, "y": 365, "width": 375},
    {"file": "decoration-02.png", "role": "decoration", "x": 300, "y": 600, "width": 375},
    {"file": "decoration-03.png", "role": "decoration", "x": 75, "y": 835, "width": 375}
  ]
}
```

将布局存为 `layout.json`。各图路径相对该文件。每层选 `width` 或 `height` 之一等比缩放，选 `y` 或 `bottom` 之一定位。指定的尺寸是裁掉透明外边距后、画布裁切前的尺寸。人物和风景可用 `clip_sides` 指定侧裁。左侧裁切用负数 `x` 并设 `clip_sides: ["left"]`，右侧裁切让 `x + width` 超过画宽并设 `clip_sides: ["right"]`。也可同时指定两侧。人物侧裁仅限外伸手臂。风景需要截在上边或下边时，可先用 `crop: [left, top, right, bottom]` 指定源图裁切矩形，再将裁口对齐对应画边。

脚本会检查底部留边和人物顶部留白。默认有装饰时发顶留白上限为 16%，无装饰时为 12%。如用户指定更大留白，或为保留双肩需要更宽松的布局，可在顶层添加 `"portrait_top_limit": 20`，用 0–100 的整数百分比指定上限。存在 `role: "decoration"` 时，风景图层需在下半幅且高约为画高的 45–55%。无装饰时，风景图层至少占画高的 45%，可超过 55%。需看合成预览确认发顶、双肩、躯干截边、风景主体的露出与手臂裁口。数组顺序为从底到顶，`background` 写成 null 可导出透明画布。

```sh
python scripts/compose.py layout.json combined.png
```
