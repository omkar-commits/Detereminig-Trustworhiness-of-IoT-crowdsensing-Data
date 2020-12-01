
# coding: utf-8

# In[ ]:


#Determining Trustworthiness of Data in IoT Crowd Sensing Environments 


# In[1]:


import json
from math import sin, cos, sqrt, atan2, radians
with open('F:\Project material\TTT\opdata\\reportcollision17-18.json') as a:
    collision = json.load(a)

with open('F:\Project material\TTT\opdata\\userVotedData.json') as b:
    voting = json.load(b)
    
with open('F:\Project material\TTT\opdata\\usersdata.json') as c:
    users = json.load(c)


# In[2]:


import pandas as pd
df_voting = pd.DataFrame(voting)
# list(tusers)


# In[3]:


df_voting.to_excel('C:\\Users\OMKAR\Desktop\VotingData.xlsx')


# In[4]:


import pandas as pd
df_collision = pd.DataFrame(collision)
#df_user = pd.DataFrame(users)


# In[5]:


df_collision.to_excel('C:\\Users\OMKAR\Desktop\CollisionData.xlsx')
#df_user.to_excel('C:\\Users\OMKAR\Desktop\UserData.xlsx')


# In[6]:


#store users input data in csv format using pandas
import pandas as pd
df_input = pd.DataFrame(users)
# list(tusers)


# In[7]:


df_input.head(50)


# In[8]:


df_input.to_excel('C:\\Users\OMKAR\Desktop\Input1.xlsx')


# In[9]:


def searchUserindex(users, Name):
    IndexOfUser = 0
    index = 0
    for user in users:
        if user['userId'] == Name:
            IndexOfUser = index
            break
        index = index + 1
    return IndexOfUser


# In[10]:


searchUserindex(users, 'u2006180')


# In[11]:


users[49]['userExperience']


# In[12]:


def user_Experience(users):
    k=0
    maxExp=1
    minExp=1
    alpha=0.1
    for user in users:
        if k<len(users):
            newExperience= users[k]['userExperience']+(alpha*users[k]['userIteration']*(1-users[k]['userExperience']))
            #print(tusers[k]['userId'],"%.2f" % newExperience,tusers[k]['userExperience'])
            k=k+1
            UI = searchUserindex(users, user['userId'])
            users[UI]['userExperience'] = newExperience
            #print(UI)
            #print(newExperience)
    return users    
   
    


# In[13]:


def user_TrustWorthiness(users, Name):
    user_trustValue = 0
    for user in users:
        if user['userId'] == Name:
            user_trustValue = user['usertrustWorthiness']
            break

    return user_trustValue


# In[57]:


from geopy.distance import vincenty
def DistanceBetweenUsers(root_user, SecondUser):
    user1lattitude = radians(root_user['latitude'])
    user1longitude = radians(root_user['longitude'])
    user2lattitude = radians(SecondUser['latitude'])
    user2longitude = radians(SecondUser['longitude'])
    a = (user1lattitude, user1longitude)
    b  = (user2lattitude,user2longitude)
    distance = vincenty(a, b, miles=True)
    #print ("Result:" + str(distance))
    return distance


# In[15]:


len(users)


# In[16]:


#IMPLEMENTATION OF REK MODEL


# In[17]:


#REPUTATION CALCULATION BASED ON EXPERIENCE


# In[18]:


def experienceReputation(users):
    r=0
    sor=0
    sumofPositiveReputation=0
    sumofNegativeReputation=0
    negativeExperience=0
    positiveExperience=0
    damping=0.75
    sor1=0
    e=0
    sor2=0
    sum1=0
    sum2=0
    for user in users:
        if r<len(users):   
            if(users[r]['userExperience']>0.75):
                sumofPositiveReputation+=users[r]['userReputationExp']
                positiveExperience+=users[r]['userExperience']
                sor1=0.012+damping*(sumofPositiveReputation*(users[r]['userExperience']/positiveExperience))
               #print(sor1)
            else:
                sumofNegativeReputation+=users[r]['userReputationExp']
                negativeExperience+=users[r]['userExperience']
                sor2=0.012+damping*(sumofNegativeReputation*((1-users[r]['userExperience'])/negativeExperience))

            sor=(sor1-sor2)*10
            r=r+1
          # print(user['userId'])
            UI= searchUserindex(users, user['userId'])
            users[UI]['userReputationExp'] = sor
           
    return users
       
