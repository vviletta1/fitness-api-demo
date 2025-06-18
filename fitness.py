import requests

def get_cardio_exercises():
    url = "https://api.api-ninjas.com/v1/exercises?type=cardio"
    headers = {
        'X-Api-Key': 'pGHeYB0k65nBgM2JLMBAlg==polLgln2bjxCHI6Q'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        exercises = response.json()

        print("\n🏋️‍♀️ Top Cardio Exercises:\n")
        for i, exercise in enumerate(exercises[:5], 1):
            name = exercise.get("name", "N/A")
            muscle = exercise.get("muscle", "N/A")
            equipment = exercise.get("equipment", "N/A")
            difficulty = exercise.get("difficulty", "N/A")
            instructions = exercise.get("instructions", "N/A")[:120]

            print(f"{i}. {name} ({difficulty})")
            print(f"   Muscle: {muscle} | Equipment: {equipment}")
            print(f"   📝 Instructions: {instructions}...\n")

    except requests.exceptions.RequestException as e:
        print(f"❌ API call failed: {e}")

get_cardio_exercises()