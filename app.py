from flask import Flask,request
app=Flask(__name__)
stores=[
    {
        "name":"My Store",
        "items":[
            {
                "name":"Chair",
                "price":15.99
            }
        ]
    }
]

@app.get("/stores")
def get_stores():
    return {"stores": stores}

@app.post("/stores")
def create_stores():
    request_data=request.get_json()
    new_store={"name":request_data["name"],"items":[]}
    stores.append(new_store)
    return new_store,201



if __name__ == "__main__":
    app.run(debug=True)