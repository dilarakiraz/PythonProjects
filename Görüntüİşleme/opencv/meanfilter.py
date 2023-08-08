import cv2

image=cv2.imread("res/lena.jpg") #resime filtreleme işlemi yapabilmek için resmi çağırmak gerekiyor.resimi image değişkenine atadım
#res klasörü altındaki lena.jpg resmine eriştim.imread fonksiyonuyla çağırdım.

meanFilter=cv2.blur(image,(3,3)) #OpenCV kütüphanesi kullanılarak bir görüntünün ortalama filtre ile düzgünleştirilmesini sağlar.
#cv2.blur() fonksiyonu, ortalama filtre uygulamak için kullanılır. İlk argüman olarak filtre uygulanacak görüntü belirtilir.
# İkinci argüman ise filtre boyutunu belirtir.
#Bu filtre, her pikselin ortalaması alınarak uygulanır. Yani, filtre boyutu içindeki her pikselin değerleri toplanır ve bu toplam, piksel sayısına bölünerek ortalama değer hesaplanır.
#Sonrasında bu ortalama değer, filtre boyutu içindeki pikselin yer aldığı konuma atanır.
#Bu işlem sonucu, görüntünün gürültüsünü azaltarak daha düzgün bir görüntü elde edilmesini sağlar.
meanFilter2=cv2.blur(image,(5,5)) #5*5 lik matris ile yumuşatma
meanFilter3=cv2.blur(image,(7,7)) #7*7 lik matris ile yumuşatma


cv2.imshow("orijinal resim",image) #pencerede gösterilecek orijinal resim.

cv2.imshow("mean filter 3*3",meanFilter) #pencerede gösterilecek mean filterlı resim
cv2.imshow("mean filter 5*5",meanFilter2) #pencerede gösterilecek mean filterlı 5*5 matrisli resim
cv2.imshow("mean filter 7*7",meanFilter3) #pencerede gösterilecek mean filterlı 7*7 matrisli resim

cv2.waitKey(0) #cv2.waitKey() fonksiyonu, klavyeden bir tuşa basılıncaya kadar bekleyen bir fonksiyondur.
# Bu fonksiyon genellikle OpenCV ile görüntü işleme uygulamaları yaparken kullanılır ve kullanıcıya görüntüyü göstermek için kullanılır.
cv2.destroyAllWindows() #cv2.destroyAllWindows() fonksiyonu, OpenCV kütüphanesi kullanılarak açılmış olan tüm pencereleri kapatır.