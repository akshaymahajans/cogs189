# COGS 189 - Neurosky headset for classifying musical genres

# Motivation
Music is part of everyday life and we are interested in seeing if musical genres elicit different EEG responses and if they can be separated and identified according to their respective genres. For instance, there could be differences in amplitude and frequency of EEG signals for users listening to hip-hop vs EDM (electronic dance music).

# Purpose
We aim to classify musical genres based on the EEG data.

# Methods
We used the NeuroSky Mindwave Mobile headset to record our EEG data. To collect data for our project, we had to install a Windows OS on our Mac machine to get the programs to work. We used the 32-bit version of the thinkgear_testapp C program provided by NeuroSky's Windows Developer Tools 3.2.

# Classification
- To classify our data, we used Scikit-learn to split our data into training and testing sets, and to develop models for classificaiton. The two models we explored were binary logisitic regression and support vector machines.

# Dependencies
- NumPy
- pandas
- Scikit-learn
