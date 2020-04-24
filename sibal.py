def merge(input_list):
    result=[]
    for i, elem in enumerate(input_list):
        if i%2 is 1:
            s1=set()
            for ele in elem:
                s1.add(ele)
            for ele in input_list[i-1]:
                s1.add(ele)
            li = list(s1.copy())
            result.append(li)
    return result

def clustering(input_list):
	result = []
	zero_count = 0
	count = 0
	pos = 0
	flag = False
	
	for i, elem in enumerate(input_list):
		if elem is not 0:
			flag = True
			count +=1
			
		if elem is 0 and flag is True:
			zero_count += 1
			count += 1
			
		if zero_count is 3:
			pos = i
			result.append(pos - 2 - (count-2)//2)
			zero_count =0
			count = 0
			flag = False
			
	return result
	
			#result.append(elem)


#최대로 벌어진 마디가 몇번째 마디인지 (거리list , 제일벌어진마디 몇번째)		
def choichoi(index_list,list):
	import numpy as np
	index_chai_list = []
	min_list = []
	max_list = []
	minmaxcha = []
	for elem in index_list:
		if elem-10<0 or elem+10>len(list):
			index_chai_list.append(0)
			pass
		else:
			narray=np.array(list[elem-5:elem+5])
			min_idx = np.argmin(narray)
			max_idx = np.argmax(narray)
			index_chai_list.append(abs(min_idx-max_idx))
			min_list.append(narray[min_idx])
			max_list.append(narray[max_idx])
	
	idx = np.argmax(np.array(index_chai_list))
	#print("idxc:",index_chai_list,"idx:",idx)
	return (index_chai_list,idx)
		
def which_disable(avg):
	if avg < 250 :
		return "RBBB"
	else :
		return "LBBB"
	

from PIL import Image
import pdb
import numpy as np
import cv2
import matplotlib.pyplot as plt
yes = 0
no = 0

for _i in range(1,40):
	img = cv2.imread('C:\\Users\\wnddk\\Desktop\\patient\\RBBB\\'+str(_i)+'.jpg')
	im = Image.open('C:\\Users\\wnddk\\Desktop\\patient\\RBBB\\'+str(_i)+'.jpg')

	subimg = img[70:570, 128:780]
	b, g, r = cv2.split(subimg)


	cv2.imwrite('1.jpg',b)
#cv2.imshow('cutting' , subimg)



	height, width, channel = subimg.shape
#print(height, width)
 
	pix = np.array(b)

	_list=[]
	testlist=[]
##리스트가 아닌 2차원배열에 저장하는게 훨씬 좋을듯


#(y,x) 형태 데이터를 (x,y)로 바꿈
#height = 500 width = 652
	for x in range(width):
		temp = []
		for y in range(height):
			if pix[y][x] < 200:
				temp.append(y)            
		_list.append(temp)
		testlist.append(temp)

    
#list는 x좌표 0부터 시작하고 해당하는 x좌표에 따른 y좌표 : ex) list [ [110,111,112]. [113.114,115]] 
#print(list)    


#count_list :: x좌표에 그려진 y좌표의 픽셀 개수를 차례로 저장함
	count_list = []
	for x in range(width):
		count_list.append(len(_list[x]))
    
#print(count_list)    

#cv2.imshow('blue channel' , b)


##기준점 픽스 시키기
##픽셀값이 5이하이면 이걸 중앙으로 옮겨
##fixed_list는 y좌표 옮긴 값

	fixed_list = []
	distance = 0
	temp = []

# ##############테스트용
# a = [0 for i in range (width)]

# for x in range(width - 2):
#     if count_list[x] <= 3 and count_list[x+1] <=3 and count_list[x+2] <= 3: #x좌표의 y값들이 5개가 안되면 (일직선부분)
        
#         a[x] = distance
#         if list[x] and list[x][0] < 270 and list[x][0] > 230: 
#             distance = abs(list[x][0] - 250) #중간값까지의 거리
#             if list[x][0] < 250 : #그래프가 중간보다 위쪽이면
#                 distance = distance    
#             else:
#                 distance = -distance;
            
#             for y in range(len(list[x])):
#                 temp.append(list[x][y] + distance) #중간으로 위치조정하고
            
#             print(temp)
#             fixed_list.append(temp)
#             temp = []
        
#             for y in range(len(list[x+1])): #다음꺼 미리 위치조정 
#                 list[x+1][y] = list[x+1][y] + distance;

#         else :
#             fixed_list.append([250])
#     else: #x좌표의 y값들이 5개가 넘으면 (심장박동하는부분)
        
#         for y in range(len(list[x])):
#             temp.append(list[x][y]) 

#         print(temp)
#         fixed_list.append(temp)
#         temp = []
        
#         for y in range(len(list[x+1])): #다음꺼 미리 위치조정 
#              list[x+1][y] = list[x+1][y] + distance;

# ####################################3
#print(fixed_list[0])

#print(len(list[46]))
#print(len(list[49] + list[48] + list[47]))
#out = open('output.txt' , 'w')
#print(list, file=out)

##y값의 길이가 비슷한것 끼리 사이의 거리를 구함 +-10%
##세 픽셀의 값이 일정 (100개) 수준이 넘을때 마디
##세 x픽셀의 y개수의 합이 +-10% 이상이면 다른 마디임 


	test = np.zeros((height, width, 3),np.uint8)
	test_h = test.shape[0]
	test_w = test.shape[1]
	test_bpp = test.shape[2]



#fixed_list가 일단은 좌표축 조정한것.
	result=merge(merge(_list))
	for x in range(len(result)):
		for y in range(len(result[x])):
			test = cv2.line(test,(x,result[x][y]),(x,result[x][y]),(255,255,255),1)
	fixed_counter_list=[]
	for i, elem in enumerate(count_list):
		if elem<20:
			fixed_counter_list.append(0)
		else:
			fixed_counter_list.append(elem)
#print(fixed_counter_list)
#cv2.imshow("test", test)
#print(result)

	sdaf = clustering(fixed_counter_list)



	#cv2.imshow("test", subimg)

	cv2.waitKey(0)
	cv2.destroyAllWindows()
	clustered = clustering(fixed_counter_list)
	#print(clustered)
	idx = choichoi(sdaf,_list)[1]
	idx_2 = clustered[idx]
	#print(idx,idx_2)
	clustered_list = _list[idx_2-5:idx_2+5]
	#print(clustered_list)
	s1 = set()
	for i in clustered_list:
		for j in i:
			s1.add(j)
	avg = (max(s1)+min(s1))//2

	print(str(_i) + ' ' + which_disable(avg))