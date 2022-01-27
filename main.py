class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def __repr__(self):
        return "Node : {}".format(self.data)

class LinkedList:
    def __init__(self):
        self.head=None
        self.total=0

    def insertNode(self,data):
        """it will insert in very first of the node"""
        newdata=Node(data)
        if self.head is  None:
            self.head=newdata
            newdata.next=None
            self.total=self.total+1
        else:
            newdata.next=self.head
            self.head=newdata
            self.total=self.total+1
    def insertNodeLast(self,data):
        newNode=Node(data)
        self.total = self.total + 1
        if self.head is None:
            self.head=newNode
            self.head.next=None

        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            #print(temp.data)
            temp.next=newNode
            #newNode.next=None


    def printAll(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next

    def printAll(self,node1):
        temp = node1.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
    def totLength(self):
        return self.total

    def __repr__(self):
        return "LList : {}".format(self.head)

    def delNodeLast(self):

        if self.head is None:
            return
        temp=self.head
        previous=None
        while temp.next is not None:
            previous=temp
            temp=temp.next
        previous.next=None
        del(temp)
        #print("lasrt Node : {}".format(temp.data))
        #temp=None

    def delNode(self,mode):

        if self.head is None:
            return
        temp=self.head
        previous=self.head
        while temp.next is not None and temp.data!=mode:
            previous=temp
            temp=temp.next
        previous.next=temp.next
    def link2list(self,list1,list2):

        if list1 is None and list2 is None:
            return
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        newlist=LinkedList()
        temp=list1.head
        temp2=list2.head
        while temp is not None and temp2 is not None:
            if temp is not None:
                newlist.insertNode(temp.data)
                temp = temp.next
            if temp2 is not None:
                newlist.insertNode(temp2.data)
                temp2 = temp2.next

        return newlist

def bubbleSorting(arr): #comparing each element and place each in last and decrease
    #every

    for a in range(len(arr)):
        check=True
        for c in range (1,len(arr)-a):
            if(arr[c]<arr[c-1]):
                check=False
                #j=arr[a+1]
                arr[c],arr[c-1]=arr[c-1],arr[c]
        if check:
            break
def selectionSort(arr):

    for a in range (len(arr)):
        last=len(arr)-a-1
        max=maximum(arr,0,last)
        arr[max],arr[last]=arr[last],arr[max]



def maximum(arr,start,end):
    maxi=start
    for a in range(start,end+1):
        if arr[maxi]<arr[a]:
            maxi=a
    return maxi
#Tiger , peacock , dindigul , apple , 23
if __name__=="__main__":
    lt=LinkedList()
    lt1 = LinkedList()
    lt2= LinkedList()
    lt.insertNode("Amma")
    lt.insertNode("appa")
    lt1.insertNode("Thatha ")
    lt1.insertNode("paati")
    lt2.insertNode("sithi")
    lt2.insertNode("sithappa")
    print("tot Length :{}".format(lt.totLength()))

    arr=[200,150,99,23,11,1]
    selectionSort(arr)
    print(arr)
