class BookStore:
    NoOfBooks = 0

    def __init__(self,A,B):
        self.BookName = A
        self.Author = B
        BookStore.NoOfBooks +=1

    def Display(self):
        print(self.BookName, "by", self.Author,".No of books:",BookStore.NoOfBooks)

print("Enter book name :")
BookName = input()

print("Enter book author :")
Author = input()

bobj = BookStore(BookName,Author)
bobj.Display()