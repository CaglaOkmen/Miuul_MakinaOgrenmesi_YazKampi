# Miuul List Comprehension Alistirmalari

# Görev 1: List Comprehension yapısı kullanarak
# car_crashes verisindeki numeric değişkenlerin
# isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
import seaborn as sns
df = sns.load_dataset("car_crashes")

[f"NUM_{col.upper()}" if df[col].dtype != "O"  else col.upper() for col in df.columns]

#Görev 2: List Comprehension yapısı kullanarak car_crashes
# verisinde isminde "no" barındırmayan değişkenlerin
# isimlerinin sonuna "FLAG" yazınız.

[f"{col.upper()}_FLAG" if "no" not in col else col.upper() for col in df.columns]

# Görev 3: List Comprehension yapısı kullanarak aşağıda verilen
# değişken isimlerinden FARKLI olan değişkenlerin isimlerini
# seçiniz ve yeni bir data frame oluşturunuz.

og_list = ["abbrev", "no_previous"]
new_frame = [col for col in df.columns if col not in og_list]
df[new_frame].head()
