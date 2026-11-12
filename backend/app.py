from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit_station():
    station_name = request.form.get("station_name","").strip()
    area = request.form.get("area","").strip()
    connector_type = request.form.get("connector_type","").strip()
    
    if not station_name:
        return render_template("result.html", error="Enter station name!")
    elif not area:
        return render_template("result.html", error="Enter area name!")
    elif not connector_type:
        return render_template("result.html", error="Enter connector name!")
    else:
        return render_template(
            "result.html", 
            station_name=station_name, 
            area=area, 
            connector_type=connector_type 
        )


if __name__ == "__main__":
    app.run(debug=True)