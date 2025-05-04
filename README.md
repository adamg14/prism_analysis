# Prism Analysis

This repository contains analytical tools and visualisations for evaluationg an e-commerce loyalty scheme, cohort analysis and feature attribution to assess and enhance customer retention strategies


## 📊 A/B Testing: Evaluating Loyalty Scheme

The `AB_testing.py` script conducts an A/B test to compare different loyalty scheme tiers. It analyzes the `A_B_Test.csv` dataset to determine the effectiveness of each variant in driving customer engagement and revenue.

### Key Components:
- **Data Loading**: Imports customer interaction data from `A_B_Test.csv`.
- **Statistical Analysis**: Calculates conversion rates and performs significance testing between control and variant groups.
- **Visualisations**: Generates plots to illustrate performance differences across tiers/variant groups.


## 🧠 Feature Attribution: Understanding Influential Factors

The `feature_attribution.py` script identifies which features most significantly impact customer behavior and loyalty. 

### Key Components:
- **Attribution Analysis**: Applies techniques like first-touch channel and last-touch channel to identify which online advertisements are most effective in the introduction/conversion stages.
- **Visualisations**: Creates plots to visualize the contribution of each feature to the model's predictions.


## 📈 Cohort Analysis: Tracking Customer Retention Over Time

The `cohort_analysis.py` script performs cohort analysis to monitor customer retention and behavior over time. By grouping customers based on their acquisition period, it reveals trends and patterns in loyalty and engagement. This highlights the success in the analytical engineering performance, as these visualisations required zero lines of SQL code due to the pre-calculated and pre-aggregated of metrics within the marketing mart.


## 📁 Repository Structure

```plaintext
├── AB_testing.py
├── A_B_Test.csv
├── feature_attribution.py
├── cohort_analysis.py
├── cohort_data.csv
├── README.md```
