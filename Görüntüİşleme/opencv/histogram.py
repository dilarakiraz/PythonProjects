import cv2
from matplotlib import pyplot as plt  #OpenCV,NumPy, ve Matplotlib kütüphaneleri dahil ediliyor.

# Girdi olarak verilen gri görüntüyü yükleyin
img = cv2.imread('./res/gri.png', 0)  #cv2.imread() işlevi kullanılarak ./res/gri.png" dosyası, gri renk formatında okunarak "img" değişkenine atanıyor."0" argümanı ile resim gri formatta okunuyor..
img2 = cv2.equalizeHist(img) #"Görüntü İyileştirme" tekniği olan Histogram Eşitleme işlemi, gri renk formatındaki "img" görüntüsüne uygulanıyor ve eşitlenmiş görüntü "img2" değişkenine atanıyor.

#"img" ve "img2" görüntülerinin histogramları, "calcHist()" fonksiyonu kullanılarak hesaplanıyor. Her iki histogram da 256 binliğe ayrılmış ve 0-256 aralığında değerler içeriyor.
hist_input = cv2.calcHist([img],[0],None,[256],[0,256]) #verilen gri görüntü ("img") için histogramı hesaplar. cv2.calcHist() fonksiyonu, histogram hesaplama işlemini gerçekleştiren OpenCV fonksiyonlarından biridir.
# İlk parametre olarak, histogramın hesaplanacağı görüntüyü içeren bir liste alır. Görüntü gri tonlamalı olduğu için, bu listeye sadece "img" görüntüsü eklenir.
#İkinci parametre, histogramın hesaplanacağı kanalı seçer. Gri tonlamalı görüntülerde, yalnızca 0. kanal mevcuttur (sadece tek bir kanal kullanılır). Bu nedenle, bu parametrede [0] değeri kullanılır.
#Üçüncü parametre, maskenin belirtilmesi için kullanılabilir. Burada, maske kullanılmadığı için "None" olarak atanır.
#Dördüncü parametre, histogramdaki bin sayısını belirler. Burada, 256 adet bin kullanılır.
#Beşinci parametre, histogramda hesaplanacak minimum ve maksimum değerleri belirler. Bu durumda, 0 ile 256 aralığı kullanılır.
#Sonuç olarak, "hist_input" adlı değişkene, "img" görüntüsünün histogramı atanır.
hist_output = cv2.calcHist([img2] , [0] , None,[256],[0,256])

#Matplotlib kütüphanesi kullanılarak 2x2 boyutunda bir çizim yüzeyi oluşturuluyor.
# İlk satırda, "img" görüntüsü ve histogramı,
# ikinci satırda ise "img2" görüntüsü ve histogramı çizdiriliyor.
plt.subplot(221),plt.imshow(img,cmap = 'gray',vmin=0, vmax=255) #Bu satır, Matplotlib kütüphanesi kullanılarak bir çizim yüzeyi oluşturur ve "img" adlı gri görüntüyü çizer.
#plt.subplot() fonksiyonu, çizim yüzeyi üzerinde alt-parçalar oluşturmak için kullanılır. Parametre olarak, yüzeyin boyutlarını belirleyen bir demet (tuple) alır. Bu demetin ilk iki elemanı, çizim yüzeyinin boyutlarını belirler (2 satır ve 2 sütun).
# Üçüncü parametre, alt-parçanın konumunu belirler. Burada, alt-parça numarası "221" olarak atanmıştır. Bu, 2 satırlı ve 2 sütunlu çizim yüzeyindeki ilk alt-parçadır.
#plt.imshow() fonksiyonu, bir görüntüyü çizmek için kullanılır. İlk parametre olarak, çizilecek görüntüyü alır. Bu durumda, "img" adlı gri görüntüdür.
# İkinci parametre olarak, görüntüyü hangi renk haritası ile çizeceğimizi belirtiriz. Gri tonlamalı bir görüntü olduğu için "gray" renk haritası kullanılır. "vmin" ve "vmax" parametreleri, görüntünün hangi aralıkta gösterileceğini belirler. Bu durumda, görüntü 0 ila 255 aralığında gösterilir.
#Bu satır sonucunda, çizim yüzeyinin ilk alt-parçası, "img" adlı gri görüntüyle doldurulur.
plt.title('original'),plt.xticks([]), plt.yticks([]) #plt.title() fonksiyonu, çizim yüzeyinin başlığını belirler. Burada, başlık "original" olarak atanır.
#plt.xticks([]) ve plt.yticks([]) fonksiyonları, x ve y eksenindeki çizgileri kapatır. Bu satırların amacı, çizim yüzeyindeki alt-parçaların arasındaki çizgileri kapatmak ve bu sayede görüntülerin daha net görünebilmesini sağlamaktır.
#çizim yüzeyinin ilk alt-parçasına "original" başlığı ekler ve x ve y eksenindeki çizgileri kapatır.
plt.subplot(222), plt.plot(hist_input) #Bu satır, Matplotlib kütüphanesi kullanılarak bir çizim yüzeyinde ikinci bir alt-parça oluşturur ve bu alt-parçaya "hist_input" adlı bir histogram çizer.
#alt-parça numarası "222" olarak atanmıştır. Bu, 2 satırlı ve 2 sütunlu çizim yüzeyindeki ikinci alt-parçadır.
#plt.plot() fonksiyonu, verileri çizmek için kullanılır. İlk parametre olarak, çizilecek verileri alır. Bu durumda, "hist_input" adlı histogramdır.
plt.subplot(223), plt.imshow(img2,cmap= 'gray', vmin=0, vmax=255) #Matplotlib kütüphanesi kullanılarak bir çizim yüzeyinde üçüncü bir alt-parça oluşturur ve bu alt-parçaya "img2" adlı bir görüntü çizer
# ilk iki elemanı, çizim yüzeyinin boyutlarını belirler (2 satır ve 2 sütun). Üçüncü parametre, alt-parçanın konumunu belirler. Burada, alt-parça numarası "223" olarak atanmıştır. Bu, 2 satırlı ve 2 sütunlu çizim yüzeyindeki üçüncü alt-parçadır.
plt.title('Histogram'), plt.xticks([]),plt.yticks([]) #"Histogram" adlı bir başlık ekler ve x ve y eksenindeki tickleri (çizgileri) kapatır.
plt.subplot(224), plt.plot(hist_output) #Matplotlib kütüphanesi kullanılarak bir çizim yüzeyinde dördüncü bir alt-parça oluşturur ve bu alt-parçaya "hist_output" adlı bir histogram çizer.
# 2 satırlı ve 2 sütunlu çizim yüzeyindeki dördüncü alt-parçadır.Bu satır sonucunda, çizim yüzeyinin dördüncü alt-parçasına "hist_output" adlı bir histogram çizilir.

plt.show() #Tüm çizimler, ekrana getiriliyor.
