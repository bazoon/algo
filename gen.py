def long_process(id, n):
    sum = 0
    for x in range(n):
        sum += x
        # print(id, sum)
        yield
    yield sum





def run_processes(params):
	processes = []
	R = {}
	index = 1
	
	for param in params:
		id = "Id" + str(index)
		processes.append({ "id": id, "p": long_process(id, param)})
		R[id] = None
		index += 1



	for i in range(max(params) + 1):
		for process in processes:
			if R[process["id"]] is None:
				R[process["id"]] = next(process["p"])
	    
	print(R)	


run_processes([10, 100, 10000, 100000])
