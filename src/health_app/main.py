from .health import Health
from .data import save_records, load_records, get_statistics
def add_health_record(records):
    while True:
       
            name = input("Enter name: ").strip()
            weight = float(input("Enter weight (kg): "))
            height = float(input("Enter height (m): "))

            person = Health(name, weight, height)
            records.append(person)

            save_records(records)  # 
            print(f"Added {person.name}: BMI {person.bmi} ({person.get_category()}) | Ideal: {person.get_idael_weight()}kg | Advice: {person.get_health_advice()}")
            break

def view_all_records(records):
    if not records:
        print("No records found.")
        return
    for person in records:
        print(f"{person.name}: BMI {person.bmi} ({person.get_category()}), Ideal weight {person.get_idael_weight()}kg, Advice: {person.get_health_advice()}")

def view_statistics(filename="health_records.json"):
    stats = get_statistics(filename)
    print(f"Total records: {stats['total_records']}")
    print(f"Average BMI: {stats['avg_bmi']}")
    print(f"Most common category: {stats['most_common_category']}")
    print("Category_distribution:")
    for cat, count in stats['category_distribution'].items():
        print(f"  {cat}: {count}")

def main():
    records = load_records()

    while True:
        print("\n--- Health App , welcome ---")
        print("1. Add Health Record")
        print("2. View All Records")
        print("3. View Statistics")
        print("4. Save & Quit")

        x = input("Enter your number: ").strip()

        if x == "1":
            add_health_record(records)
        elif x == "2":
            view_all_records(records)
        elif x == "3":
            view_statistics()
        elif x == "4":
            save_records(records)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid x. Try again.")

if __name__ == "__main__":
    main()