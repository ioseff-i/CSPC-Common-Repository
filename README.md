# CSPC — Computer Science for Physics and Chemistry

My coursework repository for the course.
Each practical lives under `PW<n>/Lab <X>/`.

## Setup

Create and activate the environment for a given lab:

```bash
conda env create -f "PW<n>/Lab <X>/environment.yml"
conda activate cspc


PW1 — Lab A: Reproducible Foundations & Radioactive Decay Simulation
What I built:

Configured the CSPC repository environment, developed a stochastic radioactive decay simulation in Python using both loops and NumPy, and implemented unit tests.

Speed Comparison Results:

Pure-Python loop time: 2.7887 seconds

NumPy vectorised time: 0.0003 seconds

Speed-up factor: ~9176.89x faster

Test Status:

pytest -v output: 3 passed in 0.12s

Conclusion:

Using NumPy's vectorised operations significantly outperforms pure-Python loops for simulating radioactive decay, reducing execution time drastically while maintaining accurate stochastic results.



PW1 — Lab B: Automated Workflows
Results & Analysis:

The observed decay data follows an exponential decrease over time. Based on the generated figure, the experimental data points closely match the theoretical analytical law, demonstrating the expected decay behavior.

Pipeline Automation:

The Snakemake pipeline automates the generation of figure.png from decay_observed.csv using plot.py, rebuilding the visualization only when input files are modified.


PW2 — Lab A: Numerical Differentiation & Integration
Mean Acceleration Measured: -8.58 m/s²

Why Acceleration is Noisy: Differentiating data compares adjacent points, which magnifies small measurement errors; taking two derivatives amplifies this noise significantly compared to the smooth position curve. Numerical differentiation acts as a high-pass filter that magnifies small, random noise present in the position data, causing double differentiation to severely swamp the acceleration values with noise.

Integration Results: Integrating back acts as a summation process that averages and cancels out random noise, successfully recovering the original position within 1 meter.
