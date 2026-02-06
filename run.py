import uvicorn

if __name__ == "__main__":
    # "app.main:app" -> Folder.File:Variable
    uvicorn.run("app.main:app", host="0.0.0.0", port=7000, reload=True)

