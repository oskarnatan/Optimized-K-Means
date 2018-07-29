# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 19:25:59 2018

@author: Oskar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time


#inisialisasi awal
data = pd.read_csv('ruspini.csv')
maxx = max(data.x) + 10
maxy = max(data.y) + 10
colmap = {1: 'magenta', 2: 'blue', 3: 'green', 4: 'orange', 5: 'brown', 6: 'red'}
k = 4
sizey = 10
sizex = 0.8 * sizey
jarak = [0 for x in range(len(data.x))]
jarakmin = [0 for x in range(k)]
jarakcen = [0 for x in range(k-1)]
for i in range(k):
    jarakmin[i] = 1000 ** 3
centroidx = {
    i: [np.random.randint(maxx), np.random.randint(maxy)]
    for i in range(k)
}


#plot data mula - mula
print("\n\ndata")
fig = plt.figure(figsize=(sizex, sizey))
plt.scatter(data['x'], data['y'], color='black')     #PLOT INSTANCE
plt.xlim(0, maxx)
plt.ylim(0, maxy)
plt.show()




#PROSES OPTIMASI
start_time = time.time()
grandmeanx = np.mean(data.x)
grandmeany = np.mean(data.y)
for j in range(k):
    for i in range(len(data.x)):
        jarak[i] = np.sqrt((grandmeanx - data.x[i]) ** 2 + (grandmeany - data.y[i]) ** 2)
        if(j==0):
            if(jarak[i] < jarakmin[j]):
                jarakmin[j] = jarak[i]
                centroidx[j][0] = data.x[i]
                centroidx[j][1] = data.y[i]
        elif(j==1):
            jarakcen[0] = np.sqrt((centroidx[j-1][0] - data.x[i]) ** 2 + (centroidx[j-1][1] - data.y[i]) ** 2)
            if((jarak[i] < jarakmin[j]) and (jarak[i] > jarakmin[j-1]) and
               (jarakcen[0] >= jarakmin[j-1])):
                jarakmin[j] = jarak[i]
                centroidx[j][0] = data.x[i]
                centroidx[j][1] = data.y[i]
        elif(j==2):
            jarakcen[0] = np.sqrt((centroidx[j-1][0] - data.x[i]) ** 2 + (centroidx[j-1][1] - data.y[i]) ** 2)
            jarakcen[1] = np.sqrt((centroidx[j-2][0] - data.x[i]) ** 2 + (centroidx[j-2][1] - data.y[i]) ** 2)
            if((jarak[i] < jarakmin[j]) and (jarak[i] > jarakmin[j-1]) and
               (jarakcen[0] >= jarakmin[j-2]) and
               (jarakcen[1] >= jarakmin[j-1])):
                jarakmin[j] = jarak[i]
                centroidx[j][0] = data.x[i]
                centroidx[j][1] = data.y[i]
        elif(j==3):
            jarakcen[0] = np.sqrt((centroidx[j-1][0] - data.x[i]) ** 2 + (centroidx[j-1][1] - data.y[i]) ** 2)
            jarakcen[1] = np.sqrt((centroidx[j-2][0] - data.x[i]) ** 2 + (centroidx[j-2][1] - data.y[i]) ** 2)
            jarakcen[2] = np.sqrt((centroidx[j-3][0] - data.x[i]) ** 2 + (centroidx[j-3][1] - data.y[i]) ** 2)
            if((jarak[i] < jarakmin[j]) and (jarak[i] > jarakmin[j-1]) and
               (jarakcen[0] >= jarakmin[j-3]) and
               (jarakcen[1] >= jarakmin[j-2]) and
               (jarakcen[2] >= jarakmin[j-1])):
                jarakmin[j] = jarak[i]
                centroidx[j][0] = data.x[i]
                centroidx[j][1] = data.y[i]
        elif(j==4):
            jarakcen[0] = np.sqrt((centroidx[j-1][0] - data.x[i]) ** 2 + (centroidx[j-1][1] - data.y[i]) ** 2)
            jarakcen[1] = np.sqrt((centroidx[j-2][0] - data.x[i]) ** 2 + (centroidx[j-2][1] - data.y[i]) ** 2)
            jarakcen[2] = np.sqrt((centroidx[j-3][0] - data.x[i]) ** 2 + (centroidx[j-3][1] - data.y[i]) ** 2)
            jarakcen[3] = np.sqrt((centroidx[j-4][0] - data.x[i]) ** 2 + (centroidx[j-4][1] - data.y[i]) ** 2)
            if((jarak[i] < jarakmin[j]) and (jarak[i] > jarakmin[j-1]) and
               (jarakcen[0] >= jarakmin[j-4]) and
               (jarakcen[1] >= jarakmin[j-3]) and
               (jarakcen[2] >= jarakmin[j-2]) and
               (jarakcen[3] >= jarakmin[j-1])):
                jarakmin[j] = jarak[i]
                centroidx[j][0] = data.x[i]
                centroidx[j][1] = data.y[i]
        elif(j==5):
            jarakcen[0] = np.sqrt((centroidx[j-1][0] - data.x[i]) ** 2 + (centroidx[j-1][1] - data.y[i]) ** 2)
            jarakcen[1] = np.sqrt((centroidx[j-2][0] - data.x[i]) ** 2 + (centroidx[j-2][1] - data.y[i]) ** 2)
            jarakcen[2] = np.sqrt((centroidx[j-3][0] - data.x[i]) ** 2 + (centroidx[j-3][1] - data.y[i]) ** 2)
            jarakcen[3] = np.sqrt((centroidx[j-4][0] - data.x[i]) ** 2 + (centroidx[j-4][1] - data.y[i]) ** 2)
            jarakcen[4] = np.sqrt((centroidx[j-5][0] - data.x[i]) ** 2 + (centroidx[j-5][1] - data.y[i]) ** 2)
            if((jarak[i] < jarakmin[j]) and (jarak[i] > jarakmin[j-1]) and
               (jarakcen[0] >= jarakmin[j-5]) and
               (jarakcen[1] >= jarakmin[j-4]) and
               (jarakcen[2] >= jarakmin[j-3]) and
               (jarakcen[3] >= jarakmin[j-2]) and 
               (jarakcen[4] >= jarakmin[j-1])):
                jarakmin[j] = jarak[i]
                centroidx[j][0] = data.x[i]
                centroidx[j][1] = data.y[i]
