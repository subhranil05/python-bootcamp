import csv

# with open('cities.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     next(csv_file)
#     for line in csv_reader:
#         print(line[0])
        
        


# with open('cities.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
    
#     with open('new-cities.csv', 'w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='-')
        
#         for line in csv_reader:
#             csv_writer.writerow(line)
            
            
# with open('cities.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
    
#     for line in csv_reader:
#         print(line)
        
        

with open('cities.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    with open('new-cities.csv', 'w') as new_file:
        fieldnames = ['LatD', ' LatM', ' NS', ' City', ' LonD', ' LonS', ' LonM', ' State', ' EW', ' LatS']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        
        csv_writer.writeheader()
        
        for line in csv_reader:
            csv_writer.writerow(line)