import numpy as np
import cv2
#Numpy ve OpenCV modüllerini dahil ediyoruz.
#Numpy, Python'da matematiksel işlemler yapmak için kullanılırken, OpenCV görüntü işleme için kullanılır.

# Görüntüyü yükle
img = cv2.imread('res/otsu.jpg', 0)#Resmi okuyoruz. 'res/otsu.jpg' belirtilen dosya yolundaki görüntüyü okuyoruz. İkinci argüman olan '0', okunan görüntünün gri tonlamalı olmasını sağlar.

# Görüntünün boyutunu al
height, width = img.shape#Resmin yüksekliği ve genişliği alınır.

# Histogramı hesapla
hist = cv2.calcHist([img], [0], None, [256], [0, 256]) #Görüntünün histogramını hesaplar. calcHist fonksiyonu bir görüntü için histogram hesaplar. İlk argüman, görüntüdür.
# İkinci argüman, hesaplanacak histogramın kanalıdır. Gri tonlamalı görüntüler için, bu her zaman [0] dır.
# Üçüncü argüman, maskeden özellikler hesaplamak için kullanılacak bir maske belirler.
# Dördüncü argüman, histogramın boyutunu belirler.
# Beşinci argüman, hesaplanan histogramın aralığını belirler.

# Toplam piksel sayısını hesapla
total_pixels = height * width #Toplam piksel sayısı hesaplanır.

# Sınıf sayısını tanımla
class_number = 256 #piksel yoğunluklarının 0'dan 255'e kadar olan tüm olası değerlerini içeren 256 sınıfı temsil eder. Bu sayede Otsu eşikleme yöntemi, görüntüdeki farklı sınıfların (arkaplan ve nesne) ayrılmasını sağlar ve optimal bir eşik değeri bulunabilir.

# Eşik değerini bulmak için değişkenleri tanımla
max_variance = 0
threshold = 0