stop_time = ((time.time() - start_time) * 1000)


#PLOT DATA, GRANDMEAN, DAN CENTROIDX TERPILIH
print("\n\n\nPlot data(hitam), grandmean(merah), centroid awal(kuning)")
fig = plt.figure(figsize=(sizex, sizey))
plt.scatter(data['x'], data['y'], color='black')     #PLOT INSTANCE
plt.scatter(grandmeanx, grandmeany, color='red')
for i in centroidx.keys():
    plt.scatter(*centroidx[i], color="yellow")
plt.xlim(0, maxx)
plt.ylim(0, maxy)
plt.show()
#samakan titik centroidx ke titik centroid yang digunakan
centroid = {
    i+1: [centroidx[i][0], centroidx[i][1]]
    for i in range(k)
}
#print("waktu optimasi = %s ms" %stop_time)



#PLOT DATA YANG SUDAH DICLUSTER DAN CENTROIDNYA
def plot2():
    fig = plt.figure(figsize=(sizex, sizey))
    plt.scatter(data['x'], data['y'], color=data['warna'], alpha=0.2, edgecolor='k')
    for i in centroid.keys():
        plt.scatter(*centroid[i], color=colmap[i])
    plt.xlim(0, maxx)
    plt.ylim(0, maxy)
    plt.show()
    
## PERHITUNGAN JARAK EUCLIDEAN TERDEKAT ANTARA TITIK2 INSTANCE DENGAN TITIK2 CENNTROID
#LALU INSTANCE DI ASSIGN KE TITIK CENTROID TERDEKAT 
def assigndata(data, centroid):
    for i in centroid.keys(): 
        #HITUNG JARAK EUCLIDEAN SELURUH INSTANCE  DENGAN SELURUH TITIK centroid
        data['euclidean_{}'.format(i)] = (
            np.sqrt(
                #((x1 - x2)^2 - (y1 - y2)^2)
                (data['x'] - centroid[i][0]) ** 2 + (data['y'] - centroid[i][1]) ** 2
            )
        )
    centroid_distance_cols = ['euclidean_{}'.format(i) for i in centroid.keys()]
    data['terdekat'] = data.loc[:, centroid_distance_cols].idxmin(axis=1)
    data['terdekat'] = data['terdekat'].map(lambda x: int(x.lstrip('euclidean_')))
    data['warna'] = data['terdekat'].map(lambda x: colmap[x])
    return data
    
