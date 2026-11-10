# 人物画法

## 1. 先定参考与取景

按实际传图顺序给每张图指定角色。默认使用一张清楚的本人照和[随包笔法示意](../assets/portrait-technique.png)。用户提供了画风参考时，以该参考替换示意。[取色色卡](../assets/portrait-palette.png)用于选色，需明确色相时可作为独立参考传入。辅助照片仅在主照看不清某项五官时加入。裁切示例优先决定截线；它和画风示意中的其他人物、服装、场景均不进入肖像。

发出生图前，按下表写出具体观察，避免只写「像本人」「可爱一点」。

| 要记录的内容 | 观察方法 |
| --- | --- |
| 3–5 个辨识点 | 从脸形与下颌、发际线或分缝、眉眼关系、鼻形、标志性配饰中选。优先写不易互换的细节，例如「中分、两束鬓发、低马尾」。 |
| 头部结构 | 按[面部结构与局部修订](face-structure.md)记录侧倾、头部朝向、眼轴、鼻口中线、双侧颊宽及下颌弧线。 |
| 眼睛与神态 | 分别看两眼的长宽、眼睑遮盖、视线和不对称，再单独记录眉头、嘴角及闭口或露齿。标记和表情、辨识度相关的法令纹、笑纹等，记录左右侧可见程度。 |
| 姿态与衣着 | 按本人照记头部倾斜、肩线、保留的手势，以及衣着底色、图案色与配饰。 |
| 截线 | 优先用可见物定位。默认从发顶到胸下缘和上腹交界，截线低于主要胸前衣着细节、高于自然腰线。画出两侧肩线及肩缘到上臂的过渡，给肩缘留出透明边距。靠胸或向外伸出的手势都按本人照画出连续形体。确需侧裁时，在拼接时由同侧画布边缘截去外伸手臂。只有头像时按可见衣着保守延展。 |

## 2. 固定画法

| 项目 | 画到什么程度 |
| --- | --- |
| 卡通化 | 头部稍大，脸形按本人概括。保留眼轴斜率、长宽关系、眼角方向、视线和左右差异。可以轻提眼睑开口，歪头或转脸时优先保持两眼原有比例。 |
| 黑墨勾线 | 用近黑墨色（如 #201D19）沿发顶、外露脸颊与下颌、肩线及袖缘落粗笔，笔压由重转轻，转折处自然收尖。外线约为五官内线的 1.5–2 倍。眉眼、鼻口用清楚的中等线重和少量带收笔的短线，在缩图上仍可读。发束和衣缝的辅助线更轻，肩袖长轮廓尽量连贯。水平截边保留干净色块。 |
| 辨识纹路 | 优先保留主照里影响表情和辨识度的线，例如笑时鼻翼到嘴角旁的法令纹。用一两笔顺结构的短弧概括，近侧与远侧按原照的可见程度处理。次要皮纹、密集眼下线和碎阴影并入大块明暗。 |
| 面部上色 | 参考暖象牙亮面与克制的土色暗面。浅肤色可从 #F9EEDB 亮面与 #EBD2AE 浅赭阴影起步。额头、脸颊和鼻梁连成开阔亮区，发际、鼻侧、下颌和颈部落少量平涂，手和耳朵沿用同组色相。按本人肤色选择中等或深肤色亮面，暗面取同组稍深的低饱和暖棕。保留自然唇色，避免整脸粉红、金黄或渐变罩染。 |
| 面部高光（可选） | 先完成亮面与暗面的二分上色，再顺原有光向，在鼻梁、颧骨或额头的受光处点一两笔。颜色比亮面略浅，并随本人肤色调整。模拟马克笔的短平涂笔刷，边界清楚，笔端有轻微的笔压变化与参差，面积小于主要亮面。 |
| 衣服与头发 | 保留本人发色、衣着底色和关键图案。每块材质用本色与一档平涂暗色。可见水彩笔的宽笔触、参差笔端和少量纸色间隙，少画发丝、织物纹理与反光。 |
| 透明度 | 人物外部为真实 alpha 透明。人物内部的暖白亮面、眼白、浅色衣物保留不透明。 |

笔法图左上示范有侧倾的头部与粗外线，右上示范中等及深肤色的明暗，左下示范头发分块，右下示范肩袖轮廓与宽笔平涂。图中的五官和衣饰仅供观察笔法，主体造型取自本人照。[面部勾线参考](../assets/face-linework-example.png)示范清楚的眉眼鼻口线、大片亮面和少量保留的法令纹。参考用笔层次，人物的纹路位置与深浅由本人照决定。色卡的三组肤色可随照片微调；衣装和点缀色按题材选用。

## 3. 人物生成提示词

把方括号替换为本次观察所得。按实际上传顺序说明参考图各自的用途，只保留用到的输入。