# Otsu eşikleme yöntemini uygula
for i in range(1, class_number): #Otsu eşikleme yöntemini uygulamak için, görüntünün histogramındaki her piksel değeri için bir eşik değeri hesaplanır.
    # Sınıfları ayır
    class1 = np.sum(hist[:i]) #Piksel değerleri iki sınıfa bölünür.class1 değişkeni, histogramın sıfırdan i-1 arasındaki piksel değerlerinin toplamını
    class2 = np.sum(hist[i:])#Piksel değerleri iki sınıfa bölünür.class2 değişkeni ise i'den 256'ya kadar olan piksel değerlerinin toplamını verir
    # Bu şekilde, histogramdaki piksel değerleri iki sınıfa ayrılmış olur ve her sınıfın toplam piksel sayısı hesaplanmış olur. Bu sınıfların ağırlıkları daha sonra kullanılmak üzere hesaplanacaktır.

    # Piksel sayılarını hesapla
    w1 = class1 / total_pixels #Sınıfların ağırlıkları hesaplanır.
    w2 = class2 / total_pixels #Otsu eşikleme yöntemi, bir görüntüyü iki sınıfa bölerek arka plan ve nesne gibi iki bölgeyi tanımlamayı amaçlar. w1, histogramın sol tarafındaki sınıfın ağırlığıdır ve w2, histogramın sağ tarafındaki sınıfın ağırlığıdır.
    # Bu ağırlıklar, her sınıftaki piksellerin toplam sayısının görüntünün toplam piksel sayısına bölünmesi ile hesaplanır.

    # Ortalama değerleri hesapla
    if class1 == 0: #if blokları, eğer sınıfın toplam piksel sayısı 0 ise, o sınıf için ortalama değeri 0 olarak belirler. Bu durum, eğer bir sınıfta hiç piksel yoksa, o sınıfa ait ortalama değeri hesaplamaya çalışırken oluşabilecek bölme hatasını önler.
        mean1 = 0
    else:
        mean1 = np.sum(np.arange(i) * hist[:i]) / class1 # histogramda bulunan piksel değerlerinin belirli bir eşik değerine kadar olan kısmının ortalamasını hesaplar. İlk olarak, np.arange(i) ifadesi, 0'dan i'ye kadar olan tam sayıları bir dizi olarak döndürür. Bu, histogramda bulunan piksel değerlerinin dizisine karşılık gelir. Daha sonra, bu değerler histogramdaki piksel değerleriyle çarpılır. np.sum işlevi, çarpımların toplamını hesaplar. Son olarak, bu toplam, sınıf1'teki piksel sayısına bölünür, böylece belirli bir eşik değerine kadar olan piksel değerleri için ortalama değer hesaplanmış olur.
    if class2 == 0: #if blokları, eğer sınıfın toplam piksel sayısı 0 ise, o sınıf için ortalama değeri 0 olarak belirler. Bu durum, eğer bir sınıfta hiç piksel yoksa, o sınıfa ait ortalama değeri hesaplamaya çalışırken oluşabilecek bölme hatasını önler.
        mean2 = 0
    else: #mean1 ve mean2 değişkenleri hesaplanır. Bunlar, her bir sınıf için ortalama piksel değerleridir. Bu hesaplama, o sınıftaki her pikselin değeri ile o pikselin sayısının çarpımının toplamının, sınıfın toplam piksel sayısına bölünmesiyle yapılır.
        mean2 = np.sum(np.arange(i, class_number) * hist[i:]) / class2 #mean2 değişkeni, eşik değerinin sağ tarafındaki piksellerin ortalamasını hesaplar. İlk olarak, np.arange(i, class_number) ifadesi, eşik değerinin sağ tarafındaki piksel değerlerinin aralığını belirler. Daha sonra, hist[i:] ifadesi, bu piksel değerleri için histogramda ilgili piksel sayısını verir. np.arange(i, class_number) * hist[i:] ifadesi, bu piksel değerlerini ilgili piksel sayısı ile çarpıp, histogramda bu piksel değerlerine karşılık gelen toplam piksel değerlerini hesaplar. Son olarak, np.sum() işlemi, tüm bu piksel değerlerinin toplamını verir. Bu toplam, eşik değerinin sağ tarafındaki piksellerin toplam piksel değerini verir. Bu toplamı sınıf sayısına bölersek, ortalama değeri elde ederiz.
    # Varyansları hesapla
    variance = w1 * w2 * ((mean1 - mean2) ** 2) # sınıfların ağırlıkları ve ortalama değerlerinin farkının karesinin, sınıfların ağırlıklarının çarpımına çarpılmasıyla elde edilir. Bu hesaplama, sınıfların homojenliğini gösteren bir ölçüdür.
    # Varyans en büyük değerse eşik değerini güncelle
    if variance > max_variance:  #, eğer variance değeri daha önceki tüm değerlerden büyükse, max_variance değişkeni bu yeni değere eşitlenir ve threshold değişkeni de i değerine eşitlenir. Bu, şimdiye kadar hesaplanan en iyi eşik değerini belirlemeye çalışır.
        max_variance = variance
        threshold = i

# Eşik değerini düşük bir değere ayarlayarak görüntüyü ikili hale getir
binary_img = np.zeros((height, width), dtype=np.uint8) #belirtilen boyutlarda bir siyah beyaz (binary) görüntü dizisi oluşturur. height ve width değişkenleri, oluşturulan dizinin boyutlarını belirler. Dizinin tüm öğeleri başlangıçta sıfır olarak ayarlanır, yani siyah renkli bir görüntüdür. dtype değişkeni, oluşturulan dizinin veri tipini belirtir. np.uint8, 0-255 aralığında tamsayı değerleri kullanır.
binary_img[img >= 50] = 255 #img" adlı bir görüntüdeki piksellerin 130'dan büyük veya eşit olduğu durumlarda "binary_img" adlı başka bir görüntüdeki pikselleri 255 (beyaz) olarak ayarlar ve diğer tüm pikselleri 0 (siyah) olarak ayarlar. Böylece, "binary_img" adlı görüntü, 130'dan büyük olan piksellerin beyaz ve diğer tüm piksellerin siyah olduğu bir ikili görüntü olur.

# Görüntüyü göster
cv2.imshow("orijinal resim",img) #orijinal resim gösterilir
cv2.imshow('Otsu Thresholding', binary_img) #otsu eşikleme yöntemi kullanılmış resim
cv2.waitKey(0) #cv2.waitKey() fonksiyonu, klavyeden bir tuşa basılıncaya kadar bekleyen bir fonksiyondur.
# Bu fonksiyon genellikle OpenCV ile görüntü işleme uygulamaları yaparken kullanılır ve kullanıcıya görüntüyü göstermek için kullanılır.
cv2.destroyAllWindows() #cv2.destroyAllWindows() fonksiyonu, OpenCV kütüphanesi kullanılarak açılmış olan tüm pencereleri kapatır.