## UPDATE TITIK centroid 1 SAMPAI K,
#UPDATE NILAI AXIS X/Y BERASAL DARI MEAN TITIK2 X/Y INSTANCE TERDEKAT DARI HASIL ASSIGN DATA
def updatetitik():
    for i in centroid.keys():
        centroid[i][0] = np.mean(data[data['terdekat'] == i]['x'])
        centroid[i][1] = np.mean(data[data['terdekat'] == i]['y'])

#LOOP TERUS SAMPAI TIDAK ADA PERUBAHAN TITIK CENTROID LAGI
def looping():
    global data, z
    data = assigndata(data, centroid)
    print("\n\n\nProses Clustering.....")
    a_time = time.time()
    while True:
        centroid_terdekat = data['terdekat']
        updatetitik()
        data = assigndata(data, centroid)
        if centroid_terdekat.equals(data['terdekat']):
            break
    z = ((time.time() - a_time) * 1000)
    
    
#PERHITUNGAN VARIANCE
def hitungvariance():
    sumsquaredataw = 0
    dtot = 0
    for i in centroid.keys():
        #PERHITUNGAN CLUSTER VARIANCE
        #AXIS X
        sumsquaredatax = 0
        ncx = np.shape(data[data['terdekat'] == i]['x']) #HITUNG JUMLAH INSTANCE PADA SUATU CLUSTER i
        dx = np.mean(data[data['terdekat'] == i]['x']) #HITUNG RATA2 NILAI
        valx = np.array(data[data['terdekat'] == i]['x']) #UBAH KE BENTUK ARRAY DAN DISIMPAN KE VARIABLE VAR
        for j in range(ncx[0]):
            sumsquaredatax += ((valx[j] - dx) ** 2)
        vcx = np.sqrt((1/(ncx[0]-1))*sumsquaredatax)
        #AXIS Y
        sumsquaredatay = 0
        ncy = np.shape(data[data['terdekat'] == i]['y']) #HITUNG JUMLAH INSTANCE PADA SUATU CLUSTER i
        dy = np.mean(data[data['terdekat'] == i]['y']) #HITUNG RATA2 NILAI
        valy = np.array(data[data['terdekat'] == i]['y']) #UBAH KE BENTUK ARRAY DAN DISIMPAN KE VARIABLE VAR
        for j in range(ncy[0]):
            sumsquaredatay += ((valy[j] - dy) ** 2)
        vcy = np.sqrt((1/(ncy[0]-1))*sumsquaredatay)
        #XY
        vc = np.sqrt(vcx**2 + vcy**2)
        #vc = vcx + vcy
        s = 'variance vc cluster ke-' + repr(i) + ' = ' + repr(vc)
        #print(s)
        
        #PERHITUNGAN VARIANCE WITHIN CLUSTER
        sumsquaredataw += ((ncx[0]-1)*(vc**2))
        
        #PERHITUNGAN VARIANCE BETWEEN CLUSTER
        #dv = np.sqrt(dx**2 + dy**2)
        dv = dx + dy
        dtot += dv
    
    #LANJUTAN PERHITUNGAN VARIANCE WITHIN CLUSTER
    N = np.shape(data) #HITUNG JUMLAH INSTANCE PADA SUATU CLUSTER i
    vw = (1/(N[0]-k))*sumsquaredataw
    s = 'variance within cluster vw = ' + repr(vw)
    #print(s)
    
    #PERHITUNGAN VARIANCE BETWEEN CLUSTER
    dtot = dtot/k
    sumsquaredatab = 0
    for i in centroid.keys():
        ncx = np.shape(data[data['terdekat'] == i]['x']) #HITUNG JUMLAH INSTANCE PADA SUATU CLUSTER i
        dx = np.mean(data[data['terdekat'] == i]['x']) #HITUNG RATA2 NILAI
        dy = np.mean(data[data['terdekat'] == i]['y']) #HITUNG RATA2 NILAI
        dv = np.sqrt(dx**2 + dy**2)
        sumsquaredatab += (ncx[0]*((dv-dtot)**2))
    vb = (1/(k-1))*sumsquaredatab
    s = 'variance between cluster vb = ' + repr(vb)
    #print(s)
    
    v = vw / vb
    s = 'variance v = vw/vb = ' + repr(v)
    print(s)



looping()
plot2()
print("execution time = %s ms" % z)
hitungvariance()