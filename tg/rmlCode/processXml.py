from subprocess import PIPE, Popen
import os

path1 = "C:/Users/geron/AppData/Local/Programsrmlmapper/rmlmapper-java/target"
path2 = "C:/Users/geron/OneDrive - UW/Documents/linkedData/rml/2022/rmlCode"

#process = Popen(['java', '-jar', 'C:/Users/geron/AppData/Local/Programs/rmlmapper/rmlmapper-java/target/rmlm.jar', '-m', 'C:/Users/geron/OneDrive - UW/Documents/linkedData/rml/2022/rmlCode/practiceLevel1.ttl', '-o', 'turtle'], stdout=PIPE, stderr=PIPE)
#result = process.communicate()
#print(result[0].decode('utf-8'))

#print(os.system(f"java -jar C:/Users/geron/AppData/Local/Programs/rmlmapper/rmlmapper-java/target/rmlm.jar -m C:/Users/geron/OneDrive - UW/Documents/linkedData/rml/2022/rmlCode/practiceLevel1.ttl -o turtle"))

result = os.system(f"java -jar C:/Users/geron/AppData/Local/Programs/rmlmapper/rmlmapper-java/target/rmlm.jar -m practiceLevel1.ttl -s turtle")
print(result)
#print(os.system(f"java -jar /:/Users/geron/AppData/Local/Programs/rmlmapper/rmlmapper-java/target/rmlm.jar -h"))