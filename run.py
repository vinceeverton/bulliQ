from app.services import create_app

app = create_app()

if __name__ == "__main__":
    # use_reloader=False is the safest way to avoid camera "Device Busy" errors
    app.run(host="0.0.0.0", port=7000, debug=True, use_reloader=False)
