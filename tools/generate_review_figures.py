from pathlib import Path
import re

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"
BIB_PATH = ROOT / "refs" / "review.bib"


plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "Arial Unicode MS"]
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["axes.unicode_minus"] = False


PAPERS = [
    {"key": "wu2020unsup3d", "year": 2020, "short": "Probably\nSymmetric", "group": "先验/问题设定", "phase": "基础铺垫", "venue": "CVPR 2020"},
    {"key": "wang2021deep2view", "year": 2021, "short": "Deep Two-View\nSfM", "group": "先验/问题设定", "phase": "基础铺垫", "venue": "CVPR 2021"},
    {"key": "reizenstein2021co3d", "year": 2021, "short": "CO3D", "group": "数据基础", "phase": "基础铺垫", "venue": "ICCV 2021"},
    {"key": "bhalgat2023lighttouch", "year": 2023, "short": "Light\nTouch", "group": "对应/轨迹", "phase": "对应增强", "venue": "CVPR 2023"},
    {"key": "karaev2023dynamicstereo", "year": 2023, "short": "Dynamic\nStereo", "group": "对应/轨迹", "phase": "对应增强", "venue": "CVPR 2023"},
    {"key": "melaskyriazi2023realfusion", "year": 2023, "short": "RealFusion", "group": "动态/支线", "phase": "边界延伸", "venue": "CVPR 2023"},
    {"key": "melaskyriazi2023pc2", "year": 2023, "short": "PC2", "group": "动态/支线", "phase": "边界延伸", "venue": "CVPR 2023"},
    {"key": "karaev2024cotracker", "year": 2024, "short": "CoTracker", "group": "对应/轨迹", "phase": "对应增强", "venue": "ECCV 2024"},
    {"key": "szymanowicz2024splatter", "year": 2024, "short": "Splatter\nImage", "group": "动态/支线", "phase": "边界延伸", "venue": "CVPR 2024"},
    {"key": "wang2024vggsfm", "year": 2024, "short": "VGGSfM", "group": "系统求解", "phase": "系统重构", "venue": "CVPR 2024"},
    {"key": "shtedritski2024shic", "year": 2024, "short": "SHIC", "group": "对应/轨迹", "phase": "对应增强", "venue": "ECCV 2024"},
    {"key": "karaev2025cotracker3", "year": 2025, "short": "CoTracker3", "group": "对应/轨迹", "phase": "对应增强", "venue": "ICCV 2025"},
    {"key": "wang2025vggt", "year": 2025, "short": "VGGT", "group": "统一表示", "phase": "统一预测", "venue": "CVPR 2025"},
    {"key": "sucar2025dpm", "year": 2025, "short": "Dynamic Point\nMaps", "group": "动态/支线", "phase": "统一预测", "venue": "ICCV 2025"},
]

GROUP_COLORS = {
    "先验/问题设定": "#C97C5D",
    "数据基础": "#8E9AAF",
    "对应/轨迹": "#4D908E",
    "系统求解": "#355070",
    "统一表示": "#BC4749",
    "动态/支线": "#7B2CBF",
}

