from multiprocessing import Process, Pipe


def local_time(counter):
    return ' {}'.format(counter)


def calc_recv_timestamp(recv_time_stamp, counter):
    for id in range(len(counter)):
        counter[id] = max(recv_time_stamp[id], counter[id])
    return counter


def event(pid, counter):
    counter[pid] += 1
    a = str(format(pid) + local_time(counter))
    return counter


def send_message(pipe, pid, counter):
    counter[pid] += 1
    pipe.send(('Empty shell', counter))
    print(str(pid) + local_time(counter))
    return counter


def recv_message(pipe, pid, counter):
    counter[pid] += 1
    message, timestamp = pipe.recv()
    counter = calc_recv_timestamp(timestamp, counter)
    print(str(pid) + local_time(counter))
    return counter


def process_A(pipe_ab):
    pid = 0
    counter = [0, 0, 0]

    counter = send_message(pipe_ab, pid, counter)  # blue, a0 - b0
    counter = send_message(pipe_ab, pid, counter)  # green, a1 - b1
    counter = event(pid, counter)  # a2
    counter = recv_message(pipe_ab, pid, counter)  # red, b2 - a3
    counter = event(pid, counter)  # a4
    counter = event(pid, counter)  # a5
    counter = recv_message(pipe_ab, pid, counter)  # violet, b5 - a6


def process_B(pipe_ba, pipe_bc):
    pid = 1
    counter = [0, 0, 0]

    counter = recv_message(pipe_ba, pid, counter)  # blue, a0 - b0
    counter = recv_message(pipe_ba, pid, counter)  # green, a1 - b1
    counter = send_message(pipe_ba, pid, counter)  # red, b2 - a3
    counter = recv_message(pipe_bc, pid, counter)  # orange, c0 - b3
    counter = event(pid, counter)  # b4
    counter = send_message(pipe_ba, pid, counter)  # violet, b5 - a6
    counter = send_message(pipe_bc, pid, counter)  # brown, b6 - c1
    counter = send_message(pipe_bc, pid, counter)  # pink, b7 - c3


def process_C(pipe_cb):
    pid = 2
    counter = [0, 0, 0]

    counter = send_message(pipe_cb, pid, counter)  # orange, c0 - b3
    counter = recv_message(pipe_cb, pid, counter)  # brown, b6 - c1
    counter = event(pid, counter)  # c2
    counter = recv_message(pipe_cb, pid, counter)  # pink, b7 - c3


if __name__ == '__main__':

    oneandtwo, twoandone = Pipe()
    twoandthree, threeandtwo = Pipe()

    process_a = Process(target=process_A, args=(oneandtwo,))
    process_b = Process(target=process_B, args=(twoandone, twoandthree))
    process_c = Process(target=process_C, args=(threeandtwo,))

    process_a.start()
    process_b.start()
    process_c.start()

    process_a.join()
    process_b.join()
    process_c.join()