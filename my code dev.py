class Process:
    def __init__(self, pid, bt, art):
        self.pid = pid
        self.bt = bt
        self.art = art

def findavgTime(proc):
    n = len(proc)
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0

    for i in range(n):
        minm = float('inf')
        shortest = 0
        for j in range(n):
            if proc[j].art <= i and proc[j].bt < minm:
                minm = proc[j].bt
                shortest = j
        wt[shortest] = i - proc[shortest].art
        tat[shortest] = wt[shortest] + proc[shortest].bt
        proc[shortest].bt = 0

    print(" P\t\tBT\t\tWT\t\tTAT")
    for i in range(n):
        print(f"{proc[i].pid}\t\t{proc[i].bt}\t\t{wt[i]}\t\t{tat[i]}")
        total_wt += wt[i]
        total_tat += tat[i]

    print(f"\nAverage waiting time = {total_wt / n}")
    print(f"Average turn around time = {total_tat / n}")

# Example usage
proc = [Process(1, 10, 0), Process(2, 5, 1), Process(3, 8, 2)]
findavgTime(proc)
