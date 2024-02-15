import pandas as pd
import matplotlib.pyplot as plt

def plot_timeline(disk_letter):
    logfile = f'{disk_letter}:\\LOGFILE.CSV'
    try:
        df = pd.read_csv(logfile)
    except FileNotFoundError:
        print(f"Error: Could not find {logfile}")
        return

    plt.figure(figsize=(10, 6))
    plt.plot([int(s) for s in df[df.columns[0]][1:]], [float(s) for s in df[df.columns[1]][1:]], label=df.columns[1])
    plt.xlabel(df.columns[0] +' ('+ df[df.columns[0]][0] +')')
    plt.ylabel(df.columns[1] +' ('+ df[df.columns[1]][0] +')')
    plt.title(f'Timeline Data for Disk {disk_letter}')
    plt.grid(True)
    plt.legend()
    plt.show()

# Example usage:
disk_letter = input("Enter disk letter designator: ")
plot_timeline(disk_letter)
