#!/usr/bin/env python3
"""Generate the public Kalshi weather project PDF and thumbnail. Facts only."""
from pathlib import Path

from fpdf import FPDF
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
PDF_PATH = ROOT / "assets" / "files" / "Kalshi_Weather.pdf"
THUMB_PATH = ROOT / "assets" / "images" / "thumbnails" / "kalshi_weather_thumbnail.png"
FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")


class Brief(FPDF):
    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("DejaVu", "I", 9)
        self.set_text_color(90, 104, 120)
        self.cell(0, 8, "Eugenio D. Macias  ·  Weather prediction markets", align="L")
        self.ln(12)

    def footer(self):
        self.set_y(-14)
        self.set_font("DejaVu", "", 9)
        self.set_text_color(90, 104, 120)
        self.cell(0, 8, str(self.page_no()), align="C")


def add_heading(pdf, text, size=16):
    pdf.ln(3)
    pdf.set_font("DejaVu", "B", size)
    pdf.set_text_color(30, 42, 51)
    pdf.multi_cell(0, 8, text)
    pdf.set_draw_color(110, 50, 44)
    x, y = pdf.get_x(), pdf.get_y()
    pdf.line(pdf.l_margin, y, pdf.l_margin + 28, y)
    pdf.ln(4)


def add_body(pdf, text):
    pdf.set_font("DejaVu", "", 11)
    pdf.set_text_color(30, 42, 51)
    pdf.multi_cell(0, 6.2, text)
    pdf.ln(2)


def add_bullets(pdf, items):
    pdf.set_font("DejaVu", "", 11)
    pdf.set_text_color(30, 42, 51)
    for item in items:
        pdf.set_x(pdf.l_margin + 4)
        pdf.multi_cell(0, 6.2, "·  " + item)
    pdf.ln(2)


