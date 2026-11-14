from flask import Flask, render_template, request
from db import get_db_connection

app = Flask(__name__)

@app.route("/")
def home():
    connection1 = get_db_connection()
    cursor1 = connection1.cursor()

    query = "SELECT * FROM stations WHERE status='Approved'"

    cursor1.execute(query)

    results = cursor1.fetchall()
    cursor1.close()
    connection1.close()


    return render_template("index.html", results=results)


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
        connection = get_db_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO stations (station_name, area, connector_type)
        VALUES (%s, %s, %s)
        """
    
        values = (station_name, area, connector_type)

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()
        return render_template("result.html", message="Data Saved Successfully")


        

if __name__ == "__main__":
    app.run(debug=True)