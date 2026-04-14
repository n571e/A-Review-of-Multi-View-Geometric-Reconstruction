# 综述检索记录

> 主题：面向多视图几何重建的学习方法综述：以 VGG 团队为例  
> 原则：只记录一级来源或接近一级来源的入口，优先使用 CVF Open Access、arXiv、Oxford VGG 官方页面和官方代码仓库。

## 使用规则

- 正文事实、方法细节、作者与会议信息以论文原文或官方页面为准。
- `raw/Gemini_deepsearch.md` 与 `raw/GPT_deepsearch.md` 仅作为检索线索，不作为正式引用来源。
- 对“奖项”“代码开源”“项目主页”等信息，优先记录官方页面。

## VGG 主线核心论文

### 1. Unsupervised Learning of Probably Symmetric Deformable 3D Objects from Images in the Wild

- Bib key：`wu2020unsup3d`
- 年份/会议：CVPR 2020
- 官方来源：
  - arXiv: https://arxiv.org/abs/1911.11130
  - CVF PDF: https://openaccess.thecvf.com/content_CVPR_2020/papers/Wu_Unsupervised_Learning_of_Probably_Symmetric_Deformable_3D_Objects_From_Images_CVPR_2020_paper.pdf
- 研究问题：如何在无外部三维监督的条件下，从自然图像中恢复可变形物体的三维结构。
- 核心方法：利用物体“可能对称”的先验，在自监督重建框架中联合学习深度、反照率、视角与光照。
- 在主线中的作用：体现 VGG 团队早期“几何/物理先验驱动学习”的方法起点。

### 2. Deep Two-View Structure-from-Motion Revisited

- Bib key：`wang2021deep2view`
- 年份/会议：CVPR 2021
- 官方来源：
  - OpenAccess: https://openaccess.thecvf.com/content/CVPR2021/html/Wang_Deep_Two-View_Structure-From-Motion_Revisited_CVPR_2021_paper.html
  - PDF: https://openaccess.thecvf.com/content/CVPR2021/papers/Wang_Deep_Two-View_Structure-From-Motion_Revisited_CVPR_2021_paper.pdf
- 研究问题：如何以更合理的任务拆解重新构建双视图 SfM 学习框架。
- 核心方法：将光流、相对位姿恢复和尺度不变深度估计组合起来，保留问题中的经典几何可解性。
- 在主线中的作用：体现从“黑盒回归”回到“几何约束 + 学习模块”的过渡逻辑。

### 3. Common Objects in 3D: Large-Scale Learning and Evaluation of Real-Life 3D Category Reconstruction

- Bib key：`reizenstein2021co3d`
- 年份/会议：ICCV 2021
- 官方来源：
  - OpenAccess: https://openaccess.thecvf.com/content/ICCV2021/html/Reizenstein_Common_Objects_in_3D_Large-Scale_Learning_and_Evaluation_of_Real-Life_ICCV_2021_paper.html
  - PDF: https://openaccess.thecvf.com/content/ICCV2021/papers/Reizenstein_Common_Objects_in_3D_Large-Scale_Learning_and_Evaluation_of_Real-Life_ICCV_2021_paper.pdf
- 研究问题：如何为真实世界类别级三维重建提供大规模可训练、可评测的数据基础。
- 核心方法：构建大规模真实对象多视图数据集 CO3D。
- 在主线中的作用：为后续多视图学习方法提供真实数据基座。

### 4. A Light Touch Approach to Teaching Transformers Multi-View Geometry

- Bib key：`bhalgat2023lighttouch`
- 年份/会议：CVPR 2023
- 官方来源：
  - OpenAccess: https://openaccess.thecvf.com/content/CVPR2023/html/Bhalgat_A_Light_Touch_Approach_to_Teaching_Transformers_Multi-View_Geometry_CVPR_2023_paper.html
  - 项目页: https://www.robots.ox.ac.uk/~vgg/research/light-touch/
- 研究问题：如何在 Transformer 中引入多视图几何先验。
- 核心方法：利用极线几何约束 cross-attention 分布，以轻量方式教授模型跨视角几何关系。
- 在主线中的作用：是“几何先验进入表征学习”的标志性工作。

### 5. DynamicStereo: Consistent Dynamic Depth From Stereo Videos

