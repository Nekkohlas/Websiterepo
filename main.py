from website import create_app


app = create_app()

if __name__ == '__main__':  #only if we run ! this , not just importing it, app.run is executed
    app.run(debug=True)     # runs flask application, anytime code is changed - debug equals true re runs the web server
    