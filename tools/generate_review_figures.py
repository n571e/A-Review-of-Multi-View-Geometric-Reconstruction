from pathlib import Path
import re

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"
BIB_PATH = ROOT / "refs" / "review.bib"


plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "Arial Unicode MS"]
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["axes.unicode_minus"] = False


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
        (2020, "Probably\nSymmetric", "先验"),
        (2021, "Deep Two-View\nSfM", "系统"),
        (2021, "CO3D", "数据"),
        (2023, "Light\nTouch", "先验"),
        (2023, "Dynamic\nStereo", "观测"),
        (2024, "CoTracker", "观测"),
        (2024, "VGGSfM", "系统"),
        (2024, "SHIC", "对应"),
        (2025, "CoTracker3", "观测"),
        (2025, "VGGT", "统一"),
        (2025, "Dynamic Point\nMaps", "扩展"),
    ]
    color_map = {
        "先验": "#D4A373",
        "数据": "#8E9AAF",
        "观测": "#4F772D",
        "对应": "#6C757D",
        "系统": "#1D3557",
        "统一": "#C1121F",
        "扩展": "#7B2CBF",
    }

    fig, ax = plt.subplots(figsize=(11.5, 5.8))
    ax.set_xlim(2019.6, 2025.4)
    ax.set_ylim(-2.6, 2.8)
    ax.axis("off")

    ax.plot([2020, 2025], [0, 0], color="#333333", linewidth=2.2)
    for year in range(2020, 2026):
        ax.plot([year, year], [-0.08, 0.08], color="#333333", linewidth=1.4)
        ax.text(year, -0.38, str(year), ha="center", va="top", fontsize=12, fontweight="bold")

    lane_y = [1.6, -1.55, 1.0, -0.95, 2.15, -2.1, 1.6, -1.55, 1.0, -0.95, 2.15]
    offsets = [-0.18, -0.10, 0.12, 0.18, -0.18, -0.10, 0.10, 0.18, -0.18, 0.0, 0.18]
    for (year, label, stage), y, dx in zip(items, lane_y, offsets):
        x = year + dx
        ax.plot([x, x], [0, y * 0.82], color=color_map[stage], linewidth=1.6, alpha=0.9)
        box = FancyBboxPatch(
            (x - 0.32, y - 0.25),
            0.64,
            0.5,
            boxstyle="round,pad=0.02,rounding_size=0.04",
            facecolor=color_map[stage],
            edgecolor="white",
            linewidth=1.2,
            alpha=0.95,
        )
        ax.add_patch(box)
        ax.text(x, y, label, ha="center", va="center", fontsize=9.4, color="white", fontweight="bold")

    stage_bands = [
        (2020.0, 2021.9, "几何先验与数据基础"),
        (2023.0, 2024.9, "对应学习与系统重构"),
        (2025.0, 2025.35, "统一预测与动态扩展"),
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

    ax.text(2020, 2.55, "VGG 团队多视图几何学习主线时间轴（2020-2025）", fontsize=14, fontweight="bold")
    save(fig, "vgg_timeline.png")


def generate_pipeline() -> None:
    fig, ax = plt.subplots(figsize=(11.5, 6.2))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis("off")

    xs = [0.5, 3.7, 6.9, 10.1]
    titles = ["几何先验与数据基础", "对应关系学习", "可微系统重构", "统一前馈预测"]
    subtitles = [
        "Probably Symmetric\nDeep Two-View SfM\nCO3D",
        "Light Touch\nDynamicStereo\nCoTracker / SHIC",
        "VGGSfM\n全局相机恢复\n可微 BA",
        "VGGT\nDynamic Point Maps\n统一几何表示",
    ]
    colors = ["#F4A261", "#2A9D8F", "#457B9D", "#E63946"]

    for x, title, sub, c in zip(xs, titles, subtitles, colors):
        card = FancyBboxPatch(
            (x, 3.2),
            2.65,
            2.1,
            boxstyle="round,pad=0.08,rounding_size=0.08",
            facecolor=c,
            edgecolor="white",
            linewidth=1.4,
            alpha=0.95,
        )
        ax.add_patch(card)
        ax.text(x + 1.325, 4.78, title, ha="center", va="center", fontsize=12, color="white", fontweight="bold")
        ax.text(x + 1.325, 3.95, sub, ha="center", va="center", fontsize=10, color="white")

    for i in range(3):
        ax.annotate(
            "",
            xy=(xs[i + 1] - 0.15, 4.25),
            xytext=(xs[i] + 2.8, 4.25),
            arrowprops=dict(arrowstyle="->", linewidth=2.0, color="#444444"),
        )

    ax.text(7, 7.15, "VGG 团队方法主线的层次演进", ha="center", va="center", fontsize=15, fontweight="bold")
    ax.text(7, 6.45, "从“局部几何增强”到“统一场景几何表示”", ha="center", va="center", fontsize=12)

    bottom_labels = [
        ("观测层", 1.8, "#8D99AE"),
        ("求解层", 5.2, "#8D99AE"),
        ("表示层", 8.8, "#8D99AE"),
        ("统一层", 12.0, "#8D99AE"),
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

    ax.text(7, 0.45, "经典管线: 特征匹配 → 位姿恢复 → 三角化/BA    |    学习化主线: 先验 → 轨迹 → 系统 → 统一输出",
            ha="center", va="center", fontsize=10.5)
    save(fig, "vgg_pipeline.png")


def generate_year_distribution() -> None:
    year_map = parse_bib_years()
    vgg_keys = [
        "wu2020unsup3d",
        "wang2021deep2view",
        "reizenstein2021co3d",
        "bhalgat2023lighttouch",
        "karaev2023dynamicstereo",
        "melaskyriazi2023realfusion",
        "melaskyriazi2023pc2",
        "karaev2024cotracker",
        "szymanowicz2024splatter",
        "wang2024vggsfm",
        "shtedritski2024shic",
        "karaev2025cotracker3",
        "wang2025vggt",
        "sucar2025dpm",
    ]
    years = list(range(2020, 2026))
    counts = [sum(1 for key in vgg_keys if year_map.get(key) == year) for year in years]
    cumulative = []
    total = 0
    for c in counts:
        total += c
        cumulative.append(total)

    fig, ax = plt.subplots(figsize=(10.5, 5.8))
    bars = ax.bar(years, counts, color=["#A7C957", "#A7C957", "#D9D9D9", "#F4A261", "#457B9D", "#E63946"], width=0.62)
    ax.set_xlabel("年份", fontsize=11)
    ax.set_ylabel("文献数量", fontsize=11)
    ax.set_xticks(years)
    ax.set_ylim(0, max(counts) + 2)
    ax.grid(axis="y", linestyle="--", alpha=0.25)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    for bar, value in zip(bars, counts):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.08, str(value), ha="center", va="bottom", fontsize=10, fontweight="bold")

    ax2 = ax.twinx()
    ax2.plot(years, cumulative, color="#1D3557", marker="o", linewidth=2.2)
    ax2.set_ylabel("累计数量", fontsize=11)
    ax2.set_ylim(0, max(cumulative) + 2)
    ax2.spines["top"].set_visible(False)

    ax.set_title("VGG 相关核心文献的年份分布", fontsize=14, fontweight="bold", pad=14)
    ax.text(2022.05, max(counts) + 1.15, "2023-2025 年是工作集中爆发期", fontsize=10.5)
    save(fig, "vgg_year_distribution.png")


def main() -> None:
    generate_timeline()
    generate_pipeline()
    generate_year_distribution()


if __name__ == "__main__":
    main()
