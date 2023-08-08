import cv2

image=cv2.imread("res/lena.jpg") #resime filtreleme işlemi yapabilmek için resmi çağırmak gerekiyor.resimi image değişkenine atadım
#res klasörü altındaki lena.jpg resmine eriştim.imread fonksiyonuyla çağırdım.

medianFilter=cv2.medianBlur(image,3)
 #OpenCV kütüphanesi kullanılarak bir görüntünün median filtre ile düzgünleştirilmesini sağlar.
#cv2.medianBlur() fonksiyonu, median filtre uygulamak için kullanılır. İlk argüman olarak filtre uygulanacak görüntü belirtilir.
# İkinci argüman ise filtre boyutunu belirtir. Bu örnekte filtre boyutu 3 olarak belirtilmiştir, yani 3x3 boyutunda bir filtre uygulanacak demektir.
#Bu filtre, her pikselin ortancasını alarak uygulanır. Yani, filtre boyutu içindeki her pikselin değerleri sıralanır ve ortadaki değer, pikselin yeni değeri olarak atanır.
# Median filtre, özellikle tuz-biber gürültüsü gibi aşırı değerlerin bulunduğu görüntülerde etkili bir şekilde kullanılır.
medianFilter2=cv2.medianBlur(image,5) #5*5 lik matris
medianFilter3=cv2.medianBlur(image,7) #7*7 lik matris

cv2.imshow("orijinal resim",image) #pencerede gösterilecek orijinal resim.
cv2.imshow("median filter 3*3",medianFilter) #pencerede göstericek 3*3 lük median filtreli resim
cv2.imshow("median filter 5*5",medianFilter2) #pencerede göstericek 5*5 lük median filtreli resim
cv2.imshow("median filter 7*7 ",medianFilter3) #pencerede göstericek 7*7 lük median filtreli resim

cv2.waitKey(0) #cv2.waitKey() fonksiyonu, klavyeden bir tuşa basılıncaya kadar bekleyen bir fonksiyondur.
# Bu fonksiyon genellikle OpenCV ile görüntü işleme uygulamaları yaparken kullanılır ve kullanıcıya görüntüyü göstermek için kullanılır.
cv2.destroyAllWindows() #cv2.destroyAllWindows() fonksiyonu, OpenCV kütüphanesi kullanılarak açılmış olan tüm pencereleri kapatır.