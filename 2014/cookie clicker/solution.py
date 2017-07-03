for case in range(1, int(input()) + 1):
    c, f, x = map(float, input().split())

    cps = 2
    current_time = 0

    while True:
        time_to_reach_at_current_rate = x / cps
        acc_time_to_reach_at_current_rate = current_time + time_to_reach_at_current_rate

        time_to_build_farm = c / cps
        time_to_reach_with_new_farm = current_time + time_to_build_farm + x / (cps + f)

        if time_to_reach_with_new_farm < acc_time_to_reach_at_current_rate:
            cps += f
            current_time += time_to_build_farm
        else:
            current_time += time_to_reach_at_current_rate
            break
            
    print("Case #{}: {}".format(case, current_time))
