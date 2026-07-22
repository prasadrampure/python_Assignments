import schedule
import time

def Display1():
    print("Lunch time!")

def Display2():
    print('Wrap up work')

def main():
    schedule.every().day.at("13:00").do(Display1)

    schedule.every().day.at("18:00").do(Display2)

    while True:
        schedule.run_pending()
        time.sleep(5)

if __name__ == "__main__":
    main()