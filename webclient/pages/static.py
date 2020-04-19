from webclient.main import app, template, redirect, not_found


_tos_versions = {
    "1.0": "tos-1.0.html",
    "1.1": "tos-1.1.html",
    "1.2": "tos-1.2.html",
    "1.3": "tos-1.3.html",
}


@app.route("/")
def root():
    return template("main.html")


@app.route("/manager/tos")
def tos_latest():
    return redirect("tos", version="1.3")


@app.route("/manager/tos/<version>")
def tos(version):
    t = _tos_versions.get(version)
    if t:
        return template(t)
    else:
        return not_found()
