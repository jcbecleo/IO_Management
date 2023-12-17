import matplotlib.pyplot as plt

def fcfs(arr, head):
    seek_sequence = []
    total_seek_time = 0

    for track in arr:
        seek_sequence.append(track)
        total_seek_time += abs(track - head)
        head = track

    return seek_sequence, total_seek_time

def plot_graph(track_requests, seek_sequence, initial_head):
    sequence_with_head = [initial_head] + seek_sequence
    plt.plot(range(len(sequence_with_head)), sequence_with_head, color='blue', marker='o', label='Service Order')

    for i, txt in enumerate(sequence_with_head):
        plt.annotate(txt, (i, sequence_with_head[i]), textcoords="offset points", xytext=(0, 10), ha='center')

    plt.title('FCFS Disk Scheduling Algorithm')
    plt.xlabel('Point Number')
    plt.ylabel('Request Order')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    track_requests = [96, 120, 156, 80, 130, 9, 48, 32, 50, 12, 2]
    initial_head = 55

    seek_sequence, total_seek_time = fcfs(track_requests, initial_head)

    print("Seek Sequence:", seek_sequence)
    print("Total Seek Time:", total_seek_time)

    plot_graph(track_requests, seek_sequence, initial_head)
