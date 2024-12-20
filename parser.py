def parse_client_output(data) -> list:
    intervals = data.split('\n')[7:-4]
    formatted = []
    print("iperf output:")
    for interval in intervals:
        l = list(filter(lambda a: a != "", interval.split(" ")))
        if len(l) >= 6:
            formatted_interval = {
              "Interval": l[2],
              "Transfer": l[4],
              "Bandwidth": l[6],
            }
            formatted.append(formatted_interval)
            print(formatted_interval)
    print("-----------------------------")
    return formatted