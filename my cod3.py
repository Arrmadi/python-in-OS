def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x[1])
    schedule = []
    current_time = 0
    for process in processes:
        current_time = max(current_time, process[1])
        schedule.append((process[0], current_time, current_time + process[2]))
        current_time += process[2]
    return schedule

processes = [("P1", 0, 5), ("P2", 1, 3), ("P3", 2, 2), ("P4", 4, 4)]
schedule = fcfs_scheduling(processes)
