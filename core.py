from textcompare_service import init_service

app = init_service()

if __name__ == "__main__":
    app.run( debug=True)