#As Reputation of each user is set to 1 initially
#he SUM of Reputation for all users is 50
    
    


# In[19]:


users =user_Experience(users)
#print (users)
# for a in tusers:
#     print (a['userId'])
#print(users)


# In[20]:


users = experienceReputation(users)
#print (users)
for user in users:
    print ('UserExperience:',user['userExperience'],'Reputation Exp:',user['userReputationExp'])


# In[21]:


#Badge calculation based on Experience
def BadgeExp(users):
    for user in users:
        print( user['userReputationExp'])
        if user['userReputationExp'] > 2:
            user['badgeExp'] = 'Hi-award'
        else:
            user['badgeExp'] = 'Lo-award'
    return users


# In[22]:


BadgeExp= BadgeExp(users)
print (BadgeExp)


# In[23]:


#IMPLEMENTATION OF SONATA MODEL


# In[24]:


#TRUSTWORTHINESS OF DATA BASED ON SONATA


# In[25]:


def Determine_Trustworthiness(x):
    I=0
    for a in x:
        A,B = 0,0
        voteOfMainUser = a[a['UserId']]
        if I < len(users):
            A += voteOfMainUser * users[I]['userVoting'] *user_TrustWorthiness(users,users[I]['userId'])
            B += users[I]['userVoting'] *user_TrustWorthiness(users, users[I]['userId'])
            I = I + 1
            if B!=0:
                new_user_TrustWorthiness = A/B
            IndexOfUser = searchUserindex(users, a['UserId'])
            users[IndexOfUser]['usertrustWorthiness'] = new_user_TrustWorthiness 
    return users
#print(len(tusers))


# In[26]:


trustworthiness = Determine_Trustworthiness(voting)
for a in trustworthiness:
    print ('User:',a['userId'],'trustworthiness:',a['usertrustWorthiness'])
#print(trustworthiness)


# In[27]:


#PAY OFF CALCULATION BASED ON THE VOTES SUBMITTED BY USER


# In[54]:


def Decide_Payoff(voting, users):
    t=0
    for user in voting:
        t=t+1
        root_user = UserSearch(users, user['UserId'])
        SecondUser = {}
        for element, value in user.items():
            if(element != user['UserId'] and element != 'reportId' and element != 'UserId'):
                SecondUser = UserSearch(users, element)
                root_userindex = searchUserindex(users,user['UserId'])
                SecondUserindex = searchUserindex(users, element)
                
                if(DistanceBetweenUsers(root_user, SecondUser) > 1.615 and SecondUser['userVelocity'] > 35):
                    #print(DistanceBetweenUsers(root_user, SecondUser))
                    users[root_userindex]['userPayoff'] = users[root_userindex]['userPayoff'] + 1
                    users[SecondUserindex]['userPayoff'] = users[SecondUserindex]['userPayoff'] + 1
                else:
                    #print(DistanceBetweenUsers(root_user, SecondUser))
                    users[root_userindex]['userPayoff'] = users[root_userindex]['userPayoff'] - 1
                    users[SecondUserindex]['userPayoff'] = users[SecondUserindex]['userPayoff'] - 1
    return users


# In[55]:


def UserSearch(users, userName):
    x = {}
    #print ("userserachcalled")
    for user in users:
        if (user['userId']) == userName:
            x = user
            break
    return x


# In[58]:


payoffUsers = Decide_Payoff(voting, users)
for a in payoffUsers:
    print ('User:',a['userId'],'Payoff:',a['userPayoff'])
#print (payoffUsers)


# In[59]:


#REPUTATION CALCULATION OF USER BASED ON VOTES 


# In[60]:


from geopy.distance import vincenty
def Reputation(x, users):
    for a in x:
        root_user = UserSearch(users, a['UserId'])
        SecondUser = {}
        similarity = 0
        root_userVote = a[a['UserId']]
        for element, value in a.items():
            if(element != a['UserId'] and element != 'reportId' and element != 'UserId'):
                SecondUser = UserSearch(users, element)
                root_userindex = searchUserindex(users,a['UserId'])
                SecondUserindex = searchUserindex(users, element)
                if root_userVote != 0: 
                    similaritycalc = (DistanceBetweenUsers(root_user, SecondUser)/ root_userVote)
                    if(similaritycalc > 1.615):                        
                        similarity = -1
                    else:
                        similarity = 1


                    SecondUser['userVoting'] += similarity/root_userVote
                    SecondUser['userVoting'] = SecondUser['userVoting'] * -1
                    SecondUser['userReputation'] = SecondUser['userReputation'] + SecondUser['userVoting']
    return users


