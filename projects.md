---
layout: default
title: Projects
---

<section class="projects-page">

  <!-- ====== HERO / TITLE ====== -->
  <header class="projects-hero">
    <h1 class="projects-hero-title">
      <span class="pht-main">Projects</span>
      <span class="pht-gl1" aria-hidden="true">Projects</span>
      <span class="pht-gl2" aria-hidden="true">Projects</span>
    </h1>
    <p class="projects-hero-sub">Selected work across <em>quantitative research</em>, <em>ML</em>, <em>optimization</em>, and <em>systems</em>.</p>
  </header>

  <!-- ====== HONORS THESIS (HERO CARD) ====== -->
  <article class="project-card hero-card">
    <div class="pc-text">
      <h2 class="pc-title">Honors Thesis — Weak-Form Sparse Cell-to-Cell Interaction PDE Discovery from Noisy Trajectories on Curved Manifolds: WSINDy & Equation-Free Latent Model</h2>
      <p class="pc-sub">Aug 2025 – Present · Brown University</p>
      <p class="pc-desc">
        Data-driven identification of interaction laws in collective dynamics on curved Riemannian manifolds;
        grounded in measure-theoretic probability and operator-theoretic dynamical systems (curvature, geodesics, Laplace–Beltrami).
      </p>

      <details>
        <summary>Full technical scope</summary>
        <ul class="bullets">
          <li>
            <strong>WSINDy (primary)</strong>
            <ul>
              <li>Sobolev/Galerkin weak formulation with inner products against compactly supported test functions (e.g., Bernstein polynomials or smooth partition-of-unity families).</li>
              <li>Convolutional weak form replacing unstable pointwise derivatives — robust to noise.</li>
              <li>Sparse regression over a flux-form operator library: Vicsek alignment transport, Morse-type attraction–repulsion, manifold diffusion.</li>
              <li>Stability/identifiability via multi-step thresholded least squares (MSTLS) with nondimensional preconditioning & column standardization.</li>
            </ul>
          </li>

          <li>
            <strong>Equation-Free Reduced-Order Model (EF-ROM, benchmark)</strong>
            <ul>
              <li>Trajectory restriction with geodesic KDE → smooth density “movies”.</li>
              <li>Compression using POD/SVD, including explicit mass/mean mode for conservation.</li>
              <li>Latent evolution via MVAR; LSTM sequence models as nonlinear comparators.</li>
              <li>Mass-conserving lifting back to full density fields for fast forecasts.</li>
            </ul>
          </li>

          <li>
            <strong>Spectral & topological diagnostics</strong>
            <ul>
              <li>Koopman/transfer-operator eigenstructure to reveal coherent modes.</li>
              <li>Persistent homology (Vietoris–Rips, barcodes) with bottleneck/Wasserstein distances to quantify geometric robustness under noise.</li>
            </ul>
          </li>

          <li>
            <strong>Stochastic/statistical evaluation</strong>
            <ul>
              <li>Finite-sample analysis & bootstrap uncertainty quantification.</li>
              <li>Parameter recovery under subsampling/observation noise.</li>
              <li>Out-of-sample generalization across initial conditions & manifolds.</li>
            </ul>
          </li>

          <li>
            <strong>Tooling & reproducibility</strong>
            <ul>
              <li>Python/Matlab with NumPy/SciPy, scikit-learn, and GPU-accelerated PyTorch or JAX.</li>
              <li>Modular, reproducible benchmarking pipeline for WSINDy vs EF-ROM.</li>
            </ul>
          </li>
        </ul>
      </details>

      <div class="badges">
        <span class="badge">PDEs</span><span class="badge">Operator Learning</span><span class="badge">Sparse Regression</span>
        <span class="badge">Riemannian Geometry</span><span class="badge">Uncertainty</span>
      </div>
      <div class="pc-links" style="margin-top:.8rem;">
        <a class="pc-link" href="{{ '/Thesis.pdf' | relative_url }}" target="_blank" rel="noopener"><i class="fas fa-file-pdf"></i> Thesis PDF</a>
        <a class="pc-link" href="{{ '/Thesis_presentation.pdf' | relative_url }}" target="_blank" rel="noopener"><i class="fas fa-chalkboard-teacher"></i> Slides</a>
      </div>
    </div>
    <div class="pc-media hero-media">
      <div class="hero-glow"></div>
      <div class="hero-grid"></div>
      <img src="{{ site.baseurl }}/assets/images/thumbnails/Thesis_thumbnail.png" alt="Thesis Thumbnail" style="position:relative;z-index:1;width:100%;height:100%;max-height:220px;object-fit:cover;border-radius:12px;opacity:.88;">
      <div class="overlay">View Thesis →</div>
    </div>
  </article>

  <!-- ====== 5-COL FEATURED GRID ====== -->
  <div class="projects-grid top5-grid">

    <!-- DRP — PINN Optimizer Study -->
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">DRP — Optimizing the Optimizer: Self-Scaled Quasi-Newton Methods for Physics-Informed Neural Networks</h3>
        <p class="pc-sub">Spring 2026 · Brown Applied Mathematics · Karniadakis Lab · with Don C. Wong</p>
        <p class="pc-desc">
          PINNs on the 4th-order Cahn–Hilliard phase-separation PDE
          ∂<sub>t</sub>U = D∇²(∇²U + a₂U + a₄U³) on [0,128]² face a severely ill-conditioned loss
          κ(∇²ℒ) ≫ 1. We benchmark 6 quasi-Newton variants against Adam: BFGS, L-BFGS-B,
          Self-Scaled BFGS (Oren–Luenberger &amp; Al-Baali), SSBroyden1, and SSBroyden2.
          SSBroyden2 — combining a BFGS-direction Broyden-class update with automatic Hessian
          self-scaling τ<sub>k</sub> ~ s<sub>k</sub>ᵀs<sub>k</sub>/y<sub>k</sub>ᵀs<sub>k</sub> —
          achieves the lowest relative L₂ error on both domains: ε<sub>L₂</sub> = 0.854 on 128²
          (vs. Adam 1.000) and ε<sub>L₂</sub> = 0.258 on 64² (best seed). 100+ experiments across
          53 configurations and 3 seeds.
        </p>
        <details>
          <summary>Key findings</summary>
          <ul class="bullets">
            <li>Adam warmup (500–1000 epochs) is essential for quasi-Newton secant-pair stability; zero warmup diverges.</li>
            <li>Frequent collocation resampling (N<sub>change</sub> = 200 iters) prevents overfitting to fixed point sets on 128².</li>
            <li>Power-law loss transform ℒ<sup>1/p</sup> (p = 4) flattens the loss landscape on 128² but is non-transferable to 64².</li>
            <li>RAD sampling (k₂ = 0.5) focuses collocation on high-residual regions; combined modifications interfere non-additively.</li>
            <li>Low collocation residual ≠ low ε<sub>L₂</sub>: physics-aware validation against ETDRK4 reference solver is necessary.</li>
          </ul>
        </details>
        <div class="badges">
          <span class="badge">PINNs</span><span class="badge">Quasi-Newton</span><span class="badge">Cahn–Hilliard</span>
          <span class="badge">Self-Scaled BFGS</span><span class="badge">Optimization</span>
        </div>
        <div style="margin-top:10px; display:flex; gap:12px; flex-wrap:wrap;">
          <a href="{{ '/DRP_paper.pdf' | relative_url }}" target="_blank" rel="noopener" style="font-weight:700; background:linear-gradient(90deg,var(--grad1),var(--grad2)); -webkit-background-clip:text; background-clip:text; color:transparent;">View Paper →</a>
          <a href="{{ '/DRP_poster.pdf' | relative_url }}" target="_blank" rel="noopener" style="font-weight:700; background:linear-gradient(90deg,var(--grad2),var(--grad3)); -webkit-background-clip:text; background-clip:text; color:transparent;">View Poster →</a>
        </div>
      </div>
      <div class="pc-media">
        <img src="{{ site.baseurl }}/assets/images/thumbnails/DRP_thumbnail2.png" alt="DRP Thumbnail">
        <div class="overlay">View →</div>
      </div>
    </article>

    <!-- RL Research — Curiosity-Driven Transfer -->
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">RL Research: Curiosity-Driven Transfer in ProcGen</h3>
        <p class="pc-sub">2025–2026 · Brown University · Advisor: Prof. George Konidaris</p>
        <p class="pc-desc">
          Factorial sweep over four intrinsic motivation signals — <strong>ICM</strong> (forward/inverse
          dynamics model), <strong>RND</strong> (random network distillation), <strong>CFN</strong>
          (count-based feature novelty), and <strong>NLL-Surprise</strong> — augmenting PPO with an
          IMPALA-CNN backbone on ProcGen. Normalization strategies (clip / RMS) and
          η ∈ {0.001–0.05} as primary variables. Zero-shot and fine-tuned transfer evaluated at 40%
          training cutoff; VLM-guided (CLIP) reward shaping explored for semantics-aware coverage.
        </p>
        <div class="badges">
          <span class="badge">RL</span><span class="badge">PPO</span><span class="badge">Curiosity</span>
          <span class="badge">Transfer Learning</span><span class="badge">ProcGen</span>
        </div>
        <div class="pc-links">
          <a class="pc-link" href="https://github.com/harshitaggarwal01/TransferRL" target="_blank" rel="noopener"><i class="fab fa-github"></i> TransferRL</a>
          <a class="pc-link" href="{{ '/Reintegrating_AI_Course__Curiosity_Driven_Transfer_Learning___Final_Paper.pdf' | relative_url }}" target="_blank" rel="noopener"><i class="fas fa-file-pdf"></i> Paper</a>
        </div>
      </div>
      <div class="pc-media">
        <img src="{{ site.baseurl }}/assets/images/thumbnails/Reintegrating_AI_thumbnail.png" alt="RL Research Thumbnail">
        <div class="overlay">View →</div>
      </div>
    </article>
    <a class="project-card" href="assets/files/electron_dynamics_DL.pdf" target="_blank" rel="noopener">
      <div class="pc-text">
        <h3 class="pc-title">Structure-Preserving Deep Learning for Charged Particle Dynamics</h3>
        <p class="pc-desc">
          Symplectic/Poisson/PINN architectures aligned with Hamiltonian flows; inverse problems for mass/charge;
          custom symplectic blocks & latent diffeomorphisms with volume-preserving checks.
        </p>
        <div class="badges">
          <span class="badge">Symplectic NN</span><span class="badge">Physics-ML</span><span class="badge">Dynamical Systems</span>
        </div>
        <span class="pc-cta">View PDF →</span>
      </div>
      <div class="pc-media">
        <img src="{{ site.baseurl }}/assets/images/thumbnails/electron.png" alt="Electron Dynamics Thumbnail">
        <div class="overlay">View PDF →</div>
      </div>
    </a>

    <!-- PCA Investing -->
    <a class="project-card" href="{{ '/ECON_1750_PCA (1).pdf' | relative_url }}" target="_blank" rel="noopener">
      <div class="pc-text">
        <h3 class="pc-title">PCA Investing: Eigen-Portfolios for Market-Neutral Strategies</h3>
        <p class="pc-desc">
          PCA on returns → risk-normalized eigen-portfolios; OOS evaluation (Sharpe/IR), cumulative-return
          visualizations, dynamic allocation to limit look-ahead bias.
        </p>
        <div class="badges">
          <span class="badge">Quant</span><span class="badge">PCA</span><span class="badge">Portfolio</span>
        </div>
        <span class="pc-cta">View PDF →</span>
      </div>
      <div class="pc-media">
        <img src="{{ site.baseurl }}/assets/images/thumbnails/PCA_thumbnail.jpg" alt="PCA Investing Thumbnail">
        <div class="overlay">View PDF →</div>
      </div>
    </a>

    <!-- Fourier / Laplace Research -->
    <a class="project-card" href="{{ '/assets/files/Extended_Essay.pdf' | relative_url }}" target="_blank" rel="noopener">
      <div class="pc-text">
        <h3 class="pc-title">Research: Fourier Analysis &amp; Laplace's Equation</h3>
        <p class="pc-desc">
          50-page analysis of Fourier methods for 2-D Laplace with Dirichlet boundaries; convergence
          criteria and solution space characterization.
        </p>
        <div class="badges">
          <span class="badge">Fourier</span><span class="badge">PDE</span><span class="badge">Analysis</span>
        </div>
        <span class="pc-cta">View PDF →</span>
      </div>
      <div class="pc-media">
        <img src="{{ site.baseurl }}/assets/images/thumbnails/EE_thumbnail.jpg" alt="Fourier Analysis Thumbnail">
        <div class="overlay">View PDF →</div>
      </div>
    </a>

  </div>

  <!-- ====== MORE PROJECTS ====== -->
  <h3 class="section-title">More Projects</h3>
  <div class="projects-grid">

    <!-- Go Hybrid Agent -->
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">Go Hybrid Agent (PyTorch, NumPy, OpenSpiel)</h3>
        <ul class="bullets">
          <li>Policy–value networks integrated with α-β and MCTS; 60% win-rate vs baselines.</li>
          <li>Cross-validated evaluation across board sizes/openings.</li>
        </ul>
        <div class="badges"><span class="badge">RL</span><span class="badge">Search</span></div>
      </div>
    </article>

    <!-- Blackjack ReinforcedAI -->
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">Blackjack ReinforcedAI (Python, NumPy, Gymnasium)</h3>
        <ul class="bullets">
          <li>MDP state design (totals, dealer up-card, usable aces); Value-Iteration (43%) & Q-Learning (41%).</li>
          <li>100k+ Monte Carlo episodes; policy improvement via state-action refinements.</li>
        </ul>
        <div class="badges"><span class="badge">RL</span><span class="badge">MDP</span></div>
      </div>
    </article>

    <!-- Cartpole -->
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">Cartpole Control (Q-Learning)</h3>
        <ul class="bullets">
          <li>From discrete to continuous approximation with engineered features + L1 regularization.</li>
          <li>Custom rewards balancing exploration & exploitation.</li>
        </ul>
        <div class="badges"><span class="badge">Control</span><span class="badge">RL</span></div>
      </div>
    </article>

    <!-- SAT Solving -->
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">SAT Solving (GSAT / WalkSAT)</h3>
        <ul class="bullets">
          <li>Local-search SAT with randomized restarts; Sudoku & N-Queens CNF encodings.</li>
        </ul>
        <div class="badges"><span class="badge">Algorithms</span><span class="badge">Search</span></div>
      </div>
    </article>

    <!-- Time Series -->
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">Time-Series Forecasting (ongoing)</h3>
        <ul class="bullets">
          <li>Bollinger bands, Monte Carlo, changepoints, ARIMA; real-time E*TRADE API ingestion.</li>
          <li>Planned: Backtrader integration; KPI dashboards.</li>
        </ul>
        <div class="badges"><span class="badge">Quant</span><span class="badge">TS</span></div>
      </div>
    </article>

    <!-- Adversarial Search -->
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">Adversarial Search</h3>
        <ul class="bullets">
          <li>Minimax + α-β pruning for Tic-Tac-Toe & Connect Four; scalable heuristics.</li>
        </ul>
        <div class="badges"><span class="badge">AI</span><span class="badge">Search</span></div>
      </div>
    </article>

    <!-- Bias-Variance -->
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">Linear Regression & Bias–Variance</h3>
        <ul class="bullets">
          <li>Ridge/LASSO; real + synthetic data; WHO life-expectancy prediction.</li>
        </ul>
        <div class="badges"><span class="badge">ML</span><span class="badge">Stats</span></div>
      </div>
    </article>

    <!-- Portfolio site -->
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">Personal Portfolio (GitHub Pages)</h3>
        <ul class="bullets">
          <li>Static site with responsive layout, deploy via GitHub Actions.</li>
        </ul>
        <div class="badges"><span class="badge">Web</span><span class="badge">DevOps</span></div>
      </div>
    </article>

    <!-- Decision Tree -->
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">Decision-Tree Algorithm (Java)</h3>
        <ul class="bullets">
          <li>CSV ingestion, impurity-based splits; up to 96% accuracy on large datasets.</li>
        </ul>
        <div class="badges"><span class="badge">ML</span><span class="badge">Java</span></div>
      </div>
    </article>

    <!-- ReasonML Game-AI -->
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">Game-AI (ReasonML)</h3>
        <ul class="bullets">
          <li>Connect-4 on M×N boards; minimax with heuristics outperforming human baselines.</li>
        </ul>
        <div class="badges"><span class="badge">AI</span><span class="badge">ReasonML</span></div>
      </div>
    </article>

    <!-- Graph Optimizer -->
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">Graph-Optimizer (Python)</h3>
        <ul class="bullets">
          <li>Dijkstra/BFS/DFS variants; tested on 500+ node graphs with multi-objective costs.</li>
        </ul>
        <div class="badges"><span class="badge">Algorithms</span><span class="badge">Graphs</span></div>
      </div>
    </article>

    <!-- ReasonML–Racket Interpreter -->
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">ReasonML–Racket Interpreter</h3>
        <ul class="bullets">
          <li>Advanced pattern matching to evaluate Racket programs (500+ LOC) inside ReasonML.</li>
        </ul>
        <div class="badges"><span class="badge">PL</span><span class="badge">Interpreters</span></div>
      </div>
    </article>

    <!-- Mutex DB -->
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">Mutex-Safe Database (C)</h3>
        <ul class="bullets">
          <li>Multithreaded server with dynamic thread pool; 100+ concurrent clients.</li>
        </ul>
        <div class="badges"><span class="badge">Systems</span><span class="badge">C</span></div>
      </div>
    </article>

    <!-- Unix Shell -->
    <article class="project-card">
      <div class="pc-text">
        <h3 class="pc-title">Unix Shell (C)</h3>
        <ul class="bullets">
          <li>Custom shell with parsing, I/O redirection, signal handling, and process control.</li>
        </ul>
        <div class="badges"><span class="badge">Systems</span><span class="badge">C</span></div>
      </div>
    </article>

  </div>
