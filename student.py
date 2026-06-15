students = [
    {
        "name": "Kinjalk Mishra",
        "college_name": "GLA UNIVERSITY",
        "section": "CA",
        "grades": "A+",
        "city": "Lucknow",
        "marks": 95,
        "attendance": 92,
        "lab": True
    },
    {
        "name": "Jai",
        "college_name": "GLA UNIVERSITY",
        "section": "CE",
        "grades": "B",
        "city": "Kanpur",
        "marks": 78,
        "attendance": 85,
        "lab": True
    },
    {
        "name": "Harshit",
        "college_name": "GLA UNIVERSITY",
        "section": "CA",
        "grades": "F",
        "city": "Jaipur",
        "marks": 32,
        "attendance": 48,
        "lab": False
    },
    {
        "name": "Rohan",
        "college_name": "GLA UNIVERSITY",
        "section": "ME",
        "grades": "A",
        "city": "Agra",
        "marks": 88,
        "attendance": 79,
        "lab": True
    },
    {
        "name": "Priya",
        "college_name": "GLA UNIVERSITY",
        "section": "CS",
        "grades": "A+",
        "city": "Delhi",
        "marks": 97,
        "attendance": 96,
        "lab": True
    }
]

for student in students:
    # Attendance Check
    if student.get("attendance") <= 75:
        print(f"{student.get('name')} has low attendance.")
    else:
        print(f"{student.get('name')} has high attendance.")

    # Lab Status Check
    if student.get("lab"):
        print(f"{student.get('name')} has taken lab.")
    else:
        print(f"{student.get('name')} has not taken lab.")

    # Result Check
    if 40 <= student.get("marks") <= 79:
        print(f"{student.get('name')} is Pass.")
    elif 80 <= student.get("marks") <= 100:
        print(f"{student.get('name')} is Distinction.")
    else:
        print(f"{student.get('name')} is Fail.")

    print("-" * 40)
