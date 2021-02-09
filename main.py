from datetime import datetime as dt
import speedtest
import pandas as pd
import time as tm
import os

class SP_TEST():

    def __init__(self):
        self.counter=0
        self.results_dict_usa=pd.DataFrame(columns=["Date","Sample","Download","Upload","Ping","Server"])
        self.results_dict_rf=pd.DataFrame(columns=["Date","Sample","Download","Upload","Ping","Server"])
        if os.name == 'nt':
            self.path_usa=r"RESULTS\RESULTS_NL.csv"
            self.path_rf=r"RESULTS\RESULTS_COL.csv"
        else:
            self.path_usa=r"RESULTS/RESULTS_NL.csv"
            self.path_rf=r"RESULTS/RESULTS_COL.csv"
        actual_time=tm.time()+10000
        threshold_time=200
        while True:
            if abs(tm.time()-actual_time)>=threshold_time:
                self.counter=self.counter+1
                sw_sec_test=True
                while sw_sec_test:
                    print("Starting Measurement #",self.counter)
                    try:
                        self.run_test()
                        sw_sec_test=False
                    except:
                        print("ERROR: Could not connect to server")
                        tm.sleep(120)
                        sw_sec_test=True
                self.dict_manager()
                self.to_csv()
                actual_time=tm.time()
                tm.sleep(threshold_time)

    def run_test(self):

        self.test_rf=speedtest.Speedtest()
        self.test_rf.get_servers(servers=[15019])
        self.test_rf.download()
        self.test_rf.upload()
        self.data_rf=self.test_rf.results.dict()
        self.test_usa=speedtest.Speedtest()
        self.test_usa.get_servers(servers=[12872])
        self.test_usa.download()
        self.test_usa.upload()
        self.data_usa=self.test_usa.results.dict()

    def dict_manager(self):
        try:
            self.results_dict_usa=self.results_dict_usa.append({"Date":str((dt.now()).strftime("%d-%m-%Y, %H:%M:%S")),
                                                                "Sample":self.counter,"Download":((self.data_usa.get("download"))),
                                                                "Upload":((self.data_usa.get("upload"))),"Ping":(self.data_usa.get("ping")),
                                                                "Server":((self.data_usa.get("server")).get("host"))},ignore_index=True)

            self.results_dict_rf=self.results_dict_rf.append({"Date":str((dt.now()).strftime("%d-%m-%Y, %H:%M:%S")),
                                                                "Sample":self.counter,"Download":((self.data_rf.get("download"))),
                                                                "Upload":((self.data_rf.get("upload"))),"Ping":(self.data_rf.get("ping")),
                                                                "Server":((self.data_rf.get("server")).get("host"))},ignore_index=True)
        except:
            print("ERROR: Could not add results to pandas")
            self.counter=self.counter-1


    def to_csv(self):
        try:
            self.results_dict_usa.to_csv(self.path_usa,index=False)
            self.results_dict_rf.to_csv(self.path_rf, index=False)
            print("-------------------------------------NL - WILLEMSTAD--------------------------------------")
            print(self.results_dict_usa)
            print("-------------------------------------COL - BARRANQUILLA----------------------------------------")
            print(self.results_dict_rf)
        except:
            print("ERROR: Could not export csv")
            self.results_dict_usa.to_csv("BACKUP_NL.csv", index=False)
            self.results_dict_rf.to_csv("BACKUP_COL.csv", index=False)




if __name__=="__main__":
    SP_TEST()
