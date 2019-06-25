import os
import sys
import glob

path_to_data = os.path.join("/","Users","sararey","tmp") # hard code to results directory
path_to_data = os.path.join("C:\\","Users","saram","Documents","Work","mockdata")
dirlist = os.listdir(path_to_data)

run_id = "190524_D00501_0318_BHYMM2BCX2" # need to obtain on the fly
run_id = "190607_M00766_0229_000000000-CCWJY"

run_path = os.path.join(path_to_data,run_id)

#print(run_path)


def main():
    sample_level(run_path)
    return None


def sample_level(directory):
    panels_list = filter(lambda x: os.path.isdir(os.path.join(directory, x)), os.listdir(directory))
    #print(panels_list)
    panels_path_list = [os.path.join(directory, d) for d in panels_list]
    #print(panels_path_list)

    panels_dict = {}
    for i in panels_path_list:
        #print(i)
        panel_name = os.path.split(i)[1]
        print(panel_name)
        samples_list = filter(lambda x: os.path.isdir(os.path.join(i, x)), os.listdir(i))
        samples_path_list = [os.path.join(i, s) for s in samples_list]
        #print(samples_path_list)


        samples_dict = {}
        for fl in samples_path_list:
            #print(fl)
            samples_name = os.path.split(fl)[1]
            print(samples_name)
            values_dict = {}
            with open(glob.glob(fl + "\*.variables")[0]) as f:
                for line in f:
                    splitter = line.rstrip().split("=")
                    the_key = splitter[0]
                    the_value = splitter[1]
                    values_dict[the_key] = the_value
                print(values_dict)
            samples_dict[samples_name] = values_dict
        print(samples_dict)
        panels_dict[panel_name] = samples_dict
    print(panels_dict)


    return None


def run_level(directory):
    return None




if __name__ == '__main__':
        main()