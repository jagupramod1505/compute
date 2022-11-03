from fastapi import FastAPI # Step 1 is to import FastAPI
app = FastAPI() # create instance fastapi

@app.get("/") # path opreation decorater
async def root(): # path operation function
   return {"message": "Hello World"} # return conten

