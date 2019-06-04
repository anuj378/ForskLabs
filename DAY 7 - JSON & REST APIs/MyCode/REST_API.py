'''Create a client REST API that sends and receives some information from the Server by calling server's REST API.

You are expected to create two functions each for Sending and Receiving data.

    You need to make two api calls, one with POST method for sending data and the other with GET method to receive data

    All the communication i.e. sending and receiving of data with the server has to be in JSON format

    First send the data to cloud using the "http://13.127.155.43/api_v0.1/sending" api with the following fields (Field names should be same as shown ):
            Phone_Number (pass phone number as string and not as integer)
            Name
            College_Name
            Branch

    Now receive the data from cloud using the "http://13.127.155.43/api_v0.1/receiving" api with     “Phone_Number” along with the number you are looking for as query parameter
    Print the server responses from both the cases. The first one will give response-code : 200 and response-message : "Data added Successfully", if all goes well. The second one will give all the details stored with the phone number you provided as query parameter. Both the responses will be in JSON format.

Output

response-code : 200 
response-message : Data added Successfully 


Submitted_at : Mon, 11 Sep 2017 13:32:30 GMT
Phone Number : 7877757144
Name : Kunal Vaid
Branch : B.Tech CSE
College_Name : Amity University
'''
import requests

data={"Phone_Number":"7568491123",
            "Name" : "Anuj Pareek",
            "College_Name" : "ANAND ICE",
            "Branch" : "CSE"}

def upload():
     response = requests.post("http://13.127.155.43/api_v0.1/sending",json=data)
     return response
print("POST CALLED :",upload())
   
def download():
    received=requests.get("http://13.127.155.43/api_v0.1/receiving?Phone_Number=7568491123")
    response=received.json()
    print(response)
download()    

