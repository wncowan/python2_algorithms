
def run_a_filter(input_list):
    filtered_list = filter(lambda x: x % 2 == 0, input_list)
    print filtered_list

run_a_filter([1,2,3,4,5,6,7,8,9,10,20])