def write_pdf():
    pdf = Brief(format="Letter")
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.add_font("DejaVu", "", str(FONT_DIR / "DejaVuSans.ttf"))
    pdf.add_font("DejaVu", "B", str(FONT_DIR / "DejaVuSans-Bold.ttf"))
    pdf.add_font("DejaVu", "I", str(FONT_DIR / "DejaVuSans.ttf"))
    pdf.add_page()
    pdf.set_font("DejaVu", "B", 22)
    pdf.set_text_color(30, 42, 51)
    pdf.multi_cell(0, 10, "Machine learning on weather prediction markets")
    pdf.ln(1)
    pdf.set_font("DejaVu", "", 12)
    pdf.set_text_color(90, 104, 120)
    pdf.multi_cell(
        0,
        6.5,
        "Eugenio D. Macias  ·  2026–present\n"
        "Kalshi KXHIGHNY (NYC daily high) and international Polymarket NYC temperature ladders.\n"
        "Public research notes. No trading credentials, orders, or private desk details.",
    )
    pdf.ln(2)
    pdf.set_draw_color(197, 206, 216)
    pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
    pdf.ln(6)

    add_heading(pdf, "Problem")
    add_body(
        pdf,
        "Kalshi lists a daily ladder of contracts on New York City’s maximum temperature "
        "(series KXHIGHNY). Each strike is a yes/no on a temperature bracket; the ladder is "
        "meant to be an exclusive, exhaustive partition of the day’s high. International "
        "Polymarket lists a related NYC daily-high ladder. The two venues do not settle the "
        "same observation: as of October 2026, Kalshi names The Weather Company’s CLINYC "
        "report, while the configured Polymarket collector records NOAA KLGA hourly "
        "observations. NWS climate labels are therefore not automatically the Kalshi outcome, "
        "and same-city contracts are not identical instruments.",
    )
    add_body(
        pdf,
        "The research question is forecast verification, not a pitch: does the market’s "
        "implied distribution beat NOAA’s National Blend of Models (NBM) on proper scores, "
        "at which horizons, and after accounting for how the climate day is defined? A second "
        "question is whether a statistical model that sees ensemble weather, live observations, "
        "and order flow can correct those market-implied probabilities. A third is whether "
        "quoted spreads at a day’s T−24h horizon leave room for a taker at all.",
    )

    add_heading(pdf, "Data")
    add_bullets(
        pdf,
        [
            "Kalshi public market-data API: market metadata, order books, and trades for KXHIGHNY, written as gzip JSONL with UTC capture timestamps and an HTTP heartbeat database.",
            "Historical Kalshi candlesticks and market list (thousands of contracts from August 2021 onward) plus CLINYC climate-report text from the Iowa Environmental Mesonet AFOS archive, used as settlement labels when they match the venue’s then-current snapshot rule.",
            "NOAA NBM gridded percentile ladders from the public AWS/NOMADS blend archive, read with HTTP byte-range requests against .idx sidecars so full GRIB files are not downloaded. The retrospective backbone is the 18-hour max-window percentile product (NBM v4 era).",
            "IEM ASOS observations at KNYC (Central Park) and KLGA, used for clock calibration and for the station-basis between venues.",
            "Polymarket Gamma market discovery (nyc-daily-weather) and CLOB books, stored in a separate heartbeat file so the two venues cannot overwrite each other.",
            "Independent weather-capture jobs for recent NWS observations and forecasts, kept separate from the market loggers.",
        ],
    )
    add_body(
        pdf,
        "Folder dates are UTC capture dates, not contract dates. Readers skip a truncated last "
        "line after a hard crash; complete prior lines are flushed. Trades cursors resume. "
        "Known logger gaps are treated as missing, not as zero activity.",
    )

    add_heading(pdf, "Methods")
    add_body(
        pdf,
        "Scoring treats the day’s strikes as an ordered ladder. The primary proper score is the "
        "ranked probability score (squared error between forecast and observed cumulative "
        "distributions). Multi-category Brier scores and a log score with a probability floor "
        "are reported alongside. Murphy’s decomposition of the (binary, pooled) Brier score "
        "separates reliability, resolution, and uncertainty. Skill is 1 − score / reference, "
        "with the reference method named in advance. Intervals are percentile bootstraps over "
        "climate-day clusters, not independent brackets.",
    )
    add_body(
        pdf,
        "A forecast that is not a probability distribution over the ladder is refused or "
        "explicitly renormalized; six independent 0.3s are not a forecast. Comparisons run only "
        "on the events every method actually scored, so a method cannot look better by skipping "
        "hard days. Holdout reports are blocked unless a study specification is frozen first.",
    )
    add_bullets(
        pdf,
        [
            "Spread census (pre-registered): median quoted spread at T−24h on two-sided books in the 10–90¢ band. Spreads of 4–6¢ are large enough that taking the market is usually uneconomic after fees.",
            "Window mismatch: NBM’s 12Z–06Z max window is close to, but not equal to, the CLI midnight-to-midnight LST climate day. The mismatch rate is measured, not assumed.",
            "Station basis: KLGA vs KNYC daily maxima; cross-venue bracket disagreement is a first-order instrument difference (about 61.5% of days in the published summary), not a trading edge by itself.",
            "Fair value: a gradient-boosted model that post-processes GEFS members, live observations, and order flow to correct market-implied probabilities. Quoting off that fair value, and reinforcement-learning quoting agents, are in design; this note does not describe live orders.",
            "Equation discovery: WSINDy-style sparse identification of drivers of the implied distribution, using the same weak-form tools as the honors thesis, applied here as a research probe rather than a production pricer.",
        ],
    )

    add_heading(pdf, "What I built")
    add_bullets(
        pdf,
        [
            "A production-quality Kalshi logger and a Polymarket logger: configurable poll cadences, rate limits, crash-safe JSONL, SIGTERM drain, kill -9 recovery, and user-level systemd units.",
            "Laptop-only historical backfill (kept off the live heartbeat database), CLINYC parsers that preserve issuance time and the TIME-column label, and checks that candlesticks omit uneventful periods rather than missing data.",
            "NBM archive tooling that subsets GRIB via index files, plus a first-availability watch so latency assumptions are measured rather than guessed.",
            "Evaluation code for ladder scores, coverage/abstention tables, clustered uncertainty, and calibration diagnostics, with tests on constructed examples so plumbing is not mistaken for a market result.",
            "A reference market-making pricing core of pure functions (fees, coherent ladders, inventory terms) with no network, no credentials, and no order placement in this repository’s loggers.",
        ],
    )
    add_body(
        pdf,
        "Code and research notes: github.com/weather-capital-markets/kalshi-weather. "
        "Public market-data endpoints only. Settlement rules, stations, and precision change "
        "by venue and by date; each contract has to be checked before it is scored.",
    )

    PDF_PATH.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(PDF_PATH))


