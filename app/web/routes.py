from flask import Flask, render_template, request
from app.automation.pipeline import run_pipeline

app = Flask(__name__)

ALL_PROVIDERS = ["remoteok", "remotive", "arbeitnow"]


@app.route("/", methods=["GET", "POST"])
def dashboard():
    jobs = []
    status = "Idle"   # 🟢 default

    if request.method == "POST":
        status = "Connected"  # 🟢 will show after fetch completes

        filters = {
            "keywords": [k.strip() for k in request.form.get("keywords", "").split(",") if k.strip()],
            "locations": [l.strip() for l in request.form.get("locations", "").split(",") if l.strip()],
            "companies": [c.strip() for c in request.form.get("companies", "").split(",") if c.strip()],
            "sources": [s for s in request.form.getlist("sources") if s],
            "job_types": [t for t in request.form.getlist("job_types") if t],
            "remote_only": bool(request.form.get("remote_only")),
            "salary_min": int(request.form.get("salary_min") or 0),
        }

        providers = [p for p in request.form.getlist("providers") if p]
        if not providers or "all" in providers:
            providers = ALL_PROVIDERS

        try:
            jobs = run_pipeline(
                return_jobs=True,
                override_filters=filters,
                override_providers=providers,
            )
        except Exception as e:
            status = f"Error • {str(e)}"

    return render_template("dashboard.html", jobs=jobs, status=status)