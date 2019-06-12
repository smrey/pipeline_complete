import os
import sys

path_to_data = os.path.join("/","Users","sararey","tmp") # hard code to results directory
dirlist = os.listdir(path_to_data)

run_id = "190524_D00501_0318_BHYMM2BCX2" # need to obtain on the fly
run_id = "190607_M00766_0229_000000000-CCWJY"

run_path = os.path.join(path_to_data,run_id)

print(run_path)


def main():
    sample_level(run_path)
    return None


def sample_level(directory):
    panels_list = filter(lambda x: os.path.isdir(os.path.join(directory, x)), os.listdir(directory))
    panels_path_list = [os.path.join(directory, d) for d in panels_list]
    print(panels_path_list)

    print([os.listdir(x) for x in panels_path_list])

    #samples_list = filter(lambda x: os.path.isdir(os.path.join(panels_path_list, x)), os.listdir(panels_path_list))
    #print(samples_list)

    return None


def run_level(directory):
    return None




if __name__ == '__main__':
        main()