- Bib key：`karaev2023dynamicstereo`
- 年份/会议：CVPR 2023
- 官方来源：
  - OpenAccess: https://openaccess.thecvf.com/content/CVPR2023/html/Karaev_DynamicStereo_Consistent_Dynamic_Depth_From_Stereo_Videos_CVPR_2023_paper.html
  - 代码: https://github.com/facebookresearch/dynamic_stereo
- 研究问题：如何在动态双目视频中获得时间一致的深度估计。
- 核心方法：通过时空一致建模提升动态场景下的深度稳定性。
- 在主线中的作用：体现从静态成对几何走向时空一致表征的中间步骤。

### 6. CoTracker: It is Better to Track Together

- Bib key：`karaev2024cotracker`
- 年份/会议：ECCV 2024
- 官方来源：
  - arXiv: https://arxiv.org/abs/2307.07635
  - ECCV PDF: https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07890.pdf
  - 代码: https://github.com/facebookresearch/co-tracker
- 研究问题：如何提高长时序、多点追踪的鲁棒性。
- 核心方法：联合建模大量点轨迹，以共享上下文方式增强遮挡和出画情况下的追踪能力。
- 在主线中的作用：为后续 VGGSfM 提供更稳定的几何观测。

### 7. Splatter Image: Ultra-Fast Single-View 3D Reconstruction

- Bib key：`szymanowicz2024splatter`
- 年份/会议：CVPR 2024
- 官方来源：
  - OpenAccess: https://openaccess.thecvf.com/content/CVPR2024/html/Szymanowicz_Splatter_Image_Ultra-Fast_Single-View_3D_Reconstruction_CVPR_2024_paper.html
- 研究问题：如何实现高效的前馈式单图三维重建。
- 核心方法：使用 3D Gaussian 表示，将单图重建映射为可快速推断的三维表示预测。
- 在主线中的作用：体现 VGG 团队对“前馈式三维表示”的并行探索。

### 8. VGGSfM: Visual Geometry Grounded Deep Structure From Motion

- Bib key：`wang2024vggsfm`
- 年份/会议：CVPR 2024
- 官方来源：
  - OpenAccess: https://openaccess.thecvf.com/content/CVPR2024/html/Wang_VGGSfM_Visual_Geometry_Grounded_Deep_Structure_From_Motion_CVPR_2024_paper.html
  - arXiv: https://arxiv.org/abs/2312.04563
  - 项目页: https://www.robots.ox.ac.uk/~vgg/publications/2024/Wang24/
- 研究问题：如何把完整 SfM 管线组织成端到端可微系统。
- 核心方法：结合点轨迹、同步相机恢复与可微 BA，实现视觉几何 grounded 的深度 SfM。
- 在主线中的作用：是从模块增强走向系统级学习化的关键转折点。

### 9. CoTracker3: Simpler and Better Point Tracking by Pseudo-Labelling Real Videos

- Bib key：`karaev2025cotracker3`
- 年份/会议：ICCV 2025
- 官方来源：
  - OpenAccess: https://openaccess.thecvf.com/content/ICCV2025/html/Karaev_CoTracker3_Simpler_and_Better_Point_Tracking_by_Pseudo-Labelling_Real_Videos_ICCV_2025_paper.html
  - 代码: https://github.com/facebookresearch/co-tracker
- 研究问题：如何利用真实视频数据进一步提升点追踪效果。
- 核心方法：通过伪标签方式利用真实视频，简化训练并提升追踪性能。
- 在主线中的作用：巩固轨迹学习作为几何系统通用底层观测的地位。

### 10. VGGT: Visual Geometry Grounded Transformer

- Bib key：`wang2025vggt`
- 年份/会议：CVPR 2025
- 官方来源：
  - arXiv: https://arxiv.org/abs/2503.11651
  - 代码: https://github.com/facebookresearch/vggt
  - Best Paper: https://cvpr.thecvf.com/Conferences/2025/BestPapersDemos
- 研究问题：能否用统一前馈网络直接输出多种关键三维属性。
- 核心方法：以 Transformer 同时预测相机参数、点图、深度图与三维点轨迹。
- 在主线中的作用：代表 VGG 团队“统一几何表示 + 前馈推断”的阶段性成果。

### 11. Dynamic Point Maps: A Versatile Representation for Dynamic 3D Reconstruction

