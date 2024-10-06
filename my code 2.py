# Define a function to implement FCFS scheduling
def fcfs_scheduling(processes):
    # Sort the processes based on their arrival time
    processes.sort(key=lambda x: x[1])

    # Initialize the current time and the schedule
    current_time = 0
    schedule = []

    # Iterate over the sorted processes
    for process in processes:
        # Update the current time to the maximum of the current time and the process arrival time
        current_time = max(current_time, process[1])

        # Add the process to the schedule
        schedule.append((process[0], current_time, current_time + process[2]))

        # Update the current time to the completion time of the process
        current_time += process[2]

    return schedule

# Example usage
processes = [
    ("P1", 0, 5),  # Process name, arrival time, burst time
    ("P2", 1, 3),
    ("P3", 2, 2),
    ("P4", 4, 4)
]

schedule = fcfs_scheduling(processes)

# Print the schedule
for process in schedule:
    print(f"Process {process[0]} starts at {process[1]} and ends at {process[2]}")
