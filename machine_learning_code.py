import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.tsa.ar_model import AR
import datetime , threading
import sqlite3
import numpy as np
from reading_file_interval import get_last_n_lines
from sklearn.metrics import mean_squared_error
'''this function check if false data is injected'''
''' D: real data, P : Predicted data'''
def check_FD(D, D_1, P, P_1,err_marginal=1.05):
    if abs(D - P) >= err_marginal and  abs(D_1 - P_1) >= err_marginal :
        return True
    else:
        return False







def delat_DB(DB_name):
    conn = sqlite3.connect(DB_name)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS data")

def add_db(DB_name, t0, t1,t2,FD):

    conn = sqlite3.connect(DB_name)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS data(id INTEGER PRIMARY KEY, time,real,predicted,FD)")
    c.execute("INSERT INTO data (time,real,predicted,FD) VALUES (?,?,?,?)", (t0, t1, t2, FD))
    conn.commit()
    c.close()
    conn.close()



''' Function of reading from DB1 data base and clear the  empty fields in between values '''
def filter_out_data(node_name, DB_name):
    conn = sqlite3.connect(DB_name)  # creat a connection to DB
    RD = pd.read_sql_query("SELECT * FROM data", conn)  # read data from DB
    x = RD[node_name].values # values with blank cells
    x = list(filter(None, x)) #values without  blanks
    xx=[]
    for item in x:
        xx.append(float(item)) # from string to Float type
    return xx

nodes=["Temperature48","Temperature31","Temperature54","Temperature32","Temperature71","Temperature65","Temperature78","Temperature37","Temperature76"]
dbs=["DB48.db","DB31.db","DB54.db","DB32.db","DB71.db","DB65.db","DB78.db","DB37.db","DB76.db"]

false_data_count= [0]*len(nodes) # every loop ( WAIT_TIME_SECONDS ) a list of False data Count generated and pushed in Archive
archive=[]


if __name__ == '__main__':
   # creat_DB("DB2.db")


    WAIT_TIME_SECONDS = 0.5
    ticker = threading.Event()

  #  for i in np.linspace(0,0.3,2): # i is the err marginal that increased from 0 to 0.3  in 30 steps
    while True:
        for node in nodes :
            DB = dbs[nodes.index(node)]
            delat_DB(DB)
            print(DB)
            X = filter_out_data(node, "falsedata112.db")

            train, test = X[1:len(X)- 35], X[len(X) - 35:] # split the Data into two parts one for training the model the other is for test
                                                           # 50 is a number of reading that compared with predictions


            #train autoregression #
            model = AR(train)        # check if we can implement Ridg instaed of AR
                                     # https://scikit-learn.org/stable/modules/linear_model.html#ridge-regression-and-classification
            model_fit = model.fit()  # autamatically select the right lags
            window = model_fit.k_ar  # window is how many lags included in calculation of AR
            print (window, node)     # just for debuging
            coef = model_fit.params  # coefficients of the AR model

            # walk forward over time steps in test

            history = train[len(train) - window:]
            history = [history[i] for i in range(len(history))]
            predictions = list()
            for t in range(len(test)):
                length = len(history)
                lag = [history[i] for i in range(length - window, length)]
                yhat = coef[0]
                for d in range(window):
                    yhat += coef[d + 1] * lag[window - d - 1] # the predicted value
                    obs = test[t]                             # the real value to be compared with the yhat
                mytime = datetime.datetime.now()
                tm = '{}:{}:{}'.format(mytime.hour, mytime.minute, mytime.second)

                predictions.append(yhat)
                history.append(obs)
                FD = "0"
                if t > 0:       # values at the first place in the list can't be compared with any previuos values
                    if check_FD(test[t],test[t-1],predictions[t],predictions[t-1]):
              #          print('predicted=%f, expected=%f' % (yhat, obs)) # just for debugging
                        false_data_count[nodes.index(node)]+= 1 # increase counter when a FD happened
                        FD = "1"
                    else :
                        FD = "0"
                #x = ticker.wait(WAIT_TIME_SECONDS)
                add_db(DB, str(tm), str(obs), str(yhat), FD)

            #

    # out of for loop

            percentage= (false_data_count[nodes.index(node)]/50)*100

            #    error = mean_squared_error(test, predictions)
            #    print('Test MSE: %.3f' % error)
            #    pyplot.close('all')
            """fig = plt.figure(constrained_layout=True)
            plt.plot(test)
            plt.plot(predictions, color='red')
            plt.xlabel('Reading Points')
            plt.ylabel('Temperature in C')
            plt.title(node+ " , the percentage of False Data is "+ str(round(percentage))+ " %")

            plt.show()"""
            x = ticker.wait(WAIT_TIME_SECONDS)
           # new_reading = get_last_n_lines("daily-min-temperatures.csv",1)
           # print(new_reading,"newreading is \n")
            #series.append(new_reading)

           # print ("tesssst")
    # the Proccess for all nodes is done for one round
    ##############
    '''
        archive.append(false_data_count)
        print(false_data_count)
        false_data_count= [0]*len(nodes)
        print ("__________________________________________________________________________")

        x = ticker.wait(WAIT_TIME_SECONDS)
    for j in range(len(archive)): # the archive contains  now 30 records
        print (archive[j],"\n")
    print("*****************************************************************************")
    '''
 #################    
