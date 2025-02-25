import json
import datetime
import os

def create_log_entry(data):
    """Creates a log entry dictionary."""
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")  # More readable timestamp
    return {
        "timestamp": timestamp,
        "data": data
    }


def write_to_json(log_entry, filename="db.json"):
    """Writes the log entry to the JSON file."""
    file_path = os.path.join(os.path.dirname(__file__), filename)  # Path relative to script
    try:
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:  # Check if file exists and is not empty
            with open(file_path, 'r') as f:
                try:
                    data = json.load(f)
                    if isinstance(data, list): # Check if the existing json is a list
                        data.append(log_entry)
                    else:
                        data = [data, log_entry] # If it's not a list, treat it as a single entry and create a list
                except json.JSONDecodeError:
                    data = [log_entry] #Handle the case where the existing json is corrupted
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)  # Use indent for pretty printing
        else:
            with open(file_path, 'w') as f:
                json.dump([log_entry], f, indent=4) # Create file if it doesn't exist and write the first entry

    except Exception as e:
        print(f"Error writing to JSON file: {e}")



def get_user_input():
    """Gets log data from the user."""
    exercise_number = input("Enter the exercise number: ")
    time_to_solution = input("Enter the time to solution: ")
    algo_speed = input("Enter the algorithm speed: ")
    algo_space = input("Enter the algorithm space: ")
    required_extra_study = input("Enter the required extra study: ")

    log_data = {
        "Exercise": exercise_number,
        "Approximate_time": time_to_solution,
        "Algorithm_speed": algo_speed,
        "Algorithm_space": algo_space,
        "Required_extra_study": required_extra_study
    }
    return log_data

if __name__ == "__main__":
    user_data = get_user_input()
    log_entry = create_log_entry(user_data)
    write_to_json(log_entry)
    print("Log entry added to db.json")
