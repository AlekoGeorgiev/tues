class Files:
    def __init__(self, file_list):
        self.file_list = file_list
        
    def add_file(self, new_file):
        self.file_list.append(new_file)
    
    def read_all(self):
        for i in self.file_list:
            with open(i, "r") as fr:
                print(fr.read())
    
    def count_all(self, word):
        count = 0
        for i in self.file_list:
            text = ""
            with open(i, "r") as fr:
                for j in fr:
                    
                    text = j.split(" ")
                    for i in range(len(text)):
                        text[i] = text[i].strip("\n \" \' , . ' ? !")
                    
                    count += text.count(word)
        
        return count
                

files = Files(["file1.txt"])
files.add_file("file2.txt")
files.read_all()
print("Number of occurances: ", files.count_all(input("Enter a word: ")))
