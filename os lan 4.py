class Process:
    def __init__(self, pid, bt, art):
        self.pid = pid
        self.bt = bt
        self.art = art

def findavgTime(proc):
    n = len(proc)
    wt = [0] * n
    for i in range(n):
        wt[i] = (i == 0) and 0 or wt[i-1] + proc[i-1].bt
    print(" P\t\tBT\t\tWT")
    for i in range(n):
        print(f"{proc[i].pid}\t\t{proc[i].bt}\t\t{wt[i]}")

# Example usage
proc = [Process(1, 10, 0), Process(2, 5, 1), Process(3, 8, 2)]
findavgTime(proc)
