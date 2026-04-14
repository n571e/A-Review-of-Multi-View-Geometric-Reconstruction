# 《面向多视图几何重建的学习方法综述：以 VGG 团队为例》写作与检索方案

## Summary
- 综述题目保持为：**面向多视图几何重建的学习方法综述：以 VGG 团队为例**。
- 新增硬性要求：**具体资料、论文元信息、方法细节、奖项与开源情况均以上网检索得到的真实一级来源为准**，不依赖现有 `Gemini_deepsearch.md` / `GPT_deepsearch.md` 作为引用依据。
- 写作定位不变：围绕“多视图几何重建中的学习方法”这一明确主题，借 VGG 团队近五年的工作分析该方向的方法演进。

## Source Strategy
- 文献与事实的来源优先级固定为：
  1. **会议官方 Open Access 页面**：CVPR/ICCV/ECCV OpenAccess
  2. **论文官方 PDF / arXiv**
  3. **Oxford VGG 官方项目页 / publication 页**
  4. **官方代码仓库**：如 `facebookresearch/vggt`、`facebookresearch/co-tracker`
- 现有两份 deepsearch 文档只用于：
  - 提炼候选关键词
  - 帮助搭建初始大纲
  - 发现可能相关论文
- 现有两份 deepsearch 文档**不得**用于：
  - 直接摘写正文事实
  - 充当参考文献来源
  - 代替论文原文阅读
- 每篇纳入正文的论文必须至少核对以下信息：
  - 题目、作者、会议/年份
  - 研究问题
  - 核心方法
  - 与前序工作的关系
  - 是否为 VGG 署名文献
  - 是否有项目页/代码/官方 PDF
- 对“影响力”类表述单独核实：
  - 如 VGGT 的 **CVPR 2025 Best Paper**，必须引用官方奖项页或 CVPR 新闻页，不只引用 GitHub README。

## Key Changes
- 文献池构建方式改为“先检索、后定稿”：
  - 先用官方来源确认 VGG 团队近五年与主题直接相关的论文名单
  - 再从中筛出正文核心论文 8-12 篇
  - 最后补充 6-8 篇领域对照论文
- 正文结构保持 5 个主体部分，但每章素材都来自已核验论文：
  1. **研究背景与问题定义**
     - 传统 SfM/MVS 与多视图几何重建的定义、流程、局限
  2. **从经典几何到学习化建模的过渡**
     - `Deep Two-View Structure-from-Motion Revisited`
     - `Common Objects in 3D`
     - 早期几何先验相关工作
  3. **几何对应学习与表征增强**
     - `A Light Touch Approach to Teaching Transformers Multi-view Geometry`
     - `CoTracker`
     - `CoTracker3`
  4. **可微几何优化与端到端 SfM**
     - `VGGSfM`
  5. **前馈式统一几何预测与方法趋势**
     - `VGGT`
     - 必要时少量引入 `DUSt3R / MASt3R` 等作定位比较
- 资料搜集时新增一个“文献卡片”环节：
  - 每篇论文形成 1 条卡片，含来源链接、关键词、方法摘要、在主线中的角色
  - 写正文时直接从文献卡片组织内容，减少误引和二手转述
- 参考文献策略固定为：
  - **VGG 署名论文不少于 10 篇**
  - 英文文献为主
  - 2015-2020 年论文总量控制在课程要求范围内
  - 所有文献都必须在正文中实际使用

## Verified Core Sources
- 已核实可作为一级来源的核心入口包括：
  - `Unsupervised Learning of Probably Symmetric Deformable 3D Objects from Images in the Wild`  
    https://arxiv.org/abs/1911.11130
  - `Deep Two-View Structure-from-Motion Revisited`  
    https://openaccess.thecvf.com/content/CVPR2021/html/Wang_Deep_Two-View_Structure-From-Motion_Revisited_CVPR_2021_paper.html
  - `Common Objects in 3D: Large-Scale Learning and Evaluation of Real-Life 3D Category Reconstruction`  
    https://openaccess.thecvf.com/content/ICCV2021/html/Reizenstein_Common_Objects_in_3D_Large-Scale_Learning_and_Evaluation_of_Real-Life_ICCV_2021_paper.html
  - `A Light Touch Approach to Teaching Transformers Multi-view Geometry`  
    https://openaccess.thecvf.com/content/CVPR2023/html/Bhalgat_A_Light_Touch_Approach_to_Teaching_Transformers_Multi-View_Geometry_CVPR_2023_paper.html  
    https://www.robots.ox.ac.uk/~vgg/research/light-touch/
  - `CoTracker: It is Better to Track Together`  
    https://www.robots.ox.ac.uk/~vedaldi/assets/pubs/karaev24cotracker.pdf  
    https://github.com/facebookresearch/co-tracker
  - `VGGSfM: Visual Geometry Grounded Deep Structure From Motion`  
    https://arxiv.org/abs/2312.04563  
    https://www.robots.ox.ac.uk/~vgg/publications/2024/Wang24/
  - `CoTracker3: Simpler and Better Point Tracking by Pseudo-Labelling Real Videos`  
    https://openaccess.thecvf.com/content/ICCV2025/html/Karaev_CoTracker3_Simpler_and_Better_Point_Tracking_by_Pseudo-Labelling_Real_Videos_ICCV_2025_paper.html
  - `VGGT: Visual Geometry Grounded Transformer`  
    https://arxiv.org/abs/2503.11651  
    https://github.com/facebookresearch/vggt
  - `VGGT` 获得 **CVPR 2025 Best Paper** 的官方确认  
    https://cvpr.thecvf.com/Conferences/2025/BestPapersDemos

## Interfaces
- LaTeX 项目结构不变：
  - `main.tex`
  - `sections/01_intro.tex` 到 `sections/06_conclusion.tex`
  - `refs/review.bib`
- 新增一个检索记录文件，建议命名为：
  - `notes/source_log.md`
- `source_log.md` 每篇论文至少记录：
  - 官方链接
  - BibTeX 来源
  - 1 句问题定义
  - 1 句核心方法
  - 1 句在 VGG 主线中的作用
- BibTeX 录入规则固定为：
  - 优先从官方页面或作者提供 BibTeX 复制
  - 若需手动修正，只修格式，不改元信息

## Test Plan
- 真实性检查：
  - 每篇核心论文都有官方链接
  - 奖项、年份、作者、会议信息可交叉验证
- 合规性检查：
  - 主题明确为“多视图几何重建的学习方法”
  - VGG 署名文献不少于 10 篇
  - 不是单纯团队成果罗列
- 可写性检查：
  - 每个章节都已对应到真实论文来源
  - 每篇论文都能回答“做什么、怎么做、比之前强在哪、在主线中起什么作用”
- LaTeX 检查：
  - 参考文献全部由 BibTeX/Biber 生成
  - 正文引用与文献条目一一对应

## Assumptions
- 默认后续写作会以**一级来源优先、二级总结禁作引用**为原则。
- 默认如出现 deepsearch 内容与论文原文不一致，以论文原文和官方页面为准。
- 默认必要时会继续在线补充对照文献，但仍优先选择 CVF OpenAccess、arXiv、Oxford VGG 官方页和官方代码仓库。
