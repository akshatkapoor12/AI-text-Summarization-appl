import streamlit_authenticator as stauth 

users={
    "akshat":{
        "name":"Akshat Kapoor",
        "password":stauth.Hasher(["password123"]).generate()[0]
        
    }
}



