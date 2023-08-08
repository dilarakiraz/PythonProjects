import cv2

image=cv2.imread("res/lena.jpg") #resime filtreleme işlemi yapabilmek için resmi çağırmak gerekiyor.resimi image değişkenine atadım
#res klasörü altındaki lena.jpg resmine eriştim.imread fonksiyonuyla çağırdım.

gauss=cv2.GaussianBlur(image,(3,3),0) #OpenCV kütüphanesi kullanılarak bir görüntünün Gaussian filtre ile düzgünleştirilmesini sağlar
#cv2.GaussianBlur() fonksiyonu, Gaussian filtre uygulamak için kullanılır. İlk argüman olarak filtre uygulanacak görüntü belirtilir.
# İkinci argüman ise filtre boyutunu belirtir. Bu örnekte filtre boyutu (3,3) olarak belirtilmiştir, yani 3x3 boyutunda bir filtre uygulanacak demektir.
gauss2=cv2.GaussianBlur(image,(5,5),0) #5*5 boyutunda bir filtre uygulanacak demektir.
gauss3=cv2.GaussianBlur(image,(7,7),0) #7*7 boyutunda bir filtre uygulanacak demektir.

cv2.imshow("orijinal resim",image) #pencerede gösterilecek orijinal resim.

cv2.imshow("gauss filter 3*3",gauss) #cv2.GaussianBlur() fonksiyonu kullanılarak elde edilen Gauss filtre uygulanmış görüntüyü ekranda göstermek için kullanılır.
#cv2.imshow() fonksiyonu, ekranda bir pencere açarak bir görüntüyü bu pencereye yerleştirir. İlk argüman olarak pencerenin adı belirtilir.
#İkinci argüman ise pencereye yerleştirilecek olan görüntüdür.
cv2.imshow("gauss filter 5*5",gauss2)
cv2.imshow("gauss filter 7*7",gauss3)



cv2.waitKey(0) #cv2.waitKey() fonksiyonu, klavyeden bir tuşa basılıncaya kadar bekleyen bir fonksiyondur.
# Bu fonksiyon genellikle OpenCV ile görüntü işleme uygulamaları yaparken kullanılır ve kullanıcıya görüntüyü göstermek için kullanılır.
cv2.destroyAllWindows() #cv2.destroyAllWindows() fonksiyonu, OpenCV kütüphanesi kullanılarak açılmış olan tüm pencereleri kapatır.