</section>

<style>
  :root{
    --bg:#fff; --ink:#0f172a; --muted:#6b7280; --line:#e5e7eb; --card:#fff;
    --grad1:#6366f1; --grad2:#06b6d4; --grad3:#22c55e;
    --shadow:0 10px 30px rgba(0,0,0,.08);
  }
  @media (prefers-color-scheme: dark){
    :root{
      --bg:#0a0b0e; --ink:#e5e7eb; --muted:#a3a3a3; --line:#1f2937; --card:#0f1115;
      --grad1:#7c83ff; --grad2:#22d3ee; --grad3:#34d399;
      --shadow:0 24px 50px rgba(0,0,0,.5);
    }
  }

  .top5-grid{
    grid-template-columns: repeat(5, 1fr) !important;
    margin-bottom: 24px;
  }
  .top5-grid .project-card{
    display: flex !important;
    flex-direction: column !important;
  }
  .top5-grid .project-card .pc-text{
    flex: 1;
  }
  .top5-grid .project-card .pc-media{
    order: -1;
    flex-shrink: 0;
    height: 100px;
    min-height: 0;
    max-height: 100px;
  }
  @media (max-width: 1100px){
    .top5-grid{ grid-template-columns: repeat(3, 1fr) !important; }
  }
  @media (max-width: 700px){
    .top5-grid{ grid-template-columns: 1fr !important; }
  }

  .projects-page{ max-width:1600px; margin:0 auto; padding:0 clamp(12px,2vw,32px); color:var(--ink); }
  .projects-hero{ text-align:center; margin:10px 0 24px; }

  /* Animated gradient title */
  .projects-hero-title{
    position:relative; display:inline-block;
    margin:0 0 .5rem; font-size:clamp(2.4rem,5vw,4rem);
    font-weight:900; letter-spacing:-.5px; line-height:1;
    background: linear-gradient(90deg, var(--grad1), var(--grad2), var(--grad3), var(--grad1));
    background-size: 300% 100%;
    -webkit-background-clip: text; background-clip: text;
    -webkit-text-fill-color: transparent; color: transparent;
    animation: gradientShift 5s linear infinite;
    filter: drop-shadow(0 0 22px rgba(124,131,255,.45));
  }
  /* Glitch layers */
  .pht-gl1, .pht-gl2{
    position:absolute; inset:0; pointer-events:none;
    background: inherit; -webkit-background-clip: text; background-clip: text;
    -webkit-text-fill-color: transparent; color: transparent;
    opacity:0;
  }
  .pht-gl1{ animation: phGlitchA  8s 0s   infinite linear; }
  .pht-gl2{ animation: phGlitchB 11s 1.8s infinite linear; }
  @keyframes phGlitchA{
    0%,87%,100%{ clip-path:none; transform:none; opacity:0; }
    89%{ clip-path:polygon(0 20%,100% 20%,100% 38%,0 38%); transform:translate(-4px,0); opacity:.8; }
    91%{ clip-path:polygon(0 55%,100% 55%,100% 70%,0 70%); transform:translate( 4px,0); opacity:.7; }
    93%{ clip-path:polygon(0 38%,100% 38%,100% 56%,0 56%); transform:translate(-2px,0); opacity:.6; }
    95%{ clip-path:none; transform:none; opacity:0; }
  }
  @keyframes phGlitchB{
    0%,81%,100%{ clip-path:none; transform:none; opacity:0; }
    83%{ clip-path:polygon(0 45%,100% 45%,100% 62%,0 62%); transform:translate( 3px,0); opacity:.7; }
    85%{ clip-path:polygon(0 10%,100% 10%,100% 28%,0 28%); transform:translate(-3px,0); opacity:.65; }
    87%{ clip-path:none; transform:none; opacity:0; }
  }

  /* Subtitle with animated word highlights */
  .projects-hero-sub{
    margin:.3rem 0 0; font-size:clamp(.95rem,1.4vw,1.1rem);
    color: var(--muted); letter-spacing:.01em;
  }
  .projects-hero-sub em{
    font-style:normal; font-weight:700;
    background: linear-gradient(90deg, var(--grad1), var(--grad2), var(--grad3), var(--grad1));
    background-size: 300% 100%;
    -webkit-background-clip: text; background-clip: text;
    -webkit-text-fill-color: transparent; color: transparent;
    animation: gradientShift 5s linear infinite;
  }
  .projects-hero-sub em:nth-child(2){ animation-delay:-.8s; }
  .projects-hero-sub em:nth-child(3){ animation-delay:-1.6s; }
  .projects-hero-sub em:nth-child(4){ animation-delay:-2.4s; }

  .section-title{
    margin:20px 0 10px; font-size:1.1rem; letter-spacing:.2px;
  }
  .section-title::after{
    content:""; display:block; height:2px; width:76px; margin-top:.35rem;
    background:linear-gradient(90deg,var(--grad1),var(--grad2),var(--grad3));
    border-radius:2px;
  }

  .projects-grid{
    display:grid; gap:14px; grid-template-columns:1fr;
    margin:0 0 24px;
  }
  @media (min-width:880px){
    .projects-grid{ grid-template-columns:1fr 1fr; }
  }

  /* ===== Card Base ===== */
  .project-card{
    position:relative; display:grid; grid-template-columns:1.4fr .9fr; gap:14px;
    text-decoration:none; color:inherit; background:var(--card); border:1px solid var(--line);
    border-radius:16px; padding:14px; box-shadow:var(--shadow);
    transition:transform .18s ease, box-shadow .18s ease, border-color .18s ease;
    overflow:hidden; isolation:isolate;
  }
  .project-card:hover{ transform:translateY(-3px); border-color:transparent; box-shadow:0 18px 40px rgba(0,0,0,.14); }
  .project-card .pc-title{
    margin:0 0 .35rem; font-size:1.02rem; line-height:1.25;
    background: linear-gradient(90deg, #7c83ff 0%, #22d3ee 35%, #34d399 65%, #a78bfa 85%, #7c83ff 100%);
    background-size: 300% 100%;
    -webkit-background-clip: text; background-clip: text;
    -webkit-text-fill-color: transparent; color: transparent;
    animation: pcTitleShift 5s linear infinite;
    filter: drop-shadow(0 0 12px rgba(124,131,255,.35));
  }
  .project-card:hover .pc-title {
    filter: drop-shadow(0 0 22px rgba(34,211,238,.65));
    animation-duration: 2.5s;
  }
  .hero-card .pc-title{ font-size:1.15rem; animation-duration:3.5s; filter: drop-shadow(0 2px 22px rgba(124,131,255,.55)); }
  @keyframes pcTitleShift {
    0% { background-position: 0% 50%; }
    100% { background-position: 300% 50%; }
  }
  .project-card .pc-desc{ margin:0; color:var(--muted); }
  .project-card .pc-sub{ margin:.1rem 0 .5rem; color:var(--muted); font-size:.92rem; }
  .project-card .pc-cta{ margin-top:.7rem; display:inline-block; font-weight:600; background:linear-gradient(90deg,var(--grad1),var(--grad2)); -webkit-background-clip:text; background-clip:text; color:transparent; }
  .pc-links{ display:flex; gap:10px; flex-wrap:wrap; margin-top:.65rem; }
  .pc-link{ display:inline-flex; align-items:center; gap:5px; padding:5px 12px; border-radius:999px; font-size:.85rem; font-weight:700; text-decoration:none; border:1px solid var(--line); color:var(--muted); transition:color .18s ease, border-color .18s ease, background .18s ease; }
  .pc-link:hover{ color:var(--ink); border-color:var(--grad1); background:rgba(124,131,255,.08); }
  .project-card .pc-media{ position:relative; border-radius:12px; overflow:hidden; border:1px solid var(--line); background:#0b0c0e; min-height:150px; }
  .project-card .pc-media img{ width:100%; height:100%; max-height:190px; object-fit:cover; display:block; transform:scale(1.02); opacity:.93; transition:transform .35s ease, opacity .35s ease; }
  .project-card:hover .pc-media img{ transform:scale(1.06); opacity:1; }
  .overlay{ position:absolute; inset:0; display:grid; place-items:end; padding:10px; color:#fff; font-weight:700; font-size:.92rem; opacity:0; transition:opacity .25s ease;
            background:linear-gradient(180deg,rgba(0,0,0,0) 40%,rgba(0,0,0,.6) 86%); }
  .project-card:hover .overlay{ opacity:1; }

  .bullets{ margin:.35rem 0 0 1.1rem; padding:0; }
  .bullets li{ margin:.25rem 0; }
  /* nested list spacing */
  .bullets ul{ margin:.35rem 0 .25rem 1.1rem; }

  .badges{ margin-top:.6rem; display:flex; flex-wrap:wrap; gap:6px; }
  .badge{ font-size:.72rem; padding:3px 8px; border-radius:999px; color:#fff; background:linear-gradient(90deg,var(--grad1),var(--grad2)); }
  .badge:nth-child(3n){ background:linear-gradient(90deg,var(--grad2),var(--grad3)); }
  .badge:nth-child(3n+2){ background:linear-gradient(90deg,var(--grad3),var(--grad1)); }

  /* ===== Hero Card Variant ===== */
  .hero-card{ grid-template-columns:1.5fr .8fr; margin-bottom:8px; }
  .hero-card .pc-title{ font-size:1.15rem; }
  @media (min-width:880px){
    .hero-card{ grid-column:1 / -1; }
  }
  .hero-media{ position:relative; display:grid; place-items:center; }
  .hero-glow{
    position:absolute; width:120%; height:120%; filter:blur(38px); opacity:.55; z-index:-1;
    background:radial-gradient(60% 60% at 50% 50%, rgba(99,102,241,.30), rgba(34,197,94,.12) 60%, rgba(6,182,212,.08) 80%, transparent 100%);
  }
  .hero-grid{
    --s:18px;
    position:absolute; inset:10px; border-radius:12px; opacity:.22; mix-blend:screen;
    background:
      linear-gradient(90deg, rgba(255,255,255,.06) 1px, transparent 1px) calc(var(--s)/2) 0 / var(--s) var(--s),
      linear-gradient(   0, rgba(255,255,255,.06) 1px, transparent 1px) 0 calc(var(--s)/2) / var(--s) var(--s),
      linear-gradient(90deg, rgba(0,0,0,.20), rgba(0,0,0,0));
    border:1px solid var(--line);
  }

  /* ===== Accessibility & Mobile ===== */
  @media (max-width:680px){
    .project-card{ grid-template-columns:1fr; }
    .hero-card{ grid-template-columns:1fr; }
    .project-card .pc-media{ order:-1; min-height:140px; }
  }
</style>
