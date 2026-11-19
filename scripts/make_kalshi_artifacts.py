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


def write_thumbnail():
    w, h = 1200, 720
    img = Image.new("RGB", (w, h), "#e8edf2")
    d = ImageDraw.Draw(img)
    # staff lines
    for i in range(5):
        y = 90 + i * 38
        d.line([(80, y), (w - 80, y)], fill="#9aa7b4", width=3)
    # temperature ladder as note heads
    xs = [180, 340, 500, 660, 820, 980]
    labels = ["59−", "60–61", "62–63", "64–65", "66–67", "68+"]
    fills = ["#2d5c52", "#6e322c", "#9a7040", "#2d5c52", "#6e322c", "#1c2733"]
    for x, lab, fill in zip(xs, labels, fills):
        cy = 90 + 2 * 38
        d.ellipse([x - 22, cy - 16, x + 22, cy + 16], fill=fill)
        d.line([(x + 20, cy), (x + 20, cy - 92)], fill=fill, width=4)
    try:
        title_font = ImageFont.truetype(str(FONT_DIR / "DejaVuSerif-Bold.ttf"), 48)
        sub_font = ImageFont.truetype(str(FONT_DIR / "DejaVuSans.ttf"), 22)
        small = ImageFont.truetype(str(FONT_DIR / "DejaVuSans.ttf"), 18)
    except OSError:
        title_font = sub_font = small = ImageFont.load_default()
    d.text((80, 340), "KXHIGHNY", font=title_font, fill="#1c2733")
    d.text(
        (80, 410),
        "NYC daily high  ·  Kalshi and Polymarket  ·  NBM, CLINYC, ASOS",
        font=sub_font,
        fill="#5a6878",
    )
    d.text((80, 470), "Forecast verification on an ordered temperature ladder", font=sub_font, fill="#5a6878")
    for x, lab in zip(xs, labels):
        d.text((x - 28, 290), lab, font=small, fill="#5a6878")
    THUMB_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(THUMB_PATH, "PNG", optimize=True)


if __name__ == "__main__":
    write_pdf()
    write_thumbnail()
    print("wrote", PDF_PATH, "bytes", PDF_PATH.stat().st_size)
    print("wrote", THUMB_PATH, "bytes", THUMB_PATH.stat().st_size)