# In[61]:


repuataionUsers = Reputation(voting, users)
for a in repuataionUsers:
    print ('User:',a['userId'],'ReputationVot:',a['userReputation'])
#print (repuataionUsers)
#badge Rewarding


# In[62]:


#REWARDING BASED ON VOTING MECHANISM


# In[63]:



def BadgeVot(users):
    for a in users:
        #print( user['userReputation'])
        if a['userReputation'] > 10:
            a['badgeVot'] = 'Hi-award'
        else:
            a['badgeVot'] = 'Lo-award'
    return users


# In[64]:


badgeVot = BadgeVot(users)
#print (badgeVot)
for a in badgeVot:
    print ('User:',a['userId'],'BadgeVot:',a['badgeVot'])


# In[65]:


for a in users:
    print ('User:',a['userId'],'lat:',a['latitude'],'lot:',a['longitude'],'trust:',a['usertrustWorthiness'],'Exp:',a['userExperience'],'It:',user['userIteration'],'RepEx:',a['userReputationExp'],'BaEx:',a['badgeExp'],'RepVot:',a['userReputation'],'BadgeVot:',a['badgeVot'])


# In[66]:


users =Determine_Trustworthiness(voting)
#print (users)

# for a in tusers:
#     print (a['userId'])
#print(tusers)


# In[67]:


print(users)


# In[68]:


#STORING RESULTS IN OUTPUT FILE


# In[69]:


import pandas as pd

df_output = pd.DataFrame(users)
# list(users)


# In[70]:


df_output['userReputationExp'] = df_output['userReputationExp'].round(3)


# In[71]:


df_output.head(50)


# In[72]:


df_output.to_excel('C:\\Users\OMKAR\Desktop\Outputiteration2.xlsx')


# In[73]:


df_input["userId"].head()


# In[74]:


df_output["userExperience"].head()


# In[75]:


df_input["userExperience"].head()


# In[76]:


##PlOT THE RESULTS FOR COMAPARISON BETWEEN INPUT AND OUTPUT FOR TWO MODELS


# In[ ]:


#ANALYSIS and COMAPRISON OF USer experience of REK MODEL with respect to input data


# In[82]:


# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
 
# data
#df=pd.DataFrame({'x':range(1,50)})

# plot
plt.plot( df_output["userId"],  df_input["userExperience"], linestyle='-', marker='o',  c='blue')
plt.plot( df_output["userId"],  df_output["userExperience"], linestyle='-', marker='o', c='green')
plt.show()


# In[ ]:


#ANALYSIS and COMAPRISON OF Pay0ff of SONATA MODEL with respect to input data


# In[78]:


plt.plot( df_output["userId"],  df_input["userPayoff"], linestyle='-', marker='o',  c='blue')
plt.plot( df_output["userId"],  df_output["userPayoff"], linestyle='-', marker='o', c='green')
plt.show()


# In[ ]:


#ANALYSIS and COMAPRISON OF trustworthiness of SONATA MODEL with respect to input data


# In[79]:


plt.plot( df_output["userId"],  df_input["usertrustWorthiness"], linestyle='-', marker='o',  c='blue')
plt.plot( df_output["userId"],  df_output["usertrustWorthiness"], linestyle='-', marker='o', c='green')
plt.show()


# In[ ]:


#ANALYSIS and COMAPRISON OF REPUTATION FROM BOTH MODELS WITH INITIAL VALUE OF REPUTATION WHICH WAS SET TO 1


# In[80]:


plt.plot( df_output["userId"],  df_input["userReputation"], linestyle='-', marker='o',  c='blue')
plt.plot( df_output["userId"],  df_output["userReputation"], linestyle='-', marker='o', c='green')
plt.plot( df_output["userId"],  df_output["userReputationExp"], linestyle='-', marker='o',  c='red')
plt.show()
plt.show()


# In[ ]:


#ANALYSIS and COMAPRISON OF Voting capacity of SONATA MODEL with respect to input data


# In[81]:


plt.plot( df_output["userId"], df_input["userVoting"], linestyle='-', marker='o',  c='blue')
plt.plot( df_output["userId"],  df_output["userVoting"], linestyle='-', marker='o', c='green')
plt.show()

