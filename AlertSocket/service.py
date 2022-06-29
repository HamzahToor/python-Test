import math


def getAlertData(parsed_data,db):
    # print(parsed_data["MAC_ADDRESS"])
    node = db.nodes.find_one({"mac":parsed_data['MAC_ADDRESS']})
    if(node and parsed_data['MESSAGE_ID']=='8'):
        environment = db.environments.find_one({"node_id":str(node["_id"])})
        print(parsed_data)
        print(environment)
        if(environment):
            temperature_alert = 0
            humidity_alert = 0
            thermistor_1_alert = 0
            thermistor_2_alert = 0
            # add calibration factor
            parsed_data["AMBIENT_TEMPERATURE"]=parsed_data["AMBIENT_TEMPERATURE"]+environment["ambient_temperature_calibration_factor"]
            parsed_data["AMBIENT_HUMIDITY"]=parsed_data["AMBIENT_HUMIDITY"]+environment["ambient_humidity_calibration_factor"]
            parsed_data["THERMISTOR_1"]=parsed_data["THERMISTOR_1"]+environment["thermistor_1_calibration_factor"]
            parsed_data["THERMISTOR_2"]=parsed_data["THERMISTOR_2"]+environment["thermistor_2_calibration_factor"]
            
            if(parsed_data["AMBIENT_TEMPERATURE"] <= environment["max_ambient_temperature"] and parsed_data["AMBIENT_TEMPERATURE"] >=environment["min_ambient_temperature"]):
                temperature_alert = 0
            
            else :

                if(parsed_data["AMBIENT_TEMPERATURE"] > environment["max_ambient_temperature"]):
                    temperature_alert = 1
                
                else :
                    temperature_alert = -1
                

            if(parsed_data["AMBIENT_HUMIDITY"] <= environment["max_ambient_humidity"] and parsed_data["AMBIENT_HUMIDITY"] >= environment["min_ambient_humidity"]): 
                humidity_alert = 0
            
            else :
                if(parsed_data["AMBIENT_HUMIDITY"] > environment["max_ambient_humidity"]):
                    humidity_alert = 1
                
                else:
                    humidity_alert = -1
            if(parsed_data["THERMISTOR_1"] <= environment["max_thermistor_1_temperature"] and parsed_data["THERMISTOR_1"] >= environment["min_thermistor_1_temperature"]):
                thermistor_1_alert = 0
            
            else:
                if(parsed_data["THERMISTOR_1"] > environment["max_thermistor_1_temperature"]):
                    thermistor_1_alert = 1
                    
                else:
                    thermistor_1_alert = -1  
     
            if(parsed_data["THERMISTOR_2"] <= environment["max_thermistor_2_temperature"] and parsed_data["THERMISTOR_2"] >=environment["min_thermistor_2_temperature"]):
                thermistor_2_alert = 0
            
            else:
                if(parsed_data["THERMISTOR_2"] > environment["max_thermistor_2_temperature"]):
                    thermistor_2_alert = 1
                
                else:
                    thermistor_2_alert = -1
                        

            alert_data = {
                "environment_id": str(environment["_id"]),
                "node_mac":node["mac"],
                "alerts":[]
            }
            if(temperature_alert==1):
                temp_data = db.alerts.find_one({"environment_id": str(environment["_id"]),"node_id":str(node["_id"]),"alert_type":'ambient-temperature',"alert_level":1,"stop_flag":False}).sort({"_id":-1}).limit(1)
               
                if(temp_data.length==1):
                    alert=alert_data['alerts']
                    print(alert)
                    alert.push({
                        "alert_type":"ambient-temperature",
                        "alert_level":1,
                        "parameter_value":parsed_data["AMBIENT_TEMPERATURE"],
                        "duration":(temp_data["end_time"] - temp_data["start_time"])/1000,
                        "timestamp":parsed_data["TIMESTAMP"]}
                    )
                
            
            elif(temperature_alert==-1):
                alert=alert_data['alerts']
                print(alert)
                temp_data = db.alerts.find_one({"environment_id": str(environment["_id"]),"node_id":str(node["_id"]),"alert_type":'ambient-temperature',"alert_level":-1,"stop_flag":False}).sort({"_id":-1}).limit(1)
                if(temp_data.length==1):
                    alert_data['alerts'].push({
                        "alert_type":"ambient-temperature",
                        "alert_level":-1,
                        "parameter_value":parsed_data["AMBIENT_TEMPERATURE"],
                        "duration":(temp_data["end_time"] - temp_data["start_time"])/1000,
                        "timestamp":parsed_data["TIMESTAMP"]}
                    )
            if(humidity_alert==1):

                humd_data =  db.alerts.find_one({"environment_id": str(environment["_id"]),"node_id":str(node["_id"]),"alert_type":'ambient-humidity',"alert_level":1,"stop_flag":False}).sort({"_id":-1}).limit(1)
                if(humd_data.length==1):
                    alert_data['alerts'].push({
                        "alert_type":"ambient-humidity",
                        "alert_level":1,
                        "parameter_value":parsed_data["AMBIENT_HUMIDITY"],
                        "duration":(humd_data["end_time"] - humd_data["start_time"])/1000,
                        "timestamp":parsed_data["TIMESTAMP"]
                })
                
            
            elif(humidity_alert==-1):

                humd_data =  db.alerts.find_one({"environment_id": str(environment["_id"]),"node_id":str(node["_id"]),"alert_type":'ambient-humidity',"alert_level":-1,"stop_flag":False}).sort({"_id":-1}).limit(1)
                if(humd_data.length==1):
                    alert_data['alerts'].push({
                        "alert_type":"ambient-humidity",
                        "alert_level":-1,
                        "parameter_value":parsed_data["AMBIENT_HUMIDITY"],
                        "duration":(humd_data["end_time"] - humd_data["start_time"])/1000,
                        "timestamp":parsed_data["TIMESTAMP"]
                    })
                

            

            if(thermistor_1_alert==1):
                temp_th_1_data =  db.alerts.find_one({"environment_id": str(environment["_id"]),"node_id":str(node["_id"]),"alert_type":'thermistor-1-temperature',"alert_level":1,"stop_flag":False}).sort({"_id":-1}).limit(1)
                if(temp_th_1_data.length==1):
                    alert_data['alerts'].push({
                        "alert_type":"thermistor-1-temperature",
                        "alert_level":1,
                        "parameter_value":parsed_data["THERMISTOR_1"],
                        "duration":(temp_th_1_data["end_time"] - temp_th_1_data["start_time"])/1000,
                        "timestamp":parsed_data["TIMESTAMP"]
                    }
                    )
                
            
            elif(thermistor_1_alert==-1):
                temp_th_1_data =  db.alerts.find_one({"environment_id": str(environment["_id"]),"node_id":str(node["_id"]),"alert_type":'thermistor-1-temperature',"alert_level":-1,"stop_flag":False}).sort({"_id":-1}).limit(1)
                if(temp_th_1_data.length==1):
                    alert_data['alerts'].push({
                        "alert_type":"thermistor-1-temperature",
                        "alert_level":-1,
                        "parameter_value":parsed_data["THERMISTOR_1"],
                        "duration":(temp_th_1_data["end_time"] - temp_th_1_data["start_time"])/1000,
                        "timestamp":parsed_data["TIMESTAMP"]
                    })
                
            if(thermistor_2_alert==1):
                temp_th_2_data =  db.alerts.find_one({"environment_id": str(environment["_id"]),"node_id":str(node["_id"]),"alert_type":'thermistor-2-temperature',"alert_level":1,"stop_flag":False}).sort({"_id":-1}).limit(1)
                if(temp_th_2_data.length==1):
                    alert_data['alerts'].push({
                        "alert_type":"thermistor-2-temperature",
                        "alert_level":1,
                        "parameter_value":parsed_data["THERMISTOR_2"],
                        "duration":(temp_th_2_data["end_time"] - temp_th_2_data["start_time"])/1000,
                        "timestamp":parsed_data["TIMESTAMP"]
                    })
                
            elif(thermistor_2_alert==-1):
                temp_th_2_data =  db.alerts.find_one({"environment_id": str(environment["_id"]),"node_id":str(node["_id"]),"alert_type":'thermistor-2-temperature',"alert_level":-1,'stop_flag':False}).sort({'_id':-1}).limit(1)
                if(temp_th_2_data.length==1):
                    alert_data['alerts'].push({
                        "alert_type":"thermistor-1-temperature",
                        "alert_level":-1,
                        "parameter_value":parsed_data["THERMISTOR_2"],
                        "duration":(temp_th_2_data["end_time"] - temp_th_2_data["start_time"])/1000,
                        "timestamp":parsed_data["TIMESTAMP"]
                    })
                
            
            return(alert_data)
        
    

        else:
            print("Not found")
            # return node

    
    
