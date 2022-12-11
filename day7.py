from collections import defaultdict


def ans(inp):
    # data = {}
    current_dir = []
    places = defaultdict(int)
    seen = set()
    for line in inp:
        line = line.strip()
        if line[0] == "$":
            if "cd" in line:
                place = line.split(" ")[-1]
                if place == "..":
                    current_dir.pop()
                else:
                    current_dir.append(place)
        elif "dir" not in line:
            # curr = data
            size, file = line.split(" ")
            full_name = "/".join(current_dir)+"/"+file
            if full_name not in seen:
                seen.add(full_name)
                for i, d in enumerate(current_dir):
                    # if d not in curr:
                    #     curr[d] = {}
                    # curr = curr[d]
                    dir_name = "/".join(current_dir[:i+1])
                    places[dir_name] += int(size)
                # curr[file] = size
    # print(data)
    # print(places.items())
    tot = 0
    for place, size in places.items():
        if size <= 100000:
            tot += size
    return tot


def ans2(inp):
    current_dir = []
    places = defaultdict(int)
    seen = set()
    for line in inp:
        line = line.strip()
        if line[0] == "$":
            if "cd" in line:
                place = line.split(" ")[-1]
                if place == "..":
                    current_dir.pop()
                else:
                    current_dir.append(place)
        elif "dir" not in line:
            size, file = line.split(" ")
            full_name = "/".join(current_dir)+"/"+file
            if full_name not in seen:
                seen.add(full_name)
                for i, d in enumerate(current_dir):
                    dir_name = "/".join(current_dir[:i+1])
                    places[dir_name] += int(size)

    all_files = places["/"]
    unused_space = 70000000 - all_files
    to_free = 30000000 - unused_space

    smallest_delete = all_files

    for place, size in places.items():
        if to_free <= size < smallest_delete:
            smallest_delete = size
    return smallest_delete



if __name__ == '__main__':
    with open("inputs/testinp7.txt") as tstfile:
        assert ans(tstfile.readlines()) == 95437

    with open("inputs/inp7.txt") as txtfile:
        assert ans(txtfile.readlines()) == 1491614

    with open("inputs/testinp7.txt") as tstfile:
        assert ans2(tstfile.readlines()) == 24933642

    with open("inputs/inp7.txt") as txtfile:
        print(ans2(txtfile.readlines()))
