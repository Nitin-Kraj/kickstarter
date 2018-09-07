
# Kickstarter Predictor

This repository contains a python package that explores different supervised learning models to predict the success of Kickstarter campaigns. The current classification models and their obtained classification accuracies are as follows: 

| Model | Train ACC | Test ACC |
| ------------- | ------------- | ------------- |
| K-Neighbors  | 95.6% | 94.8% |
| Naive BAyes  | 74.4%  | 74.3% |
| DecisionTree | 99.9%  | 99.8 |
| DecisionTree/AdaBoost  | 100.0%  | 99.8%|
| Random/AdaBoost  | 99.9%  | 99.9% |
| RandomForest/AdaBoost  | 99.9 | 99.9% |

## Methodology
The current implementation of this project utilizes the following models for the Kickstarter prediction problem: 

- K-Nearest Neighbor
- Naive Bayes
- Decision Tree
- Decision Tree - AdaBoost
- Random Forest
- Random Forest - AdaBoost

## Data
Kickstarter is one of the main online crowd funding platforms in the world. The dataset provided contains more de 300,000 projects launched on the platform in 2018. In the `data.csv` file there are the following columns:

- **ID**: internal ID, _numeric_
- **name**: name of the project, _string_
- **category**: project's category, _string_
- **main_category**: campaign's category, _string_
- **currency**: project's currency, _string_
- **deadline**: project's deadline date, _timestamp_
- **goal**: fundraising goal, _numeric_
- **launched**: project's start date, _timestamp_
- **pledged**: amount pledged by backers (project's currency), _numeric_
- **state**: project's current state, _string_; **this is what you have to predict**
- **backers**: amount of poeple that backed the project, _numeric_
- **country**: project's country, _string_
- **usd pledged**: amount pledged by backers converted to USD (conversion made by KS), _numeric_
- **usd_pledged_real**: amount pledged by backers converted to USD (conversion made by fixer.io api), _numeric_
- **usd_goal_real**: fundraising goal is USD, _numeric_

## Requirements
- numpy             1.15.0
- pandas            0.23.4
- scikit-learn      0.19.1
- matplotlib        2.2.3
- seaborn           0.9.0

## Directory Structure
```
.
├── image           
├── kickstarter     <- source files used in this projects 
│   ├── data        <- Ipython notebook filesa
│   │   ├── ext     <- Processed data files 
│   │   └── raw     <- Raw data files 
│   └── model       <- Classificatin models 
└── notebooks       <- Ipython notebook files 

```
## Installation
Install python dependencies from  `requirements.txt` using conda:
```bash
conda install --yes --file conda-requirements.txt
```

Or create a new conda environment `<new-env-name>` by importing a copy of the working conda environment `conda-kickstarter.yml` at the project root directory:
```bash
conda env create --name <new-env-name> -f conda-kickstarter.yml
```
## Usage

The notebook runner for data exploration:
```bash
./notebooks/0.1.explore.data
```
The notebook runner for classification:
```
./notebooks/1.1.classify.kickstarter.state
```

## References

## License
MIT License


