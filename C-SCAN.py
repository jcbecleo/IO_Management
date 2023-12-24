import matplotlib.pyplot as plt

def c_scan_disk_scheduling(requests, start_position, disk_size):
    total_seek_count = 0
    seek_sequence = []

    requests.append(0)
    requests.append(disk_size - 1)
    requests.sort()
    
    # Find the closest requests in both directions
    left_requests = [r for r in requests if r < start_position]
    right_requests = [r for r in requests if r >= start_position]

    seek_sequence.append(start_position)

    for request in right_requests:
        seek_sequence.append(request)
        total_seek_count += abs(request - start_position)
        start_position = request

    if left_requests:
        for request in left_requests:
            seek_sequence.append(request)
            total_seek_count += abs(request - start_position)
            start_position = request

    return seek_sequence, total_seek_count

def plot_graph(seek_sequence):
    x = list(range(len(seek_sequence)))
    plt.plot(x, seek_sequence, color='blue', marker='o', label='Service Order')

    for i, track in enumerate(seek_sequence):
        plt.text(i, track, f'{track}', fontsize=8, ha='right', va='bottom', color='blue')
        
    plt.title('C-SCAN Disk Scheduling')
    plt.xlabel('Request Order')
    plt.ylabel('Track Number')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.show()

if __name__ == "__main__":
    requests = [96, 120, 156, 80, 130, 9, 48, 32, 50, 12, 2]
    start_position = 55
    disk_size = 200

    seek_sequence, total_seek_count = c_scan_disk_scheduling(requests, start_position, disk_size)
    print("Total Seek Count:", total_seek_count)
    plot_graph(seek_sequence)