- Bib key：`sucar2025dpm`
- 年份/会议：ICCV 2025
- 官方来源：
  - arXiv: https://arxiv.org/abs/2503.16318
  - PDF: https://www.robots.ox.ac.uk/~vedaldi/assets/pubs/sucar25dynamic.pdf
- 研究问题：如何为动态 3D 重建设计统一且可扩展的几何表示。
- 核心方法：提出动态点图表示，用同一中间表示支持多种动态几何任务。
- 在主线中的作用：表明该主线已开始向时空统一几何建模扩展。

## 对照论文

### 12. Bundle Adjustment -- A Modern Synthesis

- Bib key：`triggs2000bundle`
- 来源：经典综述文献
- 作用：用于定义传统 BA 在多视图几何中的地位。

### 13. Structure-from-Motion Revisited

- Bib key：`schoenberger2016colmap`
- 来源：CVPR 2016
- 作用：用于说明传统 SfM 系统的经典工程化实现。

### 14. DUSt3R: Geometric 3D Vision Made Easy

- Bib key：`wang2024dust3r`
- 官方来源：
  - OpenAccess: https://openaccess.thecvf.com/content/CVPR2024/html/Wang_DUSt3R_Geometric_3D_Vision_Made_Easy_CVPR_2024_paper.html
- 作用：用于和 VGGSfM / VGGT 做横向比较，帮助定位“统一几何预测”范式。

### 15. MASt3R: Grounding Image Matching in 3D with MASt3R

- Bib key：`mast3r2024`
- 官方来源：
  - arXiv: https://arxiv.org/abs/2406.09756
- 作用：用于补充 DUSt3R 之后“统一几何预测 + 匹配增强”这一类方法的发展脉络。

### 16. NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis

- Bib key：`mildenhall2020nerf`
- 官方来源：
  - arXiv: https://arxiv.org/abs/2003.08934
- 作用：用于区分多视图几何重建与神经隐式渲染路线的研究目标差异。

### 17. 3D Gaussian Splatting for Real-Time Radiance Field Rendering

- Bib key：`kerbl2023gaussiansplatting`
- 官方来源：
  - arXiv: https://arxiv.org/abs/2308.04079
- 作用：用于说明高效显式场景表示与几何重建主线之间的关系和差异。

### 18. RealFusion: 360deg Reconstruction of Any Object From a Single Image

- Bib key：`melaskyriazi2023realfusion`
- 官方来源：
  - OpenAccess: https://openaccess.thecvf.com/content/CVPR2023/html/Melas-Kyriazi_RealFusion_360deg_Reconstruction_of_Any_Object_From_a_Single_Image_CVPR_2023_paper.html
- 作用：用于补充 VGG 团队在单图 3D 重建与生成先验方向上的探索。

### 19. PC2: Projection-Conditioned Point Cloud Diffusion for Single-Image 3D Reconstruction

- Bib key：`melaskyriazi2023pc2`
- 官方来源：
  - OpenAccess: https://openaccess.thecvf.com/content/CVPR2023/html/Melas-Kyriazi_PC2_Projection-Conditioned_Point_Cloud_Diffusion_for_Single-Image_3D_Reconstruction_CVPR_2023_paper.html
- 作用：用于补充 VGG 团队在单图几何生成与点云表示方面的相关工作。

### 20. SHIC: Shape-Image Correspondences with no Keypoint Supervision

- Bib key：`shtedritski2024shic`
- 年份/会议：ECCV 2024
- 官方来源：
  - VGG publication page: https://www.robots.ox.ac.uk/~vgg/publications/2024/Shtedritski24/
- 研究问题：如何在没有关键点人工标注的情况下学习图像到模板形状的对应关系。
- 核心方法：借助基础视觉模型与模板渲染，将形状对应学习转化为图像间对应学习问题。
- 在主线中的作用：用于补充 VGG 团队在“对应关系学习”上的另一条相关支线，说明几何监督正从显式标注转向可迁移的弱监督或无监督信号。

## 写作提醒

- 课程要求与模板要求并不完全一致。
- 课程要求必须满足：
  - VGG 署名论文不少于 10 篇
  - 以英文文献为主
  - 近十年覆盖，2015-2020 不超过 5 篇
- 模板里的“至少 20 篇文献、近五年每年都有文献”也建议一起满足，这样最稳妥。
