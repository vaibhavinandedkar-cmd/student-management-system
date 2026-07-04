import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    # Default to port 5001 to avoid conflicts with services on 5000
    port = int(os.getenv("PORT", "5001"))
    debug_env = os.getenv("FLASK_DEBUG")
    if debug_env is None:
        debug = True
    else:
        debug = debug_env.lower() in ("1", "true", "yes")

    app.run(debug=debug, port=port)
