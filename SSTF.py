import matplotlib.pyplot as plt

def sstf(requests, initial_head):
    total_seek_count = 0
    current_head = initial_head
    order_of_service = []
    
    while requests:
        distances = [abs(track - current_head) for track in requests]
        min_distance_index = distances.index(min(distances))
        next_track = requests.pop(min_distance_index)

        total_seek_count += distances[min_distance_index]
        order_of_service.append(next_track)

        current_head = next_track

    return total_seek_count, order_of_service

def plot_sstf(requests, initial_head):
    total_seek_count, order_of_service = sstf(requests, initial_head)

    plt.plot(range(len(order_of_service) + 1), [initial_head] + order_of_service, color='blue', marker='o', label='Service Order')

    for i, track in enumerate([initial_head] + order_of_service):
        plt.text(i, track, f'{track}', fontsize=8, ha='right', va='bottom', color='blue')

    plt.ylim(0, 200)  # Adjust the limit as needed OR remove

    plt.title('SSTF Disk Scheduling')
    plt.xlabel('Request Order')
    plt.ylabel('Track Number')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.show()

    return total_seek_count

requests = [96, 120, 156, 80, 130, 9, 48, 32, 50, 12, 2]
initial_head_position = 55

total_seek_count = plot_sstf(requests, initial_head_position)
print(f'Total Seek Count: {total_seek_count}')