def _colormap(t):
    """Blue → teal → yellow → orange → red. t in [0, 1]."""
    stops = (
        (0.00, (22, 72, 148)),
        (0.22, (46, 140, 196)),
        (0.40, (92, 188, 168)),
        (0.55, (236, 214, 112)),
        (0.72, (228, 138, 52)),
        (0.88, (196, 62, 42)),
        (1.00, (128, 24, 36)),
    )
    if t <= 0:
        return stops[0][1]
    if t >= 1:
        return stops[-1][1]
    for i in range(1, len(stops)):
        t0, c0 = stops[i - 1]
        t1, c1 = stops[i]
        if t <= t1:
            u = (t - t0) / (t1 - t0)
            return tuple(int(a + (b - a) * u) for a, b in zip(c0, c1))
    return stops[-1][1]


def write_thumbnail():
    """Landscape advection–diffusion panel for the hero card. Illustration only."""
    import numpy as np

    W, H = 1600, 900
    left, top, right, bottom = 108, 86, 230, 78
    pw, ph = W - left - right, H - top - bottom
    pad = 48
    ny, nx = ph + 2 * pad, pw + 2 * pad
    yy = np.linspace(-0.08, 1.08, ny)[:, None]
    xx = np.linspace(-0.08, 1.08, nx)[None, :]

    temp = 54 + 24 * yy + 3.2 * np.sin(2 * np.pi * xx * 1.4 + 0.6)
    front = yy - (0.46 + 0.10 * np.sin(2 * np.pi * xx * 1.15 + 0.3))
    temp = temp + 12 * np.exp(-(front ** 2) / 0.010)
    temp = temp + 7.5 * np.exp(-((xx - 0.32) ** 2) / 0.018 - ((yy - 0.30) ** 2) / 0.014)
    temp = temp - 8.0 * np.exp(-((xx - 0.70) ** 2) / 0.028 - ((yy - 0.58) ** 2) / 0.020)

    kappa = 0.20
    for _ in range(36):
        padded = np.pad(temp, 1, mode="edge")
        ddx = temp - padded[1:-1, :-2]
        ddy = temp - padded[:-2, 1:-1]
        lap = (
            padded[:-2, 1:-1]
            + padded[2:, 1:-1]
            + padded[1:-1, :-2]
            + padded[1:-1, 2:]
            - 4 * temp
        )
        speed_x = 0.55 + 0.22 * np.sin(2 * np.pi * yy)
        speed_y = 0.16 + 0.10 * np.cos(2 * np.pi * xx)
        temp = temp - speed_x * ddx - speed_y * ddy + kappa * lap

    temp = temp[pad:-pad, pad:-pad]
    ny, nx = temp.shape
    tmin, tmax = 50.0, 86.0
    temp = np.clip(temp, tmin, tmax)
    norm = (temp - tmin) / (tmax - tmin)
    stops_t = np.array([0.00, 0.22, 0.40, 0.55, 0.72, 0.88, 1.00])
    stops_c = np.array(
        [
            [22, 72, 148],
            [46, 140, 196],
            [92, 188, 168],
            [236, 214, 112],
            [228, 138, 52],
            [196, 62, 42],
            [128, 24, 36],
        ],
        dtype=np.float64,
    )
    rgb = np.stack(
        [np.interp(norm, stops_t, stops_c[:, channel]) for channel in range(3)],
        axis=-1,
    ).astype(np.uint8)

    field = Image.fromarray(rgb, "RGB")
    img = Image.new("RGB", (W, H), "#f4f7fb")
    img.paste(field, (left, top))
    draw = ImageDraw.Draw(img)

    try:
        eq_font = ImageFont.truetype(str(FONT_DIR / "DejaVuSans.ttf"), 28)
        tick_font = ImageFont.truetype(str(FONT_DIR / "DejaVuSans.ttf"), 18)
        unit_font = ImageFont.truetype(str(FONT_DIR / "DejaVuSans-Bold.ttf"), 20)
    except OSError:
        eq_font = tick_font = unit_font = ImageFont.load_default()

    lats = (43, 42, 41, 40, 39)
    lons = (78, 77, 76, 75, 74)
    grid = (28, 39, 51, 90)
    for lat in lats:
        y = top + (43 - lat) / 4 * (ph - 1)
        draw.line([(left, y), (left + pw - 1, y)], fill=grid, width=1)
        draw.text((left - 12, y), f"{lat}°N", font=tick_font, fill="#1c2733", anchor="rm")
    for lon in lons:
        x = left + (78 - lon) / 4 * (pw - 1)
        draw.line([(x, top), (x, top + ph - 1)], fill=grid, width=1)
        draw.text((x, top + ph + 10), f"{lon}°W", font=tick_font, fill="#1c2733", anchor="mt")
    draw.rectangle([left, top, left + pw - 1, top + ph - 1], outline="#1c2733", width=2)

    step = 2
    smooth = temp
    for _ in range(2):
        padded_s = np.pad(smooth, 1, mode="edge")
        smooth = (
            padded_s[:-2, 1:-1]
            + padded_s[2:, 1:-1]
            + padded_s[1:-1, :-2]
            + padded_s[1:-1, 2:]
            + 4 * smooth
        ) / 8
    sample = smooth[::step, ::step]
    levels = (54, 58, 62, 66, 70, 74, 78, 82)

    def edge_point(va, vb, p, q):
        if va == vb:
            t = 0.5
        else:
            t = (level - va) / (vb - va)
            t = 0.0 if t < 0 else 1.0 if t > 1 else t
        return (p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t)

    segments = {
        1: (3, 2), 2: (2, 1), 3: (3, 1), 4: (0, 1),
        5: (0, 3, 1, 2), 6: (0, 2), 7: (0, 3), 8: (0, 3),
        9: (0, 2), 10: (0, 1, 2, 3), 11: (0, 1), 12: (3, 1),
        13: (2, 1), 14: (3, 2),
    }
    sh, sw = sample.shape
    for level in levels:
        for i in range(1, sh - 2):
            row = sample[i]
            nxt = sample[i + 1]
            for j in range(1, sw - 2):
                va, vb = float(row[j]), float(row[j + 1])
                vc, vd = float(nxt[j + 1]), float(nxt[j])
                code = (va >= level) << 3 | (vb >= level) << 2 | (vc >= level) << 1 | (vd >= level)
                if code in (0, 15):
                    continue
                corners = (
                    (j * step, i * step),
                    ((j + 1) * step, i * step),
                    ((j + 1) * step, (i + 1) * step),
                    (j * step, (i + 1) * step),
                )
                values = (va, vb, vc, vd)
                edges = (
                    edge_point(values[0], values[1], corners[0], corners[1]),
                    edge_point(values[1], values[2], corners[1], corners[2]),
                    edge_point(values[2], values[3], corners[2], corners[3]),
                    edge_point(values[3], values[0], corners[3], corners[0]),
                )
                seq = segments[code]
                for k in range(0, len(seq), 2):
                    e0, e1 = edges[seq[k]], edges[seq[k + 1]]
                    x0, y0 = left + e0[0], top + e0[1]
                    x1, y1 = left + e1[0], top + e1[1]
                    draw.line([(x0, y0), (x1, y1)], fill=(28, 39, 51), width=4)
                    draw.line([(x0, y0), (x1, y1)], fill=(255, 255, 255), width=2)

    bar_x = left + pw + 28
    bar_w = 22
    col = np.zeros((ph, bar_w, 3), dtype=np.uint8)
    for y in range(ph):
        col[y, :] = _colormap(1 - y / (ph - 1))
    bar = Image.fromarray(col, "RGB")
    img.paste(bar, (bar_x, top))
    draw.rectangle([bar_x, top, bar_x + bar_w - 1, top + ph - 1], outline="#1c2733", width=1)
    draw.text((bar_x + bar_w + 36, top - 4), "°F", font=unit_font, fill="#1c2733", anchor="lt")
    for value in (50, 60, 70, 80):
        y = top + (tmax - value) / (tmax - tmin) * (ph - 1)
        draw.line([(bar_x + bar_w, y), (bar_x + bar_w + 8, y)], fill="#1c2733", width=1)
        draw.text((bar_x + bar_w + 12, y), str(value), font=tick_font, fill="#1c2733", anchor="lm")

    draw.text((left, 36), "∂t T + v·∇T = κ∇²T", font=eq_font, fill="#1c2733", anchor="lt")

    THUMB_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(THUMB_PATH, "PNG", optimize=True)

if __name__ == "__main__":
    write_pdf()
    write_thumbnail()
    print("wrote", PDF_PATH, "bytes", PDF_PATH.stat().st_size)
    print("wrote", THUMB_PATH, "bytes", THUMB_PATH.stat().st_size)
