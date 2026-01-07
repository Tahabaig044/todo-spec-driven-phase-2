from main import app

# This file serves as the entry point for Hugging Face Spaces
# The actual application is defined in main.py
# This is the standard entry point that Hugging Face looks for

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)