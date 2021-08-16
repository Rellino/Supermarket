# Supermarket Markov Chain Simulation 
*by Statistically Significant Four*

![MCMC Simulation](Simulator.gif)
A Monte Carlo Markov Chain simulation to predict the customers' behavior in a hypothetical supermarket with below layout:


![Supermarket layout](supermarkt.png)

## Usage
`$ python supermarket.py` 

## Repo Structure

### 1. MCMC Simulation
- supermarket.py -> the executable script that runs the simulation
- proba.py -> the calculation of the transition matrix
- visualization.py -> for an old-fashioned videogame-like visualization of the Monte Carlo Simulation
- output -> folder with the simulation output data 

### 2. Notebooks
- EDA.ipynb -> exploratory data analysis on the raw data
- theory.ipynb -> summary on Markov-Chains theory

### 3. Data
- data -> The daily supermarket raw data that form the dataset of this model (in csv format)
- data/cleaned-up -> crean data created in EDA.ipynb, and ready for calucating the transition matrix

### 4. Output
- MCMC_Simulation -> The results of the simulation in .csv file after running supermarket.py 
- dungeon_supermarket map -> buited in visualization.py


#### Credits
This project was done in collaboration with Francesco Mari, Behzad Azarhoushang & Vlasis Tritakis.

