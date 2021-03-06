# Detereminig-Trustworhiness-of-IoT-crowdsensing-Data

Master's Project:  The trustworthiness of data is one of the important aspects taken into consideration in Mobile crowd sensing context where number of users submit the data which can be false or malicious and eventually affect future predictions. In this project trustworthiness of data is determined on the crowdsensing data related to traffic and transportation domain where various users submit road traffic information which can help to determine the shortest path of travel and other traffic related parameters. This project aims to implement trustworthiness model based on voting mechanism where game theory is used to motivate participants or users to submit crowdsensing data and based on the votes submitted by user then parameters such as voting capacity, user reputation, user pay-off and trustworthiness are calculated. Another model implemented to evaluate trust on different user’s data is based on concept of Experience and Reputation where Experience is calculated based on how many times the user interacts with other user. Rewards are given to each user in the form of badges based on their reputation values. The stability of both algorithms is checked by performing it for several number of times.

1. Languages used: Python for Algorithm Implementation and JSON to create Data Set. 
2. Software or Tools Used: Jupyter Notebook and SUMO (SIMULATION OF URBAN MOBILITY)

Keywords—crowdsensing, trustworthiness, voting, experience, incentive, reputation, Game Theory, IoT, Urban Mobility.

The implementation to determine trustworthiness of data was done using the two models SONATA and REK model and can observe that both models has stable outcomes after few iterations i.e. running algorithm for certain period. The Experience of users was tending to move towards 1 which is the ideal case in the REK model, voting capacity after few iterations seems to be stable as compared to running algorithm for the first time. If the voters trying to vote positive votes and come under the criteria of threshold then vote capacity is stable.  Trustworthiness of users is set between values 0,1 and -1 for all users. The number of times the algorithm is implemented on the resulted data the reputation of users is increasing then previous values in both the models. The experience and voting capacity are tending to move towards the stable values after every successful run of algorithm. 
 
Future Scope: The following algorithms can be implemented on the simulation software to understand the behavior of users in the road traffic scenarios. Trustworthiness can be made accurate by implementing more efficient and strong incentive techniques which will motivate users to contribute accurate and useful information. The combination of SONATA and REK model can be an option to improvise the result and achieve the goal of to determine trustworthiness of data and eliminate malicious users.

Implementaion: Trust_Algorithm.py
Jupter Notebook Version : TrustworthinessAlgorith.ipynb.


Project Document: project_portfolio.pdf 
Input Files: .json format
Output files: .xlxs format.

#For Simulation on Simulation of Urban Mobility :

Steps:
Update 1:
1.	Python 3.7.3 Installation 
2.	 SUMO 1.2.0 Installation
3.	Download OSM (Open Street Map) files of few areas
4.	Use Random trip command of SUMO to check random Outputs of OSM files. For example I am using OSM map of Santry Avenue Dublin 9
5.	Three files are generated Santry.rou, sentry.rou.alt, trips,trips.
6.	
7.	If the same command is run again the values in the file Santry.rou, sentry.rou.alt, trips,trips changes and gets updated
8.	Setup the Configuration file and run the network on SUMO. Configuration file name- santry.sumocfg (.sumocfg extension for configuration file for sumo).
9.	After Running Configuration File of the network which was imported from Open Street Map
Delay was set to 100 to observe what’s going on 


