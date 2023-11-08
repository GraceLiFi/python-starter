from datetime import datetime
def main():
    date = datetime.today().strftime('%m/%d/%Y')
    f = open("C:\\Users\\f9hud0c\\Documents\\Assignments\\python-starter\\AssignmentSolutions\\output.txt", "w")
    f.write(f"Today's date is: {date}.")
    f.close()

if __name__ == "__main__":
    main()   