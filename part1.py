class Package:
    def __init__(self,id):
        self.id = id 
        self.address = ""
        self.office = ""
        self.ownerName = ""
        self.collected = False 
        self.delivered = False
        
class Truck:
    def __init__(self,id,n,loc):
        # unique identifier of the truck
        self.id = id 
        # the size of the truck; max packages can be stored in a truck 
        self.size = n 
        # current location of the truck 
        self.location = loc
        # the packages that have been loaded in a truck 
        self.packages = []
        '''
        use a stack method here since you deliver the ones on the outside first,
        and deliver the ones the went in first the last
        '''
    
    # pk from here on is a instance of the Package class
    def collectPackage(self,pk):
        if self.location == pk.office:
            self.packages.append(pk)

    
    def deliverOnePackage(self, pk):
        storage = []
        for i in range(len(self.packages)):
            if self.packages[i] == pk:
                storage += i
                
        if storage == []:
            print("There is no such package!")
            return None 
        
        if self.location == pk.address:
            self.packages.pop(storage)
            pk.delivered = True
            
    def deliverPackages(self):
        if len(self.packages) == 0:
            print("There is no package!")
            return None 
        index = []
        
        for i in self.packages:
            index += self.packages.index(i)
        
        for package in self.packages:
            index = self.packages.index(package)
            if package.address == self.location:
                package.delivered = True
                self.packages.pop(index)
                
                
        
    def driveTo(self, loc):
        self.location = loc
    
    def getPackagesIds(self):
        ids = []
        for i in self.packages:
            ids.append(i.id)
        return ids
    
    def removePackage(self,pk):
        if (pk.delivered == False) and (self.location == pk.office):
            for i in range(len(self.packages)):
                self.packages.pop(self.packages[i])
                print("package is returned to post service office")