from webclient.main import app, redirect
from webclient.main import get_session, start_session, stop_session


@app.route("/login")
def login():
    s = get_session()
    if s is None:
        s = start_session()

    s.is_auth = True
    s.display_name = "Debuguser"
    return redirect("manager_package_list")


@app.route("/logout")
def logout():
    stop_session()
    return redirect("root")
