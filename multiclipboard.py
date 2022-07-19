import sys
import clipboard # install it
import json
SAVED_DATA = "clipboard.json"

def save_data(filepath,data):
    with open(filepath,"w")as f:
        json.dump(data, f)


def load_data(filepath):
    try:
        with open(filepath,"r")as f:
            data=json.load(f)
            return data
    except:
        return{}      


if len(sys.argv)==2:
    command=sys.argv[1]
    data = load_data(SAVED_DATA)

    if command =="save":
        key=input("enter a key:")
        data[key]=clipboard.paste()
        save_data(SAVED_DATA, data)
        print("data saved")

    elif command == "load":
        key = input("enter a key:")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboaard")
        else:
            print("Key does not exist")    
       

    elif command == "list":
        print(data)
    else:
        print("unknown command")   
         
else:
    print("Please pass exactly one command.")