```text
Create a single personalized hand-drawn cartoon portrait. Keep the complete head, neck, both shoulders including their outer contours and transitions into the upper arms, and the torso down to the lower chest/upper abdomen, above the waist. Leave transparent space beyond both shoulders. Match any user-supplied crop reference. Retain the original gestures within that height. Draw any outstretched arm continuously past the planned cut so it can be cropped at the final poster border if needed. Leave out waist-level hands and lower body.
Reference roles in upload order: [main photo for identity, pose and clothing]; [auxiliary photo to clarify a specific feature, if used]; [crop reference for frame only, if used]; [style reference or bundled technique sheet for line weight, light and shadow placement, and marker handling only]; [palette for colors only, if used]. Do not borrow features, costume, or background from the style reference.
Identity anchors: [3–5 distinguishing visible traits].
Expression: [brow tension, eye opening and lids, gaze, asymmetry, mouth expression].
Pose, clothing and crop: [head direction, shoulder line, retained gesture, clothing colors, accessories, and the exact visible landmark just above the crop edge]. Keep a natural neck and a slightly larger head. Keep the subject’s eye aspect ratios, lid angles, gaze and differences between the two eyes. A subtle increase in lid opening is optional if these relationships stay intact.
Head structure: [insert subject-specific head roll and turn, eye heights, nose-to-mouth-to-chin axis, and jaw contour from the face-structure guide].
Make the drawing read as hand-inked on nearly white paper. Follow the supplied line-and-color benchmark when present. Use a bold, pressure-varied near-black brush-pen contour (#201D19 as a starting point) around the hair silhouette, exposed cheek and jaw, shoulders and sleeves. Taper the line at temples and hair tips. Use confident medium-weight near-black strokes for brows, lids, nose and mouth, with fewer marks and controlled tapers. Keep hair details and seams lighter. When a smile crease or nasolabial fold is characteristic and visible in the source, retain it with one or two economical tapered curves that follow the observed perspective. Merge minor wrinkles and fine tonal modeling into broad marker planes. Finish the horizontal torso crop with clean color shapes. Group hair into broad shapes and simplify clothing with broad pen and marker marks.
Keep the forehead, cheeks and bridge of the nose in large, open light planes. Use warm ivory (#F9EEDB) with sparse, muted pale ochre-beige shadows (#EBD2AE) for light complexions. For medium and deep complexions, match the person's own base complexion and choose a restrained, slightly darker warm earth tone for shadow. Apply a few flat marks at the hairline, nose edge, jaw and neck, with corresponding tones on the ears and hand. After establishing the two-value light and shadow planes, optionally add one or two small highlights on lit areas such as the nose bridge, cheekbone or forehead. Match the light direction and use a tone slightly lighter than the subject's light plane. Use short, flat marker-brush strokes with defined edges and subtly irregular ends. Keep the highlights small and matte. Keep natural muted lips. Preserve garment colors with one broad shadow step per material. Avoid pink or yellow casts, orange washes, blush, tonal ramps and photographic skin texture.
Export a true transparent PNG outside the person. Keep near-white highlights inside the portrait opaque. Only the person, with no scenery, decorations, captions or name strip.
```

## 4. 验收后再进入拼接

先把人物放在默认暖白底查看缩略图，再看局部和原图。

| 检查 | 发现问题后的处理 |
| --- | --- |
| 头部结构自然 | 按[结构对照顺序](face-structure.md#首稿以本人主照定结构)并排检查双眼高低、鼻口中线、下巴落点、双侧颊宽和颈部连接。结构错误先修人物层。 |
| 像本人且明显是手绘卡通 | 逐一核对事先写下的辨识点、视线和嘴角。脸画成通用模板时，补清眼形和个人特征；写实感重时，减少五官笔数和明暗层级。 |
| 截线、动作符合参考 | 对照截边附近的衣着地标。确认头部、双侧肩缘和肩部到上臂的过渡完整。若肩部或外伸手臂在图层内突然截断，先补足形体。外伸手臂需要裁切时，留到拼接阶段处理。 |
| 肤色自然，亮面开阔 | 对照本人肤色与色卡相近组。浅肤色亮面读作暖象牙色，阴影是少量浅赭色块。出现粉红或金黄罩染时，只调肤色及阴影覆盖；手、耳和脖子一起核对。 |
| 高光克制（如有） | 在缩图确认亮暗两块仍清楚。高光与光向一致，读成短促的马克笔笔触。过亮或过密时减少笔数和面积。 |
| 外沿粗黑，五官线清楚 | 在缩图看发顶、颊缘、肩袖和眉眼鼻口。边线改粗时沿用原轮廓轨迹。五官内线太细时加重必要笔画，密集细线改为少量明确的结构线。 |
| 辨识纹路保留 | 对照主照确认表情所需的法令纹或笑纹仍在，方向、长度及左右轻重符合原照。检查面部仍读成大块明暗。 |
| PNG 外透明，人物内部高光实 | 检查 alpha 通道和四角；在浅底及深底各预览一次，确认衣领、脸部亮区没有透底、白边或假棋盘格。 |

有问题时沿用最近可用稿，只重做出错的区域或图层，锁定通过检查的五官、姿态、衣着和截线。人物通过上述检查后，继续单独生成风景和装饰，拼接只移动或缩放图层。只改肤色时核对轮廓、眼神与截线。只加重外沿时，沿原轮廓内侧略加笔宽，对照脸形、五官和肩线，保留原来的落点。
