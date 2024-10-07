import sys

#To run
#python logcombiner.py new.log repo1.log repo2.log repo3.log repo4.log

def combine_and_sort_logs(output_file, *log_files):
    combined_logs = []

    # Read each log file
    for log_file in log_files:
        try:
            with open(log_file, 'r') as f:
                for line in f:
                    combined_logs.append(line.strip())
        except FileNotFoundError:
            print(f"Error: {log_file} not found.")
            return
    
    # Sort logs by the timestamp, which is the first part of each line before the '|'
    combined_logs.sort(key=lambda line: int(line.split('|')[0]))

    # Write the combined and sorted logs to the output file
    try:
        with open(output_file, 'w') as f:
            for log in combined_logs:
                f.write(log + '\n')
        print(f"Combined log written to {output_file}")
    except Exception as e:
        print(f"Error writing to {output_file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python combine_logs.py output_file log1.log log2.log ...")
    else:
        output_file = sys.argv[1]
        log_files = sys.argv[2:]
        combine_and_sort_logs(output_file, *log_files)
