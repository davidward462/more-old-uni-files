#testing computer class
import computer as cp #name file "computer" to "cp"

def countBrand(computerList):
	dell = 0
	for i in computerList:
		if i.getBrand() == "dell":
			dell += 1
	return dell
	
	
def countType(computerList):
	laptop = 0
	for i in computerList:
		if i.getType() == "laptop":
			laptop += 1
	return laptop
			

def main():
	computerList = []
	
	for i in range(0, 4):
		computerList.append(cp.computer())
	
	computerList[0].setBrand("dell")
	computerList[1].setType("laptop")
	computerList[2].setBrand("dell")
	computerList[3].setType("laptop")
	
	dellNum = countBrand(computerList)
	laptopNum = countType(computerList)
	
	print(dellNum)
	print(laptopNum)
	
	



if __name__=="__main__":
	main()