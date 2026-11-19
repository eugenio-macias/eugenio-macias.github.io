---
layout: default
title: Projects
---

<section class="projects-page">
  <header class="projects-hero">
    <h1>Projects</h1>
    <p>Selected work in scientific machine learning, prediction markets, and quantitative research. Thumbnails open the project PDF.</p>
  </header>

  <article class="project-card hero-card">
    <div class="pc-text">
      <h2 class="pc-title">Machine learning on weather prediction markets</h2>
      <p class="pc-sub">2026–present · Kalshi KXHIGHNY and international Polymarket NYC daily-high ladders</p>
      <p class="pc-desc">
        Kalshi lists a daily ladder of contracts on New York City’s maximum temperature. Each strike is a yes/no on a temperature bracket; together they are supposed to partition the day’s high. International Polymarket lists a related NYC ladder. The venues do not settle the same observation: Kalshi currently names The Weather Company’s CLINYC report, while the Polymarket collector in this project records NOAA KLGA hourly observations. Same-city contracts are not the same instrument.
      </p>
      <p class="pc-desc">
        The work is forecast verification and data infrastructure. I ask whether market-implied probabilities beat NOAA’s National Blend of Models on proper scores (Brier, with Murphy’s reliability/resolution split, and ranked probability score on the ordered ladder), at which horizons, and after the climate day is defined carefully. I also ask whether a statistical model that sees ensemble weather, live observations, and order flow can correct those implied probabilities, and whether quoted spreads at T−24h leave any room for a taker.
      </p>
      <details>
        <summary>Data, methods, and what I built</summary>
        <ul class="bullets">
          <li>
            <strong>Data.</strong>
            Kalshi public market metadata, order books, and trades, written as crash-safe gzip JSONL with an HTTP heartbeat. Historical candlesticks covering thousands of KXHIGHNY contracts from August 2021. CLINYC climate-report text from the Iowa Environmental Mesonet, used as settlement labels when they match the venue’s snapshot rule at the time. NOAA NBM percentile ladders from the public AWS/NOMADS blend archive, read with HTTP byte-range requests against <code>.idx</code> sidecars. IEM ASOS observations at KNYC and KLGA. Polymarket Gamma discovery plus CLOB books in a separate heartbeat file.
          </li>
          <li>
            <strong>Methods.</strong>
            Ranked probability score on the ordered temperature ladder; multi-category Brier and a floored log score. Murphy decomposition of Brier into reliability, resolution, and uncertainty. Clustered bootstrap over climate days. Forecasts that are not a distribution over the ladder are refused or explicitly renormalized. Pre-registered spread census at T−24h on two-sided 10–90¢ books: 4–6¢ spreads typically kill takers after fees. Station-basis between KLGA and KNYC (about 61.5% bracket disagreement in the published summary). Window mismatch between NBM’s 12Z–06Z max window and the CLI LST climate day, measured rather than assumed. A gradient-boosted model post-processing GEFS members, live observations, and order flow. WSINDy-style driver discovery as a research probe. Reinforcement-learning quoting agents are in design; this page does not describe live orders.
          </li>
          <li>
            <strong>What I built.</strong>
            Production Kalshi and Polymarket loggers (configurable cadences, rate limits, SIGTERM drain, kill -9 recovery, systemd). Laptop-only historical backfill kept off the live heartbeat database. CLINYC parsers that keep issuance time and the TIME-column label. NBM archive tooling and a first-availability watch. Evaluation code with coverage/abstention tables and tests on constructed examples. A reference market-making pricing core of pure functions with no network, no credentials, and no order placement in the loggers.
          </li>
        </ul>
      </details>
      <div class="badges">
        <span class="badge">Prediction markets</span><span class="badge">Forecast verification</span>
        <span class="badge">NBM</span><span class="badge">Kalshi</span><span class="badge">Polymarket</span>
      </div>
      <div class="pc-links">
        <a class="pc-link" href="{{ '/assets/files/Kalshi_Weather.pdf' | relative_url }}" target="_blank" rel="noopener">Project PDF</a>
        <a class="pc-link" href="https://github.com/weather-capital-markets/kalshi-weather" target="_blank" rel="noopener">Code</a>
      </div>
    </div>
    <a class="thumb-link pc-media" href="{{ '/assets/files/Kalshi_Weather.pdf' | relative_url }}" target="_blank" rel="noopener">
      <img src="{{ '/assets/images/thumbnails/kalshi_weather_thumbnail.png' | relative_url }}" alt="Temperature-ladder sketch for the Kalshi weather project">
      <div class="overlay">Open PDF</div>
    </a>
  </article>

  <article class="project-card hero-card">
    <div class="pc-text">
      <h2 class="pc-title">Honors thesis — weak-form PDE discovery for stochastic collective dynamics</h2>
      <p class="pc-sub">Advisor: Prof. Björn Sandstede · Brown University</p>
      <p class="pc-desc">
        Applied WSINDy to recover interpretable coupled PDEs for macroscopic density evolution from noisy Vicsek-alignment and Morse attraction–repulsion trajectories. Sparsity via MSTLS; time integration via ETDRK4. Density fit R² &gt; 0.99 in 8 of 9 regimes; momentum closure failed, which led to a closure-imbalance diagnostic. Equation-free ROMs (FFT symmetry reduction, POD): a 1,824-parameter MVAR matched a much larger LSTM. Open-source package with simulator, coarse-graining, WSINDy, ETDRK4, and reproduction scripts.
      </p>
      <details>
        <summary>Technical scope</summary>
        <ul class="bullets">
          <li>Sobolev/Galerkin weak form with compactly supported test functions; convolutional weak form in place of unstable pointwise derivatives.</li>
          <li>Sparse regression over a flux-form operator library: Vicsek alignment transport, Morse-type attraction–repulsion, manifold diffusion.</li>
          <li>Trajectory restriction with geodesic KDE; POD/SVD including an explicit mass/mean mode; latent evolution by MVAR, with LSTM as a nonlinear comparator.</li>
          <li>Robustness: initial-condition families, KDE bandwidths, support scales, particle number, false-positive controls, synthetic PDEs.</li>
        </ul>
      </details>
      <div class="badges">
        <span class="badge">PDEs</span><span class="badge">WSINDy</span><span class="badge">ROMs</span>
        <span class="badge">Uncertainty</span>
      </div>
      <div class="pc-links">
        <a class="pc-link" href="{{ '/Thesis.pdf' | relative_url }}" target="_blank" rel="noopener">Thesis PDF</a>
        <a class="pc-link" href="{{ '/Thesis_presentation.pdf' | relative_url }}" target="_blank" rel="noopener">Slides</a>
      </div>
    </div>
    <a class="thumb-link pc-media" href="{{ '/Thesis.pdf' | relative_url }}" target="_blank" rel="noopener">
      <img src="{{ '/assets/images/thumbnails/Thesis_thumbnail.png' | relative_url }}" alt="Thesis thumbnail">
      <div class="overlay">Open PDF</div>
    </a>
  </article>

  <div class="projects-grid top5-grid">

    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">Optimizing the optimizer: self-scaled quasi-Newton methods for PINNs</h3>
        <p class="pc-sub">Karniadakis Lab · with Don C. Wong · January–May 2026</p>
        <p class="pc-desc">
          PINNs on the fourth-order Cahn–Hilliard equation on [0,128]². Benchmarked Adam, BFGS, L-BFGS-B, and self-scaled BFGS/Broyden variants. Self-scaled Broyden cut relative L₂ error to 0.32 versus 0.79 for L-BFGS-B on the 64² domain (three seeds). Nested autodiff residuals, periodic boundary conditions, RAD sampling, 53 configurations and 100+ seeded runs on SLURM, checked against a pseudo-spectral ETDRK4 reference.
        </p>
        <div class="badges">
          <span class="badge">PINNs</span><span class="badge">Quasi-Newton</span><span class="badge">Cahn–Hilliard</span>
        </div>
        <div class="pc-links">
          <a class="pc-link" href="{{ '/DRP_paper.pdf' | relative_url }}" target="_blank" rel="noopener">Paper</a>
          <a class="pc-link" href="{{ '/DRP_poster.pdf' | relative_url }}" target="_blank" rel="noopener">Poster</a>
        </div>
      </div>
      <a class="thumb-link pc-media" href="{{ '/DRP_paper.pdf' | relative_url }}" target="_blank" rel="noopener">
        <img src="{{ '/assets/images/thumbnails/DRP_thumbnail2.png' | relative_url }}" alt="PINN optimizer study thumbnail">
        <div class="overlay">Open PDF</div>
      </a>
    </article>

    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">Curiosity-driven transfer in ProcGen</h3>
        <p class="pc-sub">Advisor: Prof. George Konidaris</p>
        <p class="pc-desc">
          PPO with an IMPALA-CNN backbone on ProcGen. Factorial sweep over ICM, RND, CFN, and NLL-Surprise, with clip/RMS normalization and η as primary variables. Zero-shot and fine-tuned transfer; CLIP reward shaping for semantics-aware coverage. Probed 507 PPO checkpoints on 12 Procgen games; an ICM cutoff lifted probe accuracy to 0.914 versus 0.812. Always-on curiosity collapsed features (rank about 4/256, 85.7% dead units).
        </p>
        <div class="badges">
          <span class="badge">RL</span><span class="badge">PPO</span><span class="badge">Curiosity</span>
        </div>
        <div class="pc-links">
          <a class="pc-link" href="https://github.com/harshitaggarwal01/TransferRL" target="_blank" rel="noopener">TransferRL</a>
          <a class="pc-link" href="{{ '/Reintegrating_AI_Course__Curiosity_Driven_Transfer_Learning___Final_Paper (13).pdf' | relative_url }}" target="_blank" rel="noopener">Paper</a>
        </div>
      </div>
      <a class="thumb-link pc-media" href="{{ '/Reintegrating_AI_Course__Curiosity_Driven_Transfer_Learning___Final_Paper (13).pdf' | relative_url }}" target="_blank" rel="noopener">
        <img src="{{ '/assets/images/thumbnails/Reintegrating_AI_thumbnail.png' | relative_url }}" alt="Curiosity-driven transfer thumbnail">
        <div class="overlay">Open PDF</div>
      </a>
    </article>

    <a class="project-card" href="{{ '/assets/files/electron_dynamics_DL.pdf' | relative_url }}" target="_blank" rel="noopener">
      <div class="pc-text">
        <h3 class="pc-title">Hamiltonian and symplectic networks for charged particle dynamics</h3>
        <p class="pc-desc">
          Poisson neural nets with PDE-residual losses learn Hamiltonian structure and invert for charge and mass. Symplectic/volume-preserving architectures aligned with the flow.
        </p>
        <div class="badges">
          <span class="badge">Symplectic NN</span><span class="badge">Physics-ML</span>
        </div>
        <span class="pc-cta">Open PDF</span>
      </div>
      <div class="pc-media">
        <img src="{{ '/assets/images/thumbnails/electron.png' | relative_url }}" alt="Charged particle dynamics thumbnail">
        <div class="overlay">Open PDF</div>
      </div>
    </a>

    <a class="project-card" href="{{ '/ECON_1750_PCA (1).pdf' | relative_url }}" target="_blank" rel="noopener">
      <div class="pc-text">
        <h3 class="pc-title">PCA investing: eigen-portfolios for market-neutral strategies</h3>
        <p class="pc-desc">
          PCA on returns, risk-normalized eigen-portfolios, out-of-sample Sharpe/IR, cumulative-return plots, dynamic allocation to limit look-ahead bias.
        </p>
        <div class="badges">
          <span class="badge">Quant</span><span class="badge">PCA</span>
        </div>
        <span class="pc-cta">Open PDF</span>
      </div>
      <div class="pc-media">
        <img src="{{ '/assets/images/thumbnails/PCA_thumbnail.jpg' | relative_url }}" alt="PCA investing thumbnail">
        <div class="overlay">Open PDF</div>
      </div>
    </a>

    <a class="project-card" href="{{ '/assets/files/Extended_Essay.pdf' | relative_url }}" target="_blank" rel="noopener">
      <div class="pc-text">
        <h3 class="pc-title">Fourier-series solutions of 2-D Laplace boundary-value problems</h3>
        <p class="pc-desc">
          About fifty pages on Fourier methods for 2-D Laplace with Dirichlet boundaries; L² convergence and truncation error.
        </p>
        <div class="badges">
          <span class="badge">Fourier</span><span class="badge">PDE</span>
        </div>
        <span class="pc-cta">Open PDF</span>
      </div>
      <div class="pc-media">
        <img src="{{ '/assets/images/thumbnails/EE_thumbnail.jpg' | relative_url }}" alt="Fourier analysis thumbnail">
        <div class="overlay">Open PDF</div>
      </div>
    </a>

  </div>

  <h2>More projects</h2>
  <div class="projects-grid">
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">Go hybrid agent (PyTorch, NumPy, OpenSpiel)</h3>
        <ul class="bullets">
          <li>Policy–value networks with α-β and MCTS; 60% win rate versus baselines.</li>
          <li>Cross-validated evaluation across board sizes and openings.</li>
        </ul>
      </div>
    </article>
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">Blackjack ReinforcedAI (Python, NumPy, Gymnasium)</h3>
        <ul class="bullets">
          <li>MDP state design (totals, dealer up-card, usable aces); value iteration (43%) and Q-learning (41%).</li>
          <li>100k+ Monte Carlo episodes.</li>
        </ul>
      </div>
    </article>
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">Cartpole control (Q-learning)</h3>
        <ul class="bullets">
          <li>Discrete to continuous approximation with engineered features and L1 regularization.</li>
        </ul>
      </div>
    </article>
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">SAT solving (GSAT / WalkSAT)</h3>
        <ul class="bullets">
          <li>Local-search SAT with randomized restarts; Sudoku and N-Queens CNF encodings.</li>
        </ul>
      </div>
    </article>
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">Time-series forecasting</h3>
        <ul class="bullets">
          <li>Bollinger bands, Monte Carlo, changepoints, ARIMA; E*TRADE API ingestion.</li>
        </ul>
      </div>
    </article>
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">Adversarial search</h3>
        <ul class="bullets">
          <li>Minimax with α-β pruning for Tic-Tac-Toe and Connect Four.</li>
        </ul>
      </div>
    </article>
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">Linear regression and bias–variance</h3>
        <ul class="bullets">
          <li>Ridge/LASSO; real and synthetic data; WHO life-expectancy prediction.</li>
        </ul>
      </div>
    </article>
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">Decision-tree algorithm (Java)</h3>
        <ul class="bullets">
          <li>CSV ingestion, impurity-based splits; up to 96% accuracy on large datasets.</li>
        </ul>
      </div>
    </article>
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">Game AI (ReasonML)</h3>
        <ul class="bullets">
          <li>Connect-4 on M×N boards; minimax with heuristics.</li>
        </ul>
      </div>
    </article>
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">Graph optimizer (Python)</h3>
        <ul class="bullets">
          <li>Dijkstra/BFS/DFS variants; tested on 500+ node graphs with multi-objective costs.</li>
        </ul>
      </div>
    </article>
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">ReasonML–Racket interpreter</h3>
        <ul class="bullets">
          <li>Pattern matching to evaluate Racket programs inside ReasonML.</li>
        </ul>
      </div>
    </article>
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">Mutex-safe database (C)</h3>
        <ul class="bullets">
          <li>Multithreaded server with a dynamic thread pool; 100+ concurrent clients.</li>
        </ul>
      </div>
    </article>
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">Unix shell (C)</h3>
        <ul class="bullets">
          <li>Parsing, I/O redirection, signal handling, and process control.</li>
        </ul>
      </div>
    </article>
  </div>
</section>
