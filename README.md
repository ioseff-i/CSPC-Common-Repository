# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.
## Setup
Create the environment for a given lab:
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc
---
## PW1 - Lab A: Reproducible Foundations
**What I built:**
- To test a radioactive decay simulation which is given by decay.py via test_decay.py and compare the speed of pure python code vs numpy code via speed.py documents.
**Speed comparison (loop vs NumPy):**
- loop : 1.7689 s
- numpy : 0.000135 s
- speed-up: 13,107 x faster
**Tests:** all passing? yes
**Conclusion:**
- In test_decay.py, all three tests passed. Observed that the speed of numpy is 13,107 times faster than pure python code. Using numpy library and pytest commands are practised, such as "pytest.raises", pytest.approx. The main problem was understanding the behaviour of "TODO 2" on teast_decay.py file, but the commands were searched and the logic behind it was succesfully understood.
---
## PW1 - Lab B: Data, Plotting, and Automation
**What I built:**
- plot.py file was completed by python shell, which is the main code for creating figure.png file. The project was automated by snakemake file which has "decay_observed.csv" as input, "figure.png" as output, and "python plot.py" as shell. 
**Test:** Did the data match the analytical law? yes
**Conclusion:**
- The data in "figure.png" showed the difference between observed and analytical data with scatter and line data graphics. The Snakemake pipeline automated the project, it means every time the data changed, the output figure can be changed by snakemake automatically, it was confirmed by running it in different conditions.
