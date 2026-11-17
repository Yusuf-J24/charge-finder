import os
from flask import Flask, render_template, request, url_for, redirect, flash
from db import get_db_connection
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("FLASH_KEY")

@app.route("/")
def home():
    connection = None
    cursor = None
    search_station = request.args.get("search_station","").strip()
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        if search_station:
            query = """
            SELECT * FROM stations
            WHERE status = %s
            AND station_name LIKE %s
            """
            values = ("Approved", f"%{search_station}%")
            cursor.execute(query, values)
            results = cursor.fetchall()
            return render_template("index.html", results=results)
        else:
            query = "SELECT * FROM stations WHERE status='Approved'"    
            cursor.execute(query)
            results = cursor.fetchall()
            return render_template("index.html", results=results)
    except Exception as e:
        print("Database Error", e)
        return "Something went wrong. Please try again later.", 500
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

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
        connection = None
        cursor = None
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            query = """
            INSERT INTO stations (station_name, area, connector_type)
            VALUES (%s, %s, %s)
            """
            values = (station_name, area, connector_type)
            cursor.execute(query, values)
            connection.commit()
            flash("Station submitted successfully!", "success")
            return redirect(url_for("home"))        
        except Exception as e:
            print("Database Error", e)
            return "Something went wrong. Please try again later.", 500
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

@app.route("/admin")
def admin():
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM stations")
        results = cursor.fetchall()
        return render_template("admin.html", results=results)
    except Exception as e:
        return "Something went wrong, Please try again later.", 500
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

@app.route("/reject", methods=["POST"])
def reject_station():
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        station_id = request.form.get("station_id")
        query="""
        UPDATE stations 
        SET status = %s
        WHERE station_id = %s
        """
        values = ("Rejected", station_id)
        cursor.execute(query,values)
        connection.commit()
        flash("Station rejected successfully!", "success")
        return redirect(url_for("admin"))
    except Exception as e:
        return "Something went wrong, Please try again later.", 500
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

@app.route("/approve", methods=["POST"])
def approve_station():
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        station_id = request.form.get("station_id")
        query="""
        UPDATE stations 
        SET status = %s
        WHERE station_id = %s
        """
        values = ("Approved", station_id)
        cursor.execute(query,values)
        connection.commit()
        flash("Station approved successfully!", "success")
        return redirect(url_for("admin"))
    except Exception as e:
        return "Something went wrong, Please try again later.", 500
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    app.run(debug=True)