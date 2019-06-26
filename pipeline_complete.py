import os
import sys
import glob

path_to_data = os.path.join("/","Users","sararey","tmp") # hard code to results directory
dirlist = os.listdir(path_to_data)

run_id = "190524_D00501_0318_BHYMM2BCX2" # need to obtain on the fly
run_id = "190607_M00766_0229_000000000-CCWJY"

run_path = os.path.join(path_to_data,run_id)

#print(run_path)

# Current versions of pipeline check?
# Load in file with currently used versions of pipeline

def main(): #pass global variables in?
    # Check results folder has been correctly created
    check_results_folder(run_path)

    # load variables file and identify pipeline- assumes that each panel has at least one sample
    try:
        print("loading variables file")
        panels_fullpath_filter = filter(lambda x: os.path.isdir(os.path.join(run_path, x)), os.listdir(run_path))
        panels_fullpath = [os.path.join(run_path, p) for p in panels_fullpath_filter]
        print(panels_fullpath)

        print("more than one panel")
        print(panels_fullpath)
        # Obtain just panel name without leading path
        panels = ([os.path.split(i)[-1] for i in panels_fullpath])
        # Create nested dictionary
        panels_dict = {}
        # Obtain samples and parse variables files
        for p in panels_fullpath:
            samples_fullpath_filter = filter(lambda x: os.path.isdir(os.path.join(p, x)),
                                                os.listdir(p))
            samples_fullpath = [os.path.join(run_path, f) for f in samples_fullpath_filter]
            #panels_samples = [os.path.split(i)[-1] for i in samples_fullpath]
            # Obtain just panel name without leading path
            panel_name = os.path.split(p)[-1]
            #print(panels_samples)

            samples_dict = {}

            # Add data to nested dictionary
            for ps in samples_fullpath:
                #print(glob.glob(os.path.join(p, ps, "*.variables")))
                print(ps)
                samples_name = os.path.split(ps)[-1]
                print(samples_name)
                # Add second key to dictionary
                values_dict = {}
                # Parse variables file
                with open(os.path.join(p, samples_name, samples_name + ".variables")) as f:
                    for line in f:
                        if not (line.startswith("#") or line.isspace()):
                            print(line.rstrip())
                            divide_line = line.rstrip().split("=")
                            variable = divide_line[0]
                            value = divide_line[1]
                            # Add data to dictionary
                            values_dict[variable] = value
                samples_dict[samples_name] = values_dict
            panels_dict[panel_name] = samples_dict
        print(panels_dict)


    except:
        raise Exception("Variables file could not be loaded or parsed")

    #panel_level(run_path)

    # Identify pipeline- where in flow to place this?

    # Check run level processing complete if applicable- germline enrichment panels only

    # Check sample level processing complete if applicable



    return None

def check_results_folder(run_directory):
    try:
        print("results folder is " + run_directory)
    except:
        raise Exception(f"There is no results folder for run {run_id} also {run_path}")

def load_variables():
    return None


def sample_level(run_directory):
    for i in run_directory:
        print(i)
        samples_list = filter(lambda x: os.path.isdir(os.path.join(i, x)), os.listdir(i))
        samples_path_list = [os.path.join(i, s) for s in samples_list]
        print(samples_path_list)

    return None


def panel_level(panel_directory):
    panels_list = filter(lambda x: os.path.isdir(os.path.join(panel_directory, x)), os.listdir(panel_directory))
    panels_path_list = [os.path.join(panel_directory, d) for d in panels_list]
    print(panels_path_list)

    return None

def check_run_level():
    return None

def check_sample_level():
    return None


if __name__ == '__main__':
        main()