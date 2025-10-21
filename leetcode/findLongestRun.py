def findLongestRun(runLogs):
    if not runLogs:
        return ''
    
    # Dictionary to store the longest run for each process
    longest_runs = {}
    
    # Start with the first process
    current_process = runLogs[0][0]
    start_time = runLogs[0][1]
    
    # Iterate through the logs
    for i in range(1, len(runLogs)):
        process_id = runLogs[i][0]
        end_time = runLogs[i][1]
        
        # If process changed, calculate the run duration
        if process_id != current_process:
            run_duration = end_time - start_time
            
            # Update longest run for this process
            if current_process not in longest_runs:
                longest_runs[current_process] = run_duration
            else:
                longest_runs[current_process] = max(longest_runs[current_process], run_duration)
            
            # Start tracking the new process
            current_process = process_id
            start_time = end_time
    
    # Don't forget the last process run
    # It runs until the end time of the last log entry
    final_end_time = runLogs[-1][1]
    run_duration = final_end_time - start_time
    
    if current_process not in longest_runs:
        longest_runs[current_process] = run_duration
    else:
        longest_runs[current_process] = max(longest_runs[current_process], run_duration)
    
    # Find the process with the longest run
    max_process = max(longest_runs, key=longest_runs.get)
    
    # Convert process number to character (0 -> 'a', 1 -> 'b', etc.)
    return chr(ord('a') + max_process)


# Test with the example
runLogs = [[0, 3], [2, 5], [0, 9], [1, 15]]
print(findLongestRun(runLogs))  # Output: 'b'
