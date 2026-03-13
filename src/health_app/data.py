import json
from .health import Health
from collections import Counter


def save_records(records, filename="health_records.json"):
    data = []

    for r in records:
        data.append({
            "name": r.name,
            "weight_kg": r.weight_kg,
            "height_m": r.height_m,
            "BMI": r.bmi
        })

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)


def load_records(filename="health_records.json"):
    try:
        with open(filename) as f:
            data = json.load(f)
            records = []

            for d in data:
                person = Health(d['name'], d['weight_kg'], d['height_m'])
                records.append(person)

            return records

    except FileNotFoundError:
        return []


def get_statistics(filename="health_records.json"):
    records = load_records(filename)
    total = len(records)

    if total == 0:
        return {
            "total_records": 0,
            "avg_bmi": 0,
            "most_common_category": None,
            "category distribution": {}
        }

    avg = round(sum(r.bmi for r in records) / total, 2)

    categories = [r.get_category() for r in records]
    

    counter = Counter(categories)

    most_common = counter.most_common(1)[0][0]

    return {
        "total_records": total,
        "avg_bmi": avg,
        "most_common_category": most_common,
        "category_distribution": dict(counter)
    }