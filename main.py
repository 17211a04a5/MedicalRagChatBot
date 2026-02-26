from app.components.DataLoader import process_and_store_data
from app.application import app

def main():
    print("Hello from medicalrag!")
    process_and_store_data()
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)

if __name__ == "__main__":
    main()
