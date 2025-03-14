# Open the file in read mode
import subprocess
def extArrival(i = 0):
         with open(f'in/{i}.txt', 'r') as file:
              lines = file.readlines() 
              nlines = 0
              for i in range(len(lines)):
                  l = lines[i].strip()
                  if len(l) == 0:
                     pass 
                  elif l[0] == 'a': 
                     separated = l.split()  
                     return separated[2]

def getArrival(start = 0, end = 0, source = ' '):
  out = [] 
  table = 'arrivalTime'
  out.append(f"DROP TABLE IF EXISTS {table};")
  out.append(f"create table {table}(ID INT, arrivalTime FLOAT, source TEXT, statement INT);")
  for i in range(start,end):   
    arrivalTime = extArrival(i= i)
    out.append(f"insert into {table}(ID, arrivalTime, source, statement) values({i}, {arrivalTime}, '{source}',{i});")
  out.append(f"SELECT * FROM {table};")
  with open('sql.sql', 'w') as sqlFile:
    sqlFile.write("\n".join(out))

getArrival(1,15, 'find')

output = subprocess.check_output('sqlite3 database.db ".mode column" ".read sql.sql"', shell=True, text=True)
print(output)
