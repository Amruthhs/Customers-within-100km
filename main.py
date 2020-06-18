import customer_records_great_circle
import readfile_input

def Main():
    cr = customer_records_great_circle.CustomerRecords('customer_list.txt', 100000, 53.339428, -6.257664)
    cr.get_closest_customers()

if __name__ == "__main__":
    Main()