PHASE_COLORS = {
    "基础铺垫": "#E9C46A",
    "对应增强": "#90BE6D",
    "系统重构": "#4D908E",
    "统一预测": "#F28482",
    "边界延伸": "#CDB4DB",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_bib_years() -> dict[str, int]:
    text = read_text(BIB_PATH)
    blocks = re.split(r"\n@", text)
    year_by_key: dict[str, int] = {}
    for idx, block in enumerate(blocks):
        if not block.strip():
            continue
        if idx > 0:
            block = "@" + block
        key_match = re.search(r"@\w+\{([^,]+),", block)
        year_match = re.search(r"year\s*=\s*\{(\d{4})\}", block)
        if key_match and year_match:
            year_by_key[key_match.group(1)] = int(year_match.group(1))
    return year_by_key


def save(fig, filename: str) -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_DIR / filename, dpi=320, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def generate_timeline() -> None:
    items = [
        paper
        for paper in PAPERS
        if paper["short"] not in {"RealFusion", "PC2", "Splatter\nImage"}
    ]

    fig, ax = plt.subplots(figsize=(12.3, 6.4))
    ax.set_xlim(2019.6, 2025.45)
    ax.set_ylim(-2.75, 3.0)
    ax.axis("off")

    ax.plot([2020, 2025], [0, 0], color="#333333", linewidth=2.2)
    for year in range(2020, 2026):
        ax.plot([year, year], [-0.08, 0.08], color="#333333", linewidth=1.4)
        ax.text(year, -0.38, str(year), ha="center", va="top", fontsize=12, fontweight="bold")

    lane_y = [1.7, -1.55, 1.05, -0.95, 2.2, -2.15, 1.7, -1.55, 1.05, -0.95, 2.2]
    offsets = [-0.18, -0.10, 0.12, 0.18, -0.18, -0.10, 0.10, 0.18, -0.18, 0.0, 0.18]
    for paper, y, dx in zip(items, lane_y, offsets):
        year = paper["year"]
        label = paper["short"]
        group = paper["group"]
        x = year + dx
        ax.plot([x, x], [0, y * 0.82], color=GROUP_COLORS[group], linewidth=1.6, alpha=0.9)
        box = FancyBboxPatch(
            (x - 0.32, y - 0.25),
            0.64,
            0.5,
            boxstyle="round,pad=0.02,rounding_size=0.04",
            facecolor=GROUP_COLORS[group],
            edgecolor="white",
            linewidth=1.2,
            alpha=0.95,
        )
        ax.add_patch(box)
        ax.text(x, y, label, ha="center", va="center", fontsize=9.4, color="white", fontweight="bold")
        venue_y = y - 0.43 if y > 0 else y + 0.43
        va = "top" if y > 0 else "bottom"
        ax.text(x, venue_y, paper["venue"], ha="center", va=va, fontsize=8.3, color="#444444")

    stage_bands = [
        (2020.0, 2021.9, "阶段一：几何先验与数据基座"),
        (2023.0, 2024.1, "阶段二：轨迹化观测与特征增强"),
        (2024.2, 2025.4, "阶段三：系统级可微与统一前馈"),
    ]
    band_colors = ["#E9C46A", "#90BE6D", "#F28482"]
    for (x0, x1, text), c in zip(stage_bands, band_colors):
        box = FancyBboxPatch(
            (x0, -2.45),
            x1 - x0,
            0.42,
            boxstyle="round,pad=0.03,rounding_size=0.04",
            facecolor=c,
            edgecolor="none",
            alpha=0.8,
        )
        ax.add_patch(box)
        ax.text((x0 + x1) / 2, -2.24, text, ha="center", va="center", fontsize=10.5, fontweight="bold")

    legend_items = [
        ("先验/问题设定", 2020.25, 2.66),
        ("数据基础", 2021.45, 2.66),
        ("对应/轨迹", 2022.45, 2.66),
        ("系统求解", 2023.55, 2.66),
        ("统一表示", 2024.55, 2.66),
        ("动态/支线", 2025.15, 2.66),
    ]
    for text, x, y in legend_items:
        chip = FancyBboxPatch(
            (x - 0.35, y - 0.12),
            0.7,
            0.24,
            boxstyle="round,pad=0.02,rounding_size=0.05",
            facecolor=GROUP_COLORS[text],
            edgecolor="none",
            alpha=0.95,
        )
        ax.add_patch(chip)
        ax.text(x, y, text, ha="center", va="center", fontsize=8.4, color="white", fontweight="bold")

    ax.text(2020, 2.92, "VGG 团队多视图几何学习主线时间轴（2020-2025）", fontsize=14, fontweight="bold")
    save(fig, "vgg_timeline.png")


def generate_pipeline() -> None:
    fig, ax = plt.subplots(figsize=(12.0, 6.8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8.6)
    ax.axis("off")

    top_xs = [0.5, 3.7, 6.9, 10.1]
    classic_titles = ["经典前端", "经典观测组织", "经典全局求解", "经典结果输出"]
    classic_subtitles = [
        "局部特征提取\n成对匹配",
        "关键点链与轨迹拼接\n几何验证",
        "位姿恢复\n三角化 / BA",
        "稀疏点云\n相机参数",
    ]
    classic_colors = ["#B8C0C8", "#AAB7C4", "#94A3B8", "#7C8DA3"]

    for x, title, sub, c in zip(top_xs, classic_titles, classic_subtitles, classic_colors):
        card = FancyBboxPatch(
            (x, 5.45),
            2.65,
            1.7,
            boxstyle="round,pad=0.08,rounding_size=0.08",
            facecolor=c,
            edgecolor="white",
            linewidth=1.4,
            alpha=0.95,
        )
        ax.add_patch(card)
        ax.text(x + 1.325, 6.7, title, ha="center", va="center", fontsize=11.5, color="white", fontweight="bold")
        ax.text(x + 1.325, 5.95, sub, ha="center", va="center", fontsize=9.5, color="white")

    bottom_titles = ["几何先验前移", "轨迹化观测", "可微系统重构", "统一前馈输出"]
    bottom_subtitles = [
        "Light Touch\nProbably Symmetric\nCO3D",
        "DynamicStereo\nCoTracker / SHIC\nCoTracker3",
        "VGGSfM\n同步相机恢复\n可微 BA",
        "VGGT\nPoint Maps\nDynamic Point Maps",
    ]
    bottom_colors = ["#F4A261", "#2A9D8F", "#457B9D", "#E63946"]

    for x, title, sub, c in zip(top_xs, bottom_titles, bottom_subtitles, bottom_colors):
        card = FancyBboxPatch(
            (x, 2.45),
            2.65,
            2.1,
            boxstyle="round,pad=0.08,rounding_size=0.08",
            facecolor=c,
            edgecolor="white",
            linewidth=1.4,
            alpha=0.96,
        )
        ax.add_patch(card)
        ax.text(x + 1.325, 4.0, title, ha="center", va="center", fontsize=12, color="white", fontweight="bold")
        ax.text(x + 1.325, 3.15, sub, ha="center", va="center", fontsize=10, color="white")

    for i in range(3):
        ax.annotate(
            "",
            xy=(top_xs[i + 1] - 0.15, 3.5),
            xytext=(top_xs[i] + 2.8, 3.5),
            arrowprops=dict(arrowstyle="->", linewidth=2.0, color="#444444"),
        )

    for x in top_xs:
        ax.annotate(
            "",
            xy=(x + 1.325, 5.42),
            xytext=(x + 1.325, 4.62),
            arrowprops=dict(arrowstyle="-|>", linewidth=1.6, color="#666666", linestyle="--"),
        )

    bottom_labels = [
        ("观测层", 1.8, "#8D99AE"),
        ("求解层", 5.2, "#8D99AE"),
        ("表示层", 8.8, "#8D99AE"),
        ("扩展层", 12.0, "#8D99AE"),
    ]
    for text, x, c in bottom_labels:
        chip = FancyBboxPatch(
            (x - 0.8, 1.15),
            1.6,
            0.58,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            facecolor=c,
            edgecolor="none",
            alpha=0.9,
        )
        ax.add_patch(chip)
        ax.text(x, 1.44, text, ha="center", va="center", fontsize=10.5, color="white", fontweight="bold")

    ax.text(7, 8.0, "VGG 团队如何重写经典多视图几何管线", ha="center", va="center", fontsize=15, fontweight="bold")
    ax.text(7, 7.45, "上排展示传统流程的功能模块，下排展示 VGG 主线对应的学习化改写路径", ha="center", va="center", fontsize=11.2)
    ax.text(7, 0.45, "经典管线的模块边界被逐步打通：先把几何前移到表征学习，再把观测、求解与输出整合为可迁移的统一表示",
            ha="center", va="center", fontsize=10.3)
    save(fig, "vgg_pipeline.png")


def generate_year_distribution() -> None:
    years = list(range(2020, 2026))
    category_groups = {
        "基础：先验/数据": {"先验/问题设定", "数据基础"},
        "前端：对应/轨迹": {"对应/轨迹"},
        "系统：求解/重构": {"系统求解"},
        "统一：表示/扩展": {"统一表示", "动态/支线"},
    }
    stack_colors = {
        "基础：先验/数据": "#C97C5D",
        "前端：对应/轨迹": "#4D908E",
        "系统：求解/重构": "#355070",
        "统一：表示/扩展": "#BC4749",
    }
    counts_by_group = {
        group: [
            sum(1 for paper in PAPERS if paper["year"] == year and paper["group"] in mapped_groups)
            for year in years
        ]
        for group, mapped_groups in category_groups.items()
    }
    counts = [sum(counts_by_group[group][idx] for group in category_groups) for idx in range(len(years))]
    cumulative = []
    total = 0
    for c in counts:
        total += c
        cumulative.append(total)

    fig, ax = plt.subplots(figsize=(10.8, 6.1))
    bottoms = np.zeros(len(years))
    for group in category_groups:
        values = np.array(counts_by_group[group])
        ax.bar(years, values, bottom=bottoms, color=stack_colors[group], width=0.64, label=group)
        bottoms += values

    ax.set_xlabel("年份", fontsize=11)
    ax.set_ylabel("文献数量", fontsize=11)
    ax.set_xticks(years)
    ax.set_ylim(0, max(counts) + 2)
    ax.grid(axis="y", linestyle="--", alpha=0.25)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    for year, value in zip(years, counts):
        ax.text(year, value + 0.08, str(value), ha="center", va="bottom", fontsize=10, fontweight="bold")

    ax2 = ax.twinx()
    ax2.plot(years, cumulative, color="#1D3557", marker="o", linewidth=2.2)
    ax2.set_ylabel("累计数量", fontsize=11)
    ax2.set_ylim(0, max(cumulative) + 2)
    ax2.spines["top"].set_visible(False)

    ax.set_title("VGG 相关核心文献的年份演进与重心迁移", fontsize=14, fontweight="bold", pad=14)
    ax.text(2021.85, max(counts) + 1.15, "图中堆叠反映正文三大阶段（前后端及统一表示），折线反映文献累计总数", fontsize=10.2)
    ax.legend(frameon=False, ncol=2, loc="upper left", fontsize=9.6)
    save(fig, "vgg_year_distribution.png")


def generate_focus_heatmap() -> None:
    years = list(range(2020, 2026))
    categories = ["先验/问题设定", "数据基础", "对应/轨迹", "系统求解", "统一表示", "动态/支线"]
    matrix = np.array(
        [
            [sum(1 for paper in PAPERS if paper["year"] == year and paper["group"] == category) for year in years]
            for category in categories
        ]
    )

    fig, ax = plt.subplots(figsize=(10.8, 5.9))
    im = ax.imshow(matrix, cmap="Blues", aspect="auto", vmin=0, vmax=max(2, int(matrix.max())))
    ax.set_xticks(range(len(years)), labels=years, fontsize=10.5)
    row_labels = [f"{category}（{int(matrix[idx].sum())}）" for idx, category in enumerate(categories)]
    ax.set_yticks(range(len(categories)), labels=row_labels, fontsize=10.2)
    ax.set_xlabel("年份", fontsize=11)
    ax.set_ylabel("研究重心类别（括号内为累计篇数）", fontsize=11)

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            value = int(matrix[i, j])
            ax.text(
                j,
                i,
                str(value),
                ha="center",
                va="center",
                fontsize=10,
                color="white" if value >= 2 else "#1F2937",
                fontweight="bold",
            )

    ax.set_title("VGG 相关文献的研究重心分布热图", fontsize=14, fontweight="bold", pad=14)
    ax.text(
        0.0,
        -0.12,
        "数值越高表示该年份在对应研究类别中的代表工作越集中",
        transform=ax.transAxes,
        fontsize=10.1,
    )
    cbar = fig.colorbar(im, ax=ax, fraction=0.045, pad=0.04)
    cbar.set_label("论文数量", fontsize=10.5)
    save(fig, "vgg_focus_heatmap.png")


def generate_obs_evolution() -> None:
    fig, ax = plt.subplots(figsize=(10, 4.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")
    
    # Left: Pairwise Matching
    ax.text(2.5, 4.2, "传统多视图：离散成对匹配", ha="center", va="center", fontsize=13, fontweight="bold")
    ax.add_patch(plt.Rectangle((0.8, 1.5), 1.2, 1.8, facecolor="#E0E0E0", edgecolor="#888", lw=1.5))
    ax.add_patch(plt.Rectangle((3.0, 1.5), 1.2, 1.8, facecolor="#E0E0E0", edgecolor="#888", lw=1.5))
    
    pairs = [
        ((1.6, 2.8), (3.4, 2.7), "#457B9D"),
        ((1.4, 2.2), (3.2, 2.3), "#457B9D"),
        ((1.8, 1.8), (3.6, 1.9), "#E63946")  # Error match
    ]
    for (x1, y1), (x2, y2), c in pairs:
        ax.plot([x1, x2], [y1, y2], color=c, lw=1.5, marker="o", markersize=4, linestyle="--")
        
    ax.text(2.5, 0.8, "容易丢失上下文，形成局部错误匹配\n多图像之间需繁琐合并且容易断链", ha="center", va="center", fontsize=9.5, color="#555")

    # Separator
    ax.plot([5, 5], [0.5, 4.5], color="#CCC", lw=2, linestyle=":")

    # Right: Point Trajectory
    ax.text(7.5, 4.2, "学习式多视图：时空稠密轨迹", ha="center", va="center", fontsize=13, fontweight="bold")
    import matplotlib.patches as patches
    for i in range(4):
        ax.add_patch(plt.Rectangle((5.8 + i*0.8, 1.5 + i*0.1), 0.9, 1.6, facecolor="#D4E6F1", edgecolor="#2980B9", lw=1.2, alpha=0.9))
        
    # Draw trajectories
    x_coords = [6.25 + i*0.8 for i in range(4)]
    y_coords1 = [2.6 + i*0.1, 2.65 + i*0.1, 2.5 + i*0.1, 2.4 + i*0.1]
    y_coords2 = [2.0 + i*0.1, 2.1 + i*0.1, 2.25 + i*0.1, 2.15 + i*0.1]
    ax.plot(x_coords, y_coords1, color="#E67E22", lw=2.5, marker="o", markersize=5)
    ax.plot(x_coords, y_coords2, color="#27AE60", lw=2.5, marker="o", markersize=5)

    ax.text(7.5, 0.8, "轨迹共享时序上下文，自然包含可见性\n有效应对短时遮挡、弱纹理和大幅运动", ha="center", va="center", fontsize=9.5, color="#555")

    save(fig, "vgg_obs_evolution.png")


def generate_vggsfm_concept() -> None:
    fig, ax = plt.subplots(figsize=(11, 4.2))
    ax.set_xlim(0, 11)
    ax.set_ylim(-0.5, 4.5)
    ax.axis("off")

    stages = [
        ("密集追踪特征\n(CoTracker)", "#A3CEF1", 1.2),
        ("全局相机初始化\n(同步恢复避免增量)", "#6096BA", 4.2),
        ("可微非线性优化\n(Differentiable BA)", "#274C77", 7.2),
        ("全局一致三维结果\n(Poses & 3D Points)", "#8B8C89", 9.8)
    ]

    for i, (text, color, x) in enumerate(stages):
        box = FancyBboxPatch(
            (x - 1.2, 1.2), 2.4, 1.6,
            boxstyle="round,pad=0.1,rounding_size=0.15",
            facecolor=color, edgecolor="white", lw=2, alpha=0.95
        )
        ax.add_patch(box)
        ax.text(x, 2.0, text, ha="center", va="center", fontsize=11, fontweight="bold", color="white")
        
        if i < len(stages) - 1:
            ax.annotate("", xy=(stages[i+1][2] - 1.3, 2.0), xytext=(x + 1.2, 2.0),
                        arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6", lw=2.5, color="#444"))

    # Add gradient flow error
    ax.annotate("", xy=(stages[0][2], 0.6), xytext=(stages[2][2], 0.6),
                arrowprops=dict(connectionstyle="bar,fraction=-0.15", arrowstyle="->,head_width=0.4,head_length=0.6", lw=2, ls="--", color="#E63946"))
    ax.text((stages[0][2] + stages[2][2])/2, 0.1, "重投影误差反向传播（系统级学习闭环）", ha="center", va="center", fontsize=10, color="#E63946", fontweight="bold")

    save(fig, "vggsfm_concept.png")


def generate_model_radar() -> None:
    categories = ['多视点全局一致性', '统一表示化', '前馈端到端特性', '可微分框架耦合']
    N = len(categories)

    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]

    models = {
        'DUSt3R': ([3, 3, 5, 2], '#3A86FF'),
        'VGGSfM': ([5, 2, 2, 5], '#FF006E'),
        'VGGT':   ([4, 5, 5, 4], '#8338EC')
    }

    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(111, polar=True)
    
    # Optional offsets handling depending on matplotlib version
    ax.set_theta_offset(np.pi / 4)
    ax.set_theta_direction(-1)

    import matplotlib.font_manager as fm
    plt.xticks(angles[:-1], categories, fontsize=12, fontweight="bold")
    ax.set_rlabel_position(0)
    plt.yticks([1, 2, 3, 4, 5], ["1", "2", "3", "4", "5"], color="grey", size=8)
    plt.ylim(0, 5.5)

    for name, (values, color) in models.items():
        v = values + values[:1]
        ax.plot(angles, v, linewidth=2, linestyle='solid', label=name, color=color)
        ax.fill(angles, v, color=color, alpha=0.1)

    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=11, frameon=False)
    plt.title("本主线与横向对比前馈模型能力雷达", size=14, fontweight="bold", y=1.05)
    
    save(fig, "model_comparison_radar.png")


def main() -> None:
    generate_timeline()
    generate_pipeline()
    generate_year_distribution()
    generate_focus_heatmap()
    generate_obs_evolution()
    generate_vggsfm_concept()
    generate_model_radar()


if __name__ == "__main__":
    main()
