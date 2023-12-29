import matplotlib.pyplot as plt

def look(arr, head):
    arr.sort()

    index = 0
    for i in range(len(arr)):
        if arr[i] >= head:
            index = i
            break

    seek_sequence = []
    total_seek_time = 0

    for i in range(index, len(arr)):
        seek_sequence.append(arr[i])
        total_seek_time += abs(arr[i] - head)
        head = arr[i]

    for i in range(index - 1, -1, -1):
        seek_sequence.append(arr[i])
        total_seek_time += abs(arr[i] - head)
        head = arr[i]

    return seek_sequence, total_seek_time

def plot_graph(track_requests, seek_sequence, initial_head):
    sequence_with_head = [initial_head] + seek_sequence
    plt.plot(range(len(sequence_with_head)), sequence_with_head, color='blue', marker='o', label='Service Order')

    for i, txt in enumerate(sequence_with_head):
        plt.annotate(txt, (i, sequence_with_head[i]), textcoords="offset points", xytext=(0, 10), ha='center')

    plt.title('LOOK Disk Scheduling Algorithm')
    plt.xlabel('Point Number')
    plt.ylabel('Request Order')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    track_requests = [96, 120, 156, 80, 130, 9, 48, 32, 50, 12, 2]

    initial_head = 55

    seek_sequence, total_seek_time = look(track_requests, initial_head)

    print("Seek Sequence:", seek_sequence)
    print("Total Seek Time:", total_seek_time)

    plot_graph(track_requests, seek_sequence, initial_head)