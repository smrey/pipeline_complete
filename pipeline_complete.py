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

    panels_samples_list = ([filter(lambda x: os.path.isdir(os.path.join(y, x)), os.listdir(y)) for y in panels_path_list])
    print([f for f in panels_samples_list])
    
    #samples_path_list = [os.path.join(directory, di) for di in samples_list]
    #print(samples_path_list)


    return None


def run_level(directory):
    return None




if __name__ == '